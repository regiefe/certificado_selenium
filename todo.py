from login import Login
nome =  input('Nome da tarefa que vamos fazer: ')
descreva = input('Descreva a tarefa que vamos fazer: ')

login = {
	"email" : 'regis@teste.com',
	"senha": '123'
}

tarefa =  {
    "name": nome,
    "desc": descreva,
}

page = Login('chrome','http://todo-brython.herokuapp.com/')
page.logando(login)
page.cria(tarefa)