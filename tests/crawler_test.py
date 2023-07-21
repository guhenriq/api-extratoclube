import pytest
from src.crawler.browser import Browser

PORTAL_URL = 'http://extratoclube.com.br/'
PORTAL_LOGIN = 'konsi'
PORTAL_PASSWORD = 'konsi'

@pytest.fixture(scope="session")
def browser():
    b = Browser()
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

def test_login_invalid_portal(browser: Browser):
    page = browser.page
    
    page.goto(PORTAL_URL)

    page.wait_for_load_state('networkidle')

    frame = page.frames[1]
    
    input_user = frame.query_selector('#user')
    input_user.fill('invalid_user')

    input_password = frame.query_selector('#pass')
    input_password.fill('invalid_password')
    
    with page.expect_response('http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login') as res:
        btn_logar = frame.query_selector('#botao')
        btn_logar.click()

    status_code = res.value.status

    assert status_code == 401

    