shell_script = """
if [[ $(id -u) -eq 0 ]]; then
    # User is root, run dmidecode directly
    dmidecode >/$DST/dmidecode.txt
else
    echo "You need to be root to run dmidecode, skipping..."
fi

if command -v lspci &>/dev/null; then
    lspci >"$DST/pci_devices.txt"
    echo "PCI devices exported to $DST/pci_devices.txt"
fi

if command -v lsusb &>/dev/null; then
    lsusb >"$DST/usb_devices.txt"
    echo "USB devices exported to $DST/usb_devices.txt"
fi

if command -v lsblk &>/dev/null; then
    lsblk >"$DST/block_devices.txt"
    echo "Block devices exported to $DST/block_devices.txt"
fi

if command -v lshw &>/dev/null; then
    lshw >"$DST/hardware.txt"
    echo "Hardware information exported to $DST/hardware.txt"
fi

if command -v lscpu &>/dev/null; then
    lscpu >"$DST/cpu.txt"
    echo "CPU information exported to $DST/cpu.txt"
    lscpu -a --extended >"$DST/cpu-extended.txt"
    echo "Extended CPU information exported to $DST/cpu-extended.txt"
fi

if command -v lsmod &>/dev/null; then
    lsmod >"$DST/modules.txt"
    echo "Kernel modules exported to $DST/modules.txt"
fi

if command -v lsinitrd &>/dev/null; then
    lsinitrd >"$DST/initrd.txt"
    echo "Initrd information exported to $DST/initrd.txt"
fi

if command -v ip &>/dev/null; then
    ip addr >"$DST/ip.txt"
    echo "IP information exported to $DST/ip.txt"
fi

df -h >"$DST/disk_usage.txt"
echo "Disk usage exported to $DST/disk_usage.txt"

cp /proc/meminfo "$DST/meminfo.txt"
echo "Memory information exported to $DST/meminfo.txt"

cp /proc/cpuinfo "$DST/cpuinfo.txt"
echo "CPU information exported to $DST/cpuinfo.txt"

echo "Configuration exported to $DST"
"""

from io import TextIOWrapper


def write_export_config_script(file: TextIOWrapper, destination: str):
    return file.write(f'DST="{destination}"\n') and file.write(shell_script)
