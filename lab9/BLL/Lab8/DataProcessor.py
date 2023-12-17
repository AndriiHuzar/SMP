import os
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class DataProcessor:
    """
    The DataProcessor class processes and visualizes data.
    """

    def __init__(self):
        """
        Initializes a DataProcessor object with a DataFrame of data and an output directory.
        """
        relative_file_path = os.path.join('..', 'Data', 'Lab8', 'Input', 'iris.csv')

        self.df = pd.read_csv(relative_file_path)

        self.output_directory = os.path.join('..', 'Data', 'Lab8', 'Output')

    def explore_data(self):
        """
        Explores the data by printing the descriptive statistics, maximum values, and minimum values of the DataFrame.
        """
        print(self.df.describe())

        print("\nMaximum values:\n", self.df.max())

        print("\nMinimum values:\n", self.df.min())

    def visualize_data(self, save=False):
        """
        Visualizes the data with various plots and saves the plots if specified.
        """
        plt.scatter(self.df['sepal.length'], self.df['sepal.width'])
        plt.title('Basic Visualization')
        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'basic_visualization.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'basic_visualization.png'), format='png')
        else:
            plt.show()

        colors = {'Setosa': 'r', 'Versicolor': 'g', 'Virginica': 'b'}
        plt.scatter(self.df['sepal.length'], self.df['sepal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        plt.title('Extended Visualization')
        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'extended_visualization.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'extended_visualization.png'), format='png')
        else:
            plt.show()

        fig, axs = plt.subplots(2)
        fig.suptitle('Vertically stacked subplots')
        axs[0].scatter(self.df['sepal.length'], self.df['sepal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        axs[0].set(xlabel='Sepal Length', ylabel='Sepal Width')
        axs[1].scatter(self.df['petal.length'], self.df['petal.width'], c=self.df['variety'].apply(lambda x: colors[x]))
        axs[1].set(xlabel='Petal Length', ylabel='Petal Width')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'multiple_subplots.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'multiple_subplots.png'), format='png')
        else:
            plt.show()

        plt.figure(figsize=(10, 6))
        sns.violinplot(x='variety', y='sepal.length', data=self.df, hue='variety', palette='Set1', legend=False)
        plt.title('Sepal Length Distribution by Variety')
        plt.xlabel('Flower Variety')
        plt.ylabel('Sepal Length')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'violin_plot.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'violin_plot.png'), format='png')
        else:
            plt.show()

        plt.figure(figsize=(10, 6))
        sns.barplot(x='variety', y='sepal.length', data=self.df)
        plt.title('Bar Plot of Sepal Length by Variety')
        plt.xlabel('Flower Variety')
        plt.ylabel('Sepal Length')

        if save:
            plt.savefig(os.path.join(self.output_directory, 'bar_plot.svg'), format='svg')
            plt.savefig(os.path.join(self.output_directory, 'bar_plot.png'), format='png')
        else:
            plt.show()
