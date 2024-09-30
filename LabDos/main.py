import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataPipeLine:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def analyze_data(self):
        print("Первые 5 строк данных:")
        print(self.data.head())
        print("\nСтатистическая информация:")
        print(self.data.describe())

    def handle_missing_values(self):
        print("\nКоличество пропусков перед обработкой:")
        print(self.data.isnull().sum())

        # Заполнение пропусков средним значением для числовых колонок
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())

        # Заполнение пропусков для строковых колонок
        object_cols = self.data.select_dtypes(include=[object]).columns
        self.data[object_cols] = self.data[object_cols].fillna('unknown')

        print("\nКоличество пропусков после обработки:")
        print(self.data.isnull().sum())

    def handle_outliers(self):
        # Удаление выбросов по Z-оценке
        for col in self.data.select_dtypes(include=[np.number]).columns:
            z_scores = (self.data[col] - self.data[col].mean()) / self.data[col].std()
            self.data = self.data[(z_scores.abs() < 3)]

    def generate_features(self):
        # Пример генерации новой фичи
        if 'Kidhome' in self.data.columns and 'Teenhome' in self.data.columns:
            self.data['new_feature'] = self.data['Kidhome'] * self.data['Teenhome']

    def visualize_data(self):
        # Проверка наличия целевой переменной
        if 'Year_Birth' not in self.data.columns:
            print("Целевая переменная не найдена.")
            return

        # Использование подмножества данных для визуализации
        sample_data = self.data.sample(n=min(1000, len(self.data)), random_state=1)

        plt.figure(figsize=(15, 5))

        # Гистограмма для целевой переменной
        plt.subplot(1, 3, 1)
        sns.histplot(sample_data['Year_Birth'], bins=30, kde=True)
        plt.title('Гистограмма целевой переменной')

        # Проверка наличия feature1 для точечного графика
        if 'NumDealsPurchases' in sample_data.columns:
            plt.subplot(1, 3, 2)
            sns.scatterplot(x=sample_data['NumDealsPurchases'], y=sample_data['Year_Birth'])
            plt.title('Точечный график зависимости')

        # BoxPlot для изучения распределения
        plt.subplot(1, 3, 3)
        sns.boxplot(y=sample_data['NumDealsPurchases'])
        plt.title('BoxPlot целевой переменной')

        plt.tight_layout()
        plt.show()

    def run_pipeline(self):
        self.analyze_data()
        self.handle_missing_values()
        self.handle_outliers()
        self.generate_features()
        self.visualize_data()

# Использование класса
file_path = 'marketing_data.csv'  # Укажите путь к вашему файлу
pipeline = DataPipeLine(file_path)
pipeline.run_pipeline()