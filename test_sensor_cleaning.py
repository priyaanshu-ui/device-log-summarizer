from sensor_cleaning import clean_sensor_readings


data1 = [100, "250.5", None, -10, "abc", 700, 50]
print("Test 1:", clean_sensor_readings(data1))


data2 = []
print("Test 2:", clean_sensor_readings(data2))


data3 = [None, -5, "abc", -100]
print("Test 3:", clean_sensor_readings(data3))