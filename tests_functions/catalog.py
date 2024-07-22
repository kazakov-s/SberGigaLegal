from pages.catalog_page import CatalogPage


def catalog_select(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.catalog_section().click()
