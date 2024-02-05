import pytest
from selenium.webdriver.common.by import By
import conftest
from page.carrinho_page import CarrinhoPage
from page.home_page import HomePage
from page.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestC01:
    def test_c01_adicionar_produtos_carrinho(self):
        # 1 Fazendo login:
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"


        login_page.fazer_login("standard_user", "secret_sauce")

        # 2 - Adicionando mochila ao carrinho:
        
        home_page.adicionar_ao_carrinho(produto_1)

        # 2.1 Verificando se a mochila foi adicionada:
        home_page.acessar_carrinho()
        breakpoint()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        

        # 2.1 voltando para tela de produtos:
        #driver.find_element(By.XPATH,"//*[text() ='Continue Shopping']").click()
        carrinho_page.clicar_continuar_comprando()

        # Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # Verificando que os 2 produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

        # Checkout e finalizando compra
        driver.find_element(By.XPATH,"//*[@id='checkout']").click()

        driver.find_element(By.ID,"first-name").send_keys("Paulo")
        driver.find_element(By.ID,"last-name").send_keys("Vinicius")
        driver.find_element(By.ID,"postal-code").send_keys("62700-00")

        driver.find_element(By.XPATH,"//*[@id='continue']").click()

        driver.find_element(By.ID,"finish").click()

        assert driver.find_element(By.XPATH,"//*[@class='complete-text' and text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']").is_displayed
        print("Compra feita com sucesso e já despachada")