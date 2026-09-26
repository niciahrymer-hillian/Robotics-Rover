"""
Line Follow Control -- fill in the four functions below.

A real, simplified PD (proportional-derivative) control loop -- the
exact model the Line-Following Control Loop Simulator tab runs live.
Same core idea as a real line-follower's firmware: read how far off
the line you are (error), read how fast that error is changing, and
turn back toward the line proportionally to both.

Run the tests as you go:  pytest exercises/test_line_follow_control.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def lateral_error_rate(v, theta):
    """How fast the rover's lateral offset from the line is currently
    changing, given its forward speed v and heading angle theta
    (small-angle approximation: dy/dt ~= v * theta). This is the
    "derivative of the error" term a PD controller needs.

    >>> lateral_error_rate(1.0, 0.5)
    0.5
    """
    # TODO: return v * theta
    raise NotImplementedError


def pd_correction(y, theta, v, Kp, Kd):
    """The actual PD control law: a proportional term (Kp times the
    current lateral error y) plus a derivative term (Kd times how fast
    that error is changing, via lateral_error_rate). This correction is
    subtracted from the heading each tick -- turn back toward the line,
    harder if you're further off (P) or moving away faster (D).

    >>> pd_correction(3.0, 0.0, 1.0, 0.15, 0.6)
    0.45
    """
    # TODO: return Kp*y + Kd*lateral_error_rate(v, theta)
    raise NotImplementedError


def simulate_line_follow(y0, theta0, v, Kp, Kd, n):
    """Run the control loop for n ticks starting from lateral offset y0
    and heading theta0, returning the list of y values at each tick
    (length n+1, including the starting value). Each tick: compute the
    correction, update theta by subtracting it, then update y using the
    PREVIOUS theta (the rover moves based on the heading it had during
    that tick, before this tick's correction takes effect).

    >>> simulate_line_follow(3.0, 0.0, 1.0, 0.15, 0.6, 3)
    [3.0, 3.0, 2.55, 1.92]
    """
    # TODO: y, theta = y0, theta0; ys = [y]; loop n times:
    #   correction = pd_correction(y, theta, v, Kp, Kd)
    #   theta_new = theta - correction
    #   y_new = y + v*theta          (uses the OLD theta, not theta_new)
    #   y, theta = y_new, theta_new; ys.append(y)
    # return ys
    raise NotImplementedError


def has_converged(y_history, threshold=0.3, window=5):
    """Has the rover settled onto the line? True if the last `window`
    values in y_history are all within `threshold` of zero -- the
    actual check for "stopped oscillating and is now tracking the
    line," not just "the most recent value happens to be small."

    >>> has_converged([3.0, 3.0, 2.55, 1.92, 1.29, 0.74, 0.33, 0.06, -0.1, -0.17, -0.19, -0.17, -0.13, -0.09])
    True
    """
    # TODO: if len(y_history) < window, return False. Otherwise return
    # True only if every value in y_history[-window:] has abs() < threshold.
    raise NotImplementedError
