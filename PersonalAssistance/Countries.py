class Countries:
    """description of class"""
    def __init__(self, name, location, capital_city, currency, population, area):
        self.name = name
        self.location = location
        self.capital_city = capital_city
        self.currency = currency
        self.population = population
        self.area = area       
 
class History:
    def __init__(self, country, field, result):
        self.country = country
        self.field = field
        self.result = result
