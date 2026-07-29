terms = 1_000_000
series_total = sum((1.0 if n % 2 == 0 else -1.0) / (2 * n + 1) for n in range(terms))
result = 4 * series_total

print(f"Terms: {terms}")
print(f"4 * series total: {result:.15f}")
