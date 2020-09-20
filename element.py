from selenium.webdriver import Remote
from time import sleep

class Element:
    """Elementos da pagina testada."""

    def __init__(self, browser, url):
        """Tem que passar um navegador e uma URL base para instanciar a Classe."""

        self.browser = browser
        self.url = url

        self.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName' : self.browser})
        self.browser.get(self.url)


    def limpa_cards(self):
        """Cancela todos os cartoes existente."""

        sleep(5)
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('cancel').click()

    def cria(self, dados):
        """
            Cria uma nova tarefa. 
            Recebe uma lista onde a chave correspondente ao nome do elemento e os valores dos campos da pagina.
        """

        sleep(5)
        self.limpa_cards()
        for chave, valor in zip(dados.keys(), dados.values()): #Varre a lista passando a chave e o valor dela para o selenium
            self.browser.find_element_by_name(chave).send_keys(valor)

        self.browser.find_element_by_class_name('btn-primary').click()

    def afazer(self):
            """Desloca o cartão para fazendo."""

        sleep(5)
        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()

    def fazendo(self):
               """Desloca o cartão para Feito."""

        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()

    def pronto(self):
               """Desloca o cartão desloca o cartao devolta para a fazer."""

        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()
