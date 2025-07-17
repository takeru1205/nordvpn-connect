# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python library for connecting to NordVPN servers programmatically. It supports both Windows and Linux platforms and provides a simple interface to initialize VPN connections, rotate servers, and disconnect.

## Architecture

The main functionality is contained in `nordvpn_connect/nordvpn_connect.py` with three core functions:

- `initialize_vpn(server_to_connect_to, nordvpn_username=None, nordvpn_password=None)`: Sets up VPN connection parameters and handles platform-specific initialization
- `rotate_VPN(parameters)`: Connects to a VPN server and verifies IP change
- `close_vpn_connection(parameters)`: Disconnects from the VPN

The library uses the NordVPN command-line client (`nordvpn`) as the underlying connection mechanism and includes country/region mappings in `nordvpn_connect/NordVPN_options/countrylist.txt`.

## Dependencies

- `psutil`: For process management (Windows service checks)
- `requests`: For IP address checking via api.myip.com
- `loguru`: For logging throughout the application

## Common Commands

### Installation and Setup
```bash
# Install dependencies and sync environment
uv sync

# Install from PyPI
uv add nordvpn-connect

# Add new dependencies
uv add <package_name>

# Add development dependencies
uv add --dev <package_name>
```

### Running Examples
```bash
# Run the demo script
uv run demo.py

# Run the main entry point
uv run main.py
```

### Development Commands
```bash
# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .

# Fix linting issues
uv run ruff check --fix .
```

### Building and Publishing
```bash
# Build package
uv build

# Install locally in development mode
uv sync --dev
```

## Platform-Specific Notes

- **Linux**: Requires NordVPN CLI to be installed and may require login credentials
- **Windows**: Requires NordVPN application to be installed in standard locations and the nordvpn-service.exe to be running

## Testing

This project currently has no automated test suite. Manual testing can be done by running `demo.py` with appropriate credentials.