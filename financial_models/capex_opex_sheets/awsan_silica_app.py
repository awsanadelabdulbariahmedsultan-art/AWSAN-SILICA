# ====================================================================
# 🌍 AWSAN SILICA PROJECT - INTERACTIVE APP ENGINE FOR CLOUD SHELL
# Powered by: Eng. Awsan Adel Abdulbari Ahmed Sultan
# Owned by: Awsan Dew For Marketing Services (Yemen)
# ====================================================================

import streamlit as st

# 1. Set Page Configuration & Branding
st.set_page_config(page_title="AWSAN SILICA - Financial Dashboard", layout="wide")

st.markdown("""
    <div style='background-color: #1B365D; padding: 20px; border-radius: 10px; margin-bottom: 25px;'>
        <h1 style='color: white; text-align: center; margin-bottom: 5px;'>🌍 سيليكا أوسان: لوحة التحكم والاستثمار الديناميكية</h1>
        <h3 style='color: #E0F2F1; text-align: center; margin-top: 0;'>AWSAN SILICA - Dynamic Financial & ROI Simulation App</h3>
        <p style='color: #7F8C8D; text-align: center; font-style: italic; margin-bottom: 0;'>
            Powered by Eng. Awsan Adel Abdulbari Ahmed Sultan | Owned by Awsan Dew For Marketing Services
        </p>
    </div>
""", unsafe_index=True)

# 🔒 Protection Tag & Status
st.sidebar.markdown("### 🔒 Security Horizon")
st.sidebar.success("Confidential Asset Secured")
st.sidebar.info("National ID: 01010305468")

# 2. Dynamic Input Controls (Sidebar Sliders)
st.sidebar.markdown("## ⚙️ Simulation Controls / مدخلات المحاكاة")

target_tonnage = st.sidebar.slider(
    "Annual Production Volume (Tons) / حجم الإنتاج السنوي (طن)", 
    min_value=100000, max_value=2000000, value=500000, step=50000
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💵 Customize Pricing / تعديل أسعار الطن ($)")
price_tier1 = st.sidebar.number_input("Tier 1: Raw Sand / الخام", value=20)
price_tier2 = st.sidebar.number_input("Tier 2: Refined Powder / المكرر", value=250)
price_tier3 = st.sidebar.number_input("Tier 3: HPQ Quartz / فائق النقاء", value=4000)
price_tier4 = st.sidebar.number_input("Tier 4: Breton Slabs / الألواح", value=3500)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📉 Customize Budget / تعديل الميزانية")
custom_capex = st.sidebar.number_input("Total CAPEX / إجمالي الرأسمالي ($)", value=125000000, step=1000000)
custom_opex = st.sidebar.number_input("Annual OPEX / إجمالي التشغيلي ($)", value=45000000, step=1000000)

# 3. Core Financial Calculations Engine
rev_tier1 = (target_tonnage * 0.40) * price_tier1
rev_tier2 = (target_tonnage * 0.35) * price_tier2
rev_tier3 = (target_tonnage * 0.15) * price_tier3
rev_tier4 = (target_tonnage * 0.10) * price_tier4

total_gross_revenue = rev_tier1 + rev_tier2 + rev_tier3 + rev_tier4
net_annual_profit = total_gross_revenue - custom_opex
roi_percentage = (net_annual_profit / custom_capex) * 100
payback_months = (custom_capex / net_annual_profit) * 12 if net_annual_profit > 0 else float('inf')

# 4. Display Key Metrics Dashboard
col1, col2, col3, col4 = st.columns(4)
col1.metric("Gross Revenue / عوائد إجمالية", f"${total_gross_revenue:,.2f}")
col2.metric("Net Profit / صافي الأرباح السنوية", f"${net_annual_profit:,.2f}", delta=f"${net_annual_profit - 476750000:,.2f} vs Base")
col3.metric("ROI Efficiency / معدل العائد", f"{roi_percentage:.2f}%")
col4.metric("Payback Horizon / استرداد رأس المال", f"{payback_months:.1f} Months / شهور")

st.markdown("---")

# 5. Differentiated Revenue Tiers Visual Layout
st.markdown("## 📊 Revenue Distribution Matrix / توزيع تدفقات الإيرادات")
t1, t2, t3, t4 = st.columns(4)

with t1:
    st.subheader("🌾 Tier 1: Raw Sand")
    st.write(f"**Volume:** {target_tonnage*0.40:,.0f} Tons")
    st.info(f"**Revenue:** ${rev_tier1:,.2f}")

with t2:
    st.subheader("🧪 Tier 2: Refined Powder")
    st.write(f"**Volume:** {target_tonnage*0.35:,.0f} Tons")
    st.info(f"**Revenue:** ${rev_tier2:,.2f}")

with t3:
    st.subheader("☀️ Tier 3: Pure HPQ Quartz")
    st.write(f"**Volume:** {target_tonnage*0.15:,.0f} Tons")
    st.info(f"**Revenue:** ${rev_tier3:,.2f}")

with t4:
    st.subheader("💎 Tier 4: Breton Slabs")
    st.write(f"**Volume:** {target_tonnage*0.10:,.0f} Tons")
    st.info(f"**Revenue:** ${rev_tier4:,.2f}")

st.markdown("---")
st.caption("🔒 Legal Proprietary Warning: Exclusive industrial asset of Eng. Awsan Adel and Awsan Dew For Marketing Services. Unauthorized deployment is legally prohibited.")
