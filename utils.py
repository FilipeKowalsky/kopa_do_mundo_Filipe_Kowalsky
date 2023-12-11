from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(selection_info):
    from datetime import datetime
    current_year = datetime.now().year
    first_cup = ""
    titles = 0

    for item in selection_info:
        first_cup = datetime.strptime(selection_info["first_cup"], "%Y-%m-%d").year
        titles = selection_info["titles"]
        if selection_info["titles"] < 0:
            raise NegativeTitlesError("titles cannot be negative")

        first_cup_year = 1930
    cup_year = []

    while first_cup_year < current_year:
        first_cup_year = first_cup_year + 4
        cup_year.append(first_cup_year)
        if cup_year[-1] == current_year:
            break

    if (first_cup in cup_year or first_cup == 1930):
        print("certo")
    else:
        raise InvalidYearCupError("there was no world cup this year")

    diferent_year = []
    while first_cup < current_year:
        first_cup = first_cup + 4
        diferent_year.append(first_cup)
    if titles > len(diferent_year):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
