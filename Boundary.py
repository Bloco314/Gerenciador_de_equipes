from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QCheckBox, QTableView
import Control, css
from tabela import Tabela
from PyQt5.QtCore import Qt


# um modelo geral de tela com algumas propriedades uteis a serem herdadas
class Tela_base(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 300
        self.left = 1000
        self.largura = 800
        self.altura = 700

    def carregarJanela(self):
        self.setFixedSize(self.largura, self.altura)
        self.setStyleSheet(f"QMainWindow{css.telaEstilo}")
        self.setGeometry(self.left, self.topo, self.largura, self.altura)

    def setTitulo(self, titulo):
        self.setWindowTitle(titulo)

    def incluibotaodeinicio(self):
        inicio = QPushButton("X", self)
        inicio.move(690, 10)
        inicio.resize(100, 80)
        inicio.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        inicio.clicked.connect(self.inicio)

    def closeEvent(self, event):
        print("chegamos ao fim")

    def inicio(self):
        self.a = Tela_inicial()
        self.a.show()
        self.setVisible(False)


# tela pra mensagens de confirmação pro usuario
class Tela_mensagem(QMainWindow):
    def __init__(self,msg):
        super().__init__()
        self.topo = 450
        self.left = 1200
        self.largura = 400
        self.altura = 350

        alert = QLineEdit(msg,self)
        alert.move(0,0)
        alert.resize(400,350)
        alert.setAlignment(Qt.AlignCenter)
        alert.setStyleSheet(f"QLineEdit{css.telaEstilo2}")

        self.carregarJanela()

    def carregarJanela(self):
        self.setFixedSize(self.largura, self.altura)
        self.setGeometry(self.left, self.topo, self.largura, self.altura)
        self.setVisible(True)


# tela com funcionalidades fora do escopo que usei para teste, na tela inicial clique no canto superior direito.
class Tela_consultas(Tela_base):
    def __init__(self):
        super().__init__()
        self.setTitulo("SECRETA")
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        self.criatabela()

        func = QPushButton("FUNC", self)
        func.move(10, 580)
        func.resize(100, 80)
        func.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        func.clicked.connect(self.funcionario)

        lider = QPushButton("LIDR", self)
        lider.move(130, 580)
        lider.resize(100, 80)
        lider.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        lider.clicked.connect(self.lider)

        ger = QPushButton("GRNT", self)
        ger.move(250, 580)
        ger.resize(100, 80)
        ger.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        ger.clicked.connect(self.gerente)

        proj = QPushButton("PROJ", self)
        proj.move(370, 580)
        proj.resize(100, 80)
        proj.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        proj.clicked.connect(self.projeto)
        
        sol = QPushButton("SOLI", self)
        sol.move(490, 580)
        sol.resize(100, 80)
        sol.setStyleSheet(f"QPushButton{css.btnEstilo2}")
        sol.clicked.connect(self.solicitacao)

    def criatabela(self):
        self.control = Control.Consultas()
        self.tabela = QTableView(self)
        self.tabela.move(20, 20)
        self.tabela.resize(600, 500)

    def lider(self):
        lista = self.control.listaLider()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def gerente(self):
        lista = self.control.listaGerente()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def funcionario(self):
        lista = self.control.listaFuncionario()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def projeto(self):
        lista = self.control.listaProjeto()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def solicitacao(self):
        lista = self.control.listaSolicitacao()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()


# tela inicial
class Tela_inicial(Tela_base):
    def __init__(self):
        super().__init__()
        self.setTitulo("TELA INICIAL")
        self.elementos()
        self.carregarJanela()
        self.show()

    def elementos(self):
        login = QPushButton("Login", self)
        login.move(265, 240)
        login.resize(120, 100)
        login.setStyleSheet(f"QPushButton {css.btnEstilo}")
        login.clicked.connect(self.login)

        cadastro = QPushButton("Cadastro", self)
        cadastro.move(405, 240)
        cadastro.resize(120, 100)
        cadastro.setStyleSheet(f"QPushButton {css.btnEstilo}")
        cadastro.clicked.connect(self.cadastro)

        secreta = QPushButton("", self)
        secreta.move(720, 0)
        secreta.resize(60, 60)
        secreta.setStyleSheet(f"QPushButton {css.telaEstilo}")
        secreta.clicked.connect(self.secreta)

    def login(self):
        self.telalogin = Tela_login()
        self.telalogin.show()
        self.setVisible(False)

    def cadastro(self):
        self.telacadastro = Tela_cadastro()
        self.telacadastro.show()
        self.setVisible(False)

    def secreta(self):
        self.telasecreta = Tela_consultas()
        self.telasecreta.show()
        self.setVisible(False)


# menu de lider
class Tela_lider(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("TELA DE LIDER")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        criaprojeto = QPushButton("CRIAR", self)
        criaprojeto.move(320, 150)
        criaprojeto.resize(170, 90)
        criaprojeto.setStyleSheet(f"QPushButton {css.btnEstilo}")
        criaprojeto.clicked.connect(self.cria)

        apresentar = QPushButton("APRESENTAR", self)
        apresentar.move(320, 250)
        apresentar.resize(170, 90)
        apresentar.setStyleSheet(f"QPushButton {css.btnEstilo}")
        apresentar.clicked.connect(self.apresenta)

        solicitaMembro = QPushButton("ADD MEMBRO", self)
        solicitaMembro.move(320, 350)
        solicitaMembro.resize(170, 90)
        solicitaMembro.setStyleSheet(f"QPushButton {css.btnEstilo}")
        solicitaMembro.clicked.connect(self.solicita)

        autorizaTra = QPushButton("TRANSFERIR", self)
        autorizaTra.move(320, 450)
        autorizaTra.resize(170, 90)
        autorizaTra.setStyleSheet(f"QPushButton {css.btnEstilo}")
        autorizaTra.clicked.connect(self.transferir)

        arquiva = QPushButton("ARQUIVAR", self)
        arquiva.move(320, 550)
        arquiva.resize(170, 90)
        arquiva.setStyleSheet(f"QPushButton {css.btnEstilo}")
        arquiva.clicked.connect(self.arquiva)

        nicked = QLineEdit(self.logado, self)
        nicked.move(5,5)
        nicked.resize(200,40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

    def cria(self):
        self.telacriaprojeto = Tela_criaProjeto(self.logado)
        self.telacriaprojeto.show()
        self.setVisible(False)

    def apresenta(self):
        self.telaapresentaprojeto = Tela_apresentaprojeto(self.logado)
        self.telaapresentaprojeto.show()
        self.setVisible(False)

    def solicita(self):
        self.telasolicitamembro = Tela_solicitamembro(self.logado)
        self.telasolicitamembro.show()
        self.setVisible(False)

    def transferir(self):
        self.telatransferemembro = Tela_transferemembro(self.logado)
        self.telatransferemembro.show()
        self.setVisible(False)

    def arquiva(self):
        self.telaarquiva = Tela_arquivaprojeto(self.logado)
        self.telaarquiva.show()
        self.setVisible(False)


# menu de gerente
class Tela_gerente(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("TELA DE GERENTE")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

    def aceitasolicitacao(self):
        self.telaaceitasolicitacao = Tela_aceitasolicitacao(self.logado)
        self.telaaceitasolicitacao.show()
        self.setVisible(False)

    def avaliaprojeto(self):
        self.telaavaliaprojeto = Tela_avaliaprojeto(self.logado)
        self.telaavaliaprojeto.show()
        self.setVisible(False)


# menu de funcionario
class Tela_funcionario(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("TELA DE FUNCIONARIO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()

        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

    def solicitatranferencia(self):
        print()


# boundary use case 1
class Tela_login(Tela_base):
    def __init__(self):
        super().__init__()
        self.setTitulo("LOGIN")
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.texto()
        self.botoes()
        self.boxes()

    def texto(self):
        self.inputnick = QLineEdit(self)
        self.inputnick.move(350, 250)
        self.inputnick.resize(200, 30)

        txt = QLineEdit("NICK:", self)
        txt.move(220, 250)
        txt.resize(100, 30)
        txt.setDisabled(True)

        self.inputpass = QLineEdit(self)
        self.inputpass.move(350, 300)
        self.inputpass.resize(200, 30)

        txt2 = QLineEdit("SENHA:", self)
        txt2.move(220, 300)
        txt2.resize(100, 30)
        txt2.setDisabled(True)

    def botoes(self):
        logar = QPushButton("ENTRAR", self)
        logar.move(350, 400)
        logar.resize(120, 100)
        logar.setStyleSheet(f"QPushButton {css.btnEstilo}")
        logar.clicked.connect(self.efetivaLogin)

        self.incluibotaodeinicio()

    def boxes(self):
        self.bx1 = QCheckBox("Funcionario", self)
        self.bx1.move(220, 350)
        self.bx1.resize(150, 20)
        self.bx1.setChecked(True)
        self.bx1.clicked.connect(self.check1)

        self.bx2 = QCheckBox("Lider", self)
        self.bx2.move(350, 350)
        self.bx2.resize(150, 20)
        self.bx2.clicked.connect(self.check2)

        self.bx3 = QCheckBox("Gerente", self)
        self.bx3.move(450, 350)
        self.bx3.resize(150, 20)
        self.bx3.clicked.connect(self.check3)

    def check1(self):
        self.bx1.setChecked(True)
        self.bx2.setChecked(False)
        self.bx3.setChecked(False)

    def check2(self):
        self.bx2.setChecked(True)
        self.bx1.setChecked(False)
        self.bx3.setChecked(False)

    def check3(self):
        self.bx3.setChecked(True)
        self.bx1.setChecked(False)
        self.bx2.setChecked(False)

    def efetivaLogin(self):
        cad = Control.Logar()
        if self.bx2.isChecked():
            if cad.loginLider(self.inputnick.text(), self.inputpass.text()):
                self.telalider = Tela_lider(self.inputnick.text())
                self.telalider.show()
                self.setVisible(False)
            else:
                self.msg = Tela_mensagem("Nick ou senha incorretos")
        elif self.bx1.isChecked():
            if cad.loginFuncionario(self.inputnick.text(), self.inputpass.text()):
                self.telafuncionario = Tela_funcionario(self.inputnick.text())
                self.telafuncionario.show()
                self.setVisible(False)
            else:
                self.msg = Tela_mensagem("Nick ou senha incorretos")
        elif self.bx3.isChecked():
            if cad.loginGerente(self.inputnick.text(), self.inputpass.text()):
                self.telagerente = Tela_gerente(self.inputnick.text())
                self.telagerente.show()
                self.setVisible(False)
            else:
                self.msg = Tela_mensagem("Nick ou senha incorretos")
        else:
            self.msg = Tela_mensagem("Selecione um campo")


# boundary usecase 2
class Tela_cadastro(Tela_base):
    def __init__(self):
        super().__init__()
        self.setTitulo("CADASTRO")
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.texto()
        self.botoes()
        self.boxes()

    def texto(self):
        self.nome = QLineEdit(self)
        self.nome.move(350, 200)
        self.nome.resize(200, 30)
        txt0 = QLineEdit("NOME:", self)
        txt0.move(220, 200)
        txt0.resize(100, 30)
        txt0.setDisabled(True)

        self.nick = QLineEdit(self)
        self.nick.move(350, 250)
        self.nick.resize(200, 30)
        txt1 = QLineEdit("NICK:", self)
        txt1.move(220, 250)
        txt1.resize(100, 30)
        txt1.setDisabled(True)

        self.senha = QLineEdit(self)
        self.senha.move(350, 300)
        self.senha.resize(200, 30)
        txt2 = QLineEdit("SENHA:", self)
        txt2.move(220, 300)
        txt2.resize(100, 30)
        txt2.setDisabled(True)

        self.cargo = QLineEdit(self)
        self.cargo.move(350, 350)
        self.cargo.resize(200, 30)
        txt3 = QLineEdit("CARGO:", self)
        txt3.move(220, 350)
        txt3.resize(100, 30)
        txt3.setDisabled(True)

    def botoes(self):
        cadastrar = QPushButton("CADASTRAR", self)
        cadastrar.move(350, 450)
        cadastrar.resize(150, 90)
        cadastrar.setStyleSheet(f"QPushButton {css.btnEstilo}")
        cadastrar.clicked.connect(self.efetivaCadastro)

        self.incluibotaodeinicio()

    def boxes(self):
        self.bx1 = QCheckBox("Funcionario", self)
        self.bx1.move(220, 400)
        self.bx1.resize(150, 20)
        self.bx1.setChecked(True)
        self.bx1.clicked.connect(self.check1)

        self.bx2 = QCheckBox("Lider", self)
        self.bx2.move(350, 400)
        self.bx2.resize(150, 20)
        self.bx2.clicked.connect(self.check2)

        self.bx3 = QCheckBox("Gerente", self)
        self.bx3.move(450, 400)
        self.bx3.resize(150, 20)
        self.bx3.clicked.connect(self.check3)

    def check1(self):
        self.bx1.setChecked(True)
        self.bx2.setChecked(False)
        self.bx3.setChecked(False)

    def check2(self):
        self.bx2.setChecked(True)
        self.bx1.setChecked(False)
        self.bx3.setChecked(False)

    def check3(self):
        self.bx3.setChecked(True)
        self.bx1.setChecked(False)
        self.bx2.setChecked(False)

    def limpaTextos(self):
        self.nick.setText("")
        self.nome.setText("")
        self.senha.setText("")
        self.cargo.setText("")

    def efetivaCadastro(self):
        cad = Control.Cadastrar()
        if self.bx2.isChecked():
            if cad.cadastraLider(self.nick.text(), self.nome.text(), self.senha.text()):
                self.tel = Tela_mensagem("Cadastrado com sucesso!")
                self.limpaTextos()
        elif self.bx1.isChecked():
            if cad.cadastraFuncionario(self.nick.text(), self.nome.text(), self.senha.text(), self.cargo.text()):
                self.tel = Tela_mensagem("Cadastrado com sucesso!")
                self.limpaTextos()
        elif self.bx3.isChecked():
            if cad.cadastraGerente(self.nick.text(), self.nome.text(), self.senha.text()):
                self.tel = Tela_mensagem("Cadastrado com sucesso!")
                self.limpaTextos()
        else:
            print("selecione um campo")


# boundary usecase 3
class Tela_criaProjeto(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("CRIAR PROJETO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        self.id = QLineEdit(self)
        self.id.move(350, 200)
        self.id.resize(200, 30)
        txt0 = QLineEdit("ID:", self)
        txt0.move(220, 200)
        txt0.resize(100, 30)
        txt0.setDisabled(True)

        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

        self.nome = QLineEdit(self)
        self.nome.move(350, 250)
        self.nome.resize(200, 30)
        txt1 = QLineEdit("NOME:", self)
        txt1.move(220, 250)
        txt1.resize(100, 30)
        txt1.setDisabled(True)

        criar = QPushButton("CRIAR PROJETO", self)
        criar.move(350, 350)
        criar.resize(200, 90)
        criar.setStyleSheet(f"QPushButton {css.btnEstilo}")
        criar.clicked.connect(self.criaProjeto)

    def criaProjeto(self):
        cria = Control.CriaProjeto()
        if cria.criaProjeto(self.id.text(), self.nome.text(), self.logado):
            self.mensagem = Tela_mensagem("Criado com sucesso!")
            self.nome.setText("")
            self.id.setText("")

    def inicio(self):
        self.a = Tela_lider(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 4
class Tela_apresentaprojeto(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("APRESENTA PROJETO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        self.criaTabela()

        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

        self.id = QLineEdit(self)
        self.id.move(300, 580)
        self.id.resize(200, 30)

        campotxt = QLineEdit("ID:",self)
        campotxt.move(210,580)
        campotxt.resize(80,30)
        campotxt.setEnabled(False)

        self.apresenta = QPushButton("Apresenta",self)
        self.apresenta.move(510,555)
        self.apresenta.resize(140,70)
        self.apresenta.setStyleSheet(f"QPushButton{css.btnEstilo}")
        self.apresenta.clicked.connect(self.apresentar)

    def apresentar(self):
        self.msg = Tela_mensagem(self.apr.apresentarProjeto(self.id.text()))
        self.id.setText("")
        self.preenche()

    def criaTabela(self):
        self.tabela = QTableView(self)
        self.tabela.move(160, 50)
        self.tabela.resize(475, 500)
        self.apr = Control.ApresentaProjeto()
        self.preenche()

    def preenche(self):
        lista = self.apr.listaProjetos(self.logado)
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def inicio(self):
        self.a = Tela_lider(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 5
class Tela_solicitamembro(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("SOLICITA MEMBRO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        self.criaTabela()
        self.preenche()
        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

        self.nickname = QLineEdit(self)
        self.nickname.move(300, 580)
        self.nickname.resize(200, 30)
        campotxt = QLineEdit("NICK:", self)
        campotxt.move(210, 580)
        campotxt.resize(80, 30)
        campotxt.setEnabled(False)

        self.idDestino = QLineEdit(self)
        self.idDestino.move(300, 630)
        self.idDestino.resize(200, 30)
        campotxt2 = QLineEdit("PROJETO:", self)
        campotxt2.move(210, 630)
        campotxt2.resize(80, 30)
        campotxt2.setEnabled(False)

        self.apresenta = QPushButton("Solicita", self)
        self.apresenta.move(510, 580)
        self.apresenta.resize(140, 70)
        self.apresenta.setStyleSheet(f"QPushButton{css.btnEstilo}")
        self.apresenta.clicked.connect(self.solicita)

    def criaTabela(self):
        self.tabela = QTableView(self)
        self.tabela.move(160, 50)
        self.tabela.resize(475, 500)
        self.apr = Control.SolicitaMembro()
        self.preenche()

    def preenche(self):
        lista = self.apr.listaFuncionarios()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def solicita(self):
        self.msg = Tela_mensagem(self.apr.solicita(self.nickname.text(),self.idDestino.text()))
        self.nickname.setText("")
        self.idDestino.setText("")
        self.preenche()

    def inicio(self):
        self.a = Tela_lider(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 6
class Tela_transferemembro(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("ACEITAR/RECUSAR TRANSFERENCIA")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()
        self.criaTabela()
        self.preenche()

        nicked = QLineEdit(self.logado, self)
        nicked.move(5, 5)
        nicked.resize(200, 40)
        nicked.setStyleSheet(f"QLineEdit{css.nickEstilo}")
        nicked.setAlignment(Qt.AlignCenter)
        nicked.setDisabled(True)

        self.aceita = QPushButton("Aceitar", self)
        self.aceita.move(230, 580)
        self.aceita.resize(140, 70)
        self.aceita.setStyleSheet(f"QPushButton{css.btnEstilo}")
        self.aceita.clicked.connect(self.aceitar)

        self.recusa = QPushButton("Recusar", self)
        self.recusa.move(440, 580)
        self.recusa.resize(140, 70)
        self.recusa.setStyleSheet(f"QPushButton{css.btnEstilo}")
        self.recusa.clicked.connect(self.recusar)

        self.help = QPushButton("?", self)
        self.help.move(700, 600)
        self.help.resize(80, 70)
        self.help.clicked.connect(self.helpme)

    def aceitar(self):
        quest = [   self.tabela.currentIndex().siblingAtColumn(0).data(),
                    self.tabela.currentIndex().siblingAtColumn(1).data(),
                    self.tabela.currentIndex().siblingAtColumn(2).data()]
        self.transfere.aceitaSolicitacao(quest)

    def recusar(self):
        quest = [self.tabela.currentIndex().siblingAtColumn(0).data(),
                 self.tabela.currentIndex().siblingAtColumn(1).data(),
                 self.tabela.currentIndex().siblingAtColumn(2).data()]
        self.transfere.recusaSolicitacao(quest)

    def helpme(self):
        self.msg = Tela_mensagem("Selecione uma linha na tabela")

    def criaTabela(self):
        self.tabela = QTableView(self)
        self.tabela.move(160, 50)
        self.tabela.resize(475, 500)
        self.transfere = Control.AceitaTransferencia()
        self.preenche()

    def preenche(self):
        lista = self.transfere.listaSolicitacoes()
        self.model = Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()

    def inicio(self):
        self.a = Tela_lider(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 7
class Tela_arquivaprojeto(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("ARQUIVAR PROJETO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()

    def inicio(self):
        self.a = Tela_lider(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 8
class Tela_aceitasolicitacao(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("ACEITAR/RECUSAR SOLICITACOES")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()

    def inicio(self):
        self.a = Tela_gerente(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 9
class Tela_avaliaprojeto(Tela_base):
    def __init__(self,nick):
        super().__init__()
        self.setTitulo("AVALIAR PROJETO")
        self.logado = nick
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()

    def inicio(self):
        self.a = Tela_gerente(self.logado)
        self.a.show()
        self.setVisible(False)


# boundary usecase 10
class Tela_solicitatranferencia(Tela_base):
    def __init__(self):
        super().__init__()
        self.setTitulo("SOLICITA TRANFERENCIA")
        self.elementos()
        self.carregarJanela()

    def elementos(self):
        self.incluibotaodeinicio()

