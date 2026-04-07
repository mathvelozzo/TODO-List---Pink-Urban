"""Migration: adds position column to list_item table."""
import sqlite3
import os

db_path = os.path.join('var', 'app-instance', 'pink_urban.db')

if not os.path.exists(db_path):
    print(f'Banco nao encontrado em {db_path} - sera recriado no proximo start.')
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(list_item)")
    columns = [row[1] for row in cursor.fetchall()]

    if 'position' in columns:
        print('Coluna position ja existe. Nada a fazer.')
    else:
        cursor.execute("ALTER TABLE list_item ADD COLUMN position INTEGER DEFAULT 0")
        # Set initial positions based on id
        cursor.execute("UPDATE list_item SET position = id")
        conn.commit()
        print('Coluna position adicionada com sucesso!')

    conn.close()
    print('Migration concluida. Reinicie o Flask: py run.py')
