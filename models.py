from typing import List
import pandas as pd


class Region:
    def __init__(self, name: str, data: pd.DataFrame) -> None:
        self.name: str = name
        self.data = data.set_index("Region")

    def _display_population(self, year: int):
        try:
            region_data = self.data.query(f"Year == {year} and Region == '{self.name}'")
            if not region_data.empty:
                pop = region_data["Pop"].iloc[0]
                print(f"{self.name} population in {year}: {pop}")
            else:
                print(f"No data found for {self.name} in {year}.")
        except Exception as e:
            raise Exception("Error displaying population: {e}")

    def _population_comparison(self, compare_region: str, year: int):
        region_data = self.data.query(
            f"Year == {year} and (Region == '{self.name}' or Region == '{compare_region}')"
        )
        if region_data.empty:
            print(f"No data found for {self.name} or {compare_region} in year {year}.")
        else:
            for region in [self.name, compare_region]:
                region_pop = region_data[region_data["Region"] == region]["Pop"].iloc[0]
                print(f"Population of {region} in {year}: {region_pop}")
        print(region_data)

    def _population_sort(self, year: int, ascending=True):
        # Sorts regions by population size in a specific year.
        sorted_pop = self.data.query(f"Year == {year}").sort_values(
            "Pop", ascending=ascending
        )
        print(sorted_pop)

    def _growth_calculator(self, year: int):
        # Calculates the annual growth rate of a region in a specific year.
        growth = self.data.query(f"Year=={year}")["Growth"]
        print(f"Growth rate: {growth}%")

    def _growth_comparison(self, compare_region: str, year: int):
        # Compares the growth rate between two regions in a specific year.
        data_sorted_by_year = self.data.query(f"Year == {year}")
        data_sorted_by_year_and_regions = data_sorted_by_year.query(
            f"Region == '{self.name}' or Region == '{compare_region}'"
        )
        data_sorted_by_year_and_regions.set_index("Region")
        print(data_sorted_by_year_and_regions)

    def _growth_sort(self, year: int, ascending=True):
        # Sorts regions by growth rate in a specific year.
        growth_by_year = self.data.query("Year=={year}").sort_values(
            "Growth", ascending=ascending
        )
        print(growth_by_year)


class Continent(Region):
    def __init__(self, name: str, data: pd.DataFrame) -> None:
        super().__init__(name, data)
