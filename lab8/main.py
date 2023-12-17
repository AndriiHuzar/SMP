from Lab8.csv_visual import DataVisualizer

def main():
    #Шлях до CSV-файлу
    csv_file_path = 'C:\\Users\guzar\OneDrive\Робочий стіл\Лабкі\СМП\Lab8\data\mock_data.csv'

    while True:
        #Створення об'єкту DataVisualizer
        data_visualizer = DataVisualizer(csv_file_path)

        #Завантаження та дослідження даних
        data_visualizer.explore_data()

        #Запит користувача щодо вибору діаграми
        user_choice = input("1. Кругова діаграма \n2. Діаграма розсіювання \n3. Стовпцева діаграма \n4. Вивести всі діаграми \nВведіть номер діаграми (1-4) або 'x' для виходу: ")

        if user_choice.lower() == 'x':
            break

        #Візуалізація даних згідно з вибором користувача
        data_visualizer.visualize_data(user_choice)

if __name__ == "__main__":
    main()
