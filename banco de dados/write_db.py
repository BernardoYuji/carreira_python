import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO estudantes(nome, idade) \
        VALUES (?, ?) 
    """,
        ("Bernardo", 19)

)

cursor.execute(
    """
        INSERT INTO disciplinas (
            estudante_id, nome_disciplina
        ) VALUES (?, ?)
    """,
    (1, "Development")
)

conn.commit()
conn.close()