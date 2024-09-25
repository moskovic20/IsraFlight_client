import sys
from PySide6.QtWidgets import QApplication
from Controllers.MainController import MainController

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    # יצירת הבקר הראשי
    main_controller = MainController()
    
    # הצגת החלון הראשי
    main_controller.show_home_window()
    
    # הרצת הלולאה של האפליקציה
    sys.exit(app.exec())
