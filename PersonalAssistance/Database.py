import sqlite3
from Countries import Countries

conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('Countries.db')
c = conn.cursor()
c.execute("""CREATE TABLE countries(
            name text,
            location text,
            capital_city text,
            currency text,
            population integer,
            area integer)""")
 
canada = Countries('Canada','North America','Ottawa', 'Canadian dollar', 32268240, 9970610)
eritrea = Countries('Eritrea','Africa','Asmara', 'Nakfa', 4401357, 117600)
iraq = Countries('Iraq','Asia','Baghdad', 'Iraqi dinar', 28807190, 438317)
jordan = Countries('Jordan','Asia','Amman', 'Jordanian dinar', 5702776, 89342)
cuba = Countries('Cuba','North America','Havana', 'Cuban peso', 11269400, 110861)
sudan = Countries('Sudan','Africa','Khartoum', 'Sudanese dinar', 36232950, 2505813)
peru = Countries('Peru','South America','Lima', 'Peruvian nuevo sol', 27968240, 1285216)

c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (canada.name, canada.location, canada.capital_city, canada.currency, canada.population, canada.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (eritrea.name, eritrea.location, eritrea.capital_city, eritrea.currency, eritrea.population, eritrea.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (iraq.name, iraq.location, iraq.capital_city, iraq.currency, iraq.population, iraq.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (jordan.name, jordan.location, jordan.capital_city, jordan.currency, jordan.population, jordan.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (cuba.name, cuba.location, cuba.capital_city, cuba.currency, cuba.population, cuba.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (sudan.name, sudan.location, sudan.capital_city, sudan.currency, sudan.population, sudan.area))
conn.commit()
c.execute("INSERT INTO countries values(?,?,?,?,?,?)", (peru.name, peru.location, peru.capital_city, peru.currency, peru.population, peru.area))

def countries():
    #return list of countries
    with conn:
        c.execute("SELECT name FROM countries")
        result = c.fetchall()
        print(result)
def locations():
    #return list of continents
        with conn:
            c.execute("SELECT location FROM countries")
            result = c.fetchall()
            print(result)

def capitalCities():
    #return list of capital cities
        with conn:
            c.execute("SELECT capital FROM countries")
            result = c.fetchall()
            print(result)

def currencies():
    #return list of currencies
        with conn:
            c.execute("SELECT currency FROM countries")
            result = c.fetchall()
            print(result)

def population():
    #returns population
        with conn:
            c.execute("SELECT population FROM countries")
            result = c.fetchall()
            print(result)

def area():
#returns population
    with conn:
        c.execute("SELECT area FROM countries")
        result = c.fetchall()
        print(result)

def displayQueries():
    user = input("Pleae type NAME, LOCATION, CURRENCY, CAPITAL_CITY, POPULATION, or AREA: ")
    if user.upper() == "NAME":
        countries()
    elif user.upper() == "LOCATION":
        locations()
    elif user.upper() == "CURRENCY":
        currencies()
    elif user.upper() == "CAPITAL CITY":
        capitalCities()
    elif user.upper() == "POPULATION":
        population()
    elif user.upper() == "AREA":
        area()
    else:
        print("Wrong input...")
        displayQueries()

def nameOfcountries(countries):
        with conn:
            c.execute("SELECT name FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)
def locationOfcountries(countries):
        with conn:
            c.execute("SELECT location FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)

def currencyOfcountries(countries):
        with conn:
            c.execute("SELECT currency FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)


def capitalCityOfcountries(countries):
        with conn:
            c.execute("SELECT capital_city FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)            

def populationOfcountries(countries):
        with conn:
            c.execute("SELECT population FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)

def areaOfcountries(countries):
        with conn:
            c.execute("SELECT area FROM countries WHERE upper(name) =:name",{'name':countries})
            result = c.fetchall()
            print(result)

def userQueries():
        userinput = str(input("Type field of a Contry: Example \"Name of Canada\":"))
        fieldnames = ["NAME", "LOCATION", "CURRENCY", "CAPITAL_CITY", "POPULATION", "AREA"]
        countrynames = ["ERITREA", "IRAQ", "CANADA","CUBA","SUDAN","PERU" ]
        splited = userinput.split(" ")
        print(splited)
        field = splited[0]
        ufield = field.upper()
        country = splited[2]
        countriesname = country.upper()
        if ufield in fieldnames:
            pass
        else:
             print("Wrong field name input try again...")
             userQueries() 

        if countriesname in countrynames:
            pass
        else:
             print("Wrong country name input try again...")
             userQueries() 

        if ufield == "NAME":
            nameOfcountries(countriesname)
        elif ufield == "LOCATION":
            locationOfcountries(countriesname)
        elif ufield == "CURRENCY":
            currencyOfcountries(countriesname)
        elif ufield == "CAPITAL_CITY":
            capitalCityOfcountries(countriesname)
        elif ufield == "POPULATION":
            populationOfcountries(countriesname)
        elif ufield == "AREA":
            areaOfcountries(countriesname)
        else:
            pass
 
userQueries()
displayQueries()
conn.commit()
conn.close()


