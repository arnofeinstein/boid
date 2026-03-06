class Boid:
    def move_boid(self, *, dt: float) -> None:
        """
        Move the boid based on its velocity

        Args:
            dt: The time step for the simulation
        """
        # Write a function that moves the boid based on its velocity
        self.position += self.velocity * dt
        ...

    def plot_trajectory(self, *, dt: float, num_steps: int) -> None:
        """
        Plot the trajectory of the boid

        Args:
            dt: The time step for the simulation
            num_steps: The number of steps to simulate
        """
        # Write the code to plot the trajectory of the boid in an other way
        traj = np.empty((2, num_steps), dtype=float)
        for i in range(num_steps):
            self.move_boid(dt=dt)
            traj[:, i] = self.position

        _, ax = plt.subplots()
        ax.plot(*traj, "o-")
        ax.set_aspect("equal")
        ...

    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        
def run_app():
    my_obj = Boid("Hi!")
    print(f"{my_obj.arg = }")
