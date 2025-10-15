# Multi-Country Address Generator

A Python tool to generate random virtual identity data from meiguodizhi.com API. Supports **22+ countries** including US, UK, Canada, Japan, Germany, France, and more. Export as structured JSON files.

> ⚠️ **DISCLAIMER**: This tool is for **educational purposes only**. The generated data is fictional and should not be used for illegal activities, fraud, or any purposes that violate terms of service of websites or applications.

---

## Features

✨ **Core Capabilities**
- Generate batch virtual identities for **22+ countries**
- Complete identity data (name, address, phone, credit card, employment, etc.)
- Export data as beautifully formatted JSON
- Automatic retry mechanism for failed requests
- Progress tracking with real-time feedback
- Rate limiting protection with configurable delays
- Robust error handling (network failures, timeouts, malformed responses)

🌍 **Supported Countries**
- **North America**: United States, Canada
- **Europe**: UK, Germany, France, Italy, Spain, Netherlands, Russia, Turkey
- **Asia**: Japan, China, Taiwan, South Korea, Hong Kong, Singapore, Malaysia, Thailand, Philippines, Vietnam
- **Oceania**: Australia
- **South America**: Argentina

📦 **Zero Configuration**
- Single-file Python script
- Minimal dependencies (only `requests`)
- Cross-platform (Windows/Mac/Linux)

---

## Requirements

- **Python**: 3.6 or higher
- **Dependencies**: 
  - `requests` library

---

## Installation

### 1. Clone or Download

Download the `address_generator.py` file to your local machine.

### 2. Install Dependencies

```bash
pip install requests
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

## Quick Start

### List All Supported Countries

```bash
python address_generator.py --list
```

### Generate 10 UK Addresses (Default)

```bash
python address_generator.py
```

### Generate 50 US Addresses

```bash
python address_generator.py -c us -n 50
```

### Generate Japanese Addresses with Custom Filename

```bash
python address_generator.py -c jp -n 20 -o japanese_data.json
```

---

## Usage

### Basic Syntax

```bash
python address_generator.py [OPTIONS]
```

### Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--country` | `-c` | Country code (us, uk, jp, etc.) | `uk` |
| `--count` | `-n` | Number of addresses to generate | 10 |
| `--output` | `-o` | Output JSON filename | `addresses_COUNTRY_TIMESTAMP.json` |
| `--delay` | `-d` | Delay between requests (seconds) | 0.5 |
| `--list` | | Show all supported countries | - |
| `--help` | `-h` | Show help message | - |

---

## Supported Countries

| Code | Country | Code | Country |
|------|---------|------|---------|
| `us` | United States | `uk` | United Kingdom |
| `ca` | Canada | `au` | Australia |
| `jp` | Japan | `tw` | Taiwan |
| `kr` | South Korea | `hk` | Hong Kong |
| `de` | Germany | `sg` | Singapore |
| `fr` | France | `it` | Italy |
| `es` | Spain | `nl` | Netherlands |
| `my` | Malaysia | `ru` | Russia |
| `cn` | China | `th` | Thailand |
| `ph` | Philippines | `ar` | Argentina |
| `tr` | Turkey | `vn` | Vietnam |

**Total: 22 countries**

Use `python address_generator.py --list` to see the full list.

---

## Examples

### Example 1: Quick Test (5 UK Addresses)

```bash
python address_generator.py -n 5
```

**Output:**
```
╔════════════════════════════════════════════════════════════╗
║      Multi-Country Address Generator v2.0                  ║
║      Educational Use Only - 22+ Countries Supported        ║
╚════════════════════════════════════════════════════════════╝

Selected Country: United Kingdom (UK)

============================================================
  Generating 5 United Kingdom Virtual Identities
============================================================

[1/5] Fetching address... ✓ Success (John Smith)
[2/5] Fetching address... ✓ Success (Emma Johnson)
[3/5] Fetching address... ✓ Success (Oliver Brown)
[4/5] Fetching address... ✓ Success (Sophia Wilson)
[5/5] Fetching address... ✓ Success (William Taylor)

============================================================
  Summary: 5 succeeded, 0 failed
============================================================

Saving to 'addresses_uk_20240115_143052.json'... ✓ Done (23.4 KB)

============================================================
  SUCCESS!
  Country: United Kingdom
  File: /path/to/addresses_uk_20240115_143052.json
  Records: 5
  Time: 3.2s
============================================================
```

