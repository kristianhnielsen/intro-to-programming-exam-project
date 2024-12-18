import pandas as pd


class Region:
    def __init__(self, name: str, population_data: pd.DataFrame):
        self.name = name
        self.population_data = population_data

    def _get_population_on_year(self, year: int):
        """Gets the data for population on a specific year"""
        return self.population_data.query(
            f"Year == {year} and Name == '{self.name}'"
        ).iloc[0]["Pop"]

    def _get_growth_on_year(self, year: int):
        """Gets the data for growth on a specific year"""
        return self.population_data.query(
            f"Year == {year} and Name == '{self.name}'"
        ).iloc[0]["Growth"]

    def display_population(self, year: int):
        """Displays the population of a region in a specific year."""
        print(
            f"\n[Region] {self.name} - Population in {year}: {self._get_population_on_year(year)}"
        )

    def population_comparison(self, other_area, year: int):
        """Compare the population with another region for a specific year."""
        pop1 = self._get_population_on_year(year)
        pop2 = other_area._get_population_on_year(year)
        if pop1 and pop2:
            larger = self if pop1 > pop2 else other_area
            smaller = self if pop1 < pop2 else other_area
            print(
                f"In {year}, {larger.name} has a larger population than {smaller.name}."
            )
            print(f"{larger.name}: {larger._get_population_on_year(year)}")
            print(f"{smaller.name}: {smaller._get_population_on_year(year)}")
        else:
            print(f"Missing population data for comparison in {year}.")

    def population_sort(self, year: int, type="Region"):
        """
        Sorts regions by population size in a specific year.
        NOTE: this method only queries the full dataset, so it is irrelevant which instance calls this method
        """
        return (
            self.population_data.query(f"Year == {year} and Type == '{type}'")
            .sort_values("Pop", ascending=False)
            .set_index("Name")[["Pop"]]
        )

    def growth_calculator(self, year: int):
        """Calculate annual growth rate for a year."""

        growth_rate = self._get_growth_on_year(year)
        print(f"The growth rate for {self.name}: {growth_rate}%")

    def growth_comparison(self, other_area, year: int):
        """Compares the growth rate between two regions in a specific year."""

        pop1 = self._get_growth_on_year(year)
        pop2 = other_area._get_growth_on_year(year)
        if pop1 and pop2:
            larger = self if pop1 > pop2 else other_area
            smaller = self if pop1 < pop2 else other_area
            print(
                f"In {year}, {larger.name} has a larger growth rate than {smaller.name}."
            )
            print(f"{larger.name}: {larger._get_growth_on_year(year)}%")
            print(f"{smaller.name}: {smaller._get_growth_on_year(year)}%")
        else:
            print(f"Missing growth rate data for comparison in {year}.")

    def growth_sort(self, year: int, type="Region"):
        """
        Sorts regions by growth rate in a specific year.
        NOTE: this method only queries the full dataset, so it is irrelevant which instance calls this method
        """

        return (
            self.population_data.query(f"Year == {year} and Type == '{type}'")
            .sort_values("Growth", ascending=False)
            .set_index("Name")[["Growth"]]
        )

    def __repr__(self):
        return f"Region({self.name})"


class Continent(Region):
    def __init__(self, name: str, population_data: pd.DataFrame):
        super().__init__(name, population_data)

    def display_population(self, year: int):
        print(
            f"[Continent] {self.name} - Population in {year}: {self._get_population_on_year(year)}"
        )

    def __repr__(self):
        return f"Continent({self.name})"
