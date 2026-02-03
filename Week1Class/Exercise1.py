import random

def simulate_world(num_simulations=100_000):
    wet_count = 0

    for _ in range(num_simulations):
        # Sample rain and sprinkler (True/False)
        rain = random.choice([True, False])
        sprinkler = random.choice([True, False])

        # Ground is wet if either rain or sprinkler is True
        ground_is_wet = rain or sprinkler

        if ground_is_wet:
            wet_count += 1

    # Estimate probability
    probability_wet = wet_count / num_simulations
    return probability_wet


# Run simulation
num_simulations = 100_000
probability = simulate_world(num_simulations)

print(f"Estimated P(ground is wet) after {num_simulations} simulations: {probability:.4f}")
