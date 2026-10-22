import json
import matplotlib.pyplot as plt


def create_temperature_chart(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            data = json.load(file)

        devices = list(data.keys())
        temperatures = [
            data[device]["average_temperature"]
            for device in devices
        ]

        plt.figure(figsize=(8, 5))
        plt.bar(devices, temperatures)

        plt.title("Average Temperature by Device")
        plt.xlabel("Device")
        plt.ylabel("Average Temperature (°C)")

        for i, value in enumerate(temperatures):
            plt.text(i, value, f"{value:.2f}", ha="center")

        plt.tight_layout()
        plt.savefig(output_file, dpi=150)
        plt.show()

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except (json.JSONDecodeError, KeyError) as error:
        print(f"Error reading data: {error}")


if __name__ == "__main__":
    create_temperature_chart(
        "telemetry_summary.json",
        "temperature_chart.png"
    )