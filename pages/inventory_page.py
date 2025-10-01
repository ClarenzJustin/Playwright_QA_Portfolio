class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    def add_item_to_cart(self, item_name: str):
        selector = f'[data-test="add-to-cart-{item_name.lower().replace(" ", "-")}"]'
        self.page.click(selector)

    def remove_item_from_cart(self, item_name: str):
        selector = f'[data-test="remove-{item_name.lower().replace(" ", "-")}"]'
        self.page.click(selector)

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_count(self):
        if self.page.is_visible(self.cart_badge):
            return int(self.page.inner_text(self.cart_badge))
        return 0
