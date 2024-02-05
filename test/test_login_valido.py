import pytest
from page.home_page import HomePage
from page.login_page import LoginPage



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestC02:
    def test_c02_login_valido(self):
        # Instancia os objetos a serem usados no teste 
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page = HomePage()
       
       # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()
       
        