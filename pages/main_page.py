from pages.base_page import Page

class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def open_market_page(self):
        self.open_url('https://soft.reelly.io/market')