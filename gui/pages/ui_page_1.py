""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from gui.widgets.my_push_button import MyPushButton
from qt_core import *

class UI_application_page_1(object):

    def __init__(self, window):
        if not window.pages.objectName():
            window.pages.setObjectName(u"application_pages")

        #############################################################################################
        # PAGE
        #############################################################################################
        self.page = QWidget()
        self.verticalLayout = QHBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0,0,0,0)  

        self.content_frame = QFrame()
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(9)

         #############################################################################################
        # TOP FRAME
        #############################################################################################
        self.top_frame = QFrame()
        self.top_frame.setMaximumHeight(50)
        # self.top_frame.setStyleSheet("background-color: grey")

        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(5,5,5,5)

        

        self.h_spacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.top_frame_layout.addSpacerItem(self.h_spacer)
        #self.top_frame_layout.addWidget(self.initial_page_btn)

        #############################################################################################
        # BOTTOM FRAME
        #############################################################################################
        self.bottom_frame = QFrame()
        # self.bottom_frame.setStyleSheet("background-color: blue")
        self.bottom_frame_layout = QHBoxLayout(self.bottom_frame)
        self.bottom_frame_layout.setSpacing(50)

        # LOGIN FRAME
        self.login_frame = QFrame()
        # self.login_frame.setStyleSheet("background-color: grey")
        self.login_frame.setMaximumHeight(509)
        self.login_frame.setMaximumWidth(400)

        self.login_layout = QVBoxLayout(self.login_frame)
        self.login_layout.setContentsMargins(9,9,9,9)

        self.login_label_frame = QFrame()
        # self.login_label_frame.setStyleSheet("background-color: green")
        self.login_label_frame.setMaximumHeight(150)
        self.login_label_layout = QHBoxLayout(self.login_label_frame)
        self.login_label_layout.setContentsMargins(0,0,0,0)
        self.login_label = QLabel("Já tenho cadastro.")
        self.login_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.login_label_layout.addSpacerItem(self.h_spacer2)
        self.login_label_layout.addWidget(self.login_label)
        self.login_label_layout.addSpacerItem(self.h_spacer2)     

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText("E-mail*")
        self.line_edit1.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit1.setMaximumWidth(400)
        self.line_edit1.setMinimumHeight(40)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText("Senha*")
        self.line_edit2.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit2.setMaximumWidth(400)
        self.line_edit2.setMinimumHeight(40)

        self.login_btn_frame = QFrame()
        self.login_btn_frame.setMaximumHeight(150)
        self.login_btn_frame_layout = QHBoxLayout(self.login_btn_frame)
        self.login_btn_frame_layout.setContentsMargins(0,0,0,0)
        self.login_btn = MyPushButton("Fazer login", "#ff4747", maximum_width=100, maximum_heigth=35)
        self.login_btn_frame_layout.addWidget(self.login_btn)

        self.login_layout.addWidget(self.login_label_frame)
        self.login_layout.addWidget(self.line_edit1)
        self.login_layout.addWidget(self.line_edit2)
        self.login_layout.addWidget(self.login_btn_frame)

        # REGISTER FRAME
        self.register_frame = QFrame()
        # self.register_frame.setStyleSheet("background-color: grey")
        self.register_frame.setMaximumHeight(509)
        self.register_frame.setMaximumWidth(400)

        self.register_layout = QVBoxLayout(self.register_frame)
        # self.register_layout.setContentsMargins(0,0,0,0)

        self.register_label_frame = QFrame()
        # self.register_label_frame.setStyleSheet("background-color: green")
        self.register_label_frame.setMaximumHeight(150)
        self.register_label_layout = QHBoxLayout(self.register_label_frame)
        self.register_label_layout.setContentsMargins(0,0,0,0)
        self.register_label = QLabel("Quero me cadastrar.")
        self.register_label.setStyleSheet("color: #ff4747; font: bold 16pt")
        self.register_label_layout.addSpacerItem(self.h_spacer2)
        self.register_label_layout.addWidget(self.register_label)
        self.register_label_layout.addSpacerItem(self.h_spacer2)     

        self.line_edit3 = QLineEdit()
        self.line_edit3.setPlaceholderText("E-mail*")
        self.line_edit3.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit3.setMaximumWidth(400)
        self.line_edit3.setMinimumHeight(40)

        self.line_edit4 = QLineEdit()
        self.line_edit4.setPlaceholderText("Crie sua senha*")
        self.line_edit4.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit4.setMaximumWidth(400)
        self.line_edit4.setMinimumHeight(40)

        self.line_edit5 = QLineEdit()
        self.line_edit5.setPlaceholderText("Confirme sua senha*")
        self.line_edit5.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit5.setMaximumWidth(400)
        self.line_edit5.setMinimumHeight(40)

        self.line_edit6 = QLineEdit()
        self.line_edit6.setPlaceholderText("CPF*")
        self.line_edit6.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit6.setMaximumWidth(400)
        self.line_edit6.setMinimumHeight(40)

        self.line_edit7 = QLineEdit()
        self.line_edit7.setPlaceholderText("CEP*")
        self.line_edit7.setStyleSheet("""
            QLineEdit{
                border: none; color: black; 
                background-color: #f3f4f4;
                border: 1px solid "#ff4747";
                padding: 8px;
                border-radius: 3}""")
        self.line_edit7.setMaximumWidth(400)
        self.line_edit7.setMinimumHeight(40)

        self.register_btn_frame = QFrame()
        self.register_btn_frame.setMaximumHeight(100)
        self.register_btn_frame_layout = QHBoxLayout(self.register_btn_frame)
        self.register_btn_frame_layout.setContentsMargins(0,0,0,0)
        self.register_btn = MyPushButton("Cadastrar", "#ff4747", maximum_width=100, maximum_heigth=35)        
        self.register_btn_frame_layout.addWidget(self.register_btn)


        self.register_layout.addWidget(self.register_label_frame)
        self.register_layout.addWidget(self.line_edit3)
        self.register_layout.addWidget(self.line_edit4)
        self.register_layout.addWidget(self.line_edit5)
        self.register_layout.addWidget(self.line_edit6)
        self.register_layout.addWidget(self.line_edit7)
        self.register_layout.addWidget(self.register_btn_frame)

        self.bottom_frame_layout.addWidget(self.login_frame)
        self.bottom_frame_layout.addWidget(self.register_frame)
        self.content_layout.addWidget(self.top_frame)
        self.content_layout.addWidget(self.bottom_frame)

        self.verticalLayout.addWidget(self.content_frame)
        window.pages.addWidget(self.page)

        self.login_btn.clicked.connect(lambda: window.account_btn.show())
        self.login_btn.clicked.connect(lambda: window.login_btn.hide())
        self.login_btn.clicked.connect(lambda: window.pages.setCurrentWidget(window.ui_page_2.page))

 