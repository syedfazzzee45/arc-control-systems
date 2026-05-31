import matplotlib.pyplot as plt

from src.pid_controller import PIDController


def main():
    setpoint = 10
    current_position = 0
    dt = 0.1
    time_steps = 100

    pid = PIDController(
        kp=1.2,
        ki=0.1,
        kd=0.05,
        setpoint=setpoint,
    )

    positions = []
    times = []

    for step in range(time_steps):
        time = step * dt

        control_output = pid.compute(current_position, dt)

        # Simple system response simulation
        current_position += control_output * dt

        times.append(time)
        positions.append(current_position)

    plt.figure()
    plt.plot(times, positions, label="System Position")
    plt.axhline(setpoint, linestyle="--", label="Target Setpoint")
    plt.title("PID Control System Response")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
