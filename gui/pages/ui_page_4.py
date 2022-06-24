""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from ctypes import alignment
from copy import deepcopy
from turtle import width

from numpy import spacing
from qt_core import *


class UI_application_page_4(object):
    def __init__(self, window):
        if not window.pages.objectName():
            window.pages.setObjectName(u"application_pages")

        self.page = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page)
        
        self.teste_frame = QFrame()
        self.teste_frame.setStyleSheet("background-color: grey")

        self.popup_frame = QFrame(self.teste_frame)
        self.popup_frame.setStyleSheet("background-color: #707070")
        self.popup_frame.setMinimumWidth(50)
        self.popup_frame.setMinimumHeight(50)
        self.popup_frame.resize(200, 200)


        self.btn = QPushButton("gdfgsdfgsdfgsdfglksdjfgçlskdgjsçdlg")
        
        self.verticalLayout_3.addWidget(self.teste_frame)
        #self.verticalLayout_3.addWidget(self.popup_frame)
        self.verticalLayout_3.addWidget(self.btn)
        window.pages.addWidget(self.page)