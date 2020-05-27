import sqlite3


conn = sqlite3.connect('stocks.db')

c = conn.cursor()

try:
# Create table example of the DDL or Data Definition Language
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

except sqlite3.OperationalError as e:
   print('Database exists') 

# Insert a row of data example of the DML or Data Manipulation Language
#c.execute("INSERT INTO stocks VALUES ('2020-05-05','BUY','RHAT',100,35.14)")
#c.execute("INSERT INTO stocks VALUES ('2020-05-06','SELL','YHOO',200,25.14)")
#c.execute("INSERT INTO stocks VALUES ('2020-05-07','BUY','GGOL',100,35.14)")
# Save (commit) the changes

#conn.commit()
# retrieve or select all the records from the database
#result = c.execute("""
#            SELECT date,symbol,trans FROM stocks WHERE date = \'2020-05-05\';
#""")
#result = c.execute("""
#            UPDATE stocks SET price=40.5 WHERE symbol = \'RHAT\';
#""")
result = c.execute("""

        DELETE FROM stocks WHERE symbol = \'RHAT\'

""")
conn.commit()

print(result)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
