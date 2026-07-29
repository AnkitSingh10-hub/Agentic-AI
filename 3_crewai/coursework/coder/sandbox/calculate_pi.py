"""Calculate the first 1,000,000 terms of the Leibniz series."""

TERMS = 1_000_000

total = sum(
    (1.0 if n % 2 == 0 else -1.0) / (2 * n + 1)
    for n in range(TERMS)
)
result = 4.0 * total

print(f"Terms: {TERMS:,}", flush=True)
print(f"4 * sum: {result:.15f}", flush=True)
