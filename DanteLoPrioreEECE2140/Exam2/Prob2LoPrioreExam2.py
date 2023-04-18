# Dante LoPriore 
# April, 11, 2022
# Exam 2 Problem 2

class House:
    
    def __init__(self, num_room, year_built, city, type = 'S'):
        self.num_room = num_room
        self.year_built = year_built
        self.city = city
        self.type = type

    # getter method
    @property
    def year_built(self):
        return self._year_built

    # setter method
    @year_built.setter
    def year_built(self, val):
        if ((0 <= val) and (val <= 2023)):
            self._year_built = val
        else:
            raise ValueError('Invalid Range')
    
    def __str__(self):
        if (self.type == 'M'):
            return f'Multi-Family house with {self.num_room} rooms located in {self.city} was built in {self.year_built}'
        if (self.type == 'S'):
            return f'Single-Family house with {self.num_room} rooms located in {self.city} was built in {self.year_built}'
        else:
            return f'{self.type}-Family house with {self.num_room} rooms located in {self.city} was built in {self.year_built}'
    
    # read-only property
    @property
    def age(self):
        return self._year_built
    
    def __gt__(self, other):
        if (isinstance(other, House)):
            return self.num_room > other.num_room
        if (isinstance(other, int)):
            return self.year_built > other
        if (isinstance(other, str)):
            return len(self.city) > len(other)
        else:
            raise ValueError("Invalid Type")

class Duplex(House):
    
    def __init__(self, num_room, year_built, city):
        super().__init__(num_room, year_built, city, 'M')
        self.num_units = 2
    
    def __add__(self, other):
        if(isinstance(other, Duplex)):
            return Duplex(self.num_room + other.num_room, max(self.year_built, other.year_built), self.city + " and " + self.city)
        else:
            raise ValueError("Invalid Type")
        
    def __iadd__(self, other):
        if(isinstance(other, Duplex)):
            self.num_room += other.num_room
            self.year_built += other.year_built
            self.city += other.city
            return self
        else:
            raise ValueError("Invalid Type")

house1 = House(4, 2020, 'Boston', 'M')
house2 = House(3, 2023, 'Boston',)
print(house1)

print(house1 > 10)

dup1 = Duplex(6, 2022, 'Chelsea')
print(dup1 + dup1)

