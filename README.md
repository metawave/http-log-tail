# Log File Monitor Script (Test-Branch)

This Python script is designed to monitor changes to a log file accessible over HTTP. It periodically checks the file for any new content and prints the updates to the console. The script supports optional Basic Authentication and allows users to specify the polling interval.

## Features

- Monitors a log file for changes over HTTP.
- Supports Basic Authentication for protected resources.
- Configurable polling interval.
- Efficiently downloads only new content using HTTP Range Requests.

## Requirements

- Python 3
- `requests` library

## Installation

Before running the script, ensure you have Python 3 installed on your system. You can then install the required `requests` library using pip:

```
pip install requests
```

## Usage

To use the script, you must provide the URL of the log file as a required argument. Optional arguments include Basic Authentication credentials and a custom polling interval.

### Basic Usage

```
python http-tail.py <url>
```

Replace `<url>` with the actual URL of the log file you wish to monitor.

### With Basic Authentication

If the log file requires Basic Authentication, provide the username and password as follows:

```
python http-tail.py <file_url> --user <username> --password <password>
```

### Custom Polling Interval

To specify a custom polling interval (in seconds), use the `--interval` option:

```
python http-tail.py <file_url> --interval <interval>
```

Replace `<interval>` with the desired number of seconds to wait between checks.

## Example

Monitor a log file with a 15-second polling interval:

```
python http-tail.py http://myhost.com/debug.log --interval 15
```

Monitor a log file with Basic Authentication and a 20-second polling interval:

```
python http-tail.py http://myhost.com/debug.log --user myusername --password mypassword --interval 20
```

## Contributing

Feel free to fork the repository and submit pull requests with any improvements or fixes.

## License

This script is provided "as is", without warranty of any kind. You are free to use, modify, and distribute it as you see fit.
