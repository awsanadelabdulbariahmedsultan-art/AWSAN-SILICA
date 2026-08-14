# ====================================================================
# 🌍 AWSAN SILICA PROJECT - AUTOMATED CAPEX EXCEL SHEET GENERATOR
# Powered by: Eng. Awsan Adel Abdulbari Ahmed Sultan
# Owned by: Awsan Dew For Marketing Services (Yemen)
# ====================================================================

import pandas as pd

def generate_capex_excel():
    # 1. Define the detailed capital expenditure (CAPEX) dataset
    capex_data = {
        "Asset ID / رمز الأصل": ["CPX-01", "CPX-02", "CPX-03", "CPX-04", "CPX-05", "CPX-06"],
        "Partner Company / الشريك الدولي": [
            "Eriez Magnetics (USA)", 
            "Metso Outotec (Finland)", 
            "TOMRA Mining (Germany)", 
            "Breton S.p.A. (Italy)", 
            "Smart Solar Grid Hub", 
            "Logistics & Warehouses"
        ],
        "Equipment Scope / نطاق المعدات الفنية والمدنية": [
            "High-Intensity Rare Earth Electromagnetic Drums (HGMS) / الفصل المغناطيسي",
            "Ceramic-Lined Vertical Grinding Mills (VTM) & Flotation Cells / الطحن والتعويم",
            "Dual-Channel Laser Sorters & ISO 5 Cleanroom Matrices / الفرز البصري والأحماض",
            "Patented BretonStone Vacuum-Vibro-Compression Production Lines / كبس الألواح الفاخرة",
            "50 MW Bifacial Monocrystalline Solar Array & 120 MWh BESS / شبكة الطاقة والبطاريات",
            "62,000 m² Climate-Controlled AS/RS Smart Inventory Hub / المخازن اللوجستية الذكية"
        ],
        "Acquisition Cost / كلفة الشراء ($)":,
        "Civil & Integration / التركيب والمدني ($)": [2500000, 6000000, 4000000, 9000000, 2500000, 2000000]
    }

    # 2. Create DataFrame and compute individual line totals
    df = pd.DataFrame(capex_data)
    df["Total Line CAPEX / إجمالي الخط ($)"] = df["Acquisition Cost / كلفة الشراء ($)"] + df["Civil & Integration / التركيب والمدني ($)"]
    
    # 3. Compute grand totals and append total row
    total_acq = df["Acquisition Cost / كلفة الشراء ($)"].sum()
    total_civil = df["Civil & Integration / التركيب والمدني ($)"].sum()
    grand_capex = df["Total Line CAPEX / إجمالي الخط ($)"].sum()
    
    totals_row = {
        "Asset ID / رمز الأصل": "TOTAL CAPEX",
        "Partner Company / الشريك الدولي": "🔒 NET PROJECT CAPEX",
        "Equipment Scope / نطاق المعدات الفنية والمدنية": "إجمالي الاستثمار الرأسمالي والتأسيسي الكلي للمشروع",
        "Acquisition Cost / كلفة الشراء ($)": total_acq,
        "Civil & Integration / التركيب والمدني ($)": total_civil,
        "Total Line CAPEX / إجمالي الخط ($)": grand_capex
    }
    
    df = pd.concat([df, pd.DataFrame([totals_row])], ignore_index=True)

    # 4. Export to Excel
    target_filename = "capex_machinery_cost.xlsx"
    with pd.ExcelWriter(target_filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="CAPEX Budget 2026", index=False)
    
    print("====================================================================")
    print(f"✅ SUCCESS: Excel file '{target_filename}' generated successfully!")
    print(f"• Total Project CAPEX Fully Capitalized: \${grand_capex:,} USD")
    print(f"• System Authentication Tag: Powered by Eng. Awsan Adel")
    print("====================================================================")

if __name__ == "__main__":
    generate_capex_excel()
