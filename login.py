from element import Element

class Login(Element):
	       """Realiza login, recebendo uma lista com as informações de logar."""
	       
    def logando(self, login):
        for chave, valor in zip(login.keys(), login.values()): #Varre a lista passando a chave e o valor dela para o selenium
            self.browser.find_element_by_name(chave).send_keys(valor)

        self.browser.find_element_by_class_name('btn-primary').click()

