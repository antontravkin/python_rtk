from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import shap

# Загрузка данных
df = pd.read_csv('/mnt/data/train.csv')

# Графики распределения
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Распределение Age')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['Balance'], bins=30, kde=True)
plt.title('Распределение Balance')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Geography')
plt.title('Количество по Geography')
plt.show()

# Корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Тепловая карта корреляций')
plt.show()

# Подготовка данных
X = df.drop(['id', 'CustomerId', 'Surname', 'Exited'], axis=1)
y = df['Exited']
categorical_features = ['Geography', 'Gender']
numerical_features = X.drop(columns=categorical_features).columns.tolist()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42)

# Препроцессор
numeric_transformer = Pipeline([('scaler', StandardScaler())])
categorical_transformer = Pipeline([('onehot', OneHotEncoder(drop='first'))])
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# Сравнение моделей
models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM': LGBMClassifier(random_state=42)
}

for name, model in models.items():
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    print(f'=== {name} ===')
    print(classification_report(y_test, y_pred))
    print('\n')

# SHAP для последней модели
explainer = shap.Explainer(pipe.named_steps['classifier'])
X_test_transformed = pipe.named_steps['preprocessor'].transform(X_test)
shap_values = explainer.shap_values(X_test_transformed)
shap.summary_plot(shap_values, X_test_transformed,
                  feature_names=pipe.named_steps['preprocessor'].get_feature_names_out())


# Полный код решения для PW_ML_3 с комментариями


# 1️⃣ Загрузка данных
df = pd.read_csv('/mnt/data/train.csv')

# 2️⃣ Разведочный анализ данных (EDA)
print(df.info())
print(df.describe())
print(df.isnull().sum())  # Проверяем пропуски

# Визуализируем распределение целевой переменной
plt.figure(figsize=(5, 4))
df['Exited'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Распределение целевой переменной Exited')
plt.xticks([0, 1], ['Остались', 'Ушли'])
plt.show()

# Визуализируем распределения признаков
plt.figure(figsize=(8, 4))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Распределение возраста клиентов')
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['Balance'], bins=30, kde=True)
plt.title('Распределение баланса клиентов')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Geography')
plt.title('География клиентов')
plt.show()

# Корреляции признаков
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Корреляции между признаками')
plt.show()

# 3️⃣ Подготовка данных
X = df.drop(['id', 'CustomerId', 'Surname', 'Exited'], axis=1)
y = df['Exited']
categorical_features = ['Geography', 'Gender']
numerical_features = X.drop(columns=categorical_features).columns.tolist()

# Разделяем данные на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42)

# 4️⃣ Препроцессинг (масштабирование и кодирование категориальных признаков)
numeric_transformer = Pipeline([('scaler', StandardScaler())])
categorical_transformer = Pipeline([('onehot', OneHotEncoder(drop='first'))])
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# 5️⃣ Построение и сравнение моделей RandomForest, XGBoost, LightGBM
models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM': LGBMClassifier(random_state=42)
}

for name, model in models.items():
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    print(f'=== Модель: {name} ===')
    print(classification_report(y_test, y_pred))
    print('Матрица ошибок:')
    print(confusion_matrix(y_test, y_pred))
    print('\n')

# 6️⃣ Интерпретация модели с помощью SHAP
explainer = shap.Explainer(pipe.named_steps['classifier'])
X_test_transformed = pipe.named_steps['preprocessor'].transform(X_test)
shap_values = explainer.shap_values(X_test_transformed)

# Визуализируем важность признаков
shap.summary_plot(shap_values, X_test_transformed,
                  feature_names=pipe.named_steps['preprocessor'].get_feature_names_out())

# ✅ Этот код закрывает все задачи PW_ML_3: загрузка данных, EDA, подготовка данных, построение нескольких моделей, оценка метрик и интерпретация модели с SHAP, готов к вставке в твой ноутбук.
