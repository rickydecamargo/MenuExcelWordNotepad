import pyautogui as escolha_opcao

#Esperar para iniciar o app
escolha_opcao.sleep(2)

#Cria a variavel opcao com a atividade confirm (ela que cria as opções para clicar)
#Cria a pergunta do Menu
#buttons são as opções que estarão disponíveis para o user clicar.
opcao = escolha_opcao.confirm('Qual aplicativo você quer acessar?', buttons = ['Excel', 'Word', 'Notepad'])

#Esperar 2 Segundos
escolha_opcao.sleep(2)

#Mensagens para informar qual escolha do usuário e abrir o aplicativo
#Se o usuário escolher o Excel abra o Excel através do windows + r
if opcao == "Excel":
    print("Escolheu Excel")
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('excel')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.typewrite('100')
    escolha_opcao.sleep(2)
    escolha_opcao.moveTo(x=1350, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.click(x=1350, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    print('Encerrou o Excel sem salvar')

#Se o usuário escolher o Word abra o Word através do windows + r
elif opcao == 'Word':
    print("Escolheu Word")
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('winword')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(5)
    escolha_opcao.typewrite('Ola, seja bem-vindo ao Word.')
    escolha_opcao.sleep(2)
    escolha_opcao.moveTo(x=1350, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.click(x=1350, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.press('tab')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(2)
    print('Encerrou o Word sem salvar')

#Se o usuário escolher o Notepad abra o Notepad através do windows + r
elif opcao == 'Notepad':
    print("Escolheu Notepad")
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Ola, seja bem-vindo ao Notepad.')
    escolha_opcao.sleep(2)
    escolha_opcao.click(x=1235, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.click(x=1350, y=15)
    escolha_opcao.sleep(2)
    escolha_opcao.press('tab')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')
    escolha_opcao.sleep(2)
    print('Encerrou o Notepad sem salvar')


