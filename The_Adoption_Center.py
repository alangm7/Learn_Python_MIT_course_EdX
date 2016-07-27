class AdoptionCenter:

    def __init__(self, name, species_types, location):
        self.name = name
        self.location = (float(location[0]),float(location[1]))
        self.species_types = species_types
    def get_number_of_species(self, animal):
        return self.species_types.get(animal,0)
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        n = self.species_types.get(species,0)
        if n == 1:
            self.species_types.pop(species)
        elif n > 1:
            self.species_types.update({species:n-1})
