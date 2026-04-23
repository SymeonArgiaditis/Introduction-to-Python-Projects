class Planet:

    def __init__(self, name, planet_type, star):
        attributes = [name, planet_type, star]
        
        for attr in attributes:
            if not isinstance(attr, str):
                raise TypeError("name, planet type, and star must be strings")
            if attr == '':
                raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet('Earth', 'Terrestrial Planet', 'Sun')
planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_3 = Planet('Neptune', 'Ice Giant', 'Sun')

print(planet_1)
print(planet_1.orbit(), '\n')
print(planet_2)
print(planet_2.orbit(), '\n')
print(planet_3)
print(planet_3.orbit(), '\n')