import sqlite3

conn = sqlite3.connect('qubrica.db')
c = conn.cursor()
c.execute(''' CREATE TABLE contatti
		      (nome text,
		      cognome text,
		      telefono text)
		      ''')

purchases = [('Mario', 'Rossi', '059 55 44 33'),
             ('Gino', 'Bianchi', '098 223 21 22'),
             ('DIno', 'Verdi', '098 282 282 282'),
            ]

c.executemany('INSERT INTO contatti VALUES (?,?,?)',purchases)
conn.commit()
conn.close




