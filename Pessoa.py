from datetime import date


class Endereco:
    def __init__(self, logradouro ="",numero = "", endereco_Comercial= False):
        #inicializar os nossos atributos com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

#CLASSE PESSOA
class Pessoa:
    def __init__(self, nome ="", rendimento =0.0, endereco = None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento


#CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento =0.0, endereco = None, cpf="", dataNascimento = None):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()


        self.cpf = cpf
        self.dataNascimento=dataNascimento

    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <=3500:
            return rendimento *0.2
        elif 3500< rendimento <= 6000:
            return(rendimento/100) *3.5
        else:
            return rendimento * 0.5


#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento =0.0, endereco = None, cnpj="", dataCriacao = None):
        if endereco is None:
            endereco = Endereco()

        if dataCriacao is None:
            dataCriacao = date.today()


        self.cnpj = cnpj
        self.dataCriacao=dataCriacao

    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 15000:
            return 0
        elif 15000 < rendimento <=35000:
            return rendimento *0.5
        elif 35000< rendimento <= 60000:
            return(rendimento/100) *3.5
        else:
            return rendimento * 0.5