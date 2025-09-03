
<div align="center">
<img width="1024" height="1024" alt="Icon" src="https://github.com/user-attachments/assets/91edf3c7-748f-469d-aeab-6d7a1dbd6a98" />

<br>

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)
![GitHub stars](https://img.shields.io/github/stars/SKaif009/ForbiddenHack?style=social)
![GitHub forks](https://img.shields.io/github/forks/SKaif009/ForbiddenHack?style=social)
![GitHub issues](https://img.shields.io/github/issues/SKaif009/ForbiddenHack)
</div
# ForbiddenHack v1.0.0 

**Advanced 403 Bypass & Reconnaissance Tool**

ForbiddenHackv1.0.0 is a comprehensive Python tool designed for security researchers and penetration testers to test and bypass HTTP 403 Forbidden responses using multiple attack vectors including header manipulation, HTTP method testing, path obfuscation, and historical snapshot analysis.
<br>


<img width="1915" height="1012" alt="image" src="https://github.com/user-attachments/assets/bd58d402-6bdf-4ba2-a217-7a990854f1fa" />

<br>
<br>


https://github.com/user-attachments/assets/bb8c1ac5-d4c8-461b-bf38-d6fab67af825



<br>

https://github.com/user-attachments/assets/e88631d1-6e05-4093-b72c-e81737975967



## Features

### Multi-Vector Bypass Testing
- **Header-based Bypass**: Tests various HTTP headers that may bypass access controls
- **HTTP Method Testing**: Attempts different HTTP methods (GET, POST, PUT, DELETE, etc.)
- **Path Obfuscation**: Advanced URL manipulation techniques including:
  - Case sensitivity variations
  - Character encoding (URL encoding, double encoding)
  - Slash tricks and directory traversal
  - File extension manipulation
  - Special character injection

### Historical Analysis
- **Wayback Machine Integration**: Discovers historical snapshots of restricted resources
- **Timeline Analysis**: Shows when protected resources were previously accessible

### User Experience
- **Colorized Output**: Easy-to-read results with color-coded status responses
- **Multiple Banner Designs**: Randomized ASCII art banners
- **Detailed Reporting**: Comprehensive results with response lengths and headers
- **Configurable Delays**: Adjustable request timing to avoid rate limiting

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Quick Install
```bash
# Clone the repository
git clone https://github.com/SKaif009/ForbiddenHack.git
cd ForbiddenHack/bin

# linux 
sudo cp ForbiddenHack /usr/bin
# test
ForbiddenHack -h
```

## Usage

### Basic Usage
```bash
ForbiddenHack -u http://example.com/admin
```

### Advanced Usage
```bash
ForbiddenHack -u https://target.com/restricted -d 0.5 -t 10
```

### Flags
- `-u, --url`: Target URL (required)
- `-d, --delay`: Delay between requests in seconds (default: 0.2)
- `-t, --timeout`: Request timeout in seconds (default: 8.0)

## Examples

### Testing a Restricted Admin Panel
```bash
ForbiddenHack -u https://example.com/admin
```

### Testing with Custom Timing
```bash
# Slower requests to avoid detection
ForbiddenHack -u https://target.com/secret -d 1.0 -t 15
```

### Testing API Endpoints
```bash
ForbiddenHack -u https://api.example.com/v1/users
```

## Bypass Techniques

### Header-Based Bypasses
- `X-Original-URL`: Override the original URL
- `X-Rewrite-URL`: URL rewriting bypass
- `X-Forwarded-*`: IP and host forwarding headers
- `X-Real-IP`: Real IP header manipulation
- `Referer/Origin`: Referrer-based bypasses

### HTTP Method Variations
Tests multiple HTTP methods including:
- Standard methods: GET, POST, PUT, DELETE, HEAD, OPTIONS
- WebDAV methods: PROPFIND, COPY, MOVE, LOCK, UNLOCK
- Extended methods: TRACE, CONNECT, PATCH

### Path Obfuscation Categories
1. **Case Sensitivity**: Upper/lower case variations
2. **Character Encoding**: URL encoding with hex variations
3. **Slash Tricks**: Double slashes, trailing slashes, backslashes
4. **Directory Traversal**: Various `../` and `./` combinations
5. **File Extensions**: Adding common file extensions (.json, .php, .html)
6. **Special Characters**: Null bytes, Unicode, and control characters

## Output Interpretation

### Status Code Colors
- 🟢 **Green (2xx)**: Successful responses - **POSSIBLE BYPASS**
- 🟡 **Yellow (3xx)**: Redirects - May indicate partial bypass
- 🔴 **Red (4xx)**: Client errors - Access still forbidden
- 🟣 **Purple (5xx)**: Server errors - May indicate successful confusion
- 🔵 **Blue (Other)**: Unexpected responses

### Key Indicators
- **Length Variations**: Different response lengths may indicate bypass
- **POSSIBLE BYPASS**: Highlighted when 200 OK is returned
- **Redirect Analysis**: Shows redirect targets for 3xx responses

## Project Structure
```
ForbiddenHack/
├── test.py                 # For Testing purpose 
├── bin/                    # Contain Binary files
│   ├── ForbiddenHack          # Linux-based Binary File
│   ├── ForbiddenHack.exe      # Windows-based binary File
├── README.md              # Documentation
├── LICENSE                # License
└── requirements.txt       # Python dependencies
```

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is designed for authorized security testing and educational purposes only.

- Only use this tool on systems you own or have explicit written permission to test
- Unauthorized access to computer systems is illegal in most jurisdictions
- Users are solely responsible for compliance with applicable laws and regulations
- The developers assume no liability for misuse of this tool


## Changelog

### Version 1.0.0
- Initial release with core bypass techniques
- Header, method, and path obfuscation testing
- Wayback Machine integration
- Colorized output and multiple banner designs


## Credits

**Made with ❤️ by BlackForgeX**

### Dependencies
- `requests`: HTTP library for Python
- `colorama`: Cross-platform colored terminal text
- `urllib3`: HTTP client for Python

### Inspiration
This tool combines various bypass techniques documented by security researchers and consolidates them into a single, easy-to-use testing framework.

## 📜 License

This project is **proprietary**.

* No license is granted to use, copy, modify, or distribute the source code.
* Only the provided binaries in the `bin/` folder may be used **for personal and educational purposes**.
* The source code (`main.py`) is **not disclosed** and will not be released.
* All rights reserved © 2025 [Kaif S](https://github.com/SKaif009).

For feature requests or suggestions, feel free to open an issue.

## Support

If you find this tool useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new features
- 📖 Improving documentation

---

**Remember**: With great power comes great responsibility. Use this tool ethically and legally.
