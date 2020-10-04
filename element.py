from selenium.webdriver import Remote
from time import sleep

class Element:

    def __init__(self, browser, url):

        print('Carregando o selenium ... \n')
        self.browser = browser
        self.url = url

        self.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName' : self.browser})
        self.browser.get(self.url)


    def cria(self, dados):

        sleep(5)
        self.limpa_cards()
        for chave, valor in zip(dados.keys(), dados.values()): #Varre a lista passando a chave e o valor dela para o selenium
            self.browser.find_element_by_name(chave).send_keys(valor)

        self.browser.find_element_by_class_name('btn-primary').click()

    def afazer(self):

        print('Aguardando sistema .... \n')
        sleep(5)
        print('Movendo para fazer todos tarefas  \n')
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('do').click()

    def fazendo(self):

        print('Movendo para tarefas prontas  \n')
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('do').click()

    def pronto(self):

        print('Refazendo todas as tarefas  \n')
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('do').click()

    def limpa_cards(self):
        
        print('Aguardando sistema .... \n')
        sleep(5)
        print('Apagando todas as tarefas  \n')
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('cancel').click()
