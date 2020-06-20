from time import sleep

print('=-='*30)
print('Olá, sejam bem vindos ao jogo da forca! ')
print('=-='*30)
sleep (1)
jogador1 = input('Informe quem será o jogador 1: ')
print('Armazenando seu nome... ')
sleep (0.3)
jogador2 = input('Informe quem será o jogador 2: ')
print('Armazenando seu nome... ')
print('=-='*30)
sleep (0.3)

while True:

    desafiador = input('Quem será o desafiador? Jogador1 ou jogador2: ')
    if desafiador == 'jogador1' or desafiador == '1':
        desafiador = jogador1
        desafiado = jogador2
        break
    elif desafiador == 'jogador2' or desafiador == '2':
        desafiador = jogador2
        desafiado = jogador1
        break
    else:
        print('Somente jogador1, 1, jogador2 e 2 são respostas válidas, favor responda novamente! ')

print('{} é o desafiador, e o {} é o desafiado! '.format(desafiador, desafiado))
print('...')
sleep(2)
print('Ok, vamos começar... ')
print('O jogo está carregando... ')
sleep(2)
print('=-='*30)

comecar_o_jogo = input('Tudo certo? Podemos começar o jogo da forca? informe qualquer letra para continuar ou informe 1 para encerrar o jogo da forca: ')
if comecar_o_jogo == '1':
    print('Obrigado por jogar! Volte logo, estarei esperando! ')
    sleep(2)
    print('Encerrando... ')
    sleep(4)
    print('Programa encerrado! ')
else:
    print('Ok, iniciando... ')
    sleep(3)

palavra_secreta = input('{}, você deve informar uma palavra para começarmos o jogo da forca: '.format(desafiador)).lower().strip()
dica_palavra_secreta = input('{}, você deve informar uma dica que esteja ligada a palavra secreta: '.format(desafiador))
print('Carregando... ')
sleep(2)
print('=-='*30)
print('A palavra definida foi: {} '.format(palavra_secreta))
print('A dica da palavra secreta é: {} '.format(dica_palavra_secreta))
print('=-='*30)
sleep(2)
print('O Terminal será limpo em 3 segundos... ')
sleep(3.5)
print('\n'*1000)
print('Terminal limpo... ')
sleep(2)

digitadas = []
acertos = []
erros = 0

while True:
    senha = ''
    for letra in palavra_secreta:
        senha += letra if letra in acertos else '.'
    print(senha)
    print('Dica: {}'.format(dica_palavra_secreta))
    print('{}, você pode chutar a palavra caso queira! '.format(desafiado))
    if senha == palavra_secreta:
        print('{} acertou!'.format(desafiado))
        sleep(1)
        print('GAME OVER!')
        sleep(3)
        print('Obrigado por jogar! ')
        sleep(3)
        print('Volte sempre, estarei esperando por você! ')
        sleep(3)
        print('Vida longa e próspera! ')
        sleep(3)
        print('Encerrando... ')
        sleep(3)
        break
    tentativa = input('\ninforme uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('{}, você já usou esta letra!'.format(desafiado))
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra_secreta:
            acertos += tentativa
        else:
            erros += 1
            print('{} errou! '.format(desafiado))
    print('\n'*100)
    print('')
    print('=-='*30)
    print('X--:--\nX  :   ')
    print('X  O   ' if erros >= 1 else 'X')
    linha2 = ''
    if erros == 2:
        linha2 = '  |   '
    elif erros == 3:
        linha2 = ' \|   '
    elif erros >= 4:
        linha2 = ' \|/ '
    print('X%s' % linha2)
    linha3 = ''
    if erros == 5:
        linha3 += ' /     '
    elif erros >= 6:
        linha3 += ' / \ '
    print('X%s' % linha3)
    print('X\n-----------')
    print('')
    if erros == 6:
        print('{} foi enforcado! '.format(desafiado))
        sleep(2)
        print('GAME OVER!')
        sleep(3)
        print('Obrigado por jogar! ')
        sleep(3)
        print('Volte sempre, estarei esperando por você! ')
        sleep(3)
        print('Vida longa e próspera! ')
        sleep(3)
        print('Encerrando... ')
        sleep(3)
        break