# Exercises — Line Follow Control

A hands-on companion to Lesson 4 in the interactive tour: the real PD (proportional-derivative) control
loop math behind the Line-Following Control Loop Simulator tab — the same kind of feedback loop real
line-follower firmware runs, simplified to its core.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 7 failing tests — every function in `line_follow_control.py` currently raises
`NotImplementedError`.

## What to do

Open `line_follow_control.py`. Implement in this order:

1. `lateral_error_rate` — the derivative term: how fast the lateral error is changing right now.
2. `pd_correction` — the actual control law: proportional term + derivative term.
3. `simulate_line_follow` — run the control loop for real, tick by tick.
4. `has_converged` — the check for "settled onto the line," not just "the last value looks small."

## When you're done

All 7 tests passing means you have the same control loop the Simulator tab runs live. Try the
Simulator with `Kp=0.15, Kd=0` (no damping — oscillates and grows), then `Kp=0.15, Kd=0.6` (damped,
converges cleanly), then `Kp=1.2, Kd=0.6` (too aggressive — diverges even with damping) to see exactly
what these functions predict, play out visually.
