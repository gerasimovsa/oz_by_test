from oz_by.model.pages.authorization_page import OzAuthorizationPage
from oz_by.model.pages.cart_page import OzCartPage
from oz_by.model.pages.catalog_page import OzCatalogPage
from oz_by.model.pages.favorites_page import OzFavoritesPage
from oz_by.model.pages.item_page import OzItemPage
from oz_by.model.pages.main_page import OzMainPage
from oz_by.model.pages.personal_data_page import OzPersonalDataPage
from oz_by.model.pages.registration_page import OzRegistrationPage
from oz_by.model.pages.search_results_page import OzSearchResultsPage


class Application:
    def __init__(self):
        self.main_page = OzMainPage()
        self.registration_page = OzRegistrationPage()
        self.auth_page = OzAuthorizationPage()
        self.personal_data_page = OzPersonalDataPage()
        self.search_result_page = OzSearchResultsPage()
        self.catalog_page = OzCatalogPage()
        self.cart_page = OzCartPage()
        self.item_page = OzItemPage()
        self.favorites_page = OzFavoritesPage()


app = Application()


