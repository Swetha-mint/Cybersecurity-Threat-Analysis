#SOURCE CODE
import pandas as pd
import matplotlib.pyplot as plt

# -------- LOGIN SYSTEM --------
print("========== LOGIN REQUIRED ==========")
username = "admin"
password = "123"

u = input("Enter Username: ")
p = input("Enter Password: ")

if u == username and p == password:
    print("\n✔ Login Successful!\n")
else:
    print("❌ Access Denied!")
    exit()

# -------- LOAD DATA --------
df = pd.read_csv("C:\\Users\\Hp\\Downloads\\Global_Cybersecurity_Threats_2015-2024 (1).csv")
print("✔ Data Loaded Successfully!\n")

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Clean columns for safe filtering
df["Country_clean"] = df["Country"].astype(str).str.strip().str.lower()
df["Attack_clean"] = df["Attack Type"].astype(str).str.strip().str.lower()
df["Industry_clean"] = df["Target Industry"].astype(str).str.strip().str.lower()
df["Year_clean"] = pd.to_numeric(df["Year"], errors='coerce')

# -------- MAIN MENU LOOP --------
while True:
    print("""
=================== MAIN MENU ===================
1. Help / Instructions
2. View Sample Data
3. Sorting Options
4. Filter Data
5. Insights / Auto Report
6. Cybersecurity Quiz
7. Interactive Graphs
8. Bar Graph - Country vs Number of Affected Users
9. Line Graph - Year vs Average Financial Loss
10. Pie Chart - Attack Type Distribution
11. Bar Graph - Industry vs Number of Incidents
12. Trend Analysis - Attack Types (Year-wise)
13. Trend Analysis - Industries (Year-wise)
14. Trend Analysis - Financial Loss (Year-wise)
15. Trend Prediction - Next Year Financial Loss
16. Overall Trend Analysis
17. Summary Statistics
18. Exit
""")
    choice = input("Type your choice: ").strip()

    # -------- 1. HELP / INSTRUCTIONS --------
    if choice == "1":
        print("""
==================== HELP / INSTRUCTIONS ====================

This project analyzes global cybersecurity data using:
→ Menu-driven Python program  
→ Sorting, Searching, Filtering  
→ Data Visualization (Graphs)  
→ Statistical Summary  
→ Cybersecurity Quiz  
→ Auto-generated Reports  

You can:
• View sample data  
• Sort data (high → low or low → high)
• Filter by multiple conditions  
• View interactive graphs  
• Test your cybersecurity knowledge  
• Generate insights/report  

=============================================================
""")

    # -------- 2. SAMPLE DATA --------
    elif choice == "2":
        print("\n========= SAMPLE DATA =========\n")
        print(df.head(10))

    # -------- 3. SORTING --------
    elif choice == "3":
        print("""
========= SORTING MENU =========
1. Sort by Financial Loss (High → Low)
2. Sort by Affected Users (High → Low)
3. Sort by Year (Old → New)
""")
        s = input("Type your choice: ").strip()
        if s == "1":
            print(df.sort_values("Financial Loss (in Million $)", ascending=False).head(10))
        elif s == "2":
            print(df.sort_values("Number of Affected Users", ascending=False).head(10))
        elif s == "3":
            print(df.sort_values("Year", ascending=True).head(10))
        else:
            print("❌ Invalid Choice")

    # -------- 4. FILTER DATA (UPDATED) --------
    elif choice == "4":
        while True:
            print("\n========= FILTER MENU =========")
            print("1. Industry & Attack Type Filter")
            print("2. Country-wise Yearly Summary")
            print("3. Back to Main Menu")

            filter_choice = input("\nType your choice: ").strip()

            # -------- OPTION 1: Industry & Attack Type Filter --------
            if filter_choice == "1":
                print("\nAvailable Attack Types:")
                print(['DDoS', 'Malware', 'Man-in-the-Middle', 'Phishing', 'Ransomware', 'SQL Injection'])
                print("\nAvailable Industries:")
                print(['Banking', 'Education', 'Government', 'Healthcare', 'IT', 'Retail', 'Telecommunications'])

                attack_input = input("\nType Attack Type (or press Enter to skip): ").strip().lower()
                industry_input = input("Type Industry (or press Enter to skip): ").strip().lower()

                filtered_df = df.copy()
                if attack_input:
                    filtered_df = filtered_df[df["Attack_clean"] == attack_input]
                if industry_input:
                    filtered_df = filtered_df[df["Industry_clean"] == industry_input]

                if filtered_df.empty:
                    print("\n❌ No matching records found.")
                else:
                    print("\n✔ FILTERED DATA:\n")
                    print(filtered_df[[
                        "Country", "Year", "Attack Type", "Target Industry",
                        "Financial Loss (in Million $)", "Number of Affected Users"
                    ]])

            # -------- OPTION 2: Country-wise Yearly Summary --------
            elif filter_choice == "2":
                print("\nAvailable Countries:")
                print(sorted(df["Country"].dropna().unique()))
                print("\nAvailable Years:")
                print(sorted(df["Year"].dropna().unique()))

                country_input = input("\nType Country (or press Enter to skip): ").strip().lower()
                year_input = input("Type Year (or press Enter to skip): ").strip()

                filtered_df = df.copy()
                if country_input:
                    filtered_df = filtered_df[df["Country_clean"] == country_input]
                if year_input.isdigit():
                    filtered_df = filtered_df[filtered_df["Year_clean"] == int(year_input)]

                if filtered_df.empty:
                    print("\n❌ No matching records found.")
                else:
                    print("\n✔ FILTERED DATA:\n")
                    print(filtered_df[[
                        "Country", "Year", "Attack Type", "Target Industry",
                        "Financial Loss (in Million $)", "Number of Affected Users"
                    ]])

            # -------- OPTION 3: BACK TO MAIN MENU --------
            elif filter_choice == "3":
                print("Returning to Main Menu...")
                break

            else:
                print("❌ Invalid choice! Please try again.")

    # -------- 5. AUTOMATIC INSIGHTS --------
    elif choice == "5":
        print("\n================= CYBERSECURITY INSIGHTS REPORT =================")
        top_country = df.groupby("Country")["Number of Affected Users"].sum().idxmax()
        top_attack = df["Attack Type"].value_counts().idxmax()
        top_year = df["Year"].value_counts().idxmax()
        max_loss_year = df.groupby("Year")["Financial Loss (in Million $)"].sum().idxmax()

        print("Most Attacked Country:", top_country)
        print("Most Common Attack Type:", top_attack)
        print("Year with Most Attacks:", top_year)
        print("Year with Highest Financial Loss:", max_loss_year)
        print("=================================================================")

    # -------- 6. CYBERSECURITY QUIZ --------
    elif choice == "6":
        print("\n========= CYBERSECURITY QUIZ =========")
        score = 0

        print("\n1) What is Phishing?")
        print("a) Fake emails to steal data")

        print("b) Hardware failure")
        print("c) Strong password")
        ans = input("Type your answer: ").lower()
        if ans == "a":
            score += 1

        print("\n2) What does Ransomware do?")
        print("a) Displays ads")
        print("b) Locks your data for ransom")
        print("c) Cleans virus")
        ans = input("Type your answer: ").lower()
        if ans == "b":
            score += 1

        print("\n3) Strong password includes?")
        print("a) Only letters")
        print("b) Letters, numbers, symbols")
        print("c) Only numbers")
        ans = input("Type your answer: ").lower()
        if ans == "b":
            score += 1

        print("\n✔ Your Score:", score, "/3")

    # -------- 7. INTERACTIVE GRAPHS --------
    elif choice == "7":
        while True:
            print("""
========= GRAPH OPTIONS =========
1. Year-wise Financial Loss (range)
2. Country vs Affected Users
3. Attack Type Trend
4. Back
""")
            g = input("Type your choice: ").strip()

            # Graph 1: Year range
            if g == "1":
                start = int(input("Start Year: "))
                end = int(input("End Year: "))
                sub = df[(df["Year"] >= start) & (df["Year"] <= end)]
                loss = sub.groupby("Year")["Financial Loss (in Million $)"].sum()
                plt.plot(loss.index, loss.values, marker="o")
                plt.title("Financial Loss from " + str(start) + " to " + str(end))
                plt.xlabel("Year")
                plt.ylabel("Loss (Million $)")
                plt.show()

            # Graph 2: Selected countries
            elif g == "2":
                print("Available countries:")
                print(df["Country"].unique())
                c = input("Type countries separated by comma: ").title().split(",")
                sub = df[df["Country"].isin([i.strip() for i in c])]
                data = sub.groupby("Country")["Number of Affected Users"].sum()
                data.plot(kind="bar")
                plt.title("Selected Countries vs Affected Users")
                plt.show()

            # Graph 3: Attack Type Trend
            elif g == "3":
                print("Available attack types:")
                print(df["Attack Type"].unique())
                a = input("Type Attack Type: ").title()
                sub = df[df["Attack Type"] == a]
                trend = sub.groupby("Year").size()
                plt.plot(trend.index, trend.values, marker='o')
                plt.title("Trend of " + a + " Attacks")
                plt.show()

            elif g == "4":
                break
            else:
                print("❌ Invalid choice!")


    # -------- 8. COUNTRY BAR GRAPH --------
    elif choice == "8":
        country_data = df.groupby("Country")["Number of Affected Users"].sum()
        plt.bar(country_data.index, country_data.values)
        plt.xticks(rotation=45)
        plt.title("Country vs Number of Affected Users")
        plt.show()

    # -------- 9. YEAR vs FINANCIAL LOSS --------
    elif choice == "9":
        year_loss = df.groupby("Year")["Financial Loss (in Million $)"].mean()
        plt.plot(year_loss.index, year_loss.values, marker='o')
        plt.title("Year-wise Average Financial Loss")
        plt.show()

    # -------- 10. PIE CHART - ATTACK TYPE --------
    elif choice == "10":
        attack_type = df["Attack Type"].value_counts()
        plt.pie(attack_type.values, labels=attack_type.index, autopct='%1.1f%%')
        plt.title("Attack Type Distribution")
        plt.show()

    # -------- 11. BAR CHART - INDUSTRY --------
    elif choice == "11":
        industry_data = df["Target Industry"].value_counts()
        plt.bar(industry_data.index, industry_data.values)
        plt.xticks(rotation=45)
        plt.title("Number of Cybersecurity Incidents by Industry")
        plt.show()

    # -------- 12. TREND ANALYSIS - ATTACK TYPES --------
    elif choice == "12":
        attack_trend = df.groupby(["Year", "Attack Type"]).size().unstack(fill_value=0)
        attack_trend.plot(kind="line", marker="o")
        plt.title("Trend of Attack Types Over Years")
        plt.show()

    # -------- 13. TREND ANALYSIS - INDUSTRIES --------
    elif choice == "13":
        industry_trend = df.groupby(["Year", "Target Industry"]).size().unstack(fill_value=0)
        industry_trend.plot(kind="line", marker="o")
        plt.title("Trend of Target Industry Attacks Over Years")
        plt.show()

    # -------- 14. TREND ANALYSIS - FINANCIAL LOSS --------
    elif choice == "14":
        financial_trend = df.groupby("Year")["Financial Loss (in Million $)"].sum()
        financial_trend.plot(kind="line", marker='o')
        plt.title("Year-wise Total Financial Loss")
        plt.show()

    # -------- 15. PREDICTION --------
    elif choice == "15":
        print("\n==== PREDICTION: NEXT YEAR FINANCIAL LOSS ====\n")

        yearly_loss = df.groupby("Year")["Financial Loss (in Million $)"].sum()
        years = list(yearly_loss.index)
        losses = list(yearly_loss.values)

        if len(losses) < 2:
            print("Not enough data to predict!")
        else:
            increase = losses[-1] - losses[-2]
            next_year = years[-1] + 1
            predicted_loss = losses[-1] + increase

            print("Last year:", years[-1], "Loss:", losses[-1])
            print("Year before:", years[-2], "Loss:", losses[-2])
            print(f"\nPredicted Financial Loss for {next_year}: {predicted_loss:.2f} Million $")

    # -------- 16. OVERALL TREND ANALYSIS --------
    elif choice == "16":
        attacks_year = df.groupby("Year").size()
        loss_year = df.groupby("Year")["Financial Loss (in Million $)"].sum()
        plt.plot(attacks_year.index, attacks_year.values, marker='o', label="Total Attacks")
        plt.plot(loss_year.index, loss_year.values, marker='s', label="Financial Loss")
        plt.legend()
        plt.title("Overall Cybersecurity Trends")
        plt.show()

    # -------- 17. SUMMARY STATISTICS --------
    elif choice == "17":
        print(df.describe(include='all'))

    # -------- 18. EXIT --------
    elif choice == "18":
        print("✔ Exiting Program...")
        break

    else:
        print("❌ Invalid Input!")