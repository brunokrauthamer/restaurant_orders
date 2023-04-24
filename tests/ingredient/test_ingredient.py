from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1 starting
def test_ingredient():
    presunto_ingredient1 = Ingredient('presunto')
    presunto_ingredient2 = Ingredient('presunto')
    assert int(presunto_ingredient1.__hash__()) == int(presunto_ingredient2.__hash__())
    salmao_ingredient = Ingredient('salmão')
    assert presunto_ingredient1.__hash__() != salmao_ingredient.__hash__()
    assert presunto_ingredient1 == presunto_ingredient2
    assert presunto_ingredient1 != salmao_ingredient
    assert presunto_ingredient1.__repr__() == "Ingredient('presunto')"
    assert presunto_ingredient1.name is "presunto"
    assert (Restriction.ANIMAL_DERIVED in presunto_ingredient1.restrictions) == True
    assert (Restriction.ANIMAL_MEAT in presunto_ingredient1.restrictions) == True