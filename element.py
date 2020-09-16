from selenium.webdriver import Remote
from time import sleep

class Element:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

        self.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName' : self.browser})
        self.browser.get(self.url)


    def limpa_cards(self):
        sleep(5)
        cards = self.browser.find_elements_by_class_name('terminal-card')
        for card in  cards:
            card.find_element_by_class_name('cancel').click()

    def cria(self, dados):
        sleep(5)
        self.limpa_cards()
        for chave, valor in zip(dados.keys(), dados.values()):
            self.browser.find_element_by_name(chave).send_keys(valor)

        self.browser.find_element_by_class_name('btn-primary').click()

    def afazer(self):
        sleep(5)
        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()

    def fazendo(self):
        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()

    def pronto(self):
        cards = self.browser.find_element_by_class_name('terminal-card')
        cards.find_element_by_class_name('do').click()
