import sqlite3

conn=sqlite3.connect("qubrica.db")
conn.row_factory=sqlite3.Row

c=conn.cursor()
rec=c.execute('''SELECT nome,cognome,telefono
                 FROM contatti
                 ORDER BY cognome''')
for row in rec:
    print(row['nome'],row['cognome'],row['telefono'])

conn.close()
