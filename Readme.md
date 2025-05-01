# DNS Amplification Tool

A simple DNS amplification tool written in Python.

## Usage

Argument parsing: The script uses the argparse module to parse command-line arguments, making it easier to use and providing help text for each option.

Error handling: The script includes error handling for socket errors, ValueError exceptions (e.g., invalid packet size or duration) and KeyboardInterrupt exceptions (e.g., when the user interrupts the script with Ctrl+C).

Help text and usage: The script provides help text and usage information when run with the -h or --help option.

To use this script, simply run it from the command line, providing the target IP address, DNS server, packet size and duration as arguments. For example:

python dns_amplification_tool.py 192.168.1.100 8.8.8.8 100 10

This will send 100-byte packets to the DNS server 8.8.8.8, which will then respond to the target IP address 192.168.1.100 for 10 seconds.