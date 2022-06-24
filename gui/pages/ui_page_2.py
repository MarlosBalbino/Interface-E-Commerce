""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from gui.widgets.py_push_button import PyPushButton
from gui.widgets.categories_list import Categories
from qt_core import *


class UI_application_page_2(object):
    def __init__(self, window):
        if not window.pages.objectName():
            window.pages.setObjectName(u"application_pages")

        #############################################################################################
        # PAGE
        #############################################################################################
        self.page = QWidget()        
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.content_frame = QFrame()
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(9)

        #############################################################################################
        # SPACERS
        #############################################################################################
        self.h_spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #############################################################################################
        # TOP FRAME
        #############################################################################################
        # self.top_frame = QFrame()
        # self.top_frame.setMaximumHeight(50)
        #self.top_frame.setStyleSheet("background-color: grey")

        # self.top_frame_layout = QHBoxLayout(self.top_frame)
        # self.top_frame_layout.setContentsMargins(5, 5, 5, 5)        

        #############################################################################################
        # MIDDLE FRAME
        #############################################################################################
        self.second_frame = QFrame()
        self.second_frame.setStyleSheet("background-color: #ff4747")
        self.second_frame.setMaximumHeight(70)
        self.second_frame_layout = QHBoxLayout(self.second_frame)
        self.second_frame_layout.setSpacing(20)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Buscar")
        self.search_box.setStyleSheet("""
            border: none; color: black;
            padding: 8px;
            background-color: #f3f4f4; 
            border-radius: 3""")
        self.search_box.setFixedWidth(300)
        self.search_box.setMinimumHeight(40)

        self.shopping_cart_btn =  PyPushButton(
            f"Carrinho | {0}",
            icon_path="cil-cart.png",
            button_color="#21232d",
            text_color="#ff4747",
            icon_color="#ff4747",
            button_hover="#b22222",
            border_radius=3
        )
        self.shopping_cart_btn.setMinimumHeight(40)
        self.shopping_cart_btn.setFixedWidth(155)

        self.toggle_btn_frame = QFrame()
        self.toggle_btn_frame.setStyleSheet("border-radius: 10")
        self.toggle_btn_frame.setFixedWidth(150)
        self.toggle_btn_frame_layout = QHBoxLayout(self.toggle_btn_frame)
        self.toggle_btn_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.toggle_btn = PyPushButton(
            "Categorias",
            icon_path="icon_menu.svg",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            border_radius=3
        )      

        self.toggle_btn_frame_layout.addWidget(self.toggle_btn)

        self.second_frame_layout.addWidget(self.toggle_btn_frame)
        self.second_frame_layout.addSpacerItem(self.h_spacer)
        self.second_frame_layout.addWidget(self.search_box)
        self.second_frame_layout.addWidget(self.shopping_cart_btn)
        self.second_frame_layout.addSpacerItem(self.h_spacer2)

        #############################################################################################
        # BOTTOM FRAME
        #############################################################################################
        self.bottom_frame = QFrame()
        self.bottom_frame.setStyleSheet("background-color: #f3f4f4")
        self.bottom_frame_layout = QHBoxLayout(self.bottom_frame)
        self.bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        
        self.products_frame = QFrame()
        # self.products_frame.setStyleSheet("background-color: #707070")

        self.bottom_frame_layout.addWidget(self.products_frame)

        self.categories_frame = Categories(self.bottom_frame)
        self.categories_frame.move(-280, 0)

        # self.bottom_frame_layout.addWidget(self.login_frame)
        # self.content_layout.addWidget(self.top_frame)
        self.content_layout.addWidget(self.second_frame)
        self.content_layout.addWidget(self.bottom_frame)

        self.verticalLayout.addWidget(self.content_frame)
        window.pages.addWidget(self.page)

        self.toggle_btn.clicked.connect(self.toggle_button)
        
    def toggle_button(self):
        # Get left menu width
        pos_x = self.categories_frame.pos().x()
        pos_y = self.categories_frame.pos().y()
        width = self.categories_frame.width()
        height = self.categories_frame.height()

        # Check width
        pos_x1 = -280
        if pos_x == -280:
            pos_x1 = 9

        # Start animation
        self.animation = QPropertyAnimation(self.categories_frame, b"geometry")
        self.animation.setStartValue(QRect(pos_x, pos_y, width, height))
        self.animation.setEndValue(QRect(pos_x1, pos_y, width, height))
        self.animation.setDuration(100)
        self.animation.start()
