class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint

        self.integral = 0
        self.previous_error = 0

    def compute(self, measured_value, dt):
        error = self.setpoint - measured_value

        self.integral += error * dt
        derivative = (error - self.previous_error) / dt

        output = (
            self.kp * error
            + self.ki * self.integral
            + self.kd * derivative
        )

        self.previous_error = error

        return output
