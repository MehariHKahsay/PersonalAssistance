import sqlite3
from Country import Country

conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('Country.db')
c = conn.cursor()
c.execute("""CREATE TABLE country(
name text,
location text,
capital_city text,
currency text,
population integer,
area integer)""")
 
canada = Country('Canada','North America','Ottawa', 'Canadian dollar', 32268240, 9970610)
eritrea = Country('Eritrea','Africa','Asmara', 'Nakfa', 4401357, 117600)
iraq = Country('Iraq','Asia','Baghdad', 'Iraqi dinar', 28807190, 438317)
jordan = Country('Jordan','Asia','Amman', 'Jordanian dinar', 5702776, 89342)
cuba = Country('Cuba','North America','Havana', 'Cuban peso', 11269400, 110861)
sudan = Country('Sudan','Africa','Khartoum', 'Sudanese dinar', 36232950, 2505813)
peru = Country('Peru','South America','Lima', 'Peruvian nuevo sol', 27968240, 1285216)

c.execute("INSERT INTO country values(?,?,?,?,?,?)", (canada.name, canada.location, canada.capital_city, canada.currency, canada.population, canada.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (eritrea.name, eritrea.location, eritrea.capital_city, eritrea.currency, eritrea.population, eritrea.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (iraq.name, iraq.location, iraq.capital_city, iraq.currency, iraq.population, iraq.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (jordan.name, jordan.location, jordan.capital_city, jordan.currency, jordan.population, jordan.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (cuba.name, cuba.location, cuba.capital_city, cuba.currency, cuba.population, cuba.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (sudan.name, sudan.location, sudan.capital_city, sudan.currency, sudan.population, sudan.area))
conn.commit()
c.execute("INSERT INTO country values(?,?,?,?,?,?)", (peru.name, peru.location, peru.capital_city, peru.currency, peru.population, peru.area))

def countries():
    #return list of countries
    with conn:
        c.execute("SELECT name FROM country")
        return c.fetchall()
def continents():
    #return list of continents
        with conn:
            c.execute("SELECT location FROM country")
            return c.fetchall()

def capitalCities():
    #return list of capital cities
        with conn:
            c.execute("SELECT capital FROM country")
            return c.fetchall()

def currencies():
    #return list of currencies
        with conn:
            c.execute("SELECT currency FROM country")
            return c.fetchall()

def population():
    #returns population
        with conn:
            c.execute("SELECT population FROM country")
            return c.fetchall()

def population():
#returns population
    with conn:
        c.execute("SELECT area FROM country")
        return c.fetchall()

def userQueries():
    userinput = str(input("Type field of a Contry: Example \"Name of Canada\""))
    splited = userinput.split(" ")
    field = splited.index(0)
    country = splited.index(2)

test = countries()
print(test)
conn.commit()
conn.close()


