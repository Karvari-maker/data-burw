import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'warga_rw.db')

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS warga")

c.execute('''CREATE TABLE warga
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nama TEXT NOT NULL,
              jenis_kelamin TEXT NOT NULL,
              umur INTEGER,
              pekerjaan TEXT,
              alamat TEXT)''')

data = [
    ('Ahmad Fauzi', 'L', 28, 'Karyawan Swasta', 'Jl. Mawar No. 5 RT 03/RW 10'),
    ('Siti Aminah', 'P', 25, 'Mahasiswa', 'Jl. Melati No. 12 RT 02/RW 10'),
    ('Budi Santoso', 'L', 35, 'Guru', 'Jl. Kenanga No. 8 RT 01/RW 10'),
    ('Dewi Lestari', 'P', 30, 'Wiraswasta', 'Jl. Anggrek No. 3 RT 04/RW 10'),
    ('Rudi Hartono', 'L', 42, 'PNS', 'Jl. Dahlia No. 9 RT 02/RW 10')
]

# FIX: 5 tanda tanya untuk 5 kolom
c.executemany("INSERT INTO warga (nama, jenis_kelamin, umur, pekerjaan, alamat) VALUES (?, ?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("Sukses! Database dibuat di:", DB_PATH)
print("Total data masuk:", len(data))