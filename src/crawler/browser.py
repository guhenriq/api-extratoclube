from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, hedless: bool = True):
        self.headless = hedless
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        p = sync_playwright().start()
        self.browser = p.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def exit(self):
        if self.browser:
            self.page.close()
            self.context.close()
            self.browser.close()
