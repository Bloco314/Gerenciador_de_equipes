import sqlite3


# control da 'tela secreta'
class Consultas:
    def listaFuncionario(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nick,nome,senha,cargo FROM FUNCIONARIO")
        lista = []
        u = ("nick", "nome", "senha", "cargo")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def listaLider(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nick,nome,senha FROM LIDER")
        lista = []
        u = ("nick", "nome", "senha")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def listaGerente(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nick,nome,senha FROM GERENTE")
        lista = []
        u = ("nick", "nome", "senha")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def listaProjeto(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id,nome,apresentado,nickLider FROM PROJETO")
        lista = []
        u = ("id", "nome","apresentado", "nickLider")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista


# control use case 1
class Logar:
    def loginLider(self, nick, senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nick,senha FROM LIDER")
            lista = []
            for linha in cursor.fetchall():
                if linha[0] == nick and linha[1] == senha:
                    return True
            return False
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def loginGerente(self, nick, senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nick,senha FROM GERENTE")
            lista = []
            for linha in cursor.fetchall():
                if linha[0] == nick and linha[1] == senha:
                    return True
            return False
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def loginFuncionario(self, nick, senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nick,senha FROM FUNCIONARIO")
            lista = []
            for linha in cursor.fetchall():
                if linha[0] == nick and linha[1] == senha:
                    return True
            return False
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


# control use case 2
class Cadastrar:
    def cadastraLider(self, nick, nome, senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            tupla = (nick, nome, senha)
            cursor.execute("""INSERT INTO LIDER (nick,nome,senha) VALUES (?,?,?)""", tupla)
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def cadastraGerente(self, nick, nome, senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            tupla = (nick, nome, senha)
            cursor.execute("""INSERT INTO GERENTE (nick,nome,senha) VALUES (?,?,?)""", tupla)
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def cadastraFuncionario(self, nick, nome, senha, cargo):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            tupla = (nick, nome, senha, cargo, None)
            cursor.execute("""INSERT INTO FUNCIONARIO (nick,nome,senha,cargo,idProjeto) VALUES (?,?,?,?,?)""", tupla)
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            False


# control use case 3
class CriaProjeto:
    def criaProjeto(self,id,nome,nick):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            tupla = (id,nome,"não apresentado",nick)
            cursor.execute("""INSERT INTO PROJETO (id,nome,apresentado,nickLider) VALUES (?,?,?,?)""", tupla)
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


# control use case 4
class ApresentaProjeto:
    def listaProjetos(self,nick):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id,nome,apresentado FROM PROJETO WHERE nickLider = ?",(nick,))
            lista = [("id","nome","status")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro","no","sql")]

    def apresentarProjeto(self,id):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(id) FROM PROJETO WHERE ID = ?", (id,))
            numberOfRows = cursor.fetchone()[0]
            if numberOfRows>0:
                cursor.execute("SELECT COUNT(id) FROM PROJETO WHERE (ID = ? AND apresentado = ?)",(id, "não apresentado"))
                numberOfRows = cursor.fetchone()[0]
                if numberOfRows > 0:
                    cursor.execute("UPDATE PROJETO SET apresentado = ? WHERE id = ?",("apresentado",id))
                    conn.commit()
                    return "Apresentado com sucesso!"
                else:
                    return "Projeto já apresentado!"
            else:
                return "Projeto não existe!"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return "Erro SQL"


# control use case 5
# control use case 6
# control use case 7
# control use case 8
# control use case 9
# control use case 10
