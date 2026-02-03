# Rocket Flight Simulation
# Author: Muhammadaziz Khamidov
# Simulates vertical rocket motion using basic physics

import matplotlib.pyplot as plt

# -------------------------
# Initial conditions
# -------------------------

time = 0
dt = 0.01
time_list = []


h = 0
v = 50
a = -9.8

height = []
velocity = []

# -------------------------
# Physics update loop
# -------------------------

while time < 10:
    v = v + a * dt
    h = h + v * dt

    height.append(h)
    velocity.append(v)
    time_list.append(time)

    time += dt

print("Simulation finished")
print(height[:10])

max_height = max(height)
max_index = height.index(max_height)
max_time = time_list[max_index]

# -------------------------
# Plot results
# -------------------------

plt.plot(time_list, height)
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.title("Rocket Height vs Time")

print("Maximum Height:", round(max_height, 2), "meters")
print("Time at Maximum Height:", round(max_time, 2), "seconds")

plt.scatter(max_time, max_height)
plt.annotate("Peak",
             (max_time, max_height),
             textcoords="offset points",
             xytext=(10,10))

plt.grid(True)

plt.savefig("plots/trajectory.png")

plt.show()
