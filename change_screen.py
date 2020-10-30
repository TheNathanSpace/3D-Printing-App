class ChangeScreen:
    def __init__(self):
        ""

    def update(self, main_window, uses_window, plastics_window):
        self.main_window = main_window
        self.uses_window = uses_window
        self.plastics_window = plastics_window

    def open_uses(self):
        self.main_window.hide()
        self.uses_window.show()

    def open_plastics(self):
        self.main_window.hide()
        self.plastics_window.show()

    def open_main(self, closed):
        closed.hide()
        self.main_window.show()
