from page.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By



class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_do_iventario = (By.XPATH,"//*[@class='inventory_item_name' and text()= '{}']")
        self.botao_adicionar_carrinho = (By.XPATH,"//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH,"//*[@class='shopping_cart_link']")
        
    
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_do_iventario[0], self.item_do_iventario[1].format(nome_item)) # by posição [0] e locator o nome [1]
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho) 
        
    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

