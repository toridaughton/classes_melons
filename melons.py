"""This file should have our melon-type classes in it."""


class MelonOrder:
    def get_base_price(self):
        return 5.0


class WatermelonOrder:

    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = self.get_base_price() * qty
        if qty >= 3:
            total *= 0.75
        return total


class Cantaloupe:
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        total = self.get_base_price() * qty
        if qty >= 5:
            total *= 0.5
        return total


class CasabasOrder:
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        total = (self.get_base_price() + 1) * qty
        return total


class ChristmasOrder:
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        total = self.get_base_price * qty
        return total

class HornedMelonOrder:
    species = 'Horned Melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.get_base_price * 1.5) * qty
        return total


class OgenOrder:
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        total = (self.get_base_price +1) * qty
        return total


class SantaClausOrder:
    species = 'Santa Claus'
    color = 'green' 
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        total = (self.get_base_price * 1.5) * qty
        return total


class SharlynOrder:
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    season = ['Summer']

    def get_price(self, qty):
        total = (self.get_base_price * 1.5) * qty
        return total


class Xigua:
    species = 'Xigua'
    color = 'black'
    imported = True
    shape ='square'
    season = ['Summer']
    
    def get_price(self, qty):
        total = (self.get_base_price * 1.5 * 2) * qty
        return total


    # def get_price(self, qty: int) -> float:
    #     """Calculate price, given a number of melons ordered."""
    #     total =  qty * self.base_price

    #     if self.species == "Casabas" or self.species == "Ogens":
    #         total+= 1
        
    #     if self.imported == True:
    #         total *= 1.5
        
    #     if self.shape == "Square":
    #         total *= 2
        
    #     if self.species == "Watermelon" and qty >= 3:
    #         total *= 0.75
        
    #     if self.species == "Cantalope" and qty >= 5:
    #         total *= 0.5

        # return total
