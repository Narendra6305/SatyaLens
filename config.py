"""
SatyaLens Configuration Module
Stores environment variables, project metadata, and domain whitelist arrays.
"""

import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#  PROJECT METADATA 
PROJECT_NAME = "SatyaLens"
PROJECT_TAGLINE = "The Truth Lens for Misinformation"
VERSION = "1.0.0"

#  API CONFIGURATION 
# Mistral AI API Key (for Mistral models)
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")

#  LLM CONFIGURATION 
# Model configuration
LLM_MODEL = os.getenv("LLM_MODEL", "mistral-small-latest")
LLM_TEMPERATURE = 0.0  # Strict temperature for factual consistency

#  DOMAIN WHITELIST 
# Indian Government & Official Regulatory Domains
INDIAN_GOVERNMENT_DOMAINS: List[str] = [
    "pib.gov.in",
    "factcheck.pib.gov.in",
    "india.gov.in",
    "rbi.org.in",
    "sebi.gov.in",
    "uidai.gov.in",
    "niti.gov.in",
    "isro.gov.in",
    "icmr.gov.in",
    "mohfw.gov.in",
    "mea.gov.in",
    "mha.gov.in",
    "incometax.gov.in",
    ".gov.in",
    ".nic.in",
    ".edu.in"
]

# International Government & Global Public Bodies
INTERNATIONAL_GOVERNMENT_DOMAINS: List[str] = [
    "who.int",
    "un.org",
    "cdc.gov",
    "nih.gov",
    "ec.europa.eu",
    "worldbank.org",
    "imf.org",
    "wmo.int",
    "unesco.org"
]

# IFCN Certified Fact-Checkers & Verified Verification Units
IFCN_CERTIFIED_DOMAINS: List[str] = [
    "factly.in",
    "boomlive.in",
    "altnews.in",
    "newschecker.in",
    "vishvasnews.com",
    "indiatoday.in",
    "thequint.com",
    "logicallyfacts.com",
    "reuters.com",
    "apnews.com",
    "snopes.com",
    "factcheck.org",
    "fullfact.org",
    "afp.com",
    "politifact.com"
]

# Combined whitelist for search API
TRUSTED_DOMAINS: List[str] = (
    INDIAN_GOVERNMENT_DOMAINS +
    INTERNATIONAL_GOVERNMENT_DOMAINS +
    IFCN_CERTIFIED_DOMAINS
)

#  SEARCH CONFIGURATION 
# Number of search results to retrieve
MAX_SEARCH_RESULTS = 5

# Search result snippet length (characters)
MAX_SNIPPET_LENGTH = 500

#  OUTPUT CONFIGURATION 
# Verdict options
VERDICT_OPTIONS = [
    "GENUINE / TRUE",
    "FAKE / FALSE",
    "MISLEADING",
    "UNVERIFIED / INSUFFICIENT DATA"
]

# Color codes for UI display
VERDICT_COLORS = {
    "GENUINE / TRUE": "#10B981",  # Green
    "FAKE / FALSE": "#EF4444",    # Red
    "MISLEADING": "#F59E0B",      # Amber/Orange
    "UNVERIFIED / INSUFFICIENT DATA": "#6B7280"  # Gray
}
