import re
from abc import ABC, abstractmethod


class Person:

    def __init__(self, id, name, is_a_student):
        if not self.is_valid_name(name):
            raise ValueError("Invalid Name")
        self.id = id
        self.__name = name
        self.is_a_student = is_a_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise ValueError("Invalid Name")
        self.__name = new_name

    @staticmethod
    def is_valid_name(name):
        if not re.fullmatch(r"([a-zA-Z]+\s)+[a-zA-Z]+", name):
            return False
        return True


class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    def maximum_occupants(self):
        by_area = self.area // 20
        by_rooms = self.number_of_rooms * 2
        return min(by_area, by_rooms)

    def register_resident(self, person):
        if person in self.__occupants.values():
            return
        if self.number_of_occupants == self.maximum_occupants:
            raise RuntimeError("No room to register person")
        self.__occupants[person.id] = person

    def unregister_resident(self, id):
        self.__occupants.pop(id)

    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]

    @abstractmethod
    def calculate_value(self):
        pass


class Villa(Residence):

    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)


class StudentKot(Residence):

    def __init__(self, address, area):
        super().__init__(address, area, 1)

    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError("Persoon moet een student zijn")
        super().register_resident(person)

    def calculate_value(self):
        return 150000 + (750 * self.area)


# maak een aantal personen
aimee = Person("12.34.56-789.01", "Aimee Backiel", False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# maak enkele woningen
my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
my_kot = StudentKot("Kortestraat 6, 3000 Leuven", 20)

# controleer de waarden van de eigenschappen
print(my_villa.calculate_value())

print(my_kot.calculate_value())


# Verhuis de mensen naar een woning
my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

# controleer de bewoners van de villa
print(my_villa.resident_names)

# Op een dag, helaas, zal Bastian opgroeien en verhuizen naar zijn studentenkot
my_villa.unregister_resident(bastian.id)
my_kot.register_resident(bastian)

# controleer de bewoners opnieuw
print(my_villa.resident_names)

print(my_kot.resident_names)

# Met al haar vrije tijd kan Aimee de garage uitbreiden om ruimte te maken voor al haar hobby's.
my_villa.garage_capacity = 3
print(my_villa.calculate_value())
