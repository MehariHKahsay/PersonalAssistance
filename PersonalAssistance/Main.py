from inspect import currentframe, getframeinfo
import sqlite3
from Countries import Countries
from Countries import History
from Calculator import Calculator

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('country.db')
c = conn.cursor()
#c.execute("DROP TABLE country")
c.execute("""CREATE TABLE IF NOT EXISTS country(
            name text,
            location text,
            capital_city text,
            currency text,
            population integer,
            area integer)""")
 

c.execute("""CREATE TABLE IF NOT EXISTS history(
            country text,
            field text,
            result text
            )""")

canada = Countries('Canada','North America','Ottawa', 'Canadian dollar', 32268240, 9970610)
eritrea = Countries('Eritrea','Africa','Asmara', 'Nakfa', 4401357, 117600)
iraq = Countries('Iraq','Asia','Baghdad', 'Iraqi dinar', 28807190, 438317)
jordan = Countries('Jordan','Asia','Amman', 'Jordanian dinar', 5702776, 89342)
cuba = Countries('Cuba','North America','Havana', 'Cuban peso', 11269400, 110861)
sudan = Countries('Sudan','Africa','Khartoum', 'Sudanese dinar', 36232950, 2505813)
peru = Countries('Peru','South America','Lima', 'Peruvian nuevo sol', 27968240, 1285216)

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
    #return list of country
    with conn:
        c.execute("SELECT distinct(name) FROM country")
        result = list(c.fetchall())
        print(result)
def locations():
    #return list of continents
        with conn:
            c.execute("SELECT distinct(location) FROM country")
            result = list(c.fetchall())
            print(result)

def capitalCities():
    #return list of capital cities
        with conn:
            c.execute("SELECT distinct(capital_city) FROM country")
            result = list(c.fetchall())
            print(result)

def currencies():
    #return list of currencies
        with conn:
            c.execute("SELECT distinct(currency) FROM country")
            result = list(c.fetchall())
            print(result)

def populations():
    #returns population
        with conn:
            c.execute("SELECT distinct(population) FROM country")
            result = list(c.fetchall())
            print(result)

def area():
#returns population
    with conn:
        c.execute("SELECT distinct(area) FROM country")
        result = list(c.fetchall())
        print(result)

#Function to display country, continents, populations, capital cities, or currencies         
def displayQueries():
    user = input("Type one of the following \n countries, continents, populations, capital cities, currencies: ")
    usertypes = ["countries", "continents","populations", "capital cities", "currencies" ]
    userlower = user.lower()
    if userlower in usertypes:
        pass
    else:
        print("Sorry, I don’t have that information, try again...")
        displayQueries()

    if userlower == "countries":
        countries()
    elif userlower == "continents":
        locations()
    elif userlower == "populations":
        populations()
    elif userlower == "capital cities":
        capitalCities()
    elif userlower == "currencies":
        currencies()
    else:
        pass

