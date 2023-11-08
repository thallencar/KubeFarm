"""Esse quiz tem como objetivo conscientizar, digulgar e popularizar o projeto KubeFarm.
Ele será disponibilizado não só em nosso site - onde o atual cliente consegue cupons dependendo da sua pontuação,
caso o compartilhe com outras pessoas - mas, também, estará presente em redes sociais para atrair novos
adeptos ao KubeFarm.
Ter uma iniciativa sócio-ambiental, por mais eficiente que seja, não vinga sem a participação da sociedade. O KubeQuiz
foi criado por entendermos que a tecnologia deve e pode fazer pelo nosso projeto o que faz de melhor:
conectar ideias e pessoas por meio da interatividade."""
# Importando re para expressões regulares (padronizar input)
import re
# Importando método choice (lib random), que sorteia e retorna um elemento de uma lista, para o jogo da forca
from random import choice
print(f"""
                Olá! Somos o projeto KubeFarm e temos como objetivo fomentar o acesso de pessoas a uma dieta alimentar saudável, 
                natural e livre de agrotóxicos - estejam essas pessoas em escolas públicas, comunidades carentes ou em regiões 
                afetadas pelo clima; e sejam elas quilombolas ou em situação de extrema pobreza - através da agricultura inteligente, 
                orgânica e sustentável. Por meio do nosso jogo KubeGame, você é convidado a concorrer a brindes, se candidatar a 
                receber informações sobre nossos eventos e atualizações e, caso queira, compartilhar o jogo com os amigos!""")
print(f"""
                                                            *KubeGame*

                                    Teste seus conhecimentos por meio de um quiz, ganhe um jogo da forca com
                                    as palavras que envolvem o nosso projeto e a ODS2 e ganhe desde brindes do 
                                    projeto KubeFarm até uma cesta de R$50 em vegetais e horliças orgânicos! 
                                    Compartilhe com os amigos :)
                                    """)


def infos():
    # Lista para abrigar informações do usuário
    listaInfos = []
    # Criando padrões para input(expressões regulares)
    padrao_email = r'.*@.*.com.*'
    padrao_nome = r'.*\s+.*'

    print("Antes de começar, nos conte mais sobre você:")
    nome = input("Qual seu nome completo?")
    while nome.isnumeric() or not re.match(padrao_nome, nome):
        print("Use letras e digite o nome completo!")
        nome = input("Digite nomamente:")
    listaInfos.append(nome)
    email = input("Qual é seu e-mail?")
    while not re.match(padrao_email, email):
        print("Email inválido! Caracteres obrigatórios: @ e .")
        email = input("Qual é seu e-mail?")
    listaInfos.append(email)

    como_conheceu = input(f"""Como ficou sabendo do projeto KubeFarm? Responda com a, b, c ou d: 
                          a.Amigos 
                          b.Redes Sociais 
                          c.Panfletos
                          d.Outros
                          Resposta: """).lower()
    while como_conheceu != 'a' and como_conheceu != 'b' and como_conheceu != 'c' and como_conheceu != 'd':
        como_conheceu = input("Erro. Digite novamente, apenas com a, b, c ou d").lower()
    listaInfos.append(como_conheceu)

    aceita_atualizacoes = input(
        f"""Aceita receber atualizações e informações sobre acões e eventos da KubeFarm pelo e-mail?"
        Dica: aceitar vai ser crucial para o seu score final do jogo e para a conquista de brindes! :)"
        Digite s para sim e n para não:""").lower()
    while aceita_atualizacoes != 's' and aceita_atualizacoes != 'n':
        aceita_atualizacoes = input("Erro. Digite novamente, apenas com a letra S ou N: ").lower()
    listaInfos.append(aceita_atualizacoes)

    return listaInfos


