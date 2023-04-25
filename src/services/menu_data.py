import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.file = pd.read_csv(source_path)
        self.dict_dishes = {}
        self.dishes = set()
        for i in range(len(self.file)):
            self.dict_dishes[self.file.iloc[i]['dish']] = [self.file.iloc[i]['price']]
        for i in range(len(self.file)):
            self.dict_dishes[self.file.iloc[i]['dish']].append((self.file.iloc[i]['ingredient'], self.file.iloc[i]['recipe_amount']))
        for key, value in self.dict_dishes.items():
            dish = self.dish_maker(key, value)
            self.dishes.add(dish)
    def dish_maker(self, dish_name: str, dish_info):
        dish = Dish(dish_name, dish_info[0])
        for idx, element in enumerate(dish_info):
            if idx != 0:
                dish.add_ingredient_dependency(Ingredient(element[0]), element[1])
        return dish