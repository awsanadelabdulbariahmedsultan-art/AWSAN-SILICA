# ====================================================================
# 🌍 AWSAN SILICA PROJECT - REVENUE PROJECTION & ROI EXCEL GENERATOR
# Powered by: Eng. Awsan Adel Abdulbari Ahmed Sultan
# Owned by: Awsan Dew For Marketing Services (Yemen)
# ====================================================================

import pandas as pd

def generate_revenue_excel():
    # 1. Define product tiers and value-addition multiplier metrics
    revenue_data = {
        "Product Tier / مستوى المنتج النهائي": [
            "Tier 1: Raw White Sand / الرمل الأبيض الخام",
            "Tier 2: Refined Micro-Powder / مسحوق السيليكا المكرر",
            "Tier 3: High-Purity Quartz (HPQ) / الكوارتز فائق النقاء",
            "Tier 4: Polished BretonStone Slabs / ألواح الكوارتز الفاخرة"
        ],
        "Target Industry / القطاع المستهدف": [
            "Construction & Basic Foundry / البناء والسباكة التقليدية",
            "Premium Optics & Luxury Glass / البصريات والزجاج الفاخر",
            "Solar Photovoltaic & Semiconductors / الألواح الشمسية والرقائق",
            "Luxury Architecture & Medical Cleanrooms / العمارة والأسطح الطبية"
        ],
        "Annual Yield (Tons) / حجم الإنتاج السنوي (طن)":,
        "Price per Ton (USD) / سعر الطن ($)": [20, 250, 4000, 3500]
    }

    df = pd.DataFrame(revenue_data)
    df["Projected Revenue / العائد السنوي المتوقع ($)"] = df["Annual Yield (Tons) / حجم الإنتاج السنوي (طن)"] * df["Price per Ton (USD) / سعر الطن ($)"]
    
    # Compute totals
    total_tonnage = df["Annual Yield (Tons) / حجم الإنتاج السنوي (طن)"].sum()
    total_gross_revenue = df["Projected Revenue / العائد السنوي المتوقع ($)"].sum()
    
    # 2. Financial Viability Calculations & Summary Sheet Creation
    capex = 125000000
    opex = 45000000
    net_annual_profit = total_gross_revenue - opex
    roi_percentage = (net_annual_profit / capex) * 100
    payback_months = (capex / net_annual_profit) * 12

    summary_data = {
        "Financial Viability Indicator / مؤشر الكفاءة المالية لمؤسسة أوسان دو": [
            "Total Capital Expenditure (CAPEX) / إجمالي الاستثمار الرأسمالي",
            "Annual Operational Expenditure (OPEX) / إجمالي النفقات التشغيلية السنوية",
            "Projected Gross Annual Revenue / إجمالي الإيرادات السنوية الإجمالية",
            "💰 NET ANNUAL CASH FLOW (NET PROFIT) / صافي الأرباح السنوية المباشرة",
            "Return on Investment (ROI) Efficiency / معدل العائد الفعلي على الاستثمار",
            "Capital Payback Period (Months) / فترة استرداد رأس المال بالشهور"
        ],
        "Computed Value / القيمة المحسوبة رقمياً": [
            f"${capex:,}",
            f"${opex:,}",
            f"${total_gross_revenue:,}",
            f"${net_annual_profit:,}",
            f"{roi_percentage:.2f}%",
            f"{payback_months:.1f} Months / شهور"
        ]
    }
    df_summary = pd.DataFrame(summary_data)

    # 3. Export both sheets into a single structured workbook
    target_filename = "revenue_projection_model.xlsx"
    with pd.ExcelWriter(target_filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Revenue Breakdown By Tier", index=False)
        df_summary.to_excel(writer, sheet_name="ROI & Financial Viability", index=False)
    
    print("====================================================================")
    print(f"✅ SUCCESS: Multi-sheet Excel workbook '{target_filename}' generated!")
    print(f"• Net Annual Profit Forecasted: \$\t{net_annual_profit:,} USD")
    print(f"• Capital Payback Velocity: {payback_months:.1f} Months")
    print(f"• System System Tag: Powered by Eng. Awsan Adel")
    print("====================================================================")

if __name__ == "__main__":
    generate_revenue_ex
  cel()
