import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

class DataVisualizer:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)

    def explore_data(self):
        #Екстремальні значення по стовпцях
        min_values = self.df.min()
        max_values = self.df.max()

        print("Мінімальні значення:")
        print(min_values)

        print("\nМаксимальні значення:")
        print(max_values)

    def visualize_data(self, user_choice):
        if user_choice == "1":
            self.pie_chart()
        elif user_choice == "2":
            self.scatter_plot()
        elif user_choice == "3":
            self.bar_chart()
        elif user_choice == "4":
            self.show_all_plots()
        else:
            print("Невірний вибір. Будь ласка, введіть номер від 1 до 4.")

    def pie_chart(self):
        #Візуалізація частки кожної марки автомобіля
        car_make_distribution = self.df['car_make'].value_counts()
        car_make_distribution.plot(kind='pie', autopct='%1.1f%%', title='Розподіл марок автомобілів')
        plt.show()

    def scatter_plot(self):
        #Візуалізація взаємозв'язку року виробництва та моделі автомобіля
        plt.scatter(self.df['car_model_year'], self.df['car_model'], alpha=0.5)
        plt.xlabel('Рік виробництва')
        plt.ylabel('Модель автомобіля')
        plt.title('Взаємозв\'язок року виробництва та моделі автомобіля')
        plt.show()

    def bar_chart(self):
        #Візуалізація кількості автомобілів за маркою
        car_make_counts = self.df['car_make'].value_counts()
        car_make_counts.plot(kind='bar', xlabel='Марка автомобіля', ylabel='Кількість',
                             title='Кількість автомобілів за маркою', rot=45)
        plt.show()

    def show_all_plots(self):
        # Вивести всі три графіки
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        # Кругова діаграма
        car_make_distribution = self.df['car_make'].value_counts()
        axes[0, 0].pie(car_make_distribution, autopct='%1.1f%%', labels=car_make_distribution.index, startangle=90)
        axes[0, 0].set_title('Розподіл марок автомобілів')

        #Діаграма розсіювання
        axes[0, 1].scatter(self.df['car_model_year'], self.df['car_model'], alpha=0.5)
        axes[0, 1].set_xlabel('Рік виробництва')
        axes[0, 1].set_ylabel('Модель автомобіля')
        axes[0, 1].set_title('Взаємозв\'язок року виробництва та моделі автомобіля')

        #Стовпцева діаграма
        car_make_counts = self.df['car_make'].value_counts()
        axes[1, 0].bar(car_make_counts.index, car_make_counts)
        axes[1, 0].set_xlabel('Марка автомобіля')
        axes[1, 0].set_ylabel('Кількість')
        axes[1, 0].set_title('Кількість автомобілів за маркою')
        axes[1, 0].tick_params(axis='x', labelrotation=90)  # Обертання тексту на горизонтальних стовпчиках
        plt.delaxes(axes[1, 1])

        #Встановлення відстані між графіками
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        #Збереження графіків у форматах PNG та HTML
        plt.savefig('C:\\Users\guzar\OneDrive\Робочий стіл\Лабкі\СМП\Lab8\data\data\output_plot.png')

        #Використання Plotly для збереження графіка у форматі HTML
        fig = px.scatter(self.df, x='car_model_year', y='car_model',
                         title='Взаємозв\'язок року виробництва та моделі автомобіля')
        fig.write_html('C:\\Users\guzar\OneDrive\Робочий стіл\Лабкі\СМП\Lab8\data\output_plot.html')

        plt.show()
