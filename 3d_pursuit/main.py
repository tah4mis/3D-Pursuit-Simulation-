import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------
soldier_speed = 1.5   # ← askerin hızı
enemy_speed = 1.0     # ← düşmanın hızı
dt = 0.02
total_time = 20

enemy_pos0 = np.array([0.0, 0.0, 0.0])
soldier_pos0 = np.array([5.0, 5.0, 5.0])

# Enemy movement (scaled by enemy_speed)
def enemy_motion(t):
    return np.array([
        5 * np.sin(0.4 * enemy_speed * t),
        5 * np.sin(0.6 * enemy_speed * t + 1),
        5 * np.sin(0.8 * enemy_speed * t + 2)
    ])

# Soldier pursuit dynamics
def dpos_dt(t, state):
    soldier = state
    enemy = enemy_motion(t)

    direction = enemy - soldier
    norm = np.linalg.norm(direction)

    if norm == 0:
        vel = np.zeros(3)
    else:
        vel = (direction / norm) * soldier_speed

    return vel

# Solve soldier path
t_eval = np.arange(0, total_time, dt)
sol = solve_ivp(dpos_dt, [0, total_time], soldier_pos0, t_eval=t_eval)
soldier_positions = sol.y.T
enemy_positions = np.array([enemy_motion(t) for t in t_eval])

# ------------------------------------------------------------
# Visualization
# ------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)

# Dots
enemy_dot, = ax.plot([], [], [], 'ro', markersize=8, label="Enemy")
soldier_dot, = ax.plot([], [], [], 'bo', markersize=8, label="Soldier")

# Trails (lines)
enemy_trail, = ax.plot([], [], [], 'r-', linewidth=1)
soldier_trail, = ax.plot([], [], [], 'b-', linewidth=1)

ax.legend()

def update(frame):
    # --- positions ---
    ex, ey, ez = enemy_positions[frame]
    sx, sy, sz = soldier_positions[frame]

    # Update dots
    enemy_dot.set_data([ex], [ey])
    enemy_dot.set_3d_properties([ez])

    soldier_dot.set_data([sx], [sy])
    soldier_dot.set_3d_properties([sz])

    # Update trails (all previous positions)
    enemy_trail.set_data(enemy_positions[:frame,0], enemy_positions[:frame,1])
    enemy_trail.set_3d_properties(enemy_positions[:frame,2])

    soldier_trail.set_data(soldier_positions[:frame,0], soldier_positions[:frame,1])
    soldier_trail.set_3d_properties(soldier_positions[:frame,2])

    return enemy_dot, soldier_dot, enemy_trail, soldier_trail

ani = FuncAnimation(fig, update, frames=len(t_eval), interval=30)

plt.show()
