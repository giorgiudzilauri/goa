#CW we have codewars

#CW 1
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
def count_by(x, n):
    result = []
    i = 1
    while i <= n:
        result.append(x * i)
        i += 1
    return result

#CW 2
def get_planet_name(id):
    if id == 1:
        return "Mercury"
    elif id == 2:
        return "Venus"
    elif id == 3:
        return "Earth"
    elif id == 4:
        return "Mars"
    elif id == 5:
        return "Jupiter"
    elif id == 6:
        return "Saturn"
    elif id == 7:
        return "Uranus"
    elif id == 8:
        return "Neptune"
    else:
        return "Unknown"


#CW 3
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        return [human_years, cat_years, dog_years]

#CW 4
def twice_as_old(dad_age, son_age):
    if dad_age >= 2 * son_age:
        return dad_age - 2 * son_age
    else:
        return 2 * son_age-dad_age
    
#CW 5
def greet(language):
    if language == 'english':
        return 'Welcome'
    elif language == 'czech':
        return 'Vitejte'
    elif language == 'danish':
        return 'Velkomst'
    elif language == 'dutch':
        return 'Welkom'
    elif language == 'estonian':
        return 'Tere tulemast'
    elif language == 'finnish':
        return 'Tervetuloa'
    elif language == 'flemish':
        return 'Welgekomen'
    elif language == 'french':
        return 'Bienvenue'
    elif language == 'german':
        return 'Willkommen'
    elif language == 'irish':
        return 'Failte'
    elif language == 'italian':
        return 'Benvenuto'
    elif language == 'latvian':
        return 'Gaidits'
    elif language == 'lithuanian':
        return 'Laukiamas'
    elif language == 'polish':
        return 'Witamy'
    elif language == 'spanish':
        return 'Bienvenido'
    elif language == 'swedish':
        return 'Valkommen'
    elif language == 'welsh':
        return 'Croeso'
    else:
        return 'Welcome'