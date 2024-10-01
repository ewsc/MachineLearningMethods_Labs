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

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())

        object_cols = self.data.select_dtypes(include=[object]).columns
        self.data[object_cols] = self.data[object_cols].fillna('unknown')

        print("\nКоличество пропусков после обработки:")
        print(self.data.isnull().sum())

    def handle_outliers(self):
        for col in self.data.select_dtypes(include=[np.number]).columns:
            z_scores = (self.data[col] - self.data[col].mean()) / self.data[col].std()
            self.data = self.data[(z_scores.abs() < 3)]

    def generate_features(self):
        if 'peakrpm' in self.data.columns and 'horsepower' in self.data.columns:
            self.data['new_feature'] = self.data['peakrpm'] + self.data['horsepower']

    def visualize_data(self):
        if 'price' not in self.data.columns:
            print("Целевая переменная не найдена.")
            return

        sample_data = self.data.sample(n=min(1000, len(self.data)), random_state=1)

        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        sns.histplot(sample_data['price'], bins=30, kde=True)
        plt.title('Гистограмма целевой переменной')

        if 'price' in sample_data.columns:
            plt.subplot(1, 3, 2)
            sns.scatterplot(x=sample_data['new_feature'], y=sample_data['price'])
            plt.title('Точечный график зависимости')
            plt.xticks(range(int(sample_data['new_feature'].min()), int(sample_data['new_feature'].max()) + 1))

        plt.subplot(1, 3, 3)
        sns.boxplot(y=sample_data['price'])
        plt.title('BoxPlot целевой переменной')

        plt.tight_layout()
        plt.show()

    def run_pipeline(self):
        self.analyze_data()
        self.handle_missing_values()
        # self.handle_outliers()
        self.generate_features()
        self.visualize_data()

file_path = 'scrap.csv'
pipeline = DataPipeLine(file_path)
pipeline.run_pipeline()