# backend/app.py  (solo para la prueba, luego lo quitaremos)
import sqlite3, pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent        # .../backend
DB_DIR   = BASE_DIR / "database"

db_path  = DB_DIR / "test.db"
sql_path = DB_DIR / "schema.sql"

conn = sqlite3.connect(db_path)
with sql_path.open("r", encoding="utf-8") as f:
    conn.executescript(f.read())

tables = [row[0] for row in conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)]
conn.close()
print("✓ Tablas creadas:", tables)
