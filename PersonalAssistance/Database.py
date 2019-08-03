import sqlite3
conn = sqlite3.connect('Country.db')
c = conn.cursor()
c.execute("""CREATE TABLE country(
Name text,
Location text,
Capital city text,
Currency text,
Population integer,
Area integer)""")

conn.commit()
conn.close()
 