# 1 Pessoa Fisica / 2 Pessoa Juridica / 3 Sair
# 1 Cadastrar Pessoa Fisica / 2 Listar pessoa Fisica / 3 Sair
# 1 Cadastrar Pessoa Juridica / 2 Listar pessoa Juridica / 3 Sair

from datetime import date, datetime
from Pessoa import PessoaFisica, Endereco

def main():
    lista_pf=[]
    while True:
        opcao = int(input("Escolha: 1 Pessoa Fisica / 2 Pessoa Juridica / 3 Sair"))

        #Pessoa Fisica
        if opcao == 1:
            while True:
                opcaopf = int(input("Escolha: 1 Cadastrar Pessoa Fisica / 2 Listar pessoa Fisica / 3 Sair"))

                # Opção 1 cadastras pessoa fisica
                if opcaopf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa física: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Somente numeros): "))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu..")
                        continue #continua o loop
                    
                    #CADASTRO DE ENDEREÇO
                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = int(input("Digite o número: "))
                    end_comercial = input("Este endereço é comercial? (S / N): ") #solicita se é comercial
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define se é comercial ou não True or false

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")
                
                #Listar pessoa Fisica
                elif opcaopf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF:{cada_pf.cpf}")
                            print(f"Endereço:{cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data de Nascimento:{cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago:{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Lista vazia.")
                        print("Digite 0 para sair.")
                        input()
                
                #Sair do Menu Atual
                elif opcaopf == 3:
                    print("Voltando ao menu anterior.")
                    break
                
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas:")

        # Pessoa Juridica            
        elif opcao == 2:
            pass
        elif opcao == 3:
            print("Obrigado por utilizar o sistema!")
            break

if __name__ == "__main__":
    main()