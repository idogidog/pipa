import questionary
from rich import print
from pipa.service.gengerate.common import quest_basic, CORES_ALL, write_title


def quest():
    workspace, freq_record, events_record, freq_stat, events_stat = quest_basic()

    annotete = questionary.select(
        "Whether to use perf-annotate?\n", choices=["Yes", "No"]
    ).ask()
    annotete = True if annotete == "Yes" else False

    taskset = questionary.select(
        "Whether to use taskset?\n", choices=["Yes", "No"]
    ).ask()

    if taskset == "Yes":
        cores = questionary.text(
            "Which cores do you want to use? (Default: 120-140)\n"
        ).ask()
        if cores == "":
            cores = "120-140"

        if cores.isdigit():
            core_list = cores.strip()
        elif cores.split("-").__len__() != 2:
            print("Please input a valid range, split by '-'.")
            exit(1)
        else:
            l, r = cores.split("-")

            l, r = l.strip(), r.strip()
            if not l.isdigit() or not r.isdigit():
                print("Please input a valid range, non-digit char detected.")
                exit(1)
            l, r = int(l), int(r)
            if l < CORES_ALL[0] or r > CORES_ALL[-1] or l >= r:
                print("Please input a valid range.")
                exit(1)
            core_list = ",".join([str(i) for i in list(range(l, r + 1))])

    command = questionary.text("What's the command of workload?\n").ask()

    if command == "":
        print("Please input a command to run workload.")
        exit(1)

    if taskset == "Yes":
        command = f"/usr/bin/taskset -c {core_list} {command}"
    return (
        workspace,
        freq_record,
        events_record,
        freq_stat,
        events_stat,
        annotete,
        command,
    )


def generate(
    workspace, freq_record, events_record, freq_stat, events_stat, annotete, command
):
    """
    Generates a shell script for collecting performance data based on user inputs.
    """

    with open(workspace + "/pipa-run.sh", "w") as f:
        write_title(f)

        f.write("WORKSPACE=" + workspace + "\n")
        f.write("mkdir -p $WORKSPACE\n\n")

        f.write(
            f"perf record -e '{events_record}' -a -F"
            + f" {freq_record} -o $WORKSPACE/perf.data {command}\n"
        )
        f.write("perf script -i $WORKSPACE/perf.data > $WORKSPACE/perf.script\n")
        f.write("perf report -i $WORKSPACE/perf.data > $WORKSPACE/perf.report\n\n")

        f.write("sar -o $WORKSPACE/sar.dat 1 >/dev/null 2>&1 &\n")
        f.write("sar_pid=$!\n")
        f.write(
            f"perf stat -e {events_stat} -C {CORES_ALL[0]}-{CORES_ALL[-1]} -A -x , -I {freq_stat} -o $WORKSPACE/perf-stat.csv {command}\n"
        )
        f.write("kill -9 $sar_pid\n")
        f.write("sar -A -f $WORKSPACE/sar.dat >$WORKSPACE/sar.txt\n\n")

        if annotete:
            f.write(
                "perf annotate -i $WORKSPACE/perf.data > $WORKSPACE/perf.annotate\n\n"
            )

        f.write("echo 'Performance data collected successfully.'\n")

        print("Shell script generated successfully.")
        print("Please check the script in " + workspace + "/pipa-run.sh")


def main():
    generate(**quest())


if __name__ == "__main__":
    main()
