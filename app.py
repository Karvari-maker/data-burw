from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

# Paksa path db nya ada di folder yang sama dengan app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'warga_rw.db')

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = []
    cari = ""
    if request.method == 'POST':
        cari = request.form['cari']
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        query = "SELECT * FROM warga WHERE nama LIKE ? ORDER BY nama"
        hasil = conn.execute(query, ('%' + cari + '%',)).fetchall()
        conn.close()
    return render_template('index.html', hasil=hasil, cari=cari)

@app.route('/warga/<int:id>')
def detail_warga(id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    warga = conn.execute('SELECT * FROM warga WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if warga is None:
        return "Data warga tidak ditemukan", 404
    
    return render_template('detail.html', warga=warga)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=False, use_reloader=False	)