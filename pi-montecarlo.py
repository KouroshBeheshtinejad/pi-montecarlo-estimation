import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Use TkAgg backend for window positioning
import matplotlib.pyplot as plt


def generate_points(n, low=-1, high=1):
    """Generate random x and y coordinates in a square"""
    rng = np.random.default_rng()
    x = rng.uniform(low, high, n)
    y = rng.uniform(low, high, n)
    return x, y


def is_inside_circle(x, y, radius=1):
    """Check if a point is inside the circle"""
    return x**2 + y**2 <= radius**2


def update_scatter_plot(fig_id, inside, outside, is_first):
    """Plot points inside and outside the circle"""
    plt.figure(fig_id)
    if is_first["in"]:
        plt.scatter(inside[0], inside[1], c='pink', s=10, label='Inside Circle')
        is_first["in"] = False
    else:
        plt.scatter(inside[0], inside[1], c='pink', s=10)

    if is_first["out"]:
        plt.scatter(outside[0], outside[1], c='orange', s=10, label='Outside Circle')
        is_first["out"] = False
    else:
        plt.scatter(outside[0], outside[1], c='orange', s=10)

    plt.legend(loc='upper right')
    plt.title("Random Points Distribution")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()


def update_pi_plot(fig_id, drops, pi_values):
    """Plot estimated Pi over time"""
    plt.figure(fig_id)
    plt.clf()
    plt.axhline(y=np.pi, color='darkseagreen', linewidth=2, linestyle='--', alpha=0.7, label='Actual π')
    plt.plot(drops, pi_values, color='mediumorchid', label='Estimated π')
    plt.title("π Estimate vs Number of Drops")
    plt.xlabel("Number of Drops")
    plt.ylabel("Estimated π")
    plt.legend()
    plt.grid(True)
    plt.draw()


def estimate_pi(n_trials):
    """Main function to estimate Pi using Monte Carlo method"""
    x_coords, y_coords = generate_points(n_trials)
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    n_inside = 0

    pi_values = []
    n_drops = []

    # Create two windows for visualizations
    plt.figure(1)
    plt.get_current_fig_manager().window.wm_geometry("+0+0")

    plt.figure(2)
    plt.get_current_fig_manager().window.wm_geometry("+960+0")

    is_first_plot = {"in": True, "out": True}

    for i in range(n_trials):
        x, y = x_coords[i], y_coords[i]
        if is_inside_circle(x, y):
            n_inside += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

        if i % 100 == 0:
            current_pi = 4 * n_inside / (i + 1)
            pi_values.append(current_pi)
            n_drops.append(i + 1)

            update_scatter_plot(1, (inside_x, inside_y), (outside_x, outside_y), is_first_plot)
            plt.figure(1)
            plt.title(f"Drop #{i + 1} | Inside: {n_inside} | π ≈ {round(current_pi, 6)}")

            update_pi_plot(2, n_drops, pi_values)
            plt.pause(0.01)

    final_pi = 4 * n_inside / n_trials
    print(f"Final estimated value of Pi after {n_trials} drops: {final_pi}")
    plt.show(block=True) 
    plt.close('all')     



if __name__ == "__main__":
    estimate_pi(n_trials=1000)
