from login import Login

browser = ['chrome', 'firefox']

login = {
    "email": "regis@teste.com",
    "senha": "123"
}

page = Login(browser[1],'http://todo-brython.herokuapp.com/')
page.logando(login)
# page.limpa_cards()

page.afazer()
page.fazendo()
page.pronto()
