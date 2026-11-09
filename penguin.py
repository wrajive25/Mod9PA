# penguin.py
# Rajive Williams
# 11/09/2026
# Class representing a penguin

class Penguin:
    def __init__(self, sample_number, species, body_mass):
        self.sample_number = sample_number
        self.species = species
        self.body_mass = body_mass

    def display_info(self):
        print(f"Sample Number: {self.sample_number}")
        print(f"Sepcies: {self.species}")
        print(f"Body Mass: {self.body_mass} g")
 
