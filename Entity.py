import sqlite3


class ADMDB:
    def __init__(self):
        self.criaDB()

    def criaDB(self):
        lider = E_Lider()
        lider.criaTabela()

        projeto = E_Projeto()
        projeto.criaTabela()

        funcionario = E_Funcionario()
        funcionario.criaTabela()

        gerente = E_Gerente()
        gerente.criaTabela()

        solicitacao = E_Solicitacao()
        solicitacao.criaTabela()

        avaliacao = E_Avaliacao()
        avaliacao.criaTabela()

    def destroiDB(self):
        lider = E_Lider()
        lider.destroiTabela()

        projeto = E_Projeto()
        projeto.destroiTabela()

        funcionario = E_Funcionario()
        funcionario.destroiTabela()

        gerente = E_Gerente()
        gerente.destroiTabela()

        solicitacao = E_Solicitacao()
        solicitacao.destroiTabela()

        avaliacao = E_Avaliacao()
        avaliacao.destroiTabela()


class E_Lider:
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

    def listar_lideres(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nick,nome,senha FROM LIDER")
        lista = []
        u = ("nick", "nome", "senha")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def valida_login(self,nick,senha):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nick,senha FROM LIDER")
            for linha in cursor.fetchall():
                if linha[0] == nick and linha[1] == senha:
                    return True
            return False
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def criar_lider(self,nick, nome, senha):
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


class E_Projeto:
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

    def listar_projetos(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id,nome,apresentado FROM PROJETO")
            lista = [("id", "nome", "status")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]

    def listar_projetos_bylider(self,nick):
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

    def listar_projetos_apresentados(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id,nome,nickLider FROM PROJETO WHERE apresentado = ?",("apresentado",))
            lista = [("id","nome","lider")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro","no","sql")]

    def listar_projetos_exceto(self, id):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id,nome,apresentado FROM PROJETO WHERE NOT id = ?", (id,))
            lista = [("id","nome","lider")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro","no","sql")]

    def cria_projeto(self, id, nome, nick):
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

    def apresentar(self,id):
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

    def deletar(self, id):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PROJETO WHERE id=?", (id,))
            conn.commit()
            return "Projeto arquivado"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]

    def projeto_existe(self, id):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(id) FROM PROJETO WHERE ID = ?", (id,))
        numberOfRows = cursor.fetchone()[0]
        if numberOfRows > 0:
            return True
        return False


class E_Funcionario:
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

    def listar_funcionarios(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nick,nome,cargo,idProjeto FROM FUNCIONARIO")
            lista = [("nick", "nome", "cargo", "projeto")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro sql")]

    def get_idprojeto_bynick(self,nick):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT idProjeto FROM FUNCIONARIO WHERE nick=?", (nick,))
            idOrigem = cursor.fetchone()[0]
            return idOrigem
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def valida_login(self,nick,senha):
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

    def cria_funcionario(self, nick, nome, senha, cargo):
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

    def desvincula_funcionarios_do_projeto(self, id):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE FUNCIONARIO SET idProjeto = ? WHERE idProjeto = ?", (id, id))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]

    def tranfere_de_projeto(self, nick, iddestino):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE FUNCIONARIO SET idProjeto = ? WHERE nick = ?", (iddestino, nick))
            conn.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]


class E_Gerente:
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

    def listar_gerentes(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nick,nome,senha FROM GERENTE")
        lista = []
        u = ("nick", "nome", "senha")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def valida_login(self,nick,senha):
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

    def criar_gerente(self, nick, nome, senha):
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


class E_Solicitacao:
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

    def listar_solicitacoes(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nickRef,idOrigem,idDestino FROM SOLICITACAO")
            lista = [("nickref", "idorigem", "iddestino")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro sql")]

    def cria_solicitacao(self, idOrigem, idDestino, nick):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SOLICITACAO VALUES (?,?,?)", (idOrigem, idDestino, nick))
            conn.commit()
            return "Solicitacao criada."
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return "Erro SQL"

    def deleta_solicitacao_semorigem(self, nick, iddestino):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SOLICITACAO WHERE nickRef=? AND idDestino=?", (nick, iddestino))
            conn.commit()
            return "Deletado com sucesso"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]

    def deleta_solicitacao(self, nick, idorigem, iddestino):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SOLICITACAO WHERE nickRef=? AND idOrigem=? AND idDestino=?",(nick, idorigem, iddestino))
            conn.commit()
            return "Deletado com sucesso"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]


class E_Avaliacao:
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

    def listar_avaliacoes(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT idProjeto,nota,comentario FROM AVALIACAO")
        lista = []
        u = ("projeto", "nota", "comentario")
        lista.append(u)
        for linha in cursor.fetchall():
            lista.append(linha)
        return lista

    def cria_avaliacao(self, id, nota, comentario):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            tupla = (id, nota, comentario)
            cursor.execute("""INSERT INTO AVALIACAO (idProjeto, nota, comentario) VALUES (?,?,?)""", tupla)
            conn.commit()
            return "Avaliado com sucesso!"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return "Falha"
