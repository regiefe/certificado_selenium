from element import Element

browser = ['chrome', 'firefox']

class Cadastro(Element):
	       """Recebe uma lista onde a chave correspondente ao nome do elemento e os valores dos campos da pagina."""

    def cadastrando(self, cadastro):

        self.browser.find_element_by_xpath('//a[text()="#cadastro"]').click()

        for chave, valor in zip(cadastro.keys(), cadastro.values()): #Varre a lista passando a chave e o valor dela para o selenium
            self.browser.find_element_by_name(chave).send_keys(valor)

        self.browser.find_element_by_class_name('btn-primary').click()

cadastro =  {
    "nome": "regis",
    "email": "regis@teste.com",
    "senha": "123"
}

page = Cadastro(browser[1],'http://todo-brython.herokuapp.com/')
page.cadastrando(cadastro)
