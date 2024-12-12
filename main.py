from typing import List
import pandas as pd
from menu_interface import MenuInterface
from models import Region
from wikipedia import create_dataframe, region_names


def save_to_csv(regions_df: pd.DataFrame):
    # export to csv by year
    regions_df.query("Year==1950").to_csv("1950.csv", index=False)
    regions_df.query("Year==1960").to_csv("1960.csv", index=False)
    regions_df.query("Year==1970").to_csv("1970.csv", index=False)
    regions_df.query("Year==1980").to_csv("1980.csv", index=False)
    regions_df.query("Year==1990").to_csv("1990.csv", index=False)
    regions_df.query("Year==2000").to_csv("2000.csv", index=False)
    regions_df.query("Year==2010").to_csv("2010.csv", index=False)
    regions_df.query("Year==2021").to_csv("2021.csv", index=False)

    print("CSV files saved")


def main():
    # Get the tables from HTML and process it in a pandas Dataframe
    wiki_page = (
        "List of continents and continental subregions by population - Wikipedia.html"
    )
    regions: pd.DataFrame = create_dataframe(html_file=wiki_page)
    print(regions)

    # Create Region instances
    region_objects: List[Region] = [
        Region(name=region_name, data=regions)
        for region_name in region_names
        if "Total" not in region_name
    ]

    menu = MenuInterface()
    selected_function, selected_area = menu.get_input()

    menu.run_statistic(
        function_name=selected_function,
        selected_region=Region(name=selected_area, data=regions),
    )

    print("done")


if __name__ == "__main__":
    main()
