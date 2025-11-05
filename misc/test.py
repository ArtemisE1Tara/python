import math

# Define the function for Newton's Law of Cooling
def newtons_law_of_cooling(Ts, T0, k, t):
    """
    Calculates the temperature T(t) using Newton's Law of Cooling.
    T(t) = Ts + (T0 - Ts) * e^(-k*t)
    """
    return Ts + (T0 - Ts) * math.exp(-k * t)

# --- Input Parameters (Using Sample Inputs for demonstration) ---
# In a final script, you might prompt the user for these, 
# but we'll use the sample values directly to match the expected output.

# Ts = 0.0  # Temperature of the surroundings (°C)
# T0 = 100.0 # Initial temperature of the object (°C)
# k = 0.2    # Heat transfer coefficient (1/sec)
# time_increment = 0.5 # Time increment per loop (seconds)
# tolerance = 0.1      # Minimum temperature change to terminate the loop

# Hardcoding the sample inputs:
try:
    # Use float() to ensure these are treated as floating-point numbers
    Ts = float(input("Enter the temperature of the surroundings (Ts in °C): "))
    T0 = float(input("Enter the initial temperature of the object (T0 in °C): "))
    k = float(input("Enter the heat transfer coefficient (k in 1/sec): "))
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()

time_increment = 0.5 # Time increment per loop (seconds)
tolerance = 0.1      # Minimum temperature change to terminate the loop

# --- Simulation Initialization ---
t = 0.0
# Calculate the initial temperature T(0), which is T0
current_temperature = newtons_law_of_cooling(Ts, T0, k, t)
previous_temperature = current_temperature + tolerance * 2 # Set a value that ensures the loop starts
temperature_change = abs(previous_temperature - current_temperature)


# --- Simulation Loop ---
print("\nStarting Simulation...")

# Loop as long as the absolute change in temperature is greater than the tolerance
# The termination condition is: (T from previous - T from current loop) < 0.1
# Note: The problem description implies 'T from previous' is the result of the previous calculation.
# Our loop structure calculates 'current_temperature' *after* the increment.
while temperature_change >= tolerance:
    
    # 1. Store the current temperature to be the 'previous_temperature' for the *next* loop's check
    previous_temperature = current_temperature
    
    # 2. Increment time for the *new* step
    t += time_increment
    
    # 3. Calculate the new temperature T(t)
    current_temperature = newtons_law_of_cooling(Ts, T0, k, t)
    
    # 4. Calculate the change in temperature
    # T from previous (previous_temperature) - T from current loop (current_temperature)
    temperature_change = previous_temperature - current_temperature
    
    # Optional: Print current status (uncomment for debugging/tracking)
    # print(f"Time: {t:.1f} s, T: {current_temperature:.2f} °C, Change: {temperature_change:.3f}")
    
# --- Output ---
print("\n--- Simulation Complete ---")
print(f"Loop terminated because the temperature change was less than {tolerance} °C.")
print(f"Final Temperature (T): {current_temperature:.2f} °C")
print(f"Time Taken (t): {t:.1f} seconds")

# Verify with sample output values:
# Input: Ts=0, T0=100, k=0.2
# Expected Output: T = 0.91 (°C), t = 23.5 (seconds)