### Example 2: Generate US Addresses

```bash
python address_generator.py -c us -n 10
```

### Example 3: Generate Japanese Addresses with Slower Rate

```bash
python address_generator.py -c jp -n 20 -d 1.0
```

### Example 4: Multiple Countries in Sequence

```bash
# Generate data for multiple countries
python address_generator.py -c us -n 100 -o us_addresses.json
python address_generator.py -c uk -n 100 -o uk_addresses.json
python address_generator.py -c jp -n 100 -o jp_addresses.json
```

### Example 5: Large Batch with Safety Check

```bash
python address_generator.py -c de -n 1500
```

**Output:**
```
⚠ Warning: Generating more than 1000 addresses may take a long time
          and could trigger API rate limiting.
Continue? (y/n): y
```

---

## Output Format

The generated JSON file contains an array of identity objects:

### UK Address Example

```json
[
  {
    "address": {
      "Address": "12 Black Lion St",
      "Telephone": "+44 7745756986",
      "City": "Brighton & Hove",
      "Zip_Code": "CH6D 5HF",
      "State": "England",
      "Full_Name": "Serstone",
      "Gender": "Female",
      "Title": "Mrs.",
      "Birthday": "7/28/1995",
      "Credit_Card_Type": "Visa",
      "Credit_Card_Number": "4019999619872918",
      "CVV2": "356",
      "Expires": "07/2027",
      "Username": "weddingshortsighted",
      "Password": "QMEv9ciG5f0s",
      "Temporary_mail": "qwogfdkcde@iubridge.com",
      "Occupation": "Industrial Equipment, Deputy Sheriff",
      "Employment_Status": "Retired",
      "Monthly_Salary": "$7,500",
      "Height": "6' 3\" (193cm)",
      "Weight": "150.1lbs (68.1kg)",
      "Blood_Type": "AB-",
      "System": "Windows 7",
      "GUID": "878ac990-87c0-477b-99c8-801b6a8c7f5c",
      "Browser_User_Agent": "Mozilla/5.0...",
      "Educational_Background": "Doctorate and/or professional degree",
      "Website": "njviuuycg.com",
      "Security_Question": "what in the world is ssn?",
      "Security_Answer": "activityhand-to-hand"
    },
    "status": "ok"
  }
]
```

### Japanese Address Example

```json
[
  {
    "address": {
      "Address": "ニイガタケン, シバタシ, オオツキ, 386-1089",
      "Trans_Address": "386-1089, Otsuki, Shibata-shi, Niigata",
      "Trans_Cn_Address": "新潟县芝田市大月386-1089号",
      "Telephone": "+8149-275-0687",
      "City": "Niigata",
      "Zip_Code": "957-0465",
      "Full_Name": "三輪 黒宮",
      "Credit_Card_Type": "JCB",
      "Credit_Card_Number": "3568612841932429",
      "Monthly_Salary": "980,000Yen",
      ...
    },
    "status": "ok"
  }
]
```

### Complete Field List (39 fields)

Each address object contains up to 39 fields:

**Address Information**
- Address, Address_Alias, Trans_Address, Trans_Cn_Address
- City, State, State_Full, Zip_Code

**Personal Information**
- Full_Name, Full_Name_Tran, Gender, Title, Birthday
- Height, Weight, Blood_Type, Hair_Color

**Contact Information**
- Telephone, Fax, Temporary_mail

**Financial Information**
- Credit_Card_Type, Credit_Card_Number, CVV2, Expires

**Employment Information**
- Occupation, Employment_Status, Monthly_Salary

**Account Information**
- Username, Password, Security_Question, Security_Answer

