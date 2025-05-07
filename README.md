# js-analyzer
A Python tool to scan JavaScript files for API endpoints, secrets, and dangerous function calls.

# 🔍 JS Analyzer

A lightweight Python tool to scan JavaScript files for:

- 🔗 API Endpoints
- 🔐 Tokens / Secrets / Keys
- ⚠️ Dangerous JavaScript Function Calls

---

## 📦 Features

- Regex-based analysis
- Supports multiple `.js` files
- Outputs readable report files
- Useful for bug bounty hunters, pentesters, and developers

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/<your-username>/js-analyzer.git
cd js-analyzer 


##Usage
python3 js_analyzer.py <file1.js> [file2.js] ...
##Example:
python3 js_analyzer.py example/sample.js
📁 This creates sample_analysis.txt containing the results.
