from login import Login

browser = ['chrome', 'firefox']

login = {
    "email": "regis@teste.com",
    "senha": "123"
}

page = Login(browser[0],'http://todo-brython.herokuapp.com/')
page.logando(login)

page.afazer()
page.fazendo()
page.pronto()
page.limpa_cards()
