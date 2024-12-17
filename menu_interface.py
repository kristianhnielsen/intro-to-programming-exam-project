from typing import List, Literal
import pandas as pd
from models import Region, Continent
from wikipedia import DataManager


class UserInterface:
    def __init__(self):
        self.regions: dict[str, Region] = {}
        self.continents = {}
        self.numbered_options = []

    def load_data(self, data: pd.DataFrame):
        for _, row in data.iterrows():
            name = row["Name"]
            if row.get("Type") == "Continent":
                self.continents[name] = Continent(name, data)
            else:
                self.regions[name] = Region(name, data)

    def display_menu(self):
        print(
            """\nMenu:
    1. Display the population of a region or continent.
    2. Compare the population between two regions or continents.
    3. Sort regions or continents by population size.
    4. Calculate the annual growth rate of regions or continents.
    5. Compare the growth rate between two regions or continents.
    6. Sort regions or continents by growth rate.
    7. Exit
              """
        )

    def get_year_input(self, prompt="Choose a year"):
        years = [
            1950,
            1960,
            1970,
            1980,
            1990,
            2000,
            2010,
            2021,
        ]
        self.display_year()
        year_input = input(f"\n{prompt}: ")
        if len(year_input) == 1:
            try:
                return years[int(year_input) - 1]
            except IndexError:
                print("Invalid year input")
                exit(1)

        elif int(year_input) in years:
            return int(year_input)
        else:
            print("Invalid year input")
            exit(1)

    def display_year(self):
        print(
            """
              \nYears:
    1. 1950
    2. 1960
    3. 1970
    4. 1980
    5. 1990
    6. 2000
    7. 2010
    8. 2021
              """
        )

    def display_areas(self, area_type: str, areas: dict, display_num_starting_at=1):
        print(f"\n{area_type.capitalize()}:")
        for index, key in enumerate(areas.keys()):
            print(f"{index+display_num_starting_at}. {key}")
            self.numbered_options.append(key)

    def get_area(self, name: str):
        return self.regions.get(name) or self.continents.get(name)

    def sort_areas_by(self, statistic: Literal["Population", "Growth"]):
        year = self.get_year_input(prompt="Choose a year to sort by")

        # Handle no 1950 data
        if statistic == "Growth" and year == 1950:
            print("Growth rate data for the year 1950 not available.")
            return

        # Need to get ANY Region
        first_region = [region for region in self.regions.values()][0]

        # Get input from user if they want sorted regions or continents
        print(
            """\nArea types:
    1. Continents
    2. Regions
              """
        )
        area_type_input = input("Choose an area type: ").strip().lower()
        valid_input_continents = ["1", "continent", "continents"]
        valid_input_regions = ["2", "region", "regions"]

        # Continents
        if area_type_input in valid_input_continents and statistic == "Population":
            sorted_data = first_region.population_sort(year=year, type="Continent")
        elif area_type_input in valid_input_continents and statistic == "Growth":
            sorted_data = first_region.growth_sort(year=year, type="Continent")
        # Regions
        elif area_type_input in valid_input_regions and statistic == "Population":
            sorted_data = first_region.population_sort(year=year, type="Region")
        elif area_type_input in valid_input_regions and statistic == "Growth":
            sorted_data = first_region.growth_sort(year=year, type="Region")
        else:
            print("Invalid input")
            return

        print(f"\nAreas sorted by {statistic.lower()} in {year}:")
        print(sorted_data, "\n")

    def compare_statistic(self, statistic: Literal["Population", "Growth"]):
        self.display_areas(area_type="continents", areas=self.continents)
        self.display_areas(
            area_type="regions",
            areas=self.regions,
            display_num_starting_at=len(self.continents) + 1,
        )
        try:
            area_input_1 = int(input("\nEnter the first region/continent number: "))
            area_input_2 = int(input("\nEnter the second region/continent number: "))
            area_name_1 = self.numbered_options[area_input_1 - 1]
            area_name_2 = self.numbered_options[area_input_2 - 1]
        except IndexError:
            print("Invalid input")
            return
        area_object_1 = self.get_area(area_name_1)
        area_object_2 = self.get_area(area_name_2)

        year = self.get_year_input()

        # Handle no 1950 data
        if statistic == "Growth" and year == 1950:
            print("Growth rate data for the year 1950 not available.")
            return

        if area_object_1 and area_object_2 and statistic == "Population":
            area_object_1.population_comparison(area_object_2, year)
        elif area_object_1 and area_object_2 and statistic == "Growth":
            area_object_1.growth_comparison(area_object_2, year)
        else:
            print("No data found for one or both regions/continents.")

    def display_population(self):
        """Displays the population of a region in a specific year."""
        self.display_areas(area_type="continents", areas=self.continents)
        self.display_areas(
            area_type="regions",
            areas=self.regions,
            display_num_starting_at=len(self.continents) + 1,
        )
        try:
            area_input = int(input("\nEnter region/continent number: "))
            area_name = self.numbered_options[area_input - 1]
        except IndexError:
            print("Invalid input")
            return
        area_object = self.get_area(area_name)

        year = self.get_year_input()

        if area_object:
            area_object.display_population(year)
        else:
            print(f"No data for {area_name}.")

    def calculate_growth_rate(self):
        """Calculates the annual growth rate of a region in a specific year."""
        self.display_areas(area_type="continents", areas=self.continents)
        self.display_areas(
            area_type="regions",
            areas=self.regions,
            display_num_starting_at=len(self.continents) + 1,
        )
        try:
            area_input = int(input("\nEnter region/continent number: "))
            area_name = self.numbered_options[area_input - 1]
        except IndexError:
            print("Invalid input")
            return

        area_object = self.get_area(area_name)

        year = self.get_year_input()

        if area_object and year == 1950:
            print("Growth rate data for the year 1950 not available.")
        elif area_object:
            area_object.growth_calculator(year)
        else:
            print(f"No data for {area_name}.")

    def run(self):
        while True:
            self.numbered_options.clear()
            self.display_menu()
            choice = input("Choose an option: ").strip()
            print("\n")
            if choice == "1":
                self.display_population()
            elif choice == "2":
                self.compare_statistic("Population")
            elif choice == "3":
                self.sort_areas_by(statistic="Population")
            elif choice == "4":
                self.calculate_growth_rate()
            elif choice == "5":
                self.compare_statistic("Growth")
            elif choice == "6":
                self.sort_areas_by(statistic="Growth")
            elif choice == "7":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
                continue

            continue_input = input("Continue? (y/n) ")
            if continue_input.lower() == "n":
                break
