"""
Tests for line_follow_control.py. Values independently verified with a
reference implementation before being written here.
"""
import pytest

from line_follow_control import (
    lateral_error_rate,
    pd_correction,
    simulate_line_follow,
    has_converged,
)


def test_lateral_error_rate():
    assert lateral_error_rate(1.0, 0.5) == 0.5


def test_lateral_error_rate_zero_heading():
    assert lateral_error_rate(2.0, 0.0) == 0.0


def test_pd_correction_p_and_d_terms():
    assert pd_correction(3.0, 0.0, 1.0, 0.15, 0.6) == pytest.approx(0.45)


def test_pd_correction_with_nonzero_theta():
    assert pd_correction(2.0, 1.0, 1.0, 0.1, 0.5) == pytest.approx(0.7)


def test_simulate_line_follow_short_run():
    result = simulate_line_follow(3.0, 0.0, 1.0, 0.15, 0.6, 3)
    assert result == pytest.approx([3.0, 3.0, 2.55, 1.92])


def test_simulate_line_follow_converges_with_damping():
    result = simulate_line_follow(3.0, 0.0, 1.0, 0.15, 0.6, 13)
    assert has_converged(result, threshold=0.3, window=5) is True


def test_simulate_line_follow_diverges_with_high_gain():
    result = simulate_line_follow(3.0, 0.0, 1.0, 1.2, 0.6, 13)
    assert has_converged(result, threshold=0.3, window=5) is False


def test_has_converged_too_short_history():
    assert has_converged([3.0, 1.0], threshold=0.3, window=5) is False
