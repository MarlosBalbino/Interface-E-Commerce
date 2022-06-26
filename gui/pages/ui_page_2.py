""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from gui.widgets.py_push_button import PyPushButton
from gui.widgets.categories_list import Categories
from qt_core import *

import os
from gui.widgets.my_push_button import MyPushButton


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

        self.central_frame = QFrame()
        self.central_layout = QVBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(0)

        #############################################################################################
        # SPACERS
        #############################################################################################
        self.h_spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #############################################################################################
        # TOGGLE/SEARCH/SHOPPING CART FRAME
        #############################################################################################
        self.second_frame = QFrame()
        self.second_frame.setStyleSheet("background-color: #ff4747")
        self.second_frame.setFixedHeight(80)
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

        self.shopping_cart_btn = PyPushButton(
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
        # CONTENT FRAME
        #############################################################################################
        # SCROLL AREA
        self.content_area = QWidget()
        self.content_area_layout = QVBoxLayout(self.content_area)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("border: none")
        self.scroll_area.setWidgetResizable(True)

        self.v_scroll_bar = QScrollBar()
        self.v_scroll_bar.setStyleSheet("background-color: #bfbfbf")

        self.scroll_area.setVerticalScrollBar(self.v_scroll_bar)

        self.content_area_layout.addWidget(self.scroll_area)

        self.content = QWidget()
        self.content.setStyleSheet("background-color: #f3f4f4")
        self.content_layout = QHBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        self.products_frame = QFrame()
        self.products_frame.setMinimumHeight(660)
        # self.products_frame.setMaximumWidth(1150)
        # self.products_frame.setStyleSheet("background-color: #707070")

        self.sell_label = QLabel("Destaques e Novos", parent=self.products_frame)
        self.sell_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.sell_label.setMinimumWidth(300)
        self.sell_label.move(60, 15)

        self.products_layout = QGridLayout(self.products_frame)
        self.products_layout.setContentsMargins(60, 80, 60, 100)
        self.products_layout.setSpacing(25)

        self.add_product()

        self.content_layout.addWidget(self.products_frame)

        # SET WIDGET FOR SCROLL AREA
        self.scroll_area.setWidget(self.content)

        # ADD TO CENTRAL LAYOUT
        self.central_layout.addWidget(self.second_frame)
        self.central_layout.addWidget(self.content_area)
        # self.central_layout.addWidget(self.bottom_bar)

        # CATEGORIES FRAME
        self.categories_frame = Categories(self.central_frame)
        self.categories_frame.move(-280, 89)

        # PAGE LAYOUT
        self.verticalLayout.addWidget(self.central_frame)
        window.pages.addWidget(self.page)

        #############################################################################################
        # EVENTS
        #############################################################################################
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

    def add_product(self):

        app_path = os.path.abspath(os.getcwd())
        icons_folder = "gui/images/produtos"
        path = os.path.join(app_path, icons_folder)
        files = os.listdir(path)

        try:
            files = files.remove("desktop.ini")
        except:
            pass

        k = 0
        for i in range(2):
            for j in range(4):
                file = files[k]
                file_name = file
                file = file[:-4].split(sep="+")
                tittle = file[0]
                old_price = file[1]
                price = file[2]

                product = Product(
                    tittle=tittle,
                    price=price,
                    original_price=old_price,
                    img_name=file_name
                )
                self.products_layout.addWidget(product, i, j)

                k += 1


class Product(QFrame):
    def __init__(
            self,
            tittle="Titúlo do produto",
            price="R$ 999,99",
            original_price="",
            img_name=""
    ):
        super().__init__()
        self.setStyleSheet("""QFrame{
                background-color: #f3f4f4;
                border-radius: 5px;
                border: 0px solid "#ff4747";
                color: "#21232d"}
        """)
        self.setFixedHeight(500)
        self.setFixedWidth(270)

        self.shadow_effects = QGraphicsDropShadowEffect()
        self.shadow_effects.setBlurRadius(20)

        self.setGraphicsEffect(self.shadow_effects)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(15)

        self.product_frame = QFrame()
        self.product_layout = QVBoxLayout(self.product_frame)
        self.product_layout.setContentsMargins(0,0,0,0)
        self.product_layout.setSpacing(0)

        app_path = os.path.abspath(os.getcwd())
        icons_folder = "gui/images/produtos"
        path = os.path.join(app_path, icons_folder)
        image_path = os.path.normpath(os.path.join(path, img_name))

        self.image_label = QLabel()
        self.image_label.setStyleSheet("QLabel{border: none}")
        self.image = QPixmap(image_path)
        self.image_label.setPixmap(self.image.scaled(QSize(250, 250), Qt.KeepAspectRatio, Qt.SmoothTransformation), )

        self.product_tittle = QLabel(f"{tittle}")
        self.product_tittle.setStyleSheet(
            """QLabel{
                border: none;
                font: bold;
        }""")
        self.product_tittle.setWordWrap(True)

        self.product_layout.addWidget(self.image_label)
        self.product_layout.addWidget(self.product_tittle)

        self.price_frame = QFrame()
        self.price_layout = QVBoxLayout(self.price_frame)
        self.price_layout.setContentsMargins(0,0,0,0)
        self.price_layout.setSpacing(0)

        self.original_price = QLabel(f"R$ {original_price}")
        self.original_price.setStyleSheet("QLabel{border: none}")
        font = self.original_price.font()
        font.setStrikeOut(True)
        self.original_price.setFont(font)

        self.product_price = QLabel(f"R$ {price}")
        self.product_price.setStyleSheet(
            """QLabel{
                color: #ff4747;
                border: none;
                font: bold 16pt;
        }""")

        self.payment = QLabel("No Boleto ou Pix")
        self.payment.setStyleSheet("QLabel{border: none}")

        self.price_layout.addWidget(self.original_price)
        self.price_layout.addWidget(self.product_price)
        self.price_layout.addWidget(self.payment)

        self.register_btn_frame = QFrame()
        self.register_btn_frame.setStyleSheet("border: none")
        self.register_btn_frame.setFixedHeight(40)
        self.register_btn_frame_layout = QHBoxLayout(self.register_btn_frame)
        self.register_btn_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.register_btn = MyPushButton("Comprar", "#ff4747", text_color="white", maximum_width=100,
                                         maximum_heigth=35)
        self.register_btn_frame_layout.addWidget(self.register_btn)

        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Expanding)

        self.layout.addWidget(self.product_frame)
        #self.layout.addSpacerItem(self.v_spacer)
        self.layout.addWidget(self.price_frame)
        #self.layout.addSpacerItem(self.v_spacer)
        self.layout.addWidget(self.register_btn_frame)
        #self.layout.addSpacerItem(self.v_spacer)

