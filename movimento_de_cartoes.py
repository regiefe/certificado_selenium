from login import Login

login = {
    "email": "regis@teste.com",
    "senha": "123"
}

page = Login('chrome','http://todo-brython.herokuapp.com/')
page.logando(login)
# page.limpa_cards()

page.afazer()
page.fazendo()
page.pronto()
