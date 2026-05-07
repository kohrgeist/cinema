import sqlite3

class SessaoRepository:
    def __init__(self, db_name="cinema.db"):
        self.db_name = db_name
        self._inicializar_banco()

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def _inicializar_banco(self):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS sessao (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                filme TEXT,
                                data_hora TEXT,
                                ingressos_disponiveis INTEGER)''')
            
            cursor.execute("SELECT COUNT(*) FROM sessao")
            if cursor.fetchone()[0] == 0:
                dados = [
                    ("O Senhor dos Anéis: O Retorno do Rei", "19:00", 45),
                    ("Duna: Parte 2", "21:30", 0),
                    ("Matrix (Reexibição)", "18:00", 5)
                ]
                cursor.executemany("INSERT INTO sessao (filme, data_hora, ingressos_disponiveis) VALUES (?, ?, ?)", dados)
                conn.commit()

    def buscar_todas(self):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, filme, data_hora, ingressos_disponiveis FROM sessao")
            return cursor.fetchall()

    def deduzir_ingresso(self, sessao_id):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE sessao SET ingressos_disponiveis = ingressos_disponiveis - 1 WHERE id = ? AND ingressos_disponiveis > 0", (sessao_id,))
            conn.commit()
            return cursor.rowcount > 0