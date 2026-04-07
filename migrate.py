"""Database migration script - adds due_date column to list_item table."""
import sqlite3
import os

db_path = os.path.join('var', 'app-instance', 'pink_urban.db')

if not os.path.exists(db_path):
    print(f'Banco nao encontrado em {db_path} - sera recriado no proximo start.')
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if column exists
    cursor.execute("PRAGMA table_info(list_item)")
    columns = [row[1] for row in cursor.fetchall()]

    if 'due_date' in columns:
        print('Coluna due_date ja existe. Nada a fazer.')
    else:
        cursor.execute("ALTER TABLE list_item ADD COLUMN due_date DATE")
        conn.commit()
        print('Coluna due_date adicionada com sucesso!')

    conn.close()
    print('Migration concluida. Agora rode: py run.py')
