class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # This will call the setter for validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")  # Ensures correct test output
        else:
            self._page_count = value  # Assign only if valid

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  # Expected output

        