import streamlit as st
import math

# Pricing variables
price_per_project = 29.99
extra_links = 9.99
drm_cost = 24.99
forensic_watermarking_cost = 0.99

def link_math(links):
    return max(0, math.ceil((links - 200) / 100))

def screenkey_total(projects, links, drm, watermark, smarttv):
    total = 0
    total += projects * price_per_project
    total += link_math(links) * extra_links
    total += (projects * drm_cost) if drm else 0
    total += (links * forensic_watermarking_cost) if watermark else 0
    return total

def indee_total(projects, watermark, smarttv, drm):
    base_rate_per_project = 35.00
    overage_rate_per_project = 250.00
    premium_plus_rate_per_project = 500.00
    project_limit = 30
    premium_plus_project_limit = 40

    # Premium+ tier
    if projects > premium_plus_project_limit or watermark or smarttv:
        return projects * premium_plus_rate_per_project if projects > 0 else 0.0

    # Overage tier 
    if drm or watermark or projects > project_limit:
        return projects * overage_rate_per_project if projects > 0 else 0.0

    # Base price
    return projects * base_rate_per_project if projects > 0 else 0.0


header_logo_col, header_space_col = st.columns([1, 4])  # 1:4 ratio, adjust as needed

with header_logo_col:
    st.image("screenkey.png", width=120) 
col_input, spacer1, col_sk, spacer2, col_indee = st.columns([1, 0.15, 1, 0.15, 1])

with col_input:
    st.header("Your Options")
    projects = st.number_input("Number of projects", min_value=0, value=0, step=1)
    links = st.number_input("Number of total links", min_value=0, value=0, step=1)
    drm = st.checkbox("Multi-DRM Encryption")
    watermark = st.checkbox("Forensic Watermarking")
    smarttv = st.checkbox("Ability to Watch on Smart TVs")

with col_sk:
    st.header("Screenkey")
    sk_total = screenkey_total(projects, links, drm, watermark, smarttv)
    st.markdown(f"## **${sk_total:,.2f}**")

with col_indee:
    st.header("Indee")
    indee_total_amt = indee_total(projects, watermark, smarttv, drm)
    st.markdown(f"## **${indee_total_amt:,.2f}**")
