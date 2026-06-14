import data.tables as tables
from core.dice import roll_nd6


def get_star_type() -> str:
    first_roll = roll_nd6(2)
    result = tables.STAR_TYPE_DETERMINATION_TYPE[first_roll]

    if result == "Special":
        special_roll = roll_nd6(2)
        result = tables.STAR_TYPE_DETERMINATION_SPECIAL[special_roll]

        if result == "Giants":
            giants_roll = roll_nd6(2)
            result = tables.STAR_TYPE_DETERMINATION_GIANTS[giants_roll]
        elif result == "Peculiar":
            pecular_roll = roll_nd6(2)
            result = tables.STAR_TYPE_DETERMINATION_PECULIAR[pecular_roll]
    elif result == "Hot":
        hot_roll = roll_nd6(2)
        result = tables.STAR_TYPE_DETERMINATION_HOT[hot_roll]

    return result
