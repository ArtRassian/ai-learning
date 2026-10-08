import numpy as np

def analyze_numbers_numpy(
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

    return {
        "unique_numbers": np.unique(numbers),
        "mean": np.mean(numbers),
        "median": np.median(numbers),
        "min": np.min(numbers),
        "max": np.max(numbers),
    }

print(analyze_numbers_numpy([]))
print(analyze_numbers_numpy([5]))
print(analyze_numbers_numpy([1, 2]))
print(analyze_numbers_numpy([3, 3, 3]))
print(analyze_numbers_numpy([-10, 0, 10]))
print(analyze_numbers_numpy([1.5, 2.5, 3.5]))
print(analyze_numbers_numpy([10, 5, 5, 20, 15]))

array = np.array([10, 5, 5, 20, 15])

print("Массив:", array)
print("Тип объекта:", type(array))
print("Тип элементов:", array.dtype)
print("Количество измерений:", array.ndim)
print("Размер массива:", array.size)
print("Форма массива:", array.shape)