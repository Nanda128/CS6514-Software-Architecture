# Software Architecture Notebook

By: Nandakishore Vinayakrishnan - 23070854

## Manual analysis of the EVA JSON data(Meet the data)

- How is the JSON Data organized?
  - What does one record represent?
    - One Record is meant to represent one individual EVA event, where either an American or Russian astronaut performed an EVA maneuver.
  - Which fields appear in a record?
    - "eva": An index of each event, starting at 1 and increases by 1
    - "country": The country of the astronaut performing the EVA maneuver.
    - "crew": A semicolon-separated list of the names of astronauts that performed the EVA maneuvers.
    - "vehicle": The name of the vessel that the EVA maneuver was performed from.
    - "date": Date in YYYY-MM-DD of the EVA maneuver.
    - "duration": Duration of the EVA maneuver in HH:MM
    - "purpose": Likely meant to be a short description of the purpose of the EVA maneuver, however is a log of the event itself

- What are the data quality issues?
  - Does every record contain exactly the same fields
    - No, some records are missing an "eva" field, some are missing a "purpose" field, some are missing "dates".
  - How are dates represented?
    - In the format YYYY-MM-DDTHH:MM:SSZ
  - How is EVA duration represented?
    - In the format HH:MM
  - Are there missing, empty, or unusual values?
    - Some records have missing or empty values for "duration" or "purpose".
    - The purpose field is often a log of the event itself, rather than a short description of the purpose of the EVA maneuver. Probably needs change of column name to "log" or "description" to better reflect data.
    - The duration is sometimes unclear on if its HH:MM or just MM:SS.
    - Bad escaping of special characters in the "purpose" field may lead to errors when parsing the JSON data.

- What are the implications of the data quality for the code that will use the data?
  - Developers will need to spend time cleaning and validating the data before it can be used meaningfully.
  - This may involve accounting for missing values, filling in where needed, and addressing inconsistencies in the data format.
  - Developers may also spend more time than needed to determine if the duration is in HH:MM or MM:SS format.

## Software Raconteur Notebook (Meet the code)

- Q: What does the program do?
  - The program plots the amount of cumulative time spent on EVA year-over-year
- Q: Where does execution begin?
  - Line 5
- Q: What data does it read?
  - data.json, which is intended to be a file formatted similar to eva-data.json.
- Q: How is data.json used?
  - data.json is used to extract data from it, and the program doesnt change anything within the physical file. It extracts the data to plot the cumulative time spent on EVA year-by-year
- Q:What outputs does the program produce?
  - A line plot diagram with the X-axis as year vs. Y-axis as Cumulative EVA duration in hours
- Q: What variables appear important?
  - date, duration from the data.json file, which it then uses to calculate cumulative hours per year.
- Q: How are EVA durations converted?
  - EVA durations are converted into hours and decimals of hours by adding the minutes divided by 60 to the hour count.
- Q: How is cumulative EVA time calculated?
  - The EVA durations are added onto the hours from other entries from the same year, and appended onto a "cumulative_hours" array. This creates an ordered array of the cumulative hours against each year.
- Q: Which parts of the code depend on other parts?
  - The plotting code relies on the initial for loop at line 10 to create a records data list that has both the date and duration in hours calculated. The plotting system also requires the cumulative duration calculated via the for loop in line 29.
  - The plotting code relies on the matplotlib library.
- Q: Are any pieces of the code repeated?
- Q: Which parts are immediately understandable?
  - I found all code besides the code within the last for loop (29-32) to be immediately understandable.
- Q: Which parts require more effort to understand?
  - I found that the code used to calculate the cumulative hours would be a little difficult to understand.
- Q: What would you be nervous about changing?
  - I would be nervous about changing the code in lines 17-19, since minor changes can vastly break the future code.
