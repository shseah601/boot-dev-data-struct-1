def exponential_growth(n, factor, days):
    result = []

    for day in range(days + 1):
        result.append(n * (factor ** day))

    return result
