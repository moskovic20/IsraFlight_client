from Views.HomeWindow import HomeWindow

class HomeController:
    def __init__(self,Main_controller):
        self.mainController=Main_controller
        self.home_window = HomeWindow(self)

    def show_window(self):
        self.home_window.showMaximized()

    def show_login_screen(self):
        self.mainController.show_sing_in_window()

    def show_create_account_screen(self):
        self.mainController.show_creat_account()