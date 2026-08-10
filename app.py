"""
SatyaLens Streamlit Application
A minimal, ultra-clean, and addictive UI inspired by Perplexity AI & Claude with custom branding.
"""

import os
import base64
import streamlit as st
from satya_lens_core import SatyaLens, FactCheckResult
from config import (
    PROJECT_NAME,
    PROJECT_TAGLINE,
    VERDICT_COLORS,
    VERDICT_OPTIONS,
    TRUSTED_DOMAINS,
    LLM_MODEL
)

#  LOGO ASSET LOAD 
LOGO_PATH = os.path.join(os.path.dirname(__file__), "satyalens_logo.png")

def get_logo_base64(path=LOGO_PATH):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_logo_base64()
logo_img_html = f'<img src="data:image/png;base64,{logo_b64}" style="height: 58px; width: 58px; border-radius: 14px; object-fit: cover; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 8px 16px rgba(0,0,0,0.4);">' if logo_b64 else ""
sidebar_logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height: 32px; width: 32px; border-radius: 8px; vertical-align: middle; margin-right: 8px; border: 1px solid rgba(255,255,255,0.1);">' if logo_b64 else "🔍 "


#  PAGE CONFIGURATION 
st.set_page_config(
    page_title=f"{PROJECT_NAME} • AI Fact Checker",
    page_icon=LOGO_PATH if os.path.exists(LOGO_PATH) else "🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


#  MINIMALIST CUSTOM CSS 
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Neutral Dark Theme (Perplexity / Zinc Palette) */
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #09090B !important;
        color: #FAFAFA !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6, 
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #FAFAFA !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
    }

    p, span, label, div, .stMarkdown p, .stMarkdown span {
        color: #A1A1AA !important;
    }

    /* Main Container max width and spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 900px !important;
    }

    /* Minimalist Top Header */
    .brand-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }

    .brand-title {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #FAFAFA !important;
        margin: 0 !important;
        letter-spacing: -0.03em !important;
    }

    .brand-subtitle {
        font-size: 1rem;
        color: #71717A !important;
        margin-top: 0.4rem;
    }

    /* Minimal Text Area Input Box */
    .stTextArea label {
        color: #FAFAFA !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.4rem !important;
    }

    .stTextArea textarea {
        border-radius: 14px !important;
        background-color: #18181B !important;
        border: 1px solid #27272A !important;
        color: #FAFAFA !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        transition: border-color 0.15s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: #52525B !important;
        box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.1) !important;
    }

    /* Minimal Primary Action Button */
    .stButton > button[kind="primary"] {
        background-color: #FAFAFA !important;
        color: #09090B !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1.5rem !important;
        transition: background-color 0.15s ease !important;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #E4E4E7 !important;
        color: #09090B !important;
    }

    /* Sample Claim Pills */
    .stButton > button {
        background-color: #18181B !important;
        color: #D4D4D8 !important;
        border: 1px solid #27272A !important;
        border-radius: 20px !important;
        font-weight: 400 !important;
        font-size: 0.85rem !important;
        padding: 0.4rem 1rem !important;
        transition: all 0.15s ease !important;
    }

    .stButton > button:hover {
        background-color: #27272A !important;
        color: #FAFAFA !important;
        border-color: #3F3F46 !important;
    }

    /* Minimal Result Section Cards */
    .result-card {
        background-color: #18181B;
        border: 1px solid #27272A;
        border-radius: 14px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }

    /* Source Links Minimal Rows */
    .source-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.8rem 1rem;
        background-color: #18181B;
        border: 1px solid #27272A;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        text-decoration: none;
        transition: border-color 0.15s ease;
    }

    .source-row:hover {
        border-color: #3F3F46;
    }

    .source-title-text {
        color: #E4E4E7 !important;
        font-size: 0.9rem;
        font-weight: 500;
        text-decoration: none;
    }

    .source-domain-tag {
        color: #71717A !important;
        font-size: 0.8rem;
        font-weight: 400;
    }

    /* Sidebar minimal styling */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div {
        background-color: #18181B !important;
        border-right: 1px solid #27272A !important;
    }

    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4 {
        color: #FAFAFA !important;
    }

    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #A1A1AA !important;
    }
</style>
""", unsafe_allow_html=True)


#  SIDEBAR (CLEAN MINIMAL) 
with st.sidebar:
    st.markdown(f"### {sidebar_logo_html}**{PROJECT_NAME}**", unsafe_allow_html=True)
    st.caption("Unbiased Fact Verification Engine")
    
    st.divider()
    
    mistral_key = os.getenv("MISTRAL_API_KEY", "")
    key_status = "Connected" if mistral_key else "Key Required"
    
    st.markdown(f"**LLM Engine:** Mistral AI ({key_status})")
    st.markdown(f"**Model:** `{LLM_MODEL}`")
    st.markdown(f"**Retrieval:** DuckDuckGo (DDGS)")
    
    st.divider()
    
    with st.expander(f"Whitelisted Sources ({len(TRUSTED_DOMAINS)})"):
        for domain in TRUSTED_DOMAINS:
            st.markdown(f"• `{domain}`")


# MINIMAL BRAND HEADER WITH LOGO 
st.markdown(f"""
<div class="brand-header">
    <div style="display: flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 0.5rem;">
        {logo_img_html}
        <h1 class="brand-title">{PROJECT_NAME}</h1>
    </div>
    <p class="brand-subtitle">{PROJECT_TAGLINE}</p>
