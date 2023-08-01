import pytest
from src.crawler.browser import Browser

PORTAL_URL = 'http://extratoclube.com.br/'
PORTAL_LOGIN = 'konsiteste2'
PORTAL_PASSWORD = 'konsiteste2'

@pytest.fixture(scope="session")
def browser():
    b = Browser(headless=False)
    b.start()
    return b

def test_navigate_to_home(browser: Browser):
    page = browser.page
    page.goto(PORTAL_URL)
    assert page.url == PORTAL_URL

def test_login_portal(browser: Browser):
    page = browser.page
    
    page.goto(PORTAL_URL)

    page.wait_for_load_state('networkidle')

    frame = page.frames[1]
    
    input_user = frame.query_selector('input[name="usuario"]')
    input_user.fill(PORTAL_LOGIN)

    input_password = frame.query_selector('#pass')
    input_password.fill(PORTAL_PASSWORD)
    
    with page.expect_response('http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login') as res:
        btn_logar = frame.query_selector('#botao')
        btn_logar.click()

    status_code = res.value.status

    assert status_code == 200

def test_close_modal(browser: Browser):
    page = browser.page

    page.wait_for_load_state('networkidle')

    frame = page.frames[1]

    frame.wait_for_selector('#main')
    
    btn_close_modal = frame.query_selector('ion-button[title="Fechar"]')
    btn_close_modal.click()

def test_close_menu(browser: Browser):
    page = browser.page

    page.wait_for_load_state('networkidle')

    frame = page.frames[1]

    menu = frame.locator('ion-menu[menu-id="first"]')

    menu.click()
    
def test_extract_benefit(browser: Browser):
    page = browser.page

    page.wait_for_load_state('networkidle')

    frame = page.frames[1]

    frame.wait_for_selector('xpath=//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card')

    button_beneficio = frame.get_by_text('Encontrar Benefícios de um CPF')
    button_beneficio.click()

    input_beneficio = frame.locator(
        'xpath=//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-item/ion-input/input')
    input_beneficio.fill('033.355.888-00')
    
    page.keyboard.press('Tab', delay=1000)

    with page.expect_response('*'):
        page.keyboard.press('Enter', delay=1000)

    item = frame.evaluate(""" () => {
            var item = document.querySelectorAll(".item.md.ion-focusable.hydrated.item-label");
            var matricula = item[0].querySelector('ion-label').innerText;
            return matricula
        }   
    """)

    assert item == '6012629862'

    






    

    

    