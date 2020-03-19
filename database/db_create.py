import sqlite3
from config import db_path

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cur = con.cursor()
