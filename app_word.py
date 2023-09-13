import random


#Lista de paravras, para trocar basta manter a sintaxe:
# {"pt" : "Palavra em Portuês", "ing" : "Palavra em Inglês"},.

list_word = [
    {"pt" : "Padaria" , "ing" : "Bakery"},
    {"pt" : "Presa", "ing" : "Stuck"},
    {"pt" : "Saindo", "ing" : "Going out"},
    {"pt" : "Pensar", "ing" : "Think"},
    {"pt" : "Saber", "ing" : "Know"},
    {"pt" : "Somente", "ing" : "Just"},
    {"pt" : "Qualquer coisa", "ing" : "Anything"},
    {"pt" : "Apenas faça", "ing" : "Just do it"},
    {"pt" : "Era", "ing" : "Was"},
    {"pt" : "Primo", "ing" : "Cousin"},
    {"pt" : "Ocorrido", "ing" : "Happened"},
    {"pt" : "Shopping", "ing" : "Moll"},
    {"pt" : "Dificil", "ing" : "Tough"},
    {"pt" : "Manteiga", "ing" : "Butter"},
    {"pt" : "Século", "ing" : "Century"},
    {"pt" : "Barato", "ing" : "Cheap"},
    {"pt" : "Aplaudir", "ing" : "Cheer"},
    {"pt" : "Escolher", "ing" : "Choose"},
    {"pt" : "Nascimento", "ing" : "Birth"},
    {"pt" : "Barco", "ing" : "Boat"},
    {"pt" : "Nascido", "ing" : "Born"},
    {"pt" : "Quebrar", "ing" : "Break"},
    {"pt" : "Brilhante", "ing" : "Bright"},
    {"pt" : "Corajoso", "ing" : "Brave"},
    {"pt" : "Ser ou Estar", "ing" : "Be"},
    {"pt" : "Ter", "ing" : "Have"},
    {"pt" : "Dizer", "ing" : "Say"},
    {"pt" : "Obter ou Receber", "ing" : "Get"},
    {"pt" : "Fazer ou Criar", "ing" : "Make"},
    {"pt" : "Olhar", "ing" : "Look"},
    {"pt" : "Encontrar", "ing" : "Find"},
    {"pt" : "Dar", "ing" : "Give"},
    {"pt" : "Sentir", "ing" : "Feel"},
    {"pt" : "Perguntar", "ing" : "Ask"},
    {"pt" : "Deixar ou Sair", "ing" : "Leave"},
    {"pt" : "Chamar", "ing" : "Call"},
    {"pt" : "Tentar", "ing" : "Try"},
    {"pt" : "Torna-se", "ing" : "Become"},
    {"pt" : "Significa", "ing" : "Means"},
    {"pt" : "Manter", "ing" : "Keep"},
    {"pt" : "Permitir", "ing" : "Allow"},
    {"pt" : "Começar", "ing" : "Begin"},
    {"pt" : "Girar ou Virar", "ing" : "Turn"},
    {"pt" : "Mostrar", "ing" : "Show"},
    {"pt" : "Ouvir", "ing" : "Hear"}  ,
    {"pt" : "Nosso_Nossa", "ing" : "Our"},
    {"pt" : "Acreditar", "ing" : "Believe"},
    {"pt" : "Segurar Ou manter", "ing" : "Hold"},
    {"pt" : "Acontecer", "ing" : "Happen"},
    {"pt" : "Escrever", "ing" : "Write"},
    {"pt" : "Sentar", "ing" : "Sit"},
    {"pt" : "Ficar_de_Pé", "ing" : "Stand"},
    {"pt" : "Perder", "ing" : "Lose"},
    {"pt" : "Definir_ou_Colocar", "ing" : "Set"},
    {"pt" : "Aprender", "ing" : "Learn"},
    {"pt" : "Mudar", "ing" : "Change"},
    {"pt" : "Cobrir", "ing" : "Cover"},
    {"pt" : "Criar", "ing" : "Create"},
    {"pt" : "Falar", "ing" : "Speak"},
    {"pt" : "Ler", "ing" : "Read"},
    {"pt" : "Adicionar", "ing" : "Add"},
    {"pt" : "Caminhar", "ing" : "Walk"},
    {"pt" : "Esperar", "ing" : "Wait"},
    {"pt" : "Comprar", "ing" : "Buy"},
    {"pt" : "Dirigir", "ing" : "Drive"},
    {"pt" : "Cair", "ing" : "Fall"},
    {"pt" : "Ensinar", "ing" : "Teach"},
    {"pt" : "Melhorar", "ing" : "Improve"},
    {"pt" : "Medir", "ing" : "Measure"},
    {"pt" : "Esquecer", "ing" : "Forget"},
    {"pt" : "Juntar-se", "ing" : "Join"},
    {"pt" : "Consertar", "ing" : "Fix"},
    {"pt" : "Repetir", "ing" : "Repeat"},
    {"pt" : "Buscar", "ing" : "Search"},
    {"pt" : "Conter", "ing" : "Contain"}
             ]


# Loop onde as perguntas são geradas de forma recursiva, errando ou acertando.

while True:
    tam_list = len(list_word)
    random_word = random.randint(0, tam_list-1)
    print_list = list_word[random_word]["pt"]
    print('\033[0;31;47m',print_list,'\033[m')
    resposta = str.lower(input('Resposta: '))
    print()
    if resposta == str.lower(list_word[random_word]['ing']):
        print('Certa resposta')
        print()
    if resposta != str.lower(list_word[random_word]['ing']):
        print('Resposta errada!')
        print('A resposta correta é ', list_word[random_word]['ing'])
        print()