</div>
""", unsafe_allow_html=True)


#  MAIN INPUT SECTION 
if "claim_text" not in st.session_state:
    st.session_state.claim_text = ""

claim_input = st.text_area(
    "Verify any news headline, rumor, or claim:",
    value=st.session_state.claim_text,
    placeholder="Paste or type a claim to fact-check...",
    height=95,
    key="claim_area_key"
)

col_btn1, col_btn2 = st.columns([4, 1])
with col_btn2:
    verify_clicked = st.button("Verify Claim", type="primary", use_container_width=True)


#  QUICK SAMPLE PILLS 
st.markdown("<div style='margin-top: 1.25rem; margin-bottom: 0.5rem; font-size: 0.825rem; color: #71717A; font-weight: 500;'>Quick sample prompts:</div>", unsafe_allow_html=True)

samples = [
    "PIB Fact Check: ₹50,000 scheme",
    "WHO declared COVID emergency ended",
    "RBI crypto ban in India",
    "Free student laptops scheme"
]

sample_full_claims = {
    "PIB Fact Check: ₹50,000 scheme": "PIB Fact Check: The government has announced that all citizens will receive ₹50,000 in their bank accounts",
    "WHO declared COVID emergency ended": "WHO has declared that COVID-19 is no longer a global health emergency",
    "RBI crypto ban in India": "RBI has banned all cryptocurrencies in India",
    "Free student laptops scheme": "The Indian government launched a scheme providing free laptops to all college students"
}

cols = st.columns(4)
for idx, s_label in enumerate(samples):
    with cols[idx]:
        if st.button(s_label, key=f"pill_{idx}", use_container_width=True):
            st.session_state.claim_text = sample_full_claims[s_label]
            st.rerun()


#  RESULTS SECTION 
if verify_clicked:
    current_claim = claim_input.strip()
    if not current_claim:
        st.warning("Please enter a claim to verify.")
    else:
        st.markdown("<hr style='border-color: #27272A; margin: 2rem 0 1.5rem 0;'>", unsafe_allow_html=True)
        
        with st.status("Verifying claim with trusted sources...", expanded=True) as status_box:
            st.write("Searching whitelisted government & IFCN sources...")
            satya = SatyaLens()
            
            st.write("Analyzing evidence with Mistral AI...")
            result: FactCheckResult = satya.verify_claim(current_claim)
            
            if result:
                status_box.update(label="Fact-check complete", state="complete", expanded=False)
            else:
                status_box.update(label="Verification failed", state="error", expanded=False)

        if not result:
            st.error("Unable to complete verification. Please check your API configuration.")
        else:
            verdict_color = VERDICT_COLORS.get(result.verdict, "#71717A")
            confidence_pct = int(result.confidence_score * 100)

            # Minimal Verdict Header
            st.markdown(f"""
            <div style="margin-top: 1.5rem; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <span style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: #71717A; font-weight: 600;">VERDICT</span>
                    <div style="font-size: 1.75rem; font-weight: 700; color: {verdict_color}; margin-top: 2px;">{result.verdict}</div>
                </div>
                <div style="text-align: right;">
                    <span style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: #71717A; font-weight: 600;">CONFIDENCE</span>
                    <div style="font-size: 1.75rem; font-weight: 700; color: #FAFAFA; margin-top: 2px;">{confidence_pct}%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<hr style='border-color: #27272A; margin: 1.25rem 0;'>", unsafe_allow_html=True)

            # Executive Summary Block
            st.markdown("#### **Summary**")
            st.markdown(f"""
            <div style="font-size: 1rem; line-height: 1.6; color: #D4D4D8; background-color: #18181B; padding: 1.25rem; border-radius: 12px; border: 1px solid #27272A;">
                {result.summary}
            </div>
            """, unsafe_allow_html=True)

            # Genuine Fact Callout (if applicable)
            if result.genuine_fact:
                st.markdown("#### **Fact Check Details**")
                st.markdown(f"""
                <div style="font-size: 0.975rem; line-height: 1.6; color: #E4E4E7; background-color: #18181B; padding: 1.25rem; border-radius: 12px; border-left: 4px solid {verdict_color}; border-top: 1px solid #27272A; border-right: 1px solid #27272A; border-bottom: 1px solid #27272A;">
                    {result.genuine_fact}
                </div>
                """, unsafe_allow_html=True)

            # Verified Sources Section
            if result.verified_sources:
                st.markdown("#### **Verified Sources**")
                for i, src in enumerate(result.verified_sources, 1):
                    domain = src['url'].split('/')[2] if '://' in src['url'] else 'trusted source'
                    st.markdown(f"""
                    <div class="source-row">
                        <div>
                            <span style="color: #71717A; font-size: 0.85rem; margin-right: 8px;">{i}.</span>
                            <a href="{src['url']}" target="_blank" class="source-title-text">{src['title']}</a>
                        </div>
                        <span class="source-domain-tag">{domain} ↗</span>
                    </div>
                    """, unsafe_allow_html=True)

            # Footer disclaimer
            st.markdown("<div style='margin-top: 2rem; font-size: 0.8rem; color: #52525B; text-align: center;'>SatyaLens checks whitelisted government portals and IFCN certified sources only.</div>", unsafe_allow_html=True)


#  FOOTER 
st.markdown("""
<div style="text-align: center; color: #3F3F46; font-size: 0.8rem; margin-top: 5rem;">
    SatyaLens • Powered by Mistral AI & DuckDuckGo
</div>
""", unsafe_allow_html=True)
