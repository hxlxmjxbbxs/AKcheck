# AKcheck

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to AKcheck, a utility tool developed by hxlxmj. AKcheck is an indispensable tool for bug bounty hunters, providing an easy way to verify the provider of a specific API key. It interacts with various service endpoints to determine the API key's origin quickly and efficiently.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Installation
To install the script, clone the repository and install the required dependencies as follows:

```bash
git clone https://github.com/hxlxmj/AKcheck.git
cd AKcheck
pip install -r requirements.txt
```

## Usage
To use the tool, run the script with the API key as an argument:

```bash
python AKcheck.py --key YOUR_API_KEY_HERE
```

This will return the provider of the API key.

## Contributing
Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
