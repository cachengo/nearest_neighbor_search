from annoy import AnnoyIndex
import numpy as np  # Pickle uses this
import pickle
import sqlite3

from app import app

with sqlite3.connect(app.config['SQLALCHEMY_DATABASE_PATH']) as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM vector")
    rows = cur.fetchall()
    index = AnnoyIndex(app.config['ANN_INDEX_LENGTH'])
    for row in rows:
        index.add_item(row[0], pickle.loads(row[1]))
    index.build(10)
    index.save(app.config['ANN_INDEX_PATH'])
