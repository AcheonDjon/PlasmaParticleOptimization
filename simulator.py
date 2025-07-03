import numpy as np
import matplotlib.pyplot as plt

def simulate_drunkards_walk(duration=10.0, dt=0.01, theta=1.0, sigma=0.5):
    """
    Simulates a 1D Ornstein-Uhlenbeck process (a "drunkard's walk with a leash").

    Args:
        duration (float): Total simulation time.
        dt (float): Time step.
        theta (float): Strength of the pull back to the center (drift).
        sigma (float): Magnitude of the random kicks (diffusion).

    Returns:
        A tuple of (time_array, position_array).
    """
    num_steps = int(duration / dt)
    t = np.linspace(0, duration, num_steps)
    x = np.zeros(num_steps)  # Position array

    # Start at position x=1.0
    x[0] = 1.0

    # Pre-calculate the stochastic part's magnitude for efficiency
    random_kick_magnitude = sigma * np.sqrt(dt)

    # Euler-Maruyama integration loop
    for i in range(num_steps - 1):
        # 1. Get the current position
        current_x = x[i]

        # 2. Calculate the deterministic push (the "drift")
        deterministic_push = -theta * current_x * dt

        # 3. Calculate the random kick (the "diffusion")
        #    Z is a random number from a standard normal distribution
        Z = np.random.normal(0, 1)
        random_kick = random_kick_magnitude * Z

        # 4. Update the position
        x[i+1] = current_x + deterministic_push + random_kick

    return t, x

if __name__ == "__main__":
    # Run the simulation
    time, position = simulate_drunkards_walk()

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(time, position)
    plt.axhline(0, color='r', linestyle='--', label='Center (x=0)')
    plt.title("Euler-Maruyama Simulation of a Drunkard's Walk with a Leash")
    plt.xlabel("Time")
    plt.ylabel("Position (x)")
    plt.legend()
    plt.grid(True)
    plt.show()
