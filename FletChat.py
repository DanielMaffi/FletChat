import flet as ft
import random
from datetime import datetime

# Cria a funcao principal do aplicativo 
def main(page):

    def dateTime():
        time = datetime.now()
                            #"%d/%m/%Y %H:%M:%S"
        return time.strftime("%d/%m/%Y %H:%M") 
    
    # Cria a funcao que gera as mensagems de boas vindas
    def welcomeMassagem():
        wordList = [
                    f"{userNameField.value} entrou no chat", 
                    f"Bananas me mordam!!! {userNameField.value} entrou no chat",
                    f"Mais diversão chegou {userNameField.value} acabou de entrar no chat"
                    ]
        welcomeMassagem = f"{dateTime()} {random.choice(wordList)}"
        page.pubsub.send_all(welcomeMassagem)
    
    # Funcao do botao quando entra no chat
    # Funcao que exclui elementos das pagina de entrar no chat
    # Tambem adiciona os elementos do chat
    def joinChat(evento):
        userName = userNameField.value
        if userName != "":
            page.remove(titulo)
            page.remove(buttonStartChat)
            popup.open = False
            page.add(chatBox)
            page.add(rowMassage)
            welcomeMassagem()
            page.update()
    
        
    # Criar o elemento
    titulo = ft.Text("FletChat")

    titleWindow = ft.Text("Bem-vindo ao FletChat")
    userNameField = ft.TextField(label="Escreva seu nome no chat", on_submit=joinChat )

    chatBox = ft.Column()

    # Configuracao do socket para enviar as mensagem para todo mundo
    def sendMassageSocket(massage):
        chatText = ft.Text(massage)
        chatBox.controls.append(chatText)
        page.scroll = "always"
        page.update()

    page.pubsub.subscribe(sendMassageSocket)

    # Funcao para enviar as mensagens dos usuarios
    def sendMassage(event):
        messageBox = messageField.value
        userName = userNameField.value
        if messageBox != "":
            massage = f"{dateTime()} {userName}: {messageBox}"
            page.pubsub.send_all(massage)
            messageField.value = ""
            page.update()
        messageField.focus()

    messageField = ft.TextField(label="Digite uma mensagem", on_submit=sendMassage)
    buttonSendMessage = ft.ElevatedButton("Enviar", on_click=sendMassage)

    # Criando uma linha de elementos para ser adicionada e ficara uma do lado do outro
    rowMassage = ft.Row([messageField, buttonSendMessage])

    buttonJoinChat = ft.ElevatedButton("Entrar no chat", on_click=joinChat)
    popup = ft.AlertDialog(title=titleWindow, content=userNameField, actions=[buttonJoinChat])

    # Cria o popup pedindo o nome do usuario junto com o botao de inicair chat
    def startChat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    buttonStartChat = ft.ElevatedButton("Iniciar Chat", on_click=startChat)

    # Adiciona o elemento na pagina
    page.add(titulo)
    page.add(buttonStartChat)

# Roda o aplicativo pela funcao main
# View e para determina como ela vai ser aberta WEB_BROWSERvai abrir como navegador
ft.app(main, view=ft.WEB_BROWSER)