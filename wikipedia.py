from typing import List
import numpy as np
import pandas as pd

table_names: List[str] = [
    "Eastern Africa",
    "Middle Africa",
    "Northern Africa",
    "Southern Africa",
    "Western Africa",
    "Total Africa",
    "Total Americas",
    "Caribbean",
    "Central America",
    "Northern America",
    "Total North America",
    "Total South America",
    "Central Asia",
    "Eastern Asia",
    "South-eastern Asia",
    "Southern Asia",
    "Western Asia",
    "Total Asia",
    "Eastern Europe",
    "Northern Europe",
    "Southern Europe",
    "Western Europe",
    "Total Europe",
    "Total Oceania",
    "Total World",
]
region_name: List[str] = [name for name in table_names if "Total" not in name]


class DataManager:
    def __init__(self) -> None:
        self.population_data = self.extract_data()
        self.rename_cols()
        self.convert_growth_to_float()

    def rename_cols(self):
        self.population_data = self.population_data.rename(
            columns={"±% p.a.": "Growth", "Pop.": "Pop"}
        )

    def convert_growth_to_float(self):
        # Replace "—" with NaN and remove % symbol
        self.population_data["Growth"] = self.population_data["Growth"].replace(
            "—", np.nan
        )
        self.population_data["Growth"] = self.population_data["Growth"].str.replace(
            "%", "", regex=False
        )

        # Convert the column to float
        self.population_data["Growth"] = pd.to_numeric(
            self.population_data["Growth"], errors="coerce"
        )

    def import_data(self):
        wiki_page = "List of continents and continental subregions by population - Wikipedia.html"
        return pd.read_html(wiki_page)

    def extract_data(self):
        wikipedia_tables = self.import_data()
        region_tables = wikipedia_tables[3:]
        for index, table in enumerate(region_tables):
            if table_names[index] in region_name:
                table["Type"] = "Region"
                table["Name"] = table_names[index]
            else:
                table["Type"] = "Continent"
                table["Name"] = table_names[index].replace("Total", "").strip()

        # combine list of dataframes to one dataframe
        regions_df = pd.concat(region_tables)

        return regions_df

    def save_to_csv(self, year: int):
        data_to_save = self.population_data.query(f"Year == {year}")
        data_to_save.to_csv(f"{year}.csv", index=False)

    def save_csv(self):
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
        for year in years:
            self.save_to_csv(year)