**Technical Information**
- System, Browser_User_Agent, GUID, Website, Educational_Background

**Other**
- rowkey, Social_Security_Number, status

---

## Configuration

You can modify the following constants in `address_generator.py`:

```python
API_URL = "https://www.meiguodizhi.com/api/v1/dz"
DEFAULT_COUNT = 10          # Default number of addresses
DEFAULT_COUNTRY = "uk"      # Default country code
MAX_RETRIES = 3             # Maximum retry attempts per request
TIMEOUT = 10                # Request timeout in seconds
RETRY_DELAY = 2             # Delay between retries
```

---

## Error Handling

The tool handles various error scenarios:

- **Network Failures**: Automatic retry with exponential backoff
- **HTTP Errors**: Logs status codes and skips failed requests
- **Timeouts**: Configurable timeout with retry logic
- **Invalid JSON**: Graceful error messages
- **Rate Limiting**: Configurable delay between requests
- **Invalid Country Code**: Validates country code before execution

Example output with errors:

```
[5/10] Fetching address...   ⚠ HTTP 429 on attempt 1/3
[5/10] Fetching address...   ✓ Success (John Doe)
[6/10] Fetching address...   ⚠ Timeout on attempt 1/3
[6/10] Fetching address...   ✓ Success (Jane Smith)
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'requests'`

**Solution**: Install the requests library
```bash
pip install requests
```

### Issue: Invalid country code error

**Solution**: Check supported countries
```bash
python address_generator.py --list
```

### Issue: All requests fail with timeouts

**Solution**: Check your internet connection or increase the timeout
```python
TIMEOUT = 30  # Increase to 30 seconds
```

### Issue: HTTP 429 (Rate Limiting)

**Solution**: Increase the delay between requests
```bash
python address_generator.py -c us -n 100 -d 2.0
```

### Issue: File permission error

**Solution**: Run with appropriate permissions or change output directory
```bash
python address_generator.py -c jp -o ~/Documents/addresses.json
```

---

## API Reference

This tool uses the public API endpoint:

```
POST https://www.meiguodizhi.com/api/v1/dz
Content-Type: application/json

{
  "path": "/COUNTRY-address",
  "method": "address"
}
```

**Supported Paths**:
- `/` - United States (default/homepage path)
- `/uk-address` - United Kingdom
- `/jp-address` - Japan
- `/de-address` - Germany
- `/fr-address` - France
- ... (see full list with `--list` flag)

**Note**: The US address endpoint uses the root path `/` instead of `/us-address`.

**Response Structure**:
```json
{
  "address": { ... },
  "status": "ok"
}
```

---

## Use Cases

📚 **Educational Applications**
- Learning API interaction patterns and HTTP requests
- Understanding JSON data structures
- Practicing database design and testing
- Learning about international address formats
- Testing form validation logic across different countries

🧪 **Development & Testing**
- Populate test databases with realistic data
- UI/UX testing with diverse name formats (Latin, CJK characters)
- Internationalization (i18n) testing
- Address validation algorithm testing
- Payment form testing (non-functional card numbers)

---

## Legal & Ethics

⚖️ **Legal Notice**
- This tool accesses a publicly available API for educational purposes
- Generated data is **fictional** and randomly created
- Do NOT use generated credit card numbers for actual transactions
- Do NOT use generated identities to impersonate real people
- Do NOT violate any website's Terms of Service
- Do NOT use for fraud, identity theft, or illegal activities

📚 **Responsible Use**
- Only use for learning, testing, and development purposes
- Never use generated data to deceive or defraud
- Respect API rate limits and usage policies
- Be aware of your local laws regarding synthetic data

---

## Architecture

```
address_generator.py (368 lines)
├── Configuration Layer
│   ├── API endpoint & headers
│   ├── Country mappings (22 countries)
│   ├── Retry/timeout constants
│   └── Default values
│
├── Core Logic Layer
│   ├── fetch_address(country_code)    # API call with retry
│   ├── generate_batch(country, n)     # Batch generation
│   └── save_to_json(data, filepath)   # File I/O
│
├── Utility Layer
│   ├── list_countries()               # Display all countries
│   └── parse_arguments()              # CLI parsing
│
└── Main Entry Point
    ├── Argument validation
    ├── Country selection
    ├── Batch generation with progress
    └── Result summary
```

