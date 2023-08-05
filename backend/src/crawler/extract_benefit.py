from .browser import Browser


class ExtractBenefit:
    
    def __init__(self, browser: Browser) -> None:
        self.browser = browser
        self.url = 'http://extratoclube.com.br/'

    def execute(self, cpf: str, username: str, password: str):
        try:
            self.browser.start()

            self.__home()

            logado = self.__login(username, password)

            if not logado:
                return {'msg': 'invalid credentials'}
            
            data = self.__extract_data(cpf)

            return data

        except Exception as e:
            print(e)
        finally:
            self.browser.exit()

    def __home(self):
        page = self.browser.page
        page.goto(self.url)

        page.wait_for_load_state('networkidle')

    def __login(self, username: str, password: str):
        page = self.browser.page

        frame = page.frames[1]

        input_user = frame.query_selector('input[name="usuario"]')
        input_user.fill(username)

        input_password = frame.query_selector('#pass')
        input_password.fill(password)

        with page.expect_response('http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login') as res:
            btn_logar = frame.query_selector('#botao')
            btn_logar.click()

        status_code = res.value.status

        if status_code == 200:
            return True
        if status_code == 401:
            return False
        
    def __extract_data(self, cpf: str):
        page = self.browser.page

        frame = page.frames[1]

        page.wait_for_load_state('networkidle')

        frame.wait_for_selector('#main')

        btn_close_modal = frame.query_selector('ion-button[title="Fechar"]')
        btn_close_modal.click()

        menu = frame.locator('ion-menu[menu-id="first"]')
        menu.click()

        frame.wait_for_selector('xpath=//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card')

        btn_active = frame.locator('ion-button[color="warning"]')
        btn_active.click()

        button_beneficio = frame.get_by_text('Encontrar Benefícios de um CPF')
        button_beneficio.click()

        input_beneficio = frame.locator(
            'xpath=//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-item/ion-input/input')
        input_beneficio.fill(cpf)
        
        page.keyboard.press('Tab', delay=1000)

        with page.expect_response('*'):
            page.keyboard.press('Enter', delay=1000)

        item = frame.evaluate(""" () => {
                var item = document.querySelectorAll(".item.md.ion-focusable.hydrated.item-label");
                var matricula = item[0].querySelector('ion-label').innerText;
                return matricula
            }   
        """)

        return item


