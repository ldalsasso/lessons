import random


# Courses
MAT = 'Matemática'
ENG = 'Inglés'
FRA = 'Frances'
GER = 'Aleman'
FIS = 'Física'

# Courses choices
COURSES_CHOICES = (
    (MAT, MAT),
    (ENG, ENG),
    (FRA, FRA),
    (GER, GER),
    (FIS, FIS),
)


def get_random_choice_from_choices(choices_list):
    """Return a random choice from a choices list"""
    choices = [x[0] for x in choices_list]

    return random.choice(choices)
