#PROJETO FINAL - INTRODUÇÃO A PROGRAMAÇÃO PYTHON IFSP
#ALUNA - ANA CLÁUDIA GOMES SOUZA
#PROJETO DE UM SISTEMA DE CADASTRO DE ALUNOS

import sys

class Aluno:
    qtdAlunos = 0
    qtdReprovados = 0
    qtdExame = 0
    qtdAprovados = 0
    qtdAprovadosF = 0
    qtdExameF = 0
    qtdReprovadosF = 0
    qtdAprovadosM = 0
    qtdExameM = 0
    qtdReprovadosM = 0
    qtdAprovadosE = 0
    qtdReprovadosE = 0
    
    def __init__(self, nome, sexo, nota1, nota2, nota3, media,situacao,exame):
        
        self.nome = nome.upper()
        self.sexo = sexo.upper()
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media
        self.situacao = situacao.upper()
        self.exame = exame
        Aluno.qtdAlunos += 1

    def Calcula_Media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3


    def Analise_Situacao(self):
        if(self.media<4.0):
            self.situacao = "REPROVADO"
            Aluno.qtdReprovados += 1
        elif(self.media >= 4.0 and self.media<7.0):
            self.situacao = "EXAME"
            Aluno.qtdExame += 1
        elif(self.media >= 7.0):
            self.situacao = "APROVADO"
            Aluno.qtdAprovados += 1
    

    def Imprime_Cadastro(self):
            print("%.100s      %.20s  (NOTA1) %.2f  (NOTA2) %.2f  (NOTA3) %.2f  (MÉDIA) %.2f  (SITUAÇÃO) %.20s  (NOTA EXAME) %.2f "%(self.nome,self.sexo,self.nota1,self.nota2,self.nota3,self.media,self.situacao,self.exame))
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    def Insere_Exame(self,exame):
        if(self.situacao == "EXAME"):
            self.exame = exame
        elif(self.situacao == "REPROVADO"):
            print("Não foi possível inserir nota do exame, pois o aluno encontra-se em situação reprovado!")
        elif(self.situacao == "APROVADO"):
            print("Não foi possível inserir nota do exame, pois o aluno encontra-se em situação aprovado!")



    def Situacao_Exame(self):
        if(self.exame >= 7.0):
            self.situacao = "APROVADO"
            Aluno.qtdAprovadosE += 1
        else:
            self.situacao = "REPROVADO"
            Aluno.qtdReprovadosE += 1



    def Contador_Absoluto(self):
        if(self.situacao == "APROVADO" and self.sexo == "FEMININO"):
            Aluno.qtdAprovadosF += 1
        elif(self.situacao == "APROVADO" and self.sexo == "MASCULINO"):
            Aluno.qtdAprovadosM += 1
        elif(self.situacao == "EXAME" and self.sexo == "FEMININO"):
            Aluno.qtdExameF += 1
        elif(self.situacao == "EXAME" and self.sexo == "MASCULINO"):
            Aluno.qtdExameM += 1
        elif(self.situacao == "REPROVADO" and self.sexo == "FEMININO"):
            Aluno.qtdReprovadosF += 1
        elif(self.situacao == "REPROVADO" and self.sexo == "MASCULINO"):
            Aluno.qtdReprovadosM += 1
            








opc = 0
lista = []


