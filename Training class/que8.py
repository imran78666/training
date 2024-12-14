n = int(input("Enter the total steps (N): "))  # Total steps to climb
m = int(input("Enter the max steps Alice can climb in one turn (M): "))  # Steps Alice can take in one turn

# Calculate the number of climbs
if n % m == 0:  # If N is divisible by M
    climbs = n // m  # Exact number of M-step climbs
else:
    climbs = (n // m) + 1  # Full M-step climbs + 1 additional climb for the remainder

print("Minimum number of climbs:", climbs)