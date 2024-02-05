import pytest
import time
from selenium.webdriver.common.by import By
import conftest
from page.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestC03:
    def test_c03_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        driver = conftest.driver
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login("standard_user", "senha_digitada_incorreta")        
        
        # Verificar se o login não foi realizado e a mensagem de erro apareceu
        login_page.verificar_mensagem_erro_login_existe()

        # Verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_error_login
        

       
        