"""Reproduce the worked example using only the standard library."""
import math


def loss(w):
    return 0.5 * (2 * w - 6) ** 2


def step(w, rate):
    gradient = (2 * w - 6) * 2
    updated = w - rate * gradient
    return gradient, updated, loss(updated)


if __name__ == "__main__":
    for rate, expected_w, expected_loss in [(0.1, 1.8, 2.88), (0.2, 2.6, 0.32), (0.6, 5.8, 15.68)]:
        gradient, updated, value = step(1, rate)
        assert math.isclose(updated, expected_w)
        assert math.isclose(value, expected_loss)
        print(f"rate={rate}: gradient={gradient}, w={updated:.2f}, loss={value:.2f}")
    h = 1e-5
    numerical = (loss(1 + h) - loss(1 - h)) / (2 * h)
    assert math.isclose(numerical, -8, abs_tol=1e-8)
    print("All worked values and the finite-difference gradient agree.")
