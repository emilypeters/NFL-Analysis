import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\emily\\Downloads\\team_stats_2003_2023.csv")

bills_data = (df[df["team"] == "Buffalo Bills"])

avg_turnover_pct = bills_data["turnover_pct"].mean()
avg_wins = bills_data["wins"].mean()

year = bills_data["year"]
wins = bills_data["wins"]

plt.plot(year, wins)

plt.title("Buffalo Bills Wins over the Years")
plt.xlabel("Year")
plt.ylabel("Wins")

plt.show()
