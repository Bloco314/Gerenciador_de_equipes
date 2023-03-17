import sqlite3

import Entity


# control da 'tela secreta' com consultas
class Consultas:
    def listar_funcionarios(self):
        a = Entity.E_Funcionario()
        return a.listar_funcionarios()

    def listar_lideres(self):
        a = Entity.E_Lider()
        return a.listar_lideres()

    def listar_gerentes(self):
        a = Entity.E_Gerente()
        return a.listar_gerentes()

    def listar_projetos(self):
        a = Entity.E_Projeto()
        return a.listar_projetos()

    def listar_solicitacoes(self):
        a = Entity.E_Solicitacao()
        return a.listar_solicitacoes()

    def listar_avaliacoes(self):
        a = Entity.E_Avaliacao()
        return a.listar_avaliacoes()


# control use case 1
class C_Fazer_login:
    def loginLider(self, nick, senha):
        E = Entity.E_Lider()
        return E.valida_login(nick,senha)

    def loginGerente(self, nick, senha):
        E = Entity.E_Gerente()
        return E.valida_login(nick,senha)

    def loginFuncionario(self, nick, senha):
        E = Entity.E_Funcionario()
        return E.valida_login(nick, senha)


# control use case 2
class C_Realiza_cadastro:
    def cadastraLider(self, nick, nome, senha):
        E = Entity.E_Lider()
        return E.criar_lider(nick,nome,senha)

    def cadastraGerente(self, nick, nome, senha):
        E = Entity.E_Gerente()
        return E.criar_gerente(nick,nome,senha)

    def cadastraFuncionario(self, nick, nome, senha, cargo):
        E = Entity.E_Funcionario()
        return E.cria_funcionario(nick, nome, senha, cargo)


# control use case 3
class C_Cria_projeto:
    def criaProjeto(self, id, nome, nick):
        E = Entity.E_Projeto()
        return E.cria_projeto(id,nome,nick)


# control use case 4
class C_Apresenta_projeto:
    def listaProjetos(self,nick):
        E = Entity.E_Projeto()
        return E.listar_projetos_bylider(nick)

    def apresentarProjeto(self,id):
        E = Entity.E_Projeto()
        return E.apresentar(id)


# control use case 5
class C_Solicita_membro:
    def listaFuncionarios(self):
        E = Entity.E_Funcionario()
        return E.listar_funcionarios()

    def solicita(self,nick,idDestino):
        E = Entity.E_Funcionario()
        idO = E.get_idprojeto_bynick(nick)
        S = Entity.E_Solicitacao()
        return S.cria_solicitacao(idO,idDestino,nick)


# control use case 6
class C_Transfere_membro:
    def listaSolicitacoes(self):
        E = Entity.E_Solicitacao()
        return E.listar_solicitacoes()

    def aceitaSolicitacao(self,quest):
        E = Entity.E_Solicitacao()

        F = Entity.E_Funcionario()
        F.tranfere_de_projeto(quest[0], quest[2])
        if quest[1]==None:
            E.deleta_solicitacao_semorigem(quest[0],quest[2])
        else:
            E.deleta_solicitacao(quest[0], quest[1],quest[2])
        return "Transferido"

    def recusaSolicitacao(self,quest):
        E = Entity.E_Solicitacao()
        if quest[1] == None:
            E.deleta_solicitacao_semorigem(quest[0], quest[2])
        else:
            E.deleta_solicitao(quest[0],quest[1],quest[2])
        return "Recusado com sucesso"


# control use case 7
class C_Arquiva_projeto:
    def listaProjetos(self,nick):
        E = Entity.E_Projeto()
        return E.listar_projetos_bylider(nick)

    def arquivaProjeto(self,id):
        E = Entity.E_Projeto()
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            if E.projeto_existe(id):
                F = Entity.E_Funcionario()
                F.desvincula_funcionarios_do_projeto(id)
                return E.deletar(id)
            else:
                return "ID invalido"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]


# control use case 8
# control use case 9
# control use case 10