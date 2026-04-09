import pandas as pd
import re
from tabulate import tabulate
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def clean_fatal(val):
    val = str(val).strip().upper()
    if val == 'Y': return 1
    if val in ['N', 'N ', ' N']: return 0
    return None


def clean_age(val):
    val = str(val).lower()
    if 'teen' in val: return 15
    nums = re.findall(r'\d+', val)
    if nums: return int(nums[0])
    return None


def load_file_and_clean(url):
    print("Connecting to database and fetching latest records...")

    # Using 'xlrd' engine because the file extension is .xls
    # If you get an error here, run: pip install xlrd
    df = pd.read_excel(url, engine='xlrd')
    time.sleep(1)

    print("\nWohoo, Data is fetched successfully !!")

    # Data Cleaning logic
    df['Is_Fatal'] = df['Fatal Y/N'].apply(clean_fatal)
    df['Age_Clean'] = df['Age'].apply(clean_age)
    df['Country'] = df['Country'].str.strip().str.upper()

    # Filtering for modern historical data
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df[(df['Year'] >= 1900) & (df['Year'] <= 2026)].copy()

    # Dropping noise columns
    cols_to_drop = ['Unnamed: 22', 'Unnamed: 21', 'original order', 'Case Number',
                    'Case Number.1', 'href', 'href formula', 'pdf']
    df = df.drop(columns=cols_to_drop, errors='ignore')
    return df


def run_summary(df):
    print("\n" + "=" * 70)
    print("       GLOBAL SHARK ATTACK RISK ANALYSIS: EXECUTIVE SUMMARY       ")
    print("=" * 80)
    time.sleep(1)

    # Global Metrics
    print(f"OVERALL MARKET SCOPE:")
    print(f"- Total Validated Incidents: {len(df):,}")

    # Calculate average fatality while ignoring None values
    fatality_rate = df['Is_Fatal'].mean()
    print(f"- Global Avg. Fatality Rate: {fatality_rate:.2%}")
    print("-" * 80)
    time.sleep(1)
    # Top 10 Countries
    print("\n[TABLE 1] REGIONAL RISK: TOP 10 COUNTRIES")
    country_counts = df['Country'].value_counts().head(10).reset_index()
    country_counts.columns = ['Country', 'Incident Count']
    print(tabulate(country_counts, headers='keys', tablefmt='fancy_grid', showindex=False))
    time.sleep(1)

    # Top 10 Activities
    print("\n[TABLE 2] ACTIVITY RISK PROFILE")
    activity_analysis = df.groupby('Activity')['Is_Fatal'].agg(['count', 'mean'])
    activity_analysis = activity_analysis.sort_values(by='count', ascending=False).head(10).reset_index()
    activity_analysis.columns = ['Activity', 'Volume', 'Fatality Rate']
    activity_analysis['Fatality Rate'] = activity_analysis['Fatality Rate'].map(lambda x: f"{x:.2%}")
    print(tabulate(activity_analysis, headers='keys', tablefmt='fancy_grid', showindex=False))

    # D. Recommendations
    print("-" * 80)
    print("INSURANCE RECOMMENDATIONS & RISK INSIGHTS:")
    print("1. Apply 'High-Severity' surcharges for activities with Fatality Rates > 20%.")
    print("2. Focus volume-based pricing in USA and AUSTRALIA.")
    print(
        f"3. High-risk age demographic identified: {df[df['Age_Clean'] <= 19]['Age_Clean'].count()} incidents involve minors/teens.")
    print("4. Target 61+ age demographics for specialized adventure riders based on emerging trends.")