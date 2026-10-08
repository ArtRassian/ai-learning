def analyze_numbers(
    numbers: list[int | float],
) -> dict[str, object]:
    """
    Анализирует переданный список чисел.

    Возвращает словарь с уникальными значениями,
    средним, медианой, минимумом и максимумом.
    """
    if not numbers:
        return {
            "unique_numbers": [],
            "mean": None,
            "median": None,
            "min": None,
            "max": None,
        }

    unique_numbers = sorted(set(numbers))
    sorted_numbers = sorted(numbers)

    count = len(sorted_numbers)
    mean = sum(sorted_numbers) / count

    middle = count // 2

    if count % 2 == 0:
        median = (
            sorted_numbers[middle - 1]
            + sorted_numbers[middle]
        ) / 2
    else:
        median = sorted_numbers[middle]

    return {
        "unique_numbers": unique_numbers,
        "mean": mean,
        "median": median,
        "min": sorted_numbers[0],
        "max": sorted_numbers[-1],
    }