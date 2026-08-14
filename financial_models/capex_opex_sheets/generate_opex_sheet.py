# ====================================================================
# 🌍 AWSAN SILICA PROJECT - AUTOMATED OPEX EXCEL SHEET GENERATOR
# Powered by: Eng. Awsan Adel Abdulbari Ahmed Sultan
# Owned by: Awsan Dew For Marketing Services (Yemen)
# ====================================================================

import os
import pandas as pd

def generate_opex_excel():
    # 1. Define the detailed operational cost ledger data
    opex_data = {
        "Cost Center ID / رمز البند": [
            "OPX-LOG-01", "OPX-LOG-02", "OPX-LOG-03", "OPX-LOG-04",
            "OPX-CHM-01", "OPX-CHM-02", "OPX-CHM-03",
            "OPX-HR-01", "OPX-HR-02", "OPX-HR-03"
        ],
        "Category / القطاع التشغيلي": [
            "Logistics / اللوجستيات", "Logistics / اللوجستيات", "Logistics / اللوجستيات", "Logistics / اللوجستيات",
            "Chemicals / الكيماويات", "Chemicals / الكيماويات", "Chemicals / الكيماويات",
            "Human Capital / الأجور", "Human Capital / الأجور", "Human Capital / الأجور"
        ],
        "Cost Description / تفصيل النفقة التشغيلية": [
            "Inland Heavy Trucking (Sana'a/Shabwah to Ports) / النقل البري للموانئ",
            "Socotra Eco-Conveyor & Suction Sourcing Maintenance / سيور سقطرى البيئية",
            "International Maritime Freight Cargo & Port Clearing / الشحن البحري الدولي",
            "Global Cargo Logistics Insurance Coverage / التأمين الشامل على البضائع",
            "Eco-friendly Organic Frothers & Collectors (Metso) / مواد التعويم الرغوي",
            "Hot Vapor Hydrochloric/Hydrofluoric Acids (Leaching) / أحماض الغسيل الساخن",
            "Vacuum Chamber Chlorine Gas Processing (TOMRA) / غاز الكلور للتنقية الفائقة",
            "International Mining Experts & Senior Consultants / المستشارين والخبراء الدوليين",
            "Domestic Technical Labor & Quarry Control Staff / العمالة والمهندسين محلياً",
            "Awsan Dew Corporate Management Overhead / إدارة مؤسسة أوسان دو والعموميات"
        ],
        "Annual Cost in USD / الكلفة السنوية ($)": [
            8500000, 1500000, 11000000, 3000000,
            4500000, 7000000, 3500000,
            2500000, 2000000, 1500000
        ]
    }

    # 2. Create the DataFrame
    df = pd.DataFrame(opex_data)
    
    # 3. Add a Totals Row programmatically
    total_opex = df["Annual Cost in USD / الكلفة السنوية ($)"].sum()
    totals_row = {
        "Cost Center ID / رمز البند": "TOTAL OPEX",
        "Category / القطاع التشغيلي": "🔒 NET ANNUAL OPEX",
        "Cost Description / تفصيل النفقة التشغيلية": "إجمالي المصاريف التشغيلية السنوية الكلية للمشروع",
        "Annual Cost in USD / الكلفة السنوية ($)": total_opex
    }
    
    # Append the totals row to the DataFrame using concat
    df = pd.concat([df, pd.DataFrame([totals_row])], ignore_index=True)

    # 4. Set the exact export path matching the repository design
    target_filename = "opex_operational_cost.xlsx"
    
    # Use standard excel writer to generate the spreadsheet file
    with pd.ExcelWriter(target_filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="OPEX Ledgers 2026", index=False)
    
    print("====================================================================")
    print(f"✅ SUCCESS: Excel file '{target_filename}' generated successfully!")
    print(f"• Total Annualized OPEX Computed: \${total_opex:,} USD")
    print(f"• System System Tag: Powered by Eng. Awsan Adel")
    print("====================================================================")

if __name__ == "__main__":
    generate_opex_exc
  el()