---

## Advanced Usage

### Batch Processing Multiple Countries

Create a shell script to generate data for multiple countries:

```bash
#!/bin/bash
# generate_all.sh

countries=("us" "uk" "ca" "au" "jp" "de" "fr")

for country in "${countries[@]}"; do
    echo "Generating $country addresses..."
    python address_generator.py -c $country -n 50 -d 0.8
done

echo "All done!"
```

### JSON Processing Examples

**Extract all names with jq:**
```bash
cat addresses_us_*.json | jq '.[].address.Full_Name'
```

**Count addresses by gender:**
```bash
cat addresses_*.json | jq '[.[].address.Gender] | group_by(.) | map({gender: .[0], count: length})'
```

**Filter by employment status:**
```bash
cat addresses_*.json | jq '[.[] | select(.address.Employment_Status == "Full-time work")]'
```

### Python Post-Processing

```python
import json

# Load generated addresses
with open('addresses_us_20240115.json', 'r') as f:
    data = json.load(f)

# Extract specific fields
emails = [item['address']['Temporary_mail'] for item in data]
names = [item['address']['Full_Name'] for item in data]

# Filter by criteria
full_time_workers = [
    item for item in data 
    if item['address']['Employment_Status'] == 'Full-time work'
]

print(f"Total: {len(data)}")
print(f"Full-time workers: {len(full_time_workers)}")
```

---

## Performance

**Benchmarks** (approximate, depends on network):

| Count | Delay | Time | File Size |
|-------|-------|------|-----------|
| 10 | 0.5s | ~6s | ~15 KB |
| 50 | 0.5s | ~30s | ~75 KB |
| 100 | 0.5s | ~55s | ~150 KB |
| 1000 | 0.5s | ~9min | ~1.5 MB |

**Tips for large batches:**
- Use `-d 0.3` to speed up (but watch for rate limits)
- Run overnight for 1000+ addresses
- Monitor network stability for long-running tasks

---

## Contributing

This is a standalone educational tool. Suggestions for improvement:
1. Add support for city-specific addresses (e.g., NYC, Tokyo)
2. Add CSV export option
3. Add filtering options (gender, age range, etc.)
4. Add data validation and statistics

---

## Changelog

### v2.0 (2025-10-16)
- **Major**: Added support for 22 countries
- Added `--country` / `-c` parameter
- Added `--list` flag to show all countries
- Updated output filename format: `addresses_COUNTRY_TIMESTAMP.json`
- Improved country-specific progress messages
- Added country validation

### v1.0 (2025-10-16)
- Initial release
- UK addresses only
- Batch generation with progress tracking
- JSON export with pretty formatting
- Retry mechanism and error handling
- CLI argument support

---

## License

MIT License - Feel free to modify and distribute for educational purposes.

---

---

## FAQ

**Q: Why are some fields empty (like `Social_Security_Number`)?**  
A: Some fields are region-specific or randomly left empty by the API.

**Q: Are the credit card numbers real?**  
A: No. They follow valid formatting rules but are not linked to real accounts.

**Q: Can I use this data in production?**  
A: Absolutely not. This is for educational and testing purposes only.

**Q: How do I generate data for a specific city?**  
A: Currently not supported. The tool generates random addresses within the selected country.

**Q: Why does Japanese output include Chinese translations?**  
A: The API provides multiple translation formats for CJK addresses (Japanese characters, Romanization, Chinese).

**Q: Can I run this concurrently?**  
A: Yes, but be careful about rate limiting. Run different countries in parallel:
```bash
python address_generator.py -c us -n 100 &
python address_generator.py -c uk -n 100 &
python address_generator.py -c jp -n 100 &
```

---

**Remember**: With great power comes great responsibility. Use this tool ethically and legally. 🎓