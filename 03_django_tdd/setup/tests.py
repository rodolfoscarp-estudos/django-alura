from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            Path(__file__).parent.parent / 'chromedriver')

    def tearDown(self) -> None:
        self.browser.close()

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuario encontra um animal na pesquisa
        """
        self.browser.get(self.live_server_url)

        #
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')

        self.assertEqual('Busca Animal', brand_element.text)

        #
        buscar_animal_input = self.browser.find_element(
            By.CSS_SELECTOR, 'input#buscar-animal')

        self.assertEqual(buscar_animal_input.get_attribute(
            'placeholder'), 'Exemplo: leão')

        #
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        #
        caracteristas = self.browser.find_elements(
            By.CSS_SELECTOR, '.result-description')

        self.assertGreater(len(caracteristas), 3)
