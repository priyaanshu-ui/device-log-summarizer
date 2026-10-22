# Prompt Log

## Initial Prompt

I need to build a Device Log Summarizer CLI tool in Python.

The tool should:
- Read device telemetry data from a CSV file.
- Group records by device_id.
- Calculate total records.
- Calculate average temperature.
- Count ERROR status records.
- Ignore devices whose average temperature is above 80°C.
- Export the summary to a JSON file.
- Print a readable summary in the terminal.

I also need the code to handle missing files and invalid CSV data gracefully.

## AI Bug / Formatting Issue

In the first attempt, the generated output/code formatting was not clear enough for the required terminal summary.

## Follow-up Prompt

Please fix the formatting of the terminal output so that each device is displayed clearly with its device ID, total records, average temperature, and error count. Also make sure the JSON output is correctly formatted and the program handles errors gracefully.

## Result

After applying the changes, the program was tested using the provided device telemetry CSV file and generated the required JSON summary successfully.