while(opc!=5):
    print("\n\n========== MENU ==========")
    print("1 - Cadastrar Alunos ")
    print("2 - Dados Estatísticos e Absolutos")
    print("3 - Imprimir Cadastro de Alunos")
    print("4 - Sair do Sistema Escolar")

    opc = int(input("Selecione uma opcao: "))

    while(opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=5):
        opc = int(input("Opcao incorreta! Por favor selecione uma opcao: "))

    if(opc==1):
        nome = input("Digite o nome do aluno: ")
        sexo = input("Digite o sexo do aluno: ")
        sexo = sexo.upper()
        while(sexo!="MASCULINO" and sexo!="FEMININO"):
            sexo = input("Valor incorreto para sexo! Digite um valor válido: ")
            sexo = sexo.upper()
        
        nota1 = float(input("Digite a 1° nota: "))
        while(nota1<0.0 or nota1>10.0):
            nota1 = float(input("Valor incorreto para 1° nota! Por favor insira novamente um valor: "))
    
        nota2 = float(input("Digite a 2° nota: "))
        while(nota2<0.0 or nota2>10.0):
            nota2 = float(input("Valor incorreto para 2° nota! Por favor insira novamente um valor: "))
            
        nota3 = float(input("Digite a 3° nota: "))
        while(nota3<0.0 or nota3>10.0):
            nota3 = float(input("Valor incorreto para 3° nota! Por favor insira novamente um valor: "))

            
        media = 0.0
        situacao = "INDEFINIDA"
        exame = 0.0
        aux = (nota1+nota2+nota3)/3
        temp = Aluno
        temp = Aluno(nome,sexo,nota1,nota2,nota3,media,situacao,exame)
        temp.Calcula_Media()
        temp.Analise_Situacao()
        temp.Contador_Absoluto()
        if(aux>=4.0 and aux<7.0):
            exame = float(input("Digite a nota do exame: "))
            while(exame < 0.0 and exame > 10.0):
                exame = float(input("Valor incorreto para nota de exame!Por favor digite um valor válido: "))
            
            temp.Insere_Exame(exame)
            temp.Situacao_Exame()
            
        lista.append(temp)

        print("Cadastro concluído!")

                

                

    elif(opc==2):
        
        percentualA = (Aluno.qtdAlunos * Aluno.qtdAprovados) / 100
        percentualR = (Aluno.qtdAlunos * Aluno.qtdReprovados) / 100
        percentualE = (Aluno.qtdAlunos * Aluno.qtdExame) / 100
        
        if(Aluno.qtdAlunos == 0):
            print("\n\nNão existem alunos cadastrados para dados estatísticos e absolutos!\n")
        else:
            print("\n\n--------------------PORCENTAGEM--------------------")
            print("Quantidade Porcentual de Alunos Aprovados: %.2f"%(percentualA))
            print("Quantidade Porcentual de Alunos Exame: %.2f"%(percentualE))
            print("Quantidade Porcentual de Alunos Reprovados: %.2f"%(percentualR))
            print("\n--------------------ABSOLUTOS--------------------")
            print("Total de Alunos Cadastros no Sistema: %d"%(Aluno.qtdAlunos))
            print("Quantidade de Alunos Aprovados do Gênero Feminino: %d"%(Aluno.qtdAprovadosF))
            print("Quantiade de Alunos em Exame do Gênero Feminino: %d"%(Aluno.qtdExameF))
            print("Quantidade de Alunos Repovados do Gênero Feminino: %d"%(Aluno.qtdReprovadosF))
            print("Quantidade de Alunos Aprovados do Gênero Masculino: %d"%(Aluno.qtdAprovadosM))
            print("Quantiade de Alunos em Exame do Gênero Masculino: %d"%(Aluno.qtdExameM))        
            print("Quantidade de Alunos Repovados do Gênero Masculino: %d"%(Aluno.qtdReprovadosM))
            print("Quantidade de Alunos Aprovados no Exame: %d"%(Aluno.qtdAprovadosE))
            print("Quantidade de Alunos Reprovados no Exame: %d"%(Aluno.qtdReprovadosE))
                

    elif(opc==3):
        aux = Aluno.qtdAlunos
        print("\n\n====================================================================== CADASTRO GERAL DE ALUNOS ======================================================================\n")
        for i  in range(aux):
            temp = Aluno
            temp = lista[i]
            temp.Imprime_Cadastro()

    

    elif(opc==4):
        sys.exit(1)
    

