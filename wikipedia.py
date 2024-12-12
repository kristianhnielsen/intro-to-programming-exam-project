from typing import List
import pandas as pd


region_names: List[str] = [
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


def create_dataframe(html_file: str):
    wiki_tables = pd.read_html(html_file)

    # populations_by_continental_landmass = wiki_tables[0]
    # populations_by_continent = wiki_tables[1]
    # populations_by_continental_subregion = wiki_tables[2]
    region_tables = wiki_tables[3:]
    # region_tables = wiki_tables[3:]

    for index, region in enumerate(region_tables):
        region["Region"] = region_names[index]

    # combine list of dataframes to one dataframe
    regions_df = pd.concat(region_tables)

    # Rename columns
    regions_df = regions_df.rename(columns={"±% p.a.": "Growth", "Pop.": "Pop"})

    return regions_df