def kubeQuiz():
    # Funcão para estrutura das questões do quiz, com passagem de parâmetros:
    def perguntas(questao, opcoes, gabarito):
        while True:
            print(questao)
            for i, opcao in enumerate(opcoes):
                print(f"{i + 1}. {opcao}")

            resposta = input("Digite o número da opção correta: ")

            if resposta != '1' and resposta != '2' and resposta != '3':
                print("Digite uma opção válida: apenas 1, 2 ou 3")
                continue

            if resposta == str(gabarito):
                return 1
            else:
                return 0

    q1 = "\nQUESTAO 01) O que quer dizer sigla ODS?"
    opc1 = ['''Os 17 Objetivos de Desenvolvimento Sustentável, que foram estabelecidos pela Organização das Nações Unidas (ONU) 
    em 2015 e compõem uma agenda mundial para a construção e implementação de políticas públicas que visam guiar a humanidade até 2030''',
            '''Ordem Democrática para a Sustentabilidade, estabelecida na Conferência de Estocolmo para tratar das responsibilidades
    das grandes democracias em estabelecer metas políticas claras na aplicação de leis voltadas para a sustentabilidade''',
            '''Organização para Desenvolvimento Social, criada em 2008 pela Organização das Nações Unidas (ONU) 
    com o intuito de realizar reuniões anuais entre as grandes potências para discurir e desenvolver metas para erradicação da fome no mundo.''']
    gab1 = 1

    res_q1 = perguntas(q1, opc1, gab1)
    print(f"A resposta correta era: {gab1}")

    q2 = "\nQUESTÃO 02) Qual o objetivo número 2 da ODS2?"
    opc2 = ["Agroecologia e Biodinâmica", "Fome Zero e Agricultura Sustentável", "Educação Ecológica e Permacultura"]
    gab2 = 2

    res_q2 = perguntas(q2, opc2, gab2)
    print(f"A resposta correta era: {gab2}")

    q3 = "\nQUESTÃO 3) Qual é a meta 2.1 da ODS2?"
    opc3 = ['''Até 2030, acabar com todas as formas de má-nutrição, incluindo atingir, até 2025,
    as metas acordadas internacionalmente sobre nanismo e caquexia em crianças menores de cinco anos de idade''',
            '''Aumentar o investimento, inclusive via o reforço da cooperação internacional, em infraestrutura rural, pesquisa e extensão de serviços agrícolas, 
    desenvolvimento de tecnologia, e os bancos de genes de plantas e animais''',
            '''Até 2030, acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis,
    incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano.''']
    gab3 = 3

    res_q3 = perguntas(q3, opc3, gab3)
    print(f"A resposta correta era: {gab3}")

    if res_q1 + res_q2 + res_q3 == 3:
        print("\nVocê acertou todas e acaba de ganhar um carrinho de feira personalizado da KubeFarm! :)")
        return 3
    elif res_q1 + res_q2 + res_q3 == 2:
        print("\nVocê acertou duas de três! Ganhou uma ecobag da KubeFarm pelo esforço! :)")
        return 2
    elif res_q1 + res_q2 + res_q3 == 1:
        print("\nVocê acertou só uma questão. Ganhou uma garrafinha da KubeFarm! :)")
        return 1
    else:
        print("\nVocê acertou 0 questões! Tudo bem, ainda tem mais um round para se redimir e descolar uma cesta de orgânicos KubeFarm ;)")
        return 0

def kubeForca():
    # Lista de palavras
    palavras_forca = ['hortaliça', 'agricultura', 'organico', 'kubefarm',
                      'sustentabilidade', 'vegetais', 'frutas']

    # Sorteando uma palavra para ser adivinhada no jogo
    palavra_secreta = choice(palavras_forca)
    # print(palavra_secreta) para testar o código mais facilmente

    digitadas = []
    acertos = []
    erros = 0

    # Estrutura de repetição
    while True:
        secreto = ''
        for letra in palavra_secreta:
            secreto += letra if letra in acertos else '.'
        print('PALAVRA: ' + secreto)

        # Finaliza o jogo no caso de acerto
        if secreto == palavra_secreta:
            print('Round acertado!')
            global ponto_forca
            ponto_forca = 1
            break
        # lower() para manter as letras em minúsculo e strip() para não haver espaços
        chute = input('\nDigite uma letra: ').lower().strip()

        while True:
            # Método para existir apenas letras do alfabeto no jogo
            if len(chute) != 1 or chute.isalpha() == False:
                print("Digite não mais que uma letra! (não pode ser número, dígitos especiais ou espaços)")
                print('\nPALAVRA: ' + secreto)
                chute = input('\nDigite uma letra: ').lower().strip()
                continue
            else:
                break

                # Avisa caso uma letra se repita e não será usada na mesma palavra
        if chute in digitadas:
            print('Você já tentou essa letra.\nTente novamente!!!\n')
            continue
        else:
            digitadas += chute
            if chute in palavra_secreta:
                acertos += chute
            else:
                erros += 1
                print('Errou :( Tente novamente!\n')

        # Criando o bonequinho da forca e sua estrutura:
        pont = 1
        print('''K
          ______
    K   (  .  .  )
    K   |   .    |
    K    \  O   / 
    K     \____/          ''' if erros >= 1 else 'K')

        # Peito e braços
        linha2 = ''
        if erros == 2:
            linha2 += '''          /  |  \ 
    K    /   |   \ '''
        elif erros == 3:
            linha2 += '''          /  |  \  
    K    /   |   \ 
    K        |'''
        elif erros >= 4:
            linha2 += '''          /  |  \  
    K    /   |   \ 
    K   /    |    \\
    K        |'''
        print('K%s' % linha2)

        pernas = ''
        if erros == 5:
            pernas += '''          /     \ 
    K    /        \  '''
        elif erros == 6:
            pernas += '''          /     \ 
    K    /        \  
    K   /          \   '''
        elif erros >= 7:
            pernas += '''          /     \ 
    k    /        \  
    K   /          \   
    K   O           O '''
        print('K%s' % pernas)
        # Fim do jogo
        if erros == 7:
            print('Você foi enforcado(a)! Round perdido.')
            print(f"A palavra secreta era: {palavra_secreta}")
            ponto_forca = 0
            break

