from qt_core import *
from my_widgets import PyPushButton


class Categories(QFrame):

    hovered = Signal()
    leave = Signal()

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setMinimumWidth(280)
        self.setFixedHeight(458)
        # self.setStyleSheet("background-color: grey")

        self.categories = QFrame(self)
        self.categories.setStyleSheet("""
            QFrame{
            background-color: #ff4747; 
            border-radius: 10px}
        """)
        self.categories.setFixedWidth(280)
        self.categories.setFixedHeight(298)
        self.categories_layout = QVBoxLayout(self.categories)
        self.categories_layout.setContentsMargins(9, 9, 0, 9)
        self.categories_layout.setSpacing(0)

        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)          

        #############################################################################################
        # CATEGORIES BUTTONS
        #############################################################################################
        self.electronics_btn = CustomPyPushButton(
            "Eletrônicos",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-input-power.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf",
        )
        self.hardware_btn = CustomPyPushButton(
            "Hardware",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-hardware.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )
        self.peripherals_btn = CustomPyPushButton(
            "Periféricos",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-mouse.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )
        self.computers_btn = CustomPyPushButton(
            "Computadores e Notebooks",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-devices.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )
        self.tvs_monitors_btn = CustomPyPushButton(
            "Monitores e TVs",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-tvs.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )
        self.games_btn = CustomPyPushButton(
            "Games",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-gamepad.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )
        self.smartphones_btn = CustomPyPushButton(
            "Smartphones",
            text_color="white",
            icon_color="white",
            button_color="#ff4747",
            button_pressed="#eeeeee",
            icon_path="cil-screen-smartphone.png",
            top_left_radius=10,
            bottom_left_radius=10,
            border_size=0,
            actived_color="#dfdfdf"
        )

        self.categories_layout.addWidget(self.electronics_btn)
        self.categories_layout.addWidget(self.hardware_btn)
        self.categories_layout.addWidget(self.peripherals_btn)
        self.categories_layout.addWidget(self.computers_btn)
        self.categories_layout.addWidget(self.tvs_monitors_btn)
        self.categories_layout.addWidget(self.games_btn)
        self.categories_layout.addWidget(self.smartphones_btn)
        self.categories_layout.addSpacerItem(self.v_spacer)

        for btn in self.categories.findChildren(QPushButton):
            btn.hovered.connect(self.reset_hover)

        #############################################################################################
        # CATEGORIES LIST
        #############################################################################################
        filter_frame = FilterFrame(self)
        filter_frame.move(280, 0)

        for btn, frame in zip(self.categories.findChildren(CustomPyPushButton), filter_frame.findChildren(QFrame)):
            #frame.setFixedHeight(filter_frame_height)
            btn.hovered.connect(filter_frame.hide_all)
            btn.hovered.connect(frame.show)          

    def enterEvent(self, event):
        self.setFixedWidth(560)         

    def leaveEvent(self, event):
        self.setFixedWidth(280)
        self.reset_hover()  

    def reset_hover(self):        
        for btn in self.categories.findChildren(QPushButton):            
            try:
                btn.set_active(False)
            except:
                pass

class FilterFrame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setStyleSheet("background-color: green")
        self.setFixedWidth(280)   
        self.setMinimumHeight(458)
        #self.setFixedHeight(300)
        self.v_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)     

        self.electronics = [
            "Cabos e Adaptadores",
            "Carregadores",
            "Baterias",
            "Receptores de TV",
            "Projetores",
            "Amplificadores de Áudio",
            "Cêmeras Digitais",
            "Drones",
            "Acessórios para Foto",
            "Fones de Ouvido",
            "Microfones",
        ]
        self.hardware = [
            "Processadores",
            "Placa Mãe",
            "Memórias",
            "Fontes",
            "Placas de Vídeo",
            "Disco Rígido",
            "SSDs",
            "Gabinetes",
            "Coolers"
        ]
        self.peripherals = [
            "Mouse",
            "Teclado",
            "Headset e Headphone",
            "Mousepad",
            "Impressoras",
            "Webcams",
            "Pendrives",
            "Gamepads"
        ]
        self.computers = [
            "Computadores",
            "Computadores Gamer",
            "Notebooks",
            "Notebooks Gamer",
            "Refrigeração e Bases",
            "Carregadores e Fontes"
        ]
        self.tvs_monitors = [
            "Monitores",
            "Monitores Gamer",
            "Smart TVs",
            "TV 4k",
            "TV 8k",
            "Acessórios para TV",
            "Monitor TV"
        ]
        self.games = [
            "Jogos de PC",
            "Jogos de XBOX",
            "Jogos de PS4 e PS5",
            "Consoles",
            "Controles",
            "Acessórios"
        ]
        self.smartphones = [
            "Samsung",
            "Xiaomi",
            "LG",
            "iPhone",
            "Asus",
            "Motorola",
            "Acessórios"
        ]

        for category in [
            self.electronics, 
            self.hardware,
            self.peripherals,
            self.computers,
            self.tvs_monitors,
            self.games,
            self.smartphones]:

            frame = MFrame(self)
            frame.category = category
            frame.setStyleSheet("""
                background-color: "#dfdfdf";
                border-radius: 10px
            """)
            frame.setFixedWidth(280)
            
            #frame.move(0, pos[i])
            frame.hide()

            layout = QVBoxLayout(frame)
            layout.setSpacing(0)

            for item in category:
                item_btn = ListButton()
                item_btn.setText(item)
                layout.addWidget(item_btn)
            # layout.addSpacerItem(self.v_spacer)

    def hide_all(self):
        for item in self.findChildren(QFrame):
            item.hide()

