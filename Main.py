import sys
from PySide6.QtWidgets import QApplication
from Controllers.MainController import MainController

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    main_controller = MainController()
    
    main_controller.show_home_window()
    
    #start run
    sys.exit(app.exec())
