import pandas as pd
import sqlite3

def excel_sql(nome_file_xls, nome_tabella, nome_db):
    try:
        # Legge il file Excel e ottiene il primo foglio
        df = pd.read_excel(nome_file_xls)

        # Mappa dei tipi di dati Excel a tipi di dati SQL
        type_mapping = {
            'int64': 'INTEGER',
            'float64': 'FLOAT',
            'object': 'TEXT',
            'bool': 'BOOLEAN',
            'datetime64[ns]': 'DATETIME'
        }
        # Genera la query per creare la tabella
        create_query = f"CREATE TABLE IF NOT EXISTS {nome_tabella} (\n"
        for col in df.columns:
            col_type = str(df[col].dtype)
            sql_type = type_mapping.get(col_type, 'TEXT')  # Se non trova il datatype identico mette TEXT
            create_query += f"    {col} {sql_type},\n"
        create_query = create_query.rstrip(',\n') + "\n);"
        # Connessione al database SQLite
        conn = sqlite3.connect(nome_db)
        cursor = conn.cursor()

        # Crea la tabella nel database
        print(create_query)
        cursor.execute(create_query)
        print(f"Tabella: '{nome_tabella}' creata con successo.")

        # Genera la query di inserimento dei dati
        placeholders = ", ".join(["?"] * len(df.columns))
        insert_query = f"INSERT INTO {nome_tabella} ({', '.join(df.columns)}) VALUES ({placeholders})"
        # Inserisce i dati nel database
        cursor.executemany(insert_query, df.values.tolist())
        conn.commit()
        print(f"Dati inseriti con successo nella tabella: '{nome_tabella}'.")

        print(f"Estraggo tutti i dati dalla tabella:  '{nome_tabella}'.")
        cursor.execute("SELECT * FROM anagrafiche")
        results = cursor.fetchall()
        print(results)
        # Chiude la connessione
        conn.close()
        print("Esecuzione terminata correttamente.")

    except Exception as e:
        return f"Errore durante la generazione della tabella o l'inserimento dei dati: {e}"

# Lancio script
nome_file_xls = "Anagrafiche.xlsx"
nome_tabella = "anagrafiche"
nome_db = "project_work.db" 

excel_sql(nome_file_xls, nome_tabella, nome_db)
