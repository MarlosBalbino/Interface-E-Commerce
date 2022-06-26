""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from qt_core import *

from gui.widgets.py_push_button import PyPushButton
from gui.widgets.my_push_button import MyPushButton


class UI_application_page_4(object):
    def __init__(self, window):
        if not window.pages.objectName():
            window.pages.setObjectName(u"application_pages")

        self.page = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0,0,0,0)

        #############################################################################################
        # SPACERS
        #############################################################################################
        self.h_spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #############################################################################################
        # CONTENT FRAME
        #############################################################################################
        self.content_frame = QFrame()
        # self.teste_frame.setStyleSheet("background-color: grey")
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        #############################################################################################
        # BUTTONS
        #############################################################################################
        self.btns_frame = QFrame(self.content_frame)
        self.btns_frame.setStyleSheet("background-color: #ff4747")
        self.btns_frame.setFixedHeight(80)

        self.btns_layout = QHBoxLayout(self.btns_frame)
        self.btns_layout.setSpacing(10)

        self.my_account_btn = PyPushButton(
            f"Minha Conta",
            icon_path="cil-user.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.my_account_btn.setMinimumHeight(40)
        self.my_account_btn.setFixedWidth(180)

        self.my_data_btn = PyPushButton(
            f"Meus Dados",
            icon_path="cil-clipboard.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.my_data_btn.setMinimumHeight(40)
        self.my_data_btn.setFixedWidth(180)

        self.my_address_btn = PyPushButton(
            f"Meus Endereços",
            icon_path="cil-truck.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.my_address_btn.setMinimumHeight(40)
        self.my_address_btn.setFixedWidth(180)

        self.my_orders_btn = PyPushButton(
            f"Meus Pedidos",
            icon_path="cil-notes.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.my_orders_btn.setMinimumHeight(40)
        self.my_orders_btn.setFixedWidth(180)

        self.products_btn = PyPushButton(
            f"Vender",
            icon_path="cil-share.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.products_btn.setMinimumHeight(40)
        self.products_btn.setFixedWidth(180)

        self.my_sells_btn = PyPushButton(
            f"Minhas Vendas",
            icon_path="cil-wallet.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.my_sells_btn.setMinimumHeight(40)
        self.my_sells_btn.setFixedWidth(180)

        self.chat_btn = PyPushButton(
            f"Discussões",
            icon_path="cil-comment-bubble.png",
            button_color="#ff4747",
            text_color="white",
            icon_color="white",
            button_hover="#b22222",
            text_padding=45,
            border_radius=3
        )
        self.chat_btn.setMinimumHeight(40)
        self.chat_btn.setFixedWidth(180)

        self.btns_layout.addSpacerItem(self.h_spacer)
        self.btns_layout.addWidget(self.my_account_btn)
        self.btns_layout.addWidget(self.my_data_btn)
        self.btns_layout.addWidget(self.my_address_btn)
        self.btns_layout.addWidget(self.my_orders_btn)
        self.btns_layout.addWidget(self.products_btn)
        self.btns_layout.addWidget(self.my_sells_btn)
        self.btns_layout.addWidget(self.chat_btn)
        self.btns_layout.addSpacerItem(self.h_spacer)

        #############################################################################################
        # DATA PAGES
        #############################################################################################
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #ff4747")
        self.pages.setWindowTitle("data_pages")
        self.pages.setMinimumHeight(720)

        # ACCOUNT PAGE
        self.my_account_page = QFrame()
        self.my_account_page_layout = QVBoxLayout(self.my_account_page)

        self.account_label = QLabel("Minha Conta", parent=self.my_account_page)
        self.account_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.account_label.setMinimumWidth(300)
        self.account_label.move(200, 15)

        self.pages.addWidget(self.my_account_page)

        # MY DATA PAGE
        self.my_data_page = QFrame()
        self.my_data_page_layout = QVBoxLayout()

        self.my_data_label = QLabel("Meus Dados", parent=self.my_data_page)
        self.my_data_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.my_data_label.setMinimumWidth(300)
        self.my_data_label.move(200, 15)

        self.data_frame = QFrame(self.my_data_page)
        # self.data_frame.setStyleSheet("background-color: black")
        self.data_frame.move(200, 60)

        self.data_frame_layout = QVBoxLayout(self.data_frame)
        self.data_frame_layout.setSpacing(15)

        self.name = QLabel("Nome: Marlos")
        self.last_name = QLabel("Sobrenome: Balbino Nunes")
        self.user = QLabel("Usuário: marlos_balbino52")
        self.email = QLabel("E-mail: mbn2@ic.ufal.br")
        self.cpf = QLabel("CPF: ***.***.*** - 27")
        self.address = QLabel("Endereço mais usado: Rua Dom Joã...")

        self.data_frame_layout.addWidget(self.name)
        self.data_frame_layout.addWidget(self.last_name)
        self.data_frame_layout.addWidget(self.user)
        self.data_frame_layout.addWidget(self.email)
        self.data_frame_layout.addWidget(self.cpf)
        self.data_frame_layout.addWidget(self.address)

        self.pages.addWidget(self.my_data_page)

        self.my_address_page = QWidget()
        self.pages.addWidget(self.my_address_page)

        self.my_orders_page = QWidget()
        self.pages.addWidget(self.my_orders_page)

        # SELL PAGE
        self.content_area = QWidget()
        self.content_area_layout = QVBoxLayout(self.content_area)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("QScrollArea{border: none}")
        self.scroll_area.setWidgetResizable(True)

        self.v_scroll_bar = QScrollBar()
        self.v_scroll_bar.setStyleSheet("background-color: #bfbfbf")

        self.scroll_area.setVerticalScrollBar(self.v_scroll_bar)

        self.content_area_layout.addWidget(self.scroll_area)

        self.sell_page = QWidget()
        self.sell_page_layout = QVBoxLayout(self.sell_page)
        self.sell_page_layout.setContentsMargins(200, 60, 9, 9)

        self.sell_label = QLabel("Cadastrar Poduto", parent=self.sell_page)
        self.sell_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.sell_label.setMinimumWidth(300)
        self.sell_label.move(200, 15)

        self.sell_frame = QFrame()
        # self.sell_frame.setStyleSheet("background-color: black")
        self.sell_frame.setMaximumWidth(500)
        self.sell_frame.setMinimumHeight(750)
        # self.sell_frame.move(200, 60)

        self.sell_layout = QVBoxLayout(self.sell_frame)
        self.sell_layout.setSpacing(15)

        self.sell_page_layout.addWidget(self.sell_frame)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText("Nome do Produto*")
        self.line_edit1.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit1.setMinimumWidth(200)
        self.line_edit1.setMinimumHeight(40)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText("Quantidade*")
        self.line_edit2.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit2.setMinimumWidth(200)
        self.line_edit2.setMinimumHeight(40)

        self.line_edit3 = QLineEdit()
        self.line_edit3.setPlaceholderText("Título do Produto (como será mostrado no anúncio)*")
        self.line_edit3.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit3.setMinimumWidth(200)
        self.line_edit3.setMinimumHeight(40)

        self.line_edit4 = QLineEdit()
        self.line_edit4.setPlaceholderText("Categoria*")
        self.line_edit4.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit4.setMinimumWidth(200)
        self.line_edit4.setMinimumHeight(40)

        self.line_edit5 = QLineEdit()
        self.line_edit5.setPlaceholderText("Tags (separe as tags com vírgula)")
        self.line_edit5.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit5.setMinimumWidth(200)
        self.line_edit5.setMinimumHeight(40)

        self.line_edit6 = QLineEdit()
        self.line_edit6.setPlaceholderText("Lote*")
        self.line_edit6.setStyleSheet("""
                    QLineEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit6.setMinimumWidth(200)
        self.line_edit6.setMinimumHeight(40)

        self.line_edit7 = QTextEdit()
        self.line_edit7.setPlaceholderText("Escreva uma descrição completa do produto (no máximo 1000 caracteres)")
        self.line_edit7.setStyleSheet("""
                    QTextEdit{
                        border: none; color: black; 
                        background-color: #f3f4f4;
                        border: 1px solid "#ff4747";
                        padding: 8px;
                        border-radius: 3}""")
        self.line_edit7.setMinimumWidth(200)
        # self.line_edit7.setMinimumHeight(100)
        self.line_edit7.setMaximumHeight(170)

        self.register_btn_frame = QFrame()
        self.register_btn_frame.setFixedHeight(40)
        self.register_btn_frame_layout = QHBoxLayout(self.register_btn_frame)
        self.register_btn_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.register_btn = MyPushButton("Cadastrar", "#ff4747", text_color= "white", maximum_width=100, maximum_heigth=35)
        self.register_btn_frame_layout.addWidget(self.register_btn)

        self.sell_layout.addWidget(self.line_edit1)
        self.sell_layout.addWidget(self.line_edit2)
        self.sell_layout.addWidget(self.line_edit3)
        self.sell_layout.addWidget(self.line_edit4)
        self.sell_layout.addWidget(self.line_edit5)
        self.sell_layout.addWidget(self.line_edit6)
        self.sell_layout.addWidget(self.line_edit7)
        self.sell_layout.addWidget(self.register_btn_frame)
        self.sell_layout.addSpacerItem(self.v_spacer)

        self.scroll_area.setWidget(self.sell_page)

        self.pages.addWidget(self.content_area)

        # MY SELLS PAGE
        self.my_sells_page = QWidget()
        self.pages.addWidget(self.my_sells_page)

        self.chat_page = QWidget()
        self.pages.addWidget(self.chat_page)

        self.pages.setCurrentWidget(self.my_account_page)

        self.content_layout.addWidget(self.btns_frame)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addSpacerItem(self.v_spacer)
        
        self.verticalLayout_3.addWidget(self.content_frame)

        window.pages.addWidget(self.page)

        self.my_account_btn.clicked.connect(lambda: self.pages.setCurrentWidget(self.my_account_page))
        self.my_data_btn.clicked.connect(lambda: self.pages.setCurrentWidget(self.my_data_page))
        self.products_btn.clicked.connect(lambda: self.pages.setCurrentWidget(self.content_area))