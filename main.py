from menu_interface import UserInterface
from wikipedia import DataManager


def main():
    data_manager = DataManager()
    data_manager.save_csv()

    ui = UserInterface()
    ui.load_data(data_manager.population_data)
    ui.run()


if __name__ == "__main__":
    main()
