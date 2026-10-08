from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# 1. Загрузи датасет как Pandas DataFrame.
iris = load_iris(as_frame=True)

# Посмотри, что находится внутри датасета.
print(iris.keys())
print(iris.data.head())
print(iris.target.head())
print(iris.target_names)

# 2. Отдели признаки от правильных ответов.
X = iris.data
y = iris.target

# 3. Раздели данные на обучающую и тестовую части.
X_train, X_test, y_train, y_test = train_test_split(
X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# 4. Создай модель.
model = LogisticRegression(max_iter=1000)

# 5. Обучи модель.
model.fit(X_train, y_train)

# 6. Получи прогнозы для тестовой выборки.
predictions = model.predict(X_test)

# 7. Оцени качество.
accuracy = accuracy_score(y_test, predictions)

print(f"Размер обучающей выборки: {X_train.shape}")
print(f"Размер тестовой выборки: {X_test.shape}")
print(f"Accuracy: {accuracy:.2f}")

comparison = X_test.copy()

comparison["actual"] = y_test
comparison["predicted"] = predictions
comparison["correct"] = comparison["actual"] == comparison["predicted"]

print(comparison.head(10))

mistakes = comparison[~comparison["correct"]]

print("\nОшибки модели:")
print(mistakes)



new_flower = X.iloc[[0]].copy()

prediction = model.predict(new_flower)
predicted_class = prediction[0]
predicted_name = iris.target_names[predicted_class]

print("\nНовый объект:")
print(new_flower)
print("Номер предсказанного класса:", predicted_class)
print("Название класса:", predicted_name)

print("Форма X:", X.shape)
print("Форма y:", y.shape)

print("\nРаспределение классов:")
print(y.value_counts())

print("\nНазвания признаков:")
print(X.columns.tolist())

probabilities = model.predict_proba(X_test)

print(probabilities[:5])