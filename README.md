# Shark Incident Analysis: Fatality Rates & Insurance Risk

This repository contains a comprehensive analysis of global shark incident data, focusing on trends in Australia, age-based risk factors, and the distinction between volume and severity for insurance underwriting.

---

## 🦈 H1: Fatal Shark Incidents in Australia Over Time

### Findings
* **Fatal incidents** have not risen dramatically in absolute terms.
* **Total incidents** have exploded: from **86 (1920s)** to **242 (2010s)**—nearly triple.
* **Fatality Share:** Dropped substantially. Early 1900s encounters were often fatal; modern encounters are much less so.

### Conclusions
* **Status:** Partially supported but misleading in framing.
* Raw counts are slightly elevated compared to the late 1900s but remain below the historical highs of the 1920s and 30s.
* **The "Real Story":** Increased exposure (more people in water) combined with better beach monitoring and medical response. Sharks aren't deadlier; we are better at surviving.

> [!TIP]
> **Recommendations for Insurers**
> * **Price by Severity:** Don't price Australian risk as "deadlier." Each incident is statistically less severe than in previous decades.
> * **Volume vs. Catastrophe:** Expect a higher frequency of claims but a lower average cost per claim regarding fatalities.
> * **Weight Recent Data:** Use recent decades for pricing models; 1920s fatality rates are no longer actuarially relevant.

---

## 🌏 H2: Volume vs. Fatality Rate Across Countries

### Findings
* **High-volume ≠ High-fatality:**
    * **USA:** 2,221 incidents | **7.9%** fatality rate.
    * **Papua New Guinea:** 123 incidents | **44%** fatality rate.
* **The "Provoked" Paradox:** Provoked incidents are actually **less fatal** than unprovoked ones.
    * **USA:** Drops to 1.7% when provoked.
    * **Australia:** Drops to 1.4% when provoked.

### Conclusions
* **Status:** Partially supported. The volume mismatch is real, but the "provoked" severity trend was the opposite of expectations.
* **Risk Profiles:** Provoked = High-frequency/Low-severity. Unprovoked = Low-frequency/High-severity.

> [!IMPORTANT]
> **Recommendations for Insurers**
> * **Geography is King:** Set prices country-by-country. A global average overcharges the USA and under-reserves for PNG.
> * **Focus on Unprovoked:** Big payouts come from unprovoked attacks. Focus reserve-setting on these rare, high-severity events.

---

## 👤 H3: Fatality Rate by Age

### Findings
* **The Step Function:** Risk does not rise linearly with age.
* **Lowest Risk:** Children (0-9), likely due to close supervision and shallow water usage.
* **Highest Risk:** A clear jump occurs at **50+**, with **60+** being the highest-risk group.

### Conclusions
* **Status:** Partially supported.
* **Driver:** Survivability, not frequency. Older victims are not targeted more often; they simply have a lower physiological capacity to survive severe trauma and slower rescue response times.

> [!CAUTION]
> **Recommendations for Insurers**
> * **Age Loadings:** Apply premium increases starting at age 50, with a significant step at 60+.
> * **Family Discounts:** Consider the 0-9 age group for reduced premiums.
> * **The "Danger Zone":** The highest risk segment is an older traveler (60+) in a high-severity country (e.g., PNG or Hong Kong).

---

## 📊 H4: Overall Incident Profile

### Findings
* **Concentration:** Incidents are heavily clustered in the USA, Australia, and South Africa.
* **Hotspots:** Florida, New South Wales, and California.
* **Activity Risk:** **Surfing** has the highest volume but a lower fatality rate. **Swimming** shows much higher fatality rates.

### Conclusions
* Risk is not evenly distributed. It is highly concentrated by location, activity, and incident type.
* Unprovoked incidents remain the primary driver for underwriting and claims severity.

> [!NOTE]
> **Recommendations for Insurers**
> * Treat **Activity Type** as a key severity factor (Swimming > Surfing).
> * Avoid relying on incident counts alone; volume is a poor proxy for fatality risk.
> * Combine location, activity, and incident type into a multi-factor risk model.

---

## ⚠️ Caveats & Data Limitations
* **Historical Bias:** Records from 1780–1860 are sparse and were excluded from fatality rate conclusions.
* **Incomplete Data:** 2,727 rows were dropped due to missing ages; this may bias the age-based findings.
* **Reporting Bias:** Old records are likely incomplete, particularly for non-fatal encounters.
* **Scope:** This analysis is specific to Australia and major global hotspots; results may not generalize to emerging regions.
