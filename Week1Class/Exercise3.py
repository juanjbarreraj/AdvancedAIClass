import random

# Parameters
max_possible_submarines = 5        # Universe size is unknown but bounded
sensor_accuracy = 0.8              # Chance of detecting a submarine
false_alarm_rate = 0.2             # Chance of detecting a non-existent submarine

# Step 1: Randomly generate a dynamic number of submarines (unknown to the sensor)
num_submarines = random.randint(0, max_possible_submarines)
submarines = ["Sub_" + str(i+1) for i in range(num_submarines)]

print(f"Actual submarines in the area: {submarines}")

# Step 2: Simulate sensor readings (observations) with uncertainty
sensor_readings = []

# True positives (detect real submarines)
for sub in submarines:
    if random.random() < sensor_accuracy:
        sensor_readings.append(sub)

# False positives (sensor reports submarines that don't exist)
num_false_alarms = random.randint(0, max_possible_submarines)
for i in range(num_false_alarms):
    if random.random() < false_alarm_rate:
        sensor_readings.append("Unknown_" + str(i+1))

print(f"Sensor readings (observations): {sensor_readings}")

# Step 3: Identity uncertainty
# Some readings may refer to the same submarine (duplicate detection)
# Randomly shuffle to simulate this
random.shuffle(sensor_readings)

# Step 4: Estimate number of submarines
# We count unique IDs, but unknown IDs may refer to new objects
estimated_subs = len(set(sensor_readings))
print(f"Estimated number of submarines: {estimated_subs}")
