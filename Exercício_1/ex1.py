import pandas as pd
import numpy as np

class Dataset:
    def _init_(self):
        self.X = None
        self.y = None
        self.feature_names = []
        self.target_name = None

    def load_csv(self, filename, target_col=-1):
        df = pd.read_csv(filename)
        self.target_name = df.columns[target_col]
        self.feature_names = list(df.columns[:-1])
        self.X = df.iloc[:, :-1].to_numpy()
        self.y = df.iloc[:, target_col].to_numpy()

    

    def save_csv(self, filename):
        df = pd.DataFrame(self.X, columns=self.feature_names)
        df[self.target_name] = self.y
        df.to_csv(filename, index=False)

    def describe(self):
        df = pd.DataFrame(self.X, columns=self.feature_names)
        target = pd.Series(self.y, name=self.target_name)
        df = pd.concat([df, target], axis=1)
        print(df.describe())

    def count_nulls(self):
        df = pd.DataFrame(self.X, columns=self.feature_names)
        print(df.isnull().sum())

    def replace_nulls_with_common(self):
        df = pd.DataFrame(self.X, columns=self.feature_names)
        for col in df.columns:
            mode = df[col].mode()[0]
            df[col].fillna(mode, inplace=True)
        self.X = df.to_numpy()

    def replace_nulls_with_mean(self):
        df = pd.DataFrame(self.X, columns=self.feature_names)
        for col in df.columns:
            mean = df[col].mean()
            df[col].fillna(mean, inplace=True)
        self.X = df.to_numpy()


    def summary_statistics(self):
        print("Estatísticas do eixo X:")
        print(pd.Series(self.x).describe())
        print("\nEstatísticas do eixo Y:")
        print(pd.Series(self.y).describe())
    
data = Dataset()

data.load_csv('hogwarts_legacy_reviews.csv')

data.summary_statistics()