class MFrame(QFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.category = None
    
    def teste(self):
        return len(self.category) * 40 + 18


class CustomPyPushButton(PyPushButton):

    hovered = Signal()
    leave = Signal()

    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "#c3ccdf",
        icon_path = "",
        icon_color = "#c3ccdf",
        button_color = "#44475a",
        button_hover = "#4f5368",
        button_pressed = "#282a36",
        actived_color = "#282a36", # defaul: #4f5368
        border_color = "#c3ccdf", # defaul: #282a36
        border_position = "left", # defaul: "right"       
        border_size = 3, # defaul: 5
        is_active = False,        
        parent = None,
        top_left_radius = 0,
        top_right_radius = 0,
        bottom_left_radius = 0,
        bottom_right_radius = 0,
        border_radius = 0
    ):
        super().__init__(
        text = text,
        height = height,
        minimum_width = minimum_width,
        text_padding = text_padding,
        text_color = text_color,
        icon_path = icon_path,
        icon_color = icon_color,
        button_color = button_color,
        button_hover = button_hover,
        button_pressed = button_pressed,
        actived_color = actived_color, # defaul: #4f5368
        border_color = border_color, # defaul: #282a36
        border_position = border_position, # defaul: "right"       
        border_size = border_size, # defaul: 5
        is_active = is_active,        
        parent = parent,
        top_left_radius = top_left_radius,
        top_right_radius = top_right_radius,
        bottom_left_radius = bottom_left_radius,
        bottom_right_radius = bottom_right_radius,
        border_radius = border_radius
    )

    def set_active(self, set_active):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            button_color = self.button_color,
            button_hover = self.button_hover,
            button_pressed = self.button_pressed,
            actived_color = self.actived_color,
            border_color = self.border_color,
            border_position = self.border_position,
            border_size = self.border_size,
            top_left_radius=self.top_left_radius,
            top_right_radius=self.top_right_radius,
            bottom_left_radius=self.bottom_left_radius,
            bottom_right_radius=self.bottom_right_radius,
            is_active = set_active
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "c3ccdf",
        button_color = "#44475a",
        button_hover = "#4f5368",
        button_pressed = "#282a36",
        actived_color = "#4f5368",
        border_color = "#282a36",
        border_position = "right",
        border_size = 5,
        top_left_radius=0,
        top_right_radius=0,
        bottom_left_radius=0,
        bottom_right_radius=0,
        is_active = False
    ):
        
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            border-top-left-radius: {top_left_radius}px;
            border-top-right-radius: {top_right_radius}px;
            border-bottom-left-radius: {bottom_left_radius}px;
            border-bottom-right-radius: {bottom_right_radius}px;
        }}
        QPushButton:pressed {{
            background-color: {button_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {actived_color};
            border-{border_position}: {border_size}px solid {border_color};
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def enterEvent(self, event):
        self.hovered.emit()
        self.set_active(True)

    def leaveEvent(self, event):
        self.leave.emit()

class ListButton(QPushButton):
    
    hovered = Signal()
    leave = Signal()

    _style = """
            background-color: transparent;
            color: black;
            text-align: left;
            border: none;
            padding-left: 55px;
        """

    def __init__(self):  

        super().__init__()
        self.setFixedHeight(40)
        self.setStyleSheet(self._style)

        self.hovered.connect(self.paint_text)
        self.leave.connect(self.unpaint_text)

    def paint_text(self):
        self.setStyleSheet(self._style + "color: #ff4747; text-decoration: underline;")
    
    def unpaint_text(self):
        self.setStyleSheet(self._style + "color: black")
    
    def enterEvent(self, event):
        self.hovered.emit()

    def leaveEvent(self, event):
        self.leave.emit()
