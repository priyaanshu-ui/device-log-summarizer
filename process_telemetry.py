import csv
import json


def process_telemetry(input_file, output_file):
    devices = {}

    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            device_id = row["device_id"]
            status = row["status"]
            temperature = float(row["temperature"])

            if device_id not in devices:
                devices[device_id] = {
                    "total_records": 0,
                    "temperature_sum": 0.0,
                    "error_count": 0
                }

            devices[device_id]["total_records"] += 1
            devices[device_id]["temperature_sum"] += temperature

            if status == "ERROR":
                devices[device_id]["error_count"] += 1

    results = {}

    for device_id, data in devices.items():
        average_temperature = (
            data["temperature_sum"] / data["total_records"]
        )

        if average_temperature > 80.0:
            continue

        results[device_id] = {
            "total_records": data["total_records"],
            "average_temperature": round(average_temperature, 2),
            "error_count": data["error_count"]
        }

    with open(output_file, "w") as file:
        json.dump(results, file, indent=4)

    print("Device Summary")
    print("------------------------------")

    for device_id, data in results.items():
        print(
            device_id,
            "| Records:", data["total_records"],
            "| Avg Temp:", data["average_temperature"],
            "| Errors:", data["error_count"]
        )


process_telemetry(
    "device_telemetry.csv",
    "telemetry_summary.json"
)