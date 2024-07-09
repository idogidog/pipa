# PIPA

PIPA (Platform Integrated Performance Analytics) is a platform that aggregates a complete toolchain of performance data collection, processing, and analysis.

<div align="center">
    <img src="asset/logo.png" width="400" height="400">
</div>

PIPA (枇杷, loquat) is a local fruit of Zhejiang, China.
PIPA consists of three parts: loquat tree, flower and fruit, which represent the collecting & processing, analysis and conclusion of performance data respectively.

PIPA is still in the active development process, and the current development focus is on the loquat tree.

![GitHub License](https://img.shields.io/github/license/ZJU-SPAIL/pipa)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ZJU-SPAIL/pipa/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/ZJU-SPAIL/pipa)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Features

- **Data Collecting**: PIPA can collect data from a variety of sources, using tools like perf, sar, and more. It supports multiple platforms including x86_64, ARM, and RISC-V, making it versatile and adaptable. Currently PIPA is capable of collecting and parsing perf and sar data, providing detailed performance metrics.
- **Script Generation**: To reduce the noise generated by the Python runtime, PIPA can generate scripts that collect performance data. 
- **Data Processing**: PIPA can process the collected performance data, including alignment and segmentation, to serve meaningful analysis.
- **Data Visualization**: PIPA can visualize based on the performance data collected to provide intuitive insights.
- **Data Analytics**: PIPA will integrate SPAIL's performance methodology and models to provide meaningful analysis and reveal software and hardware bottlenecks.

## Installation

PIPA can be easily installed using pip:

```sh
pip install PyPIPA
```


## Quickstart

After installation, you can start using PIPA to collect, integrate, and analyze your data. 

To generate a script that collect performance data, you only need to use:

```sh
pipa generate
```
Then you can complete the interaction through the CLI to provide the necessary parameters. You can choose to start the workload with perf, or you can choose to observe the system directly.

Or you can use python interface:

```py
from pipa.service.run import run_and_collect_all

sar_df_list, perf_stat_df, perf_script_df = run_and_collect_all(
        "perf bench futex hash"
)
```

## Build

To build PIPA, you can use the `python` command with the `build` module:  `python -m build`, we use `hatchling` as the build backend.

## LICENSE

PIPA is distributed under the terms of the [MIT License](LICENSE).


## Contributing

Contributions to PIPA are always welcome. Whether it's feature enhancements, bug fixes, or documentation, your contributions are greatly appreciated.