# Caesar Cipher Tool 🔐

Caesar cipher with a rich command-line interface. Encrypt and decrypt messages with a specified shift value.

## Features ✨

- **Encrypt/Decrypt**: Supports both encryption and decryption modes
- **Rich CLI Interface**: Beautiful terminal output with `rich` library
- **Input Validation**: Ensures valid shift values and modes
- **Error Handling**: Graceful error messages for invalid inputs

## Installation ⚙️

1. **Prerequisites**:
   - Python 3.7+
   - pip package manager

2. **Installation**:
   ```bash
   git clone https://github.com/Padmapriyan27/Caesar-cipher.git

   cd caesar-cipher
   ```

   The tool will automatically install the `rich` package if not present.

## Usage 🚀

### Basic Syntax
```bash
python caesar_cipher.py "your text" shift_value mode
```

### Arguments
| Argument | Description                          | Values                  |
|----------|--------------------------------------|-------------------------|
| text     | Text to encrypt/decrypt              | Any string (use quotes) |
| shift    | Shift value for cipher               | Non-negative integer    |
| mode     | Operation mode                       | `encrypt` or `decrypt`  |

### Examples
1. **Encrypt a message**:
   ```bash
   python caesar_cipher.py "Attack at dawn!" 3 encrypt
   ```

2. **Decrypt a message**:
   ```bash
   python caesar_cipher.py "Dwwdfn dw gdzq!" 3 decrypt
   ```

3. **Show help**:
   ```bash
   python caesar_cipher.py -h
   ```

## Output Format 📊
The tool displays results in a beautiful table format showing:
- Operation mode
- Shift value used
- Original input
- Processed output

## Implementation Details 💻

### Classes
1. **CaesarCipher**:
   - Handles the core encryption/decryption logic
   - Provides sanitization of input text
   - Manages the display of results

2. **CipherApp**:
   - Manages command-line argument parsing
   - Displays help information
   - Coordinates the cipher operations

### Dependencies
- [rich](https://github.com/Textualize/rich) - For beautiful terminal formatting

---

Made with ❤️ by [0xD4rkEYe]