 # 🔍 SatyaLens - The Truth Lens for Misinformation

An end-to-end, unbiased Fact-Checker LLM application focused on Indian and International fact verification. SatyaLens verifies user claims using **ONLY** trusted government portals and IFCN-certified (International Fact-Checking Network) sources, strictly filtering out partisan or politically aligned media channels.

## 🌟 Features

- **Domain Whitelisting**: Restricts searches to trusted government and IFCN-certified sources only
- **RAG-Powered**: Uses Retrieval-Augmented Generation with web search retrieval
- **LLM Support**: Powered by Mistral AI (supports mistral-small-latest, mistral-large-latest, etc.)
- **Structured Output**: Returns JSON-formatted results with verdict, confidence score, and verified sources
- **Beautiful UI**: Clean Streamlit interface with color-coded verdicts
- **Fail-Safe Design**: Returns "UNVERIFIED" when no trusted evidence is found

## 📋 Trusted Sources

SatyaLens **ONLY** verifies claims from:

### Indian Government Domains
- `pib.gov.in` - Press Information Bureau
- `factcheck.pib.gov.in` - PIB Fact Check
- `india.gov.in` - India Portal
- `rbi.org.in` - Reserve Bank of India
- `.gov.in` - All Indian government domains
- `.nic.in` - National Informatics Centre

### International Government/Global Bodies
- `who.int` - World Health Organization
- `un.org` - United Nations
- `cdc.gov` - Centers for Disease Control

### IFCN Certified Fact-Checkers
- `factly.in` - Factly
- `boomlive.in` - BOOM Live
- `altnews.in` - Alt News
- `newschecker.in` - NewsChecker
- `reuters.com` - Reuters Fact Check
- `apnews.com` - AP Fact Check

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download the Project
```bash
cd SatyaLens
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Mistral AI API key:
```bash
# Required: Mistral AI API Key
MISTRAL_API_KEY=your_mistral_api_key_here

# Optional: Choose your LLM model
LLM_MODEL=mistral-small-latest
```

### Getting API Keys

#### Mistral AI API Key (Required)
1. Visit [https://console.mistral.ai/api-keys/](https://console.mistral.ai/api-keys/)
2. Sign up or log in
3. Create a new API key

**Note:** SatyaLens uses DuckDuckGo Search for web retrieval, which is free and requires no API key. Only the Mistral AI API key is required.

## 🎯 Usage

### Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Using SatyaLens

1. **Enter a Claim**: Type or paste the claim you want to verify in the text area
2. **Click "Verify Claim"**: SatyaLens will search trusted sources and analyze the claim
3. **View Results**: 
   - **Verdict**: Color-coded result (Green=True, Red=False, Orange=Misleading, Gray=Unverified)
   - **Confidence Score**: Percentage indicating confidence in the verdict
   - **Genuine Fact**: The actual truth if the claim is false/misleading
   - **Summary**: 2-3 sentence explanation of the verdict
   - **Verified Sources**: Links to trusted sources used for verification

### Programmatic Usage

You can also use SatyaLens as a Python module:

```python
from satya_lens_core import verify_claim

# Verify a claim
result = verify_claim("The Indian government announced free laptops for all students")

# Access results
print(f"Verdict: {result.verdict}")
print(f"Confidence: {result.confidence_score}")
print(f"Summary: {result.summary}")
print(f"Sources: {result.verified_sources}")
```

## 📊 Output Format

SatyaLens returns structured JSON output:

```json
{
    "verdict": "GENUINE / TRUE",
    "confidence_score": 0.95,
    "genuine_fact": "The government has indeed announced...",
    "summary": "Based on official PIB releases...",
    "verified_sources": [
        {
            "title": "Press Information Bureau - Official Release",
            "url": "https://pib.gov.in/..."
        }
    ]
}
```

### Verdict Options
- **GENUINE / TRUE**: The claim is accurate based on trusted sources
- **FAKE / FALSE**: The claim is false based on trusted sources
- **MISLEADING**: The claim contains partial truths but is misleading
- **UNVERIFIED / INSUFFICIENT DATA**: No evidence found from trusted sources

## 🔧 Configuration

### Modifying Trusted Domains
Edit `config.py` to add or remove trusted domains:

```python
TRUSTED_DOMAINS: List[str] = [
    "pib.gov.in",
    "factcheck.pib.gov.in",
    # Add more domains here
]
```

### LLM Models
Configure `LLM_MODEL` in `.env`:
- `mistral-small-latest` (Default, fast & accurate)
- `mistral-large-latest` (Highest capability)
- `open-mistral-7b` (Lightweight model)

### Adjusting Search Parameters
Edit `config.py` to modify:
- `MAX_SEARCH_RESULTS`: Number of search results (default: 5)
- `MAX_SNIPPET_LENGTH`: Length of content snippets (default: 500)
- `LLM_TEMPERATURE`: LLM temperature (default: 0.0 for consistency)

## 🏗️ Project Structure

```
SatyaLens/
├── config.py                 # Configuration and domain whitelist
├── satya_lens_core.py        # Core retrieval and LLM logic
├── app.py                    # Streamlit UI application
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variable template
└── README.md                # This file
```

## ⚠️ Important Notes

- **No Internal Knowledge**: SatyaLens does NOT use pre-trained internal memory. It only uses retrieved evidence from trusted sources.
- **Fail-Safe**: If no trusted sources are found, the verdict defaults to "UNVERIFIED / INSUFFICIENT DATA".
- **Domain Restriction**: The system explicitly ignores general commercial media to avoid political bias.
- **API Costs**: Using OpenAI or Google APIs may incur costs. Tavily offers a free tier.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Any new domains added are government or IFCN-certified
- Code follows the existing style
- Changes maintain the fail-safe design

## 📄 License

This project is provided as-is for educational and informational purposes.

## 🙏 Acknowledgments

- DuckDuckGo for the search 
- Mistral AI for LLM capabilities
- IFCN for certifying trusted fact-checkers

---

Built with ❤️ for Truth | SatyaLens v1.0.0
