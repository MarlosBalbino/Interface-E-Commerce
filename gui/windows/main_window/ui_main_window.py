from qt_core import *

# IMPORT PAGES
from gui.pages.ui_page_1 import UI_application_page_1
from gui.pages.ui_page_2 import UI_application_page_2
from gui.pages.ui_page_3 import UI_application_page_3
from gui.pages.ui_page_4 import UI_application_page_4

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton
from my_widgets.my_scroll_bar import MyScrollBar


# MAIN WINDOW
class UI_MainWindow(object):

    def setup_ui(self, parent):
        
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INCINALS PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(480, 360)

        # CREATE MAIN FRAME
        self.main_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        self.extern_layout = QVBoxLayout(self.central_frame)
        self.extern_layout.setContentsMargins(0,0,0,0)
        self.extern_layout.setSpacing(0)

        #############################################################################################
        # SPACERS
        #############################################################################################
        self.h_spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # CONTENT
        self.content = QWidget()
        #self.content.setStyleSheet("background-color: #707070") #f2f2f2

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        # self.top_bar.setMaximumHeight(50)
        self.top_bar.setMinimumHeight(55)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(15,5,15,5)
        self.top_bar_layout.setSpacing(50)

        self.tittle_label = QLabel("Projeto e-commerce", parent=self.top_bar)
        self.tittle_label.setStyleSheet("color: #ff4747; font: bold 18pt")
        self.tittle_label.setMinimumWidth(240)
        self.tittle_label.setMinimumHeight(50)
        self.tittle_label.move(200, 5)

        self.initial_page_btn = QPushButton("Página inicial")
        self.initial_page_btn.setStyleSheet("border: none; color: #ff4747; font: 12pt")
        self.initial_page_btn.hide()

        self.login_btn = QPushButton("Login ou cadastro")
        self.login_btn.setStyleSheet("border: none; color: #ff4747; font: 12pt")

        self.logout_btn = QPushButton("Logout")
        self.logout_btn.setStyleSheet("border: none; color: #ff4747; font: 12pt")
        self.logout_btn.hide()

        self.account_btn = QPushButton("Conta")
        self.account_btn.setStyleSheet("border: none; color: #ff4747; font: 12pt")
        self.account_btn.hide()

        self.support_btn = QPushButton("Suporte")
        self.support_btn.setStyleSheet("border: none; color: #ff4747; font: 12pt")

        # TOP FRAME LAYOUT
        self.top_bar_layout.addSpacerItem(self.h_spacer)
        self.top_bar_layout.addWidget(self.login_btn)
        self.top_bar_layout.addWidget(self.account_btn)
        self.top_bar_layout.addWidget(self.initial_page_btn)
        self.top_bar_layout.addWidget(self.logout_btn)
        self.top_bar_layout.addWidget(self.support_btn)

        # spacer
        self.spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("background-color: #f3f4f4; font-size: 12pt; color: #f8f8f2")
        self.pages.setWindowTitle("application_pages")
        self.pages.resize(622, 515)
        self.ui_page_1 = UI_application_page_1(self)        
        self.ui_page_2 = UI_application_page_2(self)        
        self.ui_page_3 = UI_application_page_3(self)        
        self.ui_page_4 = UI_application_page_4(self)
        self.pages.setCurrentWidget(self.ui_page_2.page)

        # ADD WIDGETS TO CONTENT LAYOUT
        self.content_layout.addWidget(self.pages)

        # ADD WIDGETS TO MAIN LAYOUT
        self.main_layout.addWidget(self.content)
        
        # ADD WIDGETS TO CENTRAL FRAME
        self.extern_layout.addWidget(self.top_bar)
        self.extern_layout.addWidget(self.main_frame)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)

        self.login_btn.clicked.connect(self.login_handle)
        self.logout_btn.clicked.connect(self.logout_handle)
        self.account_btn.clicked.connect(self.account_handle)
        self.initial_page_btn.clicked.connect(self.initial_page_handle)

    def login_handle(self):
        self.login_btn.hide()
        self.initial_page_btn.show()
        self.pages.setCurrentWidget(self.ui_page_1.page)

    def logout_handle(self):
        self.logout_btn.hide()
        self.account_btn.hide()
        self.initial_page_btn.show()
        self.pages.setCurrentWidget(self.ui_page_1.page)

    def account_handle(self):
        self.account_btn.hide()
        self.initial_page_btn.show()
        self.pages.setCurrentWidget(self.ui_page_4.page)

    def initial_page_handle(self):
        if self.pages.currentWidget() == self.ui_page_1.page:
            self.login_btn.show()
        elif self.pages.currentWidget() == self.ui_page_4.page:
            self.account_btn.show()

        self.initial_page_btn.hide()

        self.pages.setCurrentWidget(self.ui_page_2.page)

