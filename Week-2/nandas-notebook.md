# Week 2 Nanda's Notebook

By Nandakishore Vinayakrishnan - 23070854

## First Round of Changes

### Prompt

• A researcher would like to know how much EVA time has been accumulated by a particular country.
• Add functionality that allows the program to report the total EVA duration for a selected country

### Notes

- Did I change more code than needed?
  - No, I made sure to minimize the amount of lines of code I added to minimize disturbance in other developers' reading of the code.
- Would another developer understand what I changed?
  - I feel that another developer would understand my changes, since I directly integrated my implementation with the existing logic. This makes it concise and reduces code repetition.
- Did I duplicate behavior that already existed elsewhere?
  - I didn't, instead I used existing behavior to remove the need for duplication. This also did not change the existing behavior of the system
- Are there any assumptions in my solution that another developer would need to discover?
  - I did the best I could to ensure that they would not need to have assumptions, and that the data is validated properly. I made sure to validate the country, date, and duration existing within the data.
- How confident am I that I have not broken existing behavior?
  - Deeply confident. I ran the system on my own and noticed I did not have any broken existing behavior, and I do not believe the same will reflect on other people's computers. However, there will be extra output lines that present the calculated hours.

## Second Round of Changes

### Implementation Notes

- Did I change more code than needed?
  - No, I reused the existing country totals and only added two inputs and a comparison.
- Would another developer understand what I changed?
  - Yes, the output clearly reports both totals and the country with the greater total.
- Did I duplicate behavior that already existed elsewhere?
  - No, both countries use the existing country_totals lookup.
- Are there any assumptions in my solution that another developer would need to discover?
  - Only USA, Russia, and USSR are accepted; USSR, America is normalized to Russia, USA.
- How confident am I that I have not broken existing behavior?
  - Confident, since the original cumulative chart and data processing remain unchanged.
