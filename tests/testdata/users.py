import dataclasses
import os
from enum import Enum
from typing import Tuple

from mimesis import Person
from mimesis.enums import Locale, Gender
person = Person(Locale.RU)

class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'

class Hobbies(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'

@dataclasses.dataclass
class User:
    first_name: str = person.first_name(Gender.MALE)
    last_name: str = person.last_name(Gender.MALE)
    email = person.email()
    gender = 'Male'
    mobile = str(person.telephone(mask='##########'))
    birth_day = '12'
    birth_month = 'August'
    birth_year = '1994'
    subjects: Tuple[Subject] = (Subject.History.value, Subject.Maths.value)
    hobbies: Tuple[Hobbies] = (Hobbies.Sports.value, Hobbies.Music.value)
    name_jpg = 'test_pict.jpg'
    address = person.get_current_locale()
    empty = ''
    # abs_path = path_to_jpg
    jpg = os.path.abspath(f'./resourses/{name_jpg}')


random_user = User