#programa principal:
while True:
    informacoes = infos()
    if informacoes[3] == 's':
        pont_infos = 1
    else:
        pont_infos = 0
    print(f"""
            Pronto, agradecemos! Agora vamos ao quiz. Ele vai ter três questões, cada uma valendo um ponto e um brinde!
            Caso você acerte as três questões, você vai estar também apto a concorrer ao prêmio final do KubeGame.
            Boa sorte!""")
    pont_kube_quiz = kubeQuiz()
    print(f"""
            Agora vamos para a última etapa do KubeGame: o jogo da forca.
            Serão TRÊS RODADAS (TRÊS PALAVRAS) e, caso você:
            -Ganhe as três
            -Tenha aceitado receber atualizações da KubeFarm
            -Tenha gabaritado o quiz;
            você ganha uma cesta personalizada e recheada de orgânicos no valor de RS80 da KubeFarm!\n""")
    print("\n***PRIMEIRO ROUND***")
    kubeForca()
    pForca1 = ponto_forca
    print("\n***SEGUNDO ROUND***")
    kubeForca()
    pForca2 = ponto_forca
    print("\n***TERCEIRO ROUND***")
    kubeForca()
    pForca3 = ponto_forca
    total_forca = pForca3 + pForca2 + pForca1
    print(f"""PONTUAÇÃO TOTAL DO JOGO DA FORCA: {total_forca} de 3.""")
    pontuacao_total = pont_kube_quiz + pont_infos + total_forca
    #pontuacao do jogo:
    if pontuacao_total == 7:
        print(f"""
              Parabéns! Você ganhou o jogo! Além dos brindes, ganhará uma cesta orgânica no valor de R$80 da KubeFarm.
              Mandaremos e-mail para confirmar seu endereço e enviar os mimos!""")
    elif pont_kube_quiz > 0 and pont_infos == 1:
        print(f"""
            Parabéns! Você não ganhou o jogo da forca, mas ganhou brinde no quiz. 
            Mandaremos e-mail para confirmar seu endereço e enviar os brindes!""")
    elif pont_kube_quiz > 0 and pont_infos != 1:
        print(f"""
             Parabéns pelos brindes! Infelizmente, você não ganhou o prêmio final por:
              - não ter ganho o jogo da forca, ou
              - não ter aceitado atualizações pelo e-mail. 
             Mande seu endereço para kubefarm@hotmail.com para receber os brindes. """)
    elif total_forca == 3 and pontuacao_total != 7:
        print(f"""
              Parabéns pelo jogo da forca! O prêmio só é concedido ao jogador com pontuação máxima 
              (contando com a opção de concessão ao recebimento de e-mails). 
              Mas não desanime, o KubeFarm realiza jogos, eventos e muito mais ao longo do ano
              para divulgação do nosso projeto social.
              Agradecemos a sua participação!""")
    else:
        print(f"""
              Agradecemos a participação! Você não ganhou brindes dessa vez, mas não desanime!
              O KubeFarm ainda realizará muitos jogos, eventos e muito mais ao longo do ano para 
              divulgação do nosso projeto social.
              """)

    break