from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasanha_dish = Dish('lasanha', 30.50)
    assert lasanha_dish.name == 'lasanha'
    lasanha_dish2 = Dish('lasanha', 30.50)
    assert lasanha_dish.__hash__() == lasanha_dish2.__hash__()
    feijoada_dish = Dish('feijoada', 25.30)
    assert lasanha_dish.__hash__() != feijoada_dish.__hash__()
    assert lasanha_dish == lasanha_dish2
    assert lasanha_dish != feijoada_dish
    assert lasanha_dish.__repr__() == "Dish('lasanha', R$30.50)"
    with pytest.raises(TypeError):
        Dish('macarronada', '40')
    with pytest.raises(ValueError):
        Dish('macarronada', -20)
    presunto_ingr = Ingredient('presunto')
    lasanha_dish.add_ingredient_dependency(presunto_ingr, 5)
    assert lasanha_dish.recipe.get(presunto_ingr) == 5
    restrictions = lasanha_dish.get_restrictions()
    assert (Restriction.ANIMAL_DERIVED in restrictions) == True
    assert (Restriction.ANIMAL_MEAT in restrictions) == True
    assert lasanha_dish.get_ingredients() == {presunto_ingr}