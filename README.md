# 🕷️ Divar Scraper

> **Automated Phone Number Extraction from Divar Ads**

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green?style=flat-square&logo=selenium)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

**Powerful web scraping tool for extracting contact information from Divar marketplace listings**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation)

</div>

---

## ✨ Features

- 📱 **Contact Extraction** - Intelligent phone number extraction from seller profiles
- 🔄 **Batch Processing** - Process multiple listings simultaneously with ease
- 💾 **Smart Session Caching** - Save login cookies for faster subsequent operations
- 🎭 **Anti-Detection** - Random delays and human-like behavior patterns
- 📊 **Data Export** - Structured output saved to text files
- ⚡ **Fast & Efficient** - Optimized for performance and reliability
- 🛡️ **Error Handling** - Robust error management and retry mechanisms

---

## 📋 Requirements

- **Python** 3.7 or higher
- **Chrome** or **Chromium** browser installed
- **pip** package manager

### System Requirements
- RAM: 512MB minimum
- Disk Space: 100MB for dependencies
- OS: Windows, macOS, Linux

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/divar_scraper.git
cd divar_scraper
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `selenium` (>= 4.0.0) - Web browser automation
- `webdriver-manager` (>= 3.8.0) - Automatic Chrome driver management
- `pyperclip` (>= 1.8.2) - Clipboard operations

### Step 3: Verify Installation

```bash
python divar_scraper.py --version
```

---

## 💡 Usage

### Basic Usage

```bash
python divar_scraper.py
```

### Interactive Workflow

1️⃣ **Login** (First Time Only)
   - Script launches browser with Divar homepage
   - Enter your phone number
   - Enter verification code
   - Select your city
   - Press `Enter` when login completes

2️⃣ **Enter Ad Links**
   ```
   Enter ad links (one per line):
   https://divar.ir/v/123456789
   https://divar.ir/v/987654321
   https://divar.ir/v/555555555
   
   [Press Enter twice to finish]
   ```

3️⃣ **Let It Run** ⏳
   - Script processes each link automatically
   - Extracts phone numbers
   - Implements smart delays between requests
   - Saves results to `results.txt`

4️⃣ **Collect Results** 📥
   - Check `results.txt` for extracted data
   - All phone numbers and links are organized

---

## 📁 Output Format

**File:** `results.txt`

```
Link: https://divar.ir/v/123456789
Phone: +989121234567
--------------------------------------------------
Link: https://divar.ir/v/987654321
Phone: +989359876543
--------------------------------------------------
```

---

## 🔧 Configuration

### Session Management

The script automatically saves your login session in `divar_cookies.json`:

```json
// divar_cookies.json
[
  {
    "name": "session_cookie",
    "value": "...",
    "domain": "divar.ir"
  }
]
```

**To login with a different account:**
```bash
# Delete the cookies file
rm divar_cookies.json

# Next run will prompt for fresh login
python divar_scraper.py
```

### Customizing Delays

Edit the delay values in the script (in seconds):

```python
delay = random.uniform(8, 12)  # Adjust these numbers
```

---

## 📖 Examples

### Example 1: Single Ad

```bash
$ python divar_scraper.py

Enter ad links:
https://divar.ir/v/123456789

Processing (1/1)...
   Clicked on contact info button.
   Phone: +989121234567

Complete! Saved 1 results to results.txt
```

### Example 2: Batch Processing

```bash
$ python divar_scraper.py

Enter ad links:
https://divar.ir/v/111111111
https://divar.ir/v/222222222
https://divar.ir/v/333333333

Processing (1/3)...
Processing (2/3)...
Processing (3/3)...

Complete! Saved 3 results to results.txt
```

---

## ⚠️ Troubleshooting

### ❌ "Contact info button not found"

**Cause:** The seller may have hidden their contact information.

**Solution:**
- Try a different ad listing
- Verify the ad is still active
- Check if you're logged in properly

### ❌ "Clipboard empty"

**Cause:** Browser failed to copy phone number to clipboard.

**Solution:**
- Check your internet connection
- Verify clipboard permissions
- Try manually copying the number
- Restart the script

### ❌ Chrome driver fails to initialize

**Cause:** Chrome/Chromium not installed or path issues.

**Solution:**
```bash
# Install webdriver-manager dependencies
pip install --upgrade webdriver-manager

# Or specify Chrome path manually
export CHROME_PATH=/path/to/chrome
python divar_scraper.py
```

### ❌ "Logged in as different user"

**Cause:** Existing session cookies are for another account.

**Solution:**
```bash
# Clear the session
rm divar_cookies.json

# Login fresh
python divar_scraper.py
```

---

## 🔐 Privacy & Security

✅ **What is stored:**
- Only session cookies (in `divar_cookies.json`)
- Extracted phone numbers (in `results.txt`)

❌ **What is NOT stored:**
- Your password
- Your personal credentials
- Your phone number
- Any sensitive account information

**Security Best Practices:**
- Don't share `divar_cookies.json` with others
- Use a dedicated account if possible
- Delete results when no longer needed
- Keep the script updated

---

## ⚖️ Legal & Terms of Service

**Important Notice:** 

This tool is provided for **educational purposes only**. Users are responsible for:

- ✅ Respecting Divar's Terms of Service
- ✅ Complying with local laws and regulations
- ✅ Using extracted data responsibly
- ✅ Not overloading Divar servers
- ✅ Respecting privacy rights

**By using this tool, you agree to use it lawfully and ethically.** The developers are not responsible for misuse.

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Commit** your changes (`git commit -m 'Add amazing feature'`)
5. **Push** to the branch (`git push origin feature/amazing-feature`)
6. **Open** a Pull Request

### Development Setup

```bash
# Clone repo
git clone https://github.com/yourusername/divar_scraper.git
cd divar_scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with dev dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest
```

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

MIT © 2026 Divar Scraper Contributors

---

## 🙋 FAQ

**Q: Is this legal?**  
A: Yes, data scraping is legal in most jurisdictions. However, respect the platform's ToS and use responsibly.

**Q: Will I get banned from Divar?**  
A: If used with reasonable delays and not excessively, risk is minimal. The script includes anti-detection features.

**Q: Can I use this with a proxy?**  
A: Yes, Selenium supports proxy configuration. Modify `setup_driver()` accordingly.

**Q: How many ads can I process?**  
A: Theoretically unlimited, but recommended: 50-100 per session to avoid detection.

**Q: Do I need to stay online during processing?**  
A: Yes, the browser must remain open and connected.

**Q: Can I modify the code?**  
A: Absolutely! Feel free to fork and customize for your needs.

---

## 🚀 Performance Tips

- 🔌 Use a stable internet connection
- 💻 Close other browser tabs to free resources
- ⏱️ Process ads in batches (not 1000+ at once)
- 🎯 Use realistic delays between requests
- 📊 Monitor the console output for issues

---

## 📞 Support

- 🐛 **Found a bug?** Open an [Issue](https://github.com/yourusername/divar_scraper/issues)
- 💡 **Have an idea?** Start a [Discussion](https://github.com/yourusername/divar_scraper/discussions)
- 📧 **Need help?** Check existing [Issues](https://github.com/yourusername/divar_scraper/issues) first

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ by the AmirRezaiyan**

[⬆ Back to Top](#-divar-scraper)

</div>
