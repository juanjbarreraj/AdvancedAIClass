import random

def simulate_world(num_simulations=100_000):
    wet_count = 0

    for _ in range(num_simulations):
        # Non-uniform probabilities
        rain = random.random() < 0.2        # 20% chance
        sprinkler = random.random() < 0.1   # 10% chance

        ground_is_wet = rain or sprinkler

        if ground_is_wet:
            wet_count += 1

    return wet_count / num_simulations


num_simulations = 100_000
probability = simulate_world(num_simulations)

print(f"Estimated P(ground is wet): {probability:.4f}")
