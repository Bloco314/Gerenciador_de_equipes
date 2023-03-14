import sqlite3


class ADMDB:
    def __init__(self):
        self.criaDB()

    def criaDB(self):
        lider = Lider()
        lider.criaTabela()

        projeto = Projeto()
        projeto.criaTabela()

        funcionario = Funcionario()
        funcionario.criaTabela()

        gerente = Gerente()
        gerente.criaTabela()

        solicitacao = Solicitacao()
        solicitacao.criaTabela()

        avaliacao = Avaliacao()
        avaliacao.criaTabela()

    def destroiDB(self):
        lider = Lider()
        lider.destroiTabela()

        projeto = Projeto()
        projeto.destroiTabela()

        funcionario = Funcionario()
        funcionario.destroiTabela()

        gerente = Gerente()
        gerente.destroiTabela()

        solicitacao = Solicitacao()
        solicitacao.destroiTabela()

        avaliacao = Avaliacao()
        avaliacao.destroiTabela()


class Lider:
    def __init__(self):
        self.nick = None
        self.nome = None
        self.senha = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS LIDER(
                        nick TEXT PRIMARY KEY,
                        nome TEXT ,
                        senha TEXT
                );
                """)
    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE LIDER")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM LIDER")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Projeto:
    def __init__(self):
        self.id = None
        self.nome = None
        self.apresentado = None
        self.nickLider = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS PROJETO(
                   id TEXT PRIMARY KEY,
                   nome TEXT,
                   apresentado TEXT,
                   nickLider TEXT REFERENCES LIDER(nick)
               );
               """)
    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE PROJETO")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PROJETO")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Funcionario:
    def __init__(self):
        self.nick = None
        self.nome = None
        self.senha = None
        self.cargo = None
        self.idProjeto = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                    nick TEXT PRIMARY KEY,
                    nome TEXT ,
                    senha TEXT,
                    cargo TEXT,
                    idProjeto TEXT REFERENCES PROJETO(id)
                );
                """)
    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE FUNCIONARIO")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM FUNCIONARIO")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Gerente:
    def __init__(self):
        self.nick = None
        self.nome = None
        self.senha = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS GERENTE(
                   nick TEXT PRIMARY KEY,
                   nome TEXT ,
                   senha TEXT
               );
               """)

    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE GERENTE")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM GERENTE")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Solicitacao:
    def __init__(self):
        self.idOrigem = None
        self.idDestino = None
        self.nickRef = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS SOLICITACAO(
                    idOrigem TEXT,
                    idDestino  TEXT,
                    nickRef TEXT REFERENCES FUNCIONARIO(nick)
                );
                """)
    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE SOLICITACAO")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SOLICITACAO")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Avaliacao:
    def __init__(self):
        self.comentario = None
        self.nota = None
        self.idProjeto = None

    def criaTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS AVALIACAO(
                    comentario TEXT,
                    nota INTEGER,
                    idProjeto TEXT REFERENCES PROJETO(id)         
                );
                """)

    def destroiTabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE AVALIACAO")

    def limpaTabela(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM AVALIACAO")
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False
