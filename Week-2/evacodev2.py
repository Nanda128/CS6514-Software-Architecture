import json
from datetime import datetime

import matplotlib.pyplot as plt

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []
selected_country = "USA"
country_totals = {}

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")
    country = eva.get("country")

    if not date_text or not duration_text or not country:
        continue

    try:
        date = datetime.fromisoformat(date_text)
        hours, minutes = map(int, duration_text.split(":"))
        duration_hours = hours + minutes / 60
    except (TypeError, ValueError):
        print("Malformed time/duration")
        continue

    records.append((date, duration_hours))
    country_totals[country] = country_totals.get(country, 0.0) + duration_hours

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

for date, duration_hours in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)

country_total_hours = country_totals.get(selected_country, 0.0)
print(f"{selected_country} total EVA duration: {country_total_hours:.2f} hours")
plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
