def clean_sensor_readings(values):
    cleaned = []

    for value in values:
        try:
            number = float(value)
        except (TypeError, ValueError):
            continue

        if number < 0:
            continue

        if number > 500.0:
            number = 500.0

        cleaned.append(number)

    return cleaned