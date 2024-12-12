from typing import List
from models import Region


class MenuInterface:
    def __init__(self) -> None:
        self.prompt_choice = "\n\nChoose an option: \n"
        self.functions = {
            "display_pop": "Display the population of a region or continent.",
            "compare_pop": "Compare the population between two regions or continents.",
            "sort_pop": "Sort regions or continents by population size.",
            "calc_growth": "Calculate the annual growth rate of regions or continents.",
            "compare_growth": "Compare the growth rate between two regions or continents.",
            "sort_growth": "Sort regions or continents by growth rate.",
            "exit": "Exit",
        }
        self.regions = [
            "Eastern Africa",
            "Middle Africa",
            "Northern Africa",
            "Southern Africa",
            "Western Africa",
            "Caribbean",
            "Central America",
            "Northern America",
            "Central Asia",
            "Eastern Asia",
            "South-eastern Asia",
            "Southern Asia",
            "Western Asia",
            "Eastern Europe",
            "Northern Europe",
            "Southern Europe",
            "Western Europe",
        ]
        self.continents = [
            "Africa",
            "North America",
            "South America",
            "Asia",
            "Europe",
            "Oceania",
        ]
        self.years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2021]

    def _generate_ordered_list_from_array(self, array: List):
        ordered_list = [f"{index+1}\t{value}\n" for index, value in enumerate(array)]
        stringify_ordered_list = "".join(ordered_list)
        return stringify_ordered_list

    def _get_user_selected_function(self):
        functions_text = f"\n{''.join([f"{index+1}\t{val}\n" for index, (key, val) in enumerate(self.functions.items())])}"

        selected_function = int(input("Menu:" + functions_text + self.prompt_choice))
        if selected_function > 7 or selected_function < 0:
            raise IndexError("Please choose a valid input")
        elif selected_function == 7:
            print("Bye bye")
            exit(0)

        for index, (key, value) in enumerate(self.functions.items()):
            if index + 1 == selected_function:
                return key
        raise IndexError("Couldn't find that function")

    def _get_user_selected_area(self) -> str:
        # region_or_cont_text = "You want to look at:\n1 regions\n2 continents"
        # regions_text = f"\n{self._generate_ordered_list_from_array(self.regions)}"
        # continents_text = f"\n{self._generate_ordered_list_from_array(self.continents)}"

        # # Get input
        # input_num = int(input(region_or_cont_text + self.prompt_choice))

        # # Get area name from input
        # if input_num == 1:
        #     # regions
        #     selected_area_input = int(input(regions_text + self.prompt_choice))
        #     selected_area_name = self.regions[selected_area_input - 1]
        # elif input_num == 2:
        #     # continents
        #     selected_area_input = int(input(continents_text + self.prompt_choice))
        #     selected_area_name = self.continents[selected_area_input - 1]
        # else:
        #     raise IndexError("Please choose a valid input")

        regions_text = f"\n{self._generate_ordered_list_from_array(self.regions)}"

        # Get region name from input
        selected_area_input = int(input(regions_text + self.prompt_choice))
        selected_area_name = self.regions[selected_area_input - 1]

        return selected_area_name

    def get_input(self):
        selected_function_name = self._get_user_selected_function()
        selected_area_name = self._get_user_selected_area()

        return selected_function_name, selected_area_name

    def _get_user_selected_year(self):
        # Generate prompt and prompt for year
        ordered_years = self._generate_ordered_list_from_array(self.years)
        prompt = f"\n{ordered_years}{self.prompt_choice}"
        user_input_year = int(input(prompt))
        return self.years[user_input_year - 1]

    def run_statistic(self, function_name: str, selected_region: Region):
        for index, func in enumerate(self.functions.keys()):
            if func == function_name:

                # check what key the function_name is, and execute the chosen function on the Region class
                match index:
                    case 0:
                        # func == display_pop
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._display_population(year=user_selected_year)
                    case 1:
                        # func == compare_pop
                        region_to_compare = self._get_user_selected_area()
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._population_comparison(
                            compare_region=region_to_compare, year=user_selected_year
                        )
                    case 2:
                        # func == sort_pop
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._population_sort(year=user_selected_year)
                    case 3:
                        # func == calc_growth
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._growth_calculator(year=user_selected_year)
                    case 4:
                        # func == compare_growth
                        region_to_compare = self._get_user_selected_area()
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._growth_comparison(
                            compare_region=region_to_compare, year=user_selected_year
                        )
                    case 5:
                        # func == sort_growth
                        user_selected_year: int = self._get_user_selected_year()
                        selected_region._growth_sort(year=user_selected_year)
                    case _:
                        exit(1)