#List of country, based on the argument received (Country Name)
def nameOfcountry(country):
        with conn:
            c.execute("SELECT name FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)

#List of locations, based on the argument received (Country Name)
def locationOfcountry(country):
        with conn:
            c.execute("SELECT location FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)

#List of currencies, based on the argument received (Country Name)
def currencyOfcountry(country):
        with conn:
            c.execute("SELECT currency FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)

#List of capital cities, based on the argument received (Country Name)
def capitalCityOfcountry(country):
        with conn:
            c.execute("SELECT capital_city FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)            

#List of populations, based on the argument received (Country Name)
def populationOfcountry(country):
        with conn:
            c.execute("SELECT population FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)
#Not required ---- List of areas, based on the argument received (Country Name)
def areaOfcountry(country):
        with conn:
            c.execute("SELECT area FROM country WHERE upper(name) =:name",{'name':country})
            result = list(c.fetchone())
            print(result)

#Display result when a user quereies by "Field of Country"
def userQueries():
        userinput = str(input("Type field of a Contry: Example \"Name of Canada\":"))
        fieldnames = ["NAME", "LOCATION", "CURRENCY", "CAPITAL_CITY", "POPULATION", "AREA"]
        countrynames = ["ERITREA", "IRAQ", "CANADA","CUBA","SUDAN","PERU","JORDAN" ]
        splited = userinput.split(" ")
        print(splited)
        field = splited[0]
        ufield = field.upper()
        country = splited[2]
        countryname = country.upper()

        #Error handling for field and country
        if ufield in fieldnames:
            pass
        else:
             print("Wrong field name input try again...")
             userQueries() 

        if countryname in countrynames:
            pass
        else:
             print("Wrong country name input try again...")
             userQueries() 
        
        #Returns the method that gives the required data based on the field and country passed 
        if ufield == "NAME":
            result = nameOfcountry(countryname)
            c.execute("INSERT INTO history values(?,?,?)",( countryname, ufield, result) )
        elif ufield == "LOCATION":
            result = locationOfcountry(countryname)
            c.execute("INSERT INTO history values(?,?,?)",( countryname, ufield, result) )
        elif ufield == "CURRENCY":
            result = currencyOfcountry(countryname)
            c.execute("INSERT INTO history values(?,?,?)",( countryname, ufield, result) )
        elif ufield == "CAPITAL_CITY":
            result = capitalCityOfcountry(countryname)
            c.execute("INSERT INTO history values(?,?,?)",( countryname, ufield, result) )
        elif ufield == "POPULATION":
            result = populationOfcountry(countryname)
            c.execute("INSERT INTO history values(?,?,?)",( countryname, ufield, result) )
        elif ufield == "AREA":
            areaOfcountry(countryname)
        else:
            pass
 
def showhistory():
    user = input("Type \'datum\' to see history: ")
    userlower = user.lower()
    if userlower == "datum":
        c.execute("SELECT * FROM history")
        print(c.fetchall(),"\n")
    else:
        print("Worng input try again...")
        showhistory()
 
def showhistorybylinenumber():
    user = input("Type \'datum LINE_NUMBER\' to see history, Eample datum 5: \n ")
    spliter = user.split(" ")
    LINE_NUMBER = int(spliter[1])
    datum = spliter[0]
    datumlower = datum.lower()
    if (datumlower == "datum") and (type(LINE_NUMBER) == int):
        c.execute("SELECT * FROM history")
        print(c.fetchall())
    else:
        print("Worng input try again...")
        showhistorybylinenumber()
        

def clearistory():
    askuser = input("Do you want to clear history? Y/N :\n")
    askuserlower = askuser.upper()
    if askuserlower == "Y":
        clearhistory = input("Type \'datum clear\' to clear the history \n : ")
        if clearhistory.upper() == "DATUM CLEAR":
            c.execute("DELETE FROM history")
            print("Datum history cleared!!! \n")
        else:
            print("Worng input try again...")
            clearistory()
    elif askuserlower == "N":
        pass
    else:
        print("Not valid input, try typing Y/N again...")
        clearistory()

def askusertorunprogramagain():
    askusertorunagain = input("Do you want to run the program again? Y/N\n:")
    changetolower = askusertorunagain.lower()
    if changetolower == "y":
        print("\n ############################################### Sure, you are now running the program again! ################################################## \n")
        runtheprogram()
    elif changetolower == "n":
        print("Thank you for using the PA, see you again!!!")
        pass
    else:
        askusertorunprogramagain()

#Display results for the Calculator program
def displayCalculator():
    test = Calculator()
    test.welcome()
    test.calculate()
    test.history()
    test.viewHistory()
    test.clearHistory()


#Function to display Countries program     
def displayCountries():
    displayQueries()
    userQueries()
    showhistory()
    #showhistorybylinenumber()
    clearistory()
    askusertorunprogramagain()

#Run the program
def runtheprogram():
    displayCalculator()
    displayCountries()

runtheprogram()

conn.commit()
conn.close()