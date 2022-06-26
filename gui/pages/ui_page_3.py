""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from gui.widgets.py_push_button import PyPushButton
from gui.widgets.my_push_button import MyPushButton

from qt_core import *


class UI_application_page_3(object):

    def __init__(self, window):
        if not window.pages.objectName():
            window.pages.setObjectName(u"application_pages")

        #############################################################################################
        # PAGE
        #############################################################################################
        self.page = QWidget()
        self.verticalLayout = QHBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        window.pages.addWidget(self.page)
