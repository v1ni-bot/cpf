# 1 Pessoa Fisica / 2 Pessoa Juridica / 3 Sair
# 1 Cadastrar Pessoa Fisica / 2 Listar pessoa Fisica / 3 Sair
# 1 Cadastrar Pessoa Juridica / 2 Listar pessoa Juridica / 3 Sair

from datetime import date, datetime
from Pessoa import PessoaFisica, PessoaJuridica, Endereco

def main():
    lista_pf=[]
    lista_pj=[]

    while True:
        opcao = int(input("Escolha: 1 Pessoa Fisica / 2 Pessoa Juridica / 0 Sair: "))

        #Pessoa Fisica
        if opcao == 1:
            while True:
                opcaopf = int(input("Escolha: 1 Cadastrar Pessoa Fisica / 2 Listar Pessoa Fisica / 3 Remover Pessoa Fisica / 0 Sair: "))

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
                
                # Opcao 2 Listar pessoa Fisica
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
                
                # Opcao 3 Remover pessoa Física
                elif opcaopf == 3:
                    rem = False
                    cpf_rem = int(input("Informe o cpf que deseja remover: "))
                    if lista_pf:
                        for pf in lista_pf:
                            if cpf_rem == int(pf.cpf):
                                lista_pf.remove(pf)
                                print("CPF removido com sucesso!")
                                rem = True
                                break
                        if rem == False:
                            print("CPF não encontrado.")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Não há nenhum CPF cadastrado.")
                        print("Digite 0 para sair.")
                        input()
                
                #Atualizar cadastro
                elif opcaopf == 4:
                    attpf = PessoaFisica()
                    att_end_pf = Endereco()
                    att = False

                    cpf_att = int(input("Informe o cpf que deseja atualizar: "))
                    if lista_pf:
                        for pf in lista_pf:
                            if cpf_att == int(pf.cpf):

                                print(f"------------------ DADOS DO CPF {cpf_att} -------------------")
                                print(f"Nome: {pf.nome}")
                                print(f"CPF:{pf.cpf}")
                                print(f"Endereço:{pf.endereco.logradouro}, {pf.endereco.numero}")
                                print(f"Data de Nascimento:{pf.dataNascimento.strftime('%d/%m/%Y')}")
                                print(f"Imposto a ser pago:{pf.calcular_imposto(pf.rendimento)}")
                                print("------------------- DADOS A SEREM ATUALIZADOS -----------------")
                                input("Pressione enter para continuar")
                                attpf.nome = input("Digite o nome da pessoa física: ")
                                attpf.cpf = input("Digite o CPF: ")
                                attpf.rendimento = float(input("Digite o rendimento mensal (Somente numeros): "))

                                data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                                attpf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                                idade = (date.today() - attpf.dataNascimento).days // 365

                                if idade >= 18:
                                    print("A pessoa tem mais de 18 anos")
                                else:
                                    print("A pessoa tem menos de 18 anos. Retorne ao menu..")
                                    continue #continua o loop
                                
                                #ENDEREÇO
                                att_end_pf.logradouro = input("Digite o logradouro: ")
                                att_end_pf.numero = int(input("Digite o número: "))
                                end_comercial = input("Este endereço é comercial? (S / N): ") #solicita se é comercial
                                att_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define se é comercial ou não True or false

                                attpf.endereco = att_end_pf

                                lista_pf[lista_pf.index(pf)] = attpf

                                print("CPF Atualizado com sucesso!")
                                att = True
                                break
                        if att == False:
                            print("CPF não encontrado.")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Não há nenhum CPF cadastrado.")
                        print("Digite 0 para sair.")
                        input()

                #Sair do Menu Atual
                elif opcaopf == 0:
                    print("Voltando ao menu anterior.")
                    break
                
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas:")

        # Pessoa Juridica            
        elif opcao == 2:
            while True:
                opcaopj = int(input("Escolha: 1 Cadastrar Pessoa Juridica / 2 Listar Pessoa Juridica / 3 Remover Pessoa Juridica / 0 Sair: "))

                # Opção 1 cadastras pessoa fisica
                if opcaopj == 1:
                    novapj = PessoaJuridica() 
                    novo_end_pj = Endereco()

                    novapj.nome = input("Digite o nome da pessoa Juridica: ")
                    novapj.cnpj = input("Digite o CNPJ: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (Somente numeros): "))

                    data_criacao = input("Digite a data de criação (dd/mm/aaaa): ")
                    novapj.dataCriacao = datetime.strptime(data_criacao, '%d/%m/%Y').date()
                    idade = (date.today() - novapj.dataCriacao).days // 365

                    if idade >= 1:
                        print("A pessoa tem mais de 1 ano vigente.")
                    else:
                        print("A pessoa tem menos de 1 ano vigente. Retorne ao menu..")
                        continue #continua o loop
                    
                    #CADASTRO DE ENDEREÇO
                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = int(input("Digite o número: "))
                    end_Sede = input("Este endereço é Sede? (S / N): ") #solicita se é comercial
                    novo_end_pj.endereco_Sede = end_Sede.strip().upper() == 'S' # Define se é comercial ou não True or false

                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)

                    print("Cadastro realizado com sucesso!!")
                
                # Opcao 2 Listar pessoa Juridica
                elif opcaopj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome: {cada_pj.nome}")
                            print(f"CNPJ:{cada_pj.cnpj}")
                            print(f"Endereço:{cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Data de Criação:{cada_pj.dataCriacao.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago:{cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Lista vazia.")
                        print("Digite 0 para sair.")
                        input()
                
                # Opcao 3 Remover pessoa Juridica
                elif opcaopj == 3:
                    rem = False
                    cnpj_rem = int(input("Informe o cnpj que deseja remover: "))
                    if lista_pj:
                        for pj in lista_pj:
                            if cnpj_rem == int(pj.cnpj):
                                lista_pj.remove(pj)
                                print("CNPJ removido com sucesso!")
                                rem = True
                                break
                        if rem == False:
                            print("CNPJ não encontrado.")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Não há nenhum CNPJ cadastrado.")
                        print("Digite 0 para sair.")
                        input()

                #Atualizar
                elif opcaopj == 4:
                    attpj = PessoaJuridica()
                    att_end_pj = Endereco()
                    att = False

                    cnpj_att = int(input("Informe o CNPJ que deseja atualizar: "))
                    if lista_pj:
                        for pj in lista_pj:
                            if cnpj_att == int(pj.cnpj):

                                print(f"------------------ DADOS DO CPF {cnpj_att} -------------------")
                                print(f"Nome: {pj.nome}")
                                print(f"CPF:{pj.cnpj}")
                                print(f"Endereço:{pj.endereco.logradouro}, {pj.endereco.numero}")
                                print(f"Data de Nascimento:{pj.dataCriacao.strftime('%d/%m/%Y')}")
                                print(f"Imposto a ser pago:{pj.calcular_imposto(pj.rendimento)}")
                                print("------------------- DADOS A SEREM ATUALIZADOS -----------------")
                                input("Pressione enter para continuar")
                                attpj.nome = input("Digite o nome da pessoa Jurídica: ")
                                attpj.cnpj = input("Digite o CNPJ: ")
                                attpj.rendimento = float(input("Digite o rendimento mensal (Somente numeros): "))

                                data_criacao = input("Digite a data de Criação (dd/mm/aaaa): ")
                                attpj.dataCriacao = datetime.strptime(data_criacao, '%d/%m/%Y').date()
                                idade = (date.today() - attpj.dataCriacao).days // 365

                                if idade >= 1:
                                    print("A pessoa tem mais de 1 ano vigente.")
                                else:
                                    print("A pessoa tem menos de 1 ano vigente. Retorne ao menu..")
                                    continue #continua o loop
                                
                                #ENDEREÇO
                                att_end_pj.logradouro = input("Digite o logradouro: ")
                                att_end_pj.numero = int(input("Digite o número: "))
                                end_Sede = input("Este endereço é Sede? (S / N): ") #solicita se é comercial
                                att_end_pj.endereco_Sede = end_Sede.strip().upper() == 'S' # Define se é comercial ou não True or false

                                attpj.endereco = att_end_pj

                                lista_pj[lista_pj.index(pj)] = attpj

                                print("CNPJ Atualizado com sucesso!")
                                att = True
                                break
                        if att == False:
                            print("CNPJ não encontrado.")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Não há nenhum CNPJ cadastrado.")
                        print("Digite 0 para sair.")
                        input()


                #Sair do Menu Atual
                elif opcaopj == 0:
                    print("Voltando ao menu anterior.")
                    break
                
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas:")
        elif opcao == 0:
            print("Obrigado por utilizar o sistema!")
            break

if __name__ == "__main__":
    main()