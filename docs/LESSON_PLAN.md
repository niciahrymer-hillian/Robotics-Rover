# 📖 Lesson Plan — Robotics-Rover

> **Chain K — Hardware & Systems Foundations** | A small wheeled rover with motor control — the one
> Chain K skill nothing else here touches: driving motors, not just reading sensors.

## What This Project Is

Every other build in this chain reads the world or displays to it. This one acts on it — and motors
are a genuinely different problem: they draw far more current than logic circuits, need their own
driver stage, and closing a feedback loop (line-following) is a different kind of programming than
reading a sensor value once. Get power isolation and the driver stage right first, then build a real
PD control loop that actually tracks a line instead of just reading whether it's there.

## Learning Objectives

By the end I can:

1. Explain how an H-bridge lets a low-current logic signal control a high-current motor in both
   directions, and use PWM for real speed control.
2. Explain why motors need their own battery, separate from logic, sharing only ground — and why
   skipping this causes brownouts.
3. Assemble a chassis and wire an IR sensor pair (or array) for line-following.
4. Implement a real PD (proportional-derivative) control loop, and tune it to converge instead of
   oscillate or diverge.

## Software You Will Use

- Arduino IDE (or PlatformIO) for an Arduino Uno, or MicroPython/Arduino core for an ESP32.
- A logic analyzer or oscilloscope (optional but useful) for verifying PWM output.

## Build Order

1. Wire the driver board with two separate power rails — the motor battery and the logic supply,
   sharing only ground — before connecting anything else.
   🔗 [Why Do Robots Need Separate Power for Motors and Logic?](https://techietory.com/robotics/why-robots-need-separate-power-motors-logic/)
2. Choose and wire a motor driver (a TB6612FNG breakout is the recommended pick over an L298N);
   confirm both motors spin in both directions under PWM speed control before adding any sensors.
   🎥 [TB6612FNG H-Bridge Motor Controller — Better than L298N?](https://www.youtube.com/watch?v=JPPTRj0KWbg) (DroneBot Workshop)
3. Assemble the chassis and mount an IR sensor pair (or array) for line-following.
   🎥 [Complete Assembly And Review Of A DIY Robot Smart Car Chassis Kit](https://www.youtube.com/watch?v=Q4UmbjXwoZ4) (BMonster Laboratory)
4. Implement the control loop: read the sensor error, apply a PD correction, and tune Kp/Kd until the
   rover tracks the line smoothly instead of oscillating or losing it entirely.
   🎥 [I made a SUPER FAST Line Follower Robot Using PID!](https://www.youtube.com/watch?v=QoNkpnpvEqc) (Shyam Ravi)

## Common Mistakes to Avoid

- Powering motors and logic from the same battery/regulator — motor start-up current sags the voltage
  and brownouts the microcontroller; always separate them and share only ground.
- Undersized wire gauge to the motors causing voltage drop.
- A driver board with no flyback diodes, letting motor back-EMF damage the driver (most breakout
  boards include these, but bare H-bridge ICs may not).
- Sizing the driver/battery for a motor's typical running current instead of its much higher stall
  current — motors draw far more current stalled than running free.
- Setting the proportional gain (Kp) too high with no damping (Kd), causing the rover to oscillate
  wildly or lose the line entirely instead of tracking it smoothly.

## Check Your Understanding

The quiz covers H-bridge/PWM basics, the power-isolation/brownout mechanism, PD control convergence vs
divergence, and diagnosing driver failures (stall-current sizing, flyback diodes).

## Why This Matters (Industry Application)

Motor control, current budgeting, and closed-loop control are core to robotics and embedded systems
roles — a meaningfully different (and in-demand) skill set from the sensor/radio/display focus of the
rest of this chain.

## Reflection Questions

- Why is "acting on the world" (motors) a fundamentally different problem from "reading it" (sensors),
  in terms of what can actually go wrong?
- If you found your rover oscillating right at the edge of the line instead of smoothly tracking it,
  what would you change about Kp and Kd, and why?
