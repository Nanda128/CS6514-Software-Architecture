import json
from datetime import datetime

import matplotlib.pyplot as plt

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)


def get_country(prompt):
    while True:
        country = input(prompt).strip()
        if country in ("USA", "Russia"):
            return country
        if country == "USSR":
            return "Russia"
        if country == "America":
            return "USA"
        print("Invalid country. Please enter USA, Russia, or USSR.")


records = []
first_country = get_country("Enter the first country (USA, Russia, or USSR): ")
second_country = get_country("Enter the second country (USA, Russia, or USSR): ")
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

first_country_total = country_totals.get(first_country, 0.0)
second_country_total = country_totals.get(second_country, 0.0)
print(f"{first_country} total EVA duration: {first_country_total:.2f} hours")
print(f"{second_country} total EVA duration: {second_country_total:.2f} hours")

if first_country_total > second_country_total:
    greater_country = first_country
elif second_country_total > first_country_total:
    greater_country = second_country
else:
    greater_country = "Neither country; both totals are equal"

print(f"Greater total: {greater_country}")
plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
