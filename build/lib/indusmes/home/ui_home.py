# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(816, 744)
        MainWindow.setMinimumSize(QSize(480, 640))
        MainWindow.setMaximumSize(QSize(5000, 5000))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(36, 31, 49, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(54, 46, 73, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(45, 38, 61, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(18, 15, 24, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(24, 21, 33, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(192, 97, 203, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush10 = QBrush(QColor(145, 145, 145, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setMinimumSize(QSize(480, 640))
        self.MainWidget.setMaximumSize(QSize(5000, 5000))
        self.MainWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.MainWidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(480, 40))
        self.menu.setMaximumSize(QSize(5000, 40))
        self.menu.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.horizontalLayout = QHBoxLayout(self.menu)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.profileButton = QPushButton(self.menu)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setMinimumSize(QSize(40, 30))
        self.profileButton.setMaximumSize(QSize(40, 30))
        icon = QIcon()
        icon.addFile(u":/assets/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileButton.setIcon(icon)
        self.profileButton.setIconSize(QSize(30, 30))
        self.profileButton.setCheckable(False)
        self.profileButton.setChecked(False)
        self.profileButton.setFlat(True)

        self.horizontalLayout.addWidget(self.profileButton)

        self.current_value_text = QLabel(self.menu)
        self.current_value_text.setObjectName(u"current_value_text")
        self.current_value_text.setFont(font)
        self.current_value_text.setAlignment(Qt.AlignCenter)
        self.current_value_text.setMargin(4)

        self.horizontalLayout.addWidget(self.current_value_text)

        self.settingsButton = QPushButton(self.menu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(40, 30))
        self.settingsButton.setMaximumSize(QSize(40, 30))
        icon1 = QIcon()
        icon1.addFile(u":/assets/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon1)
        self.settingsButton.setIconSize(QSize(30, 30))
        self.settingsButton.setCheckable(False)
        self.settingsButton.setFlat(True)

        self.horizontalLayout.addWidget(self.settingsButton)


        self.verticalLayout.addWidget(self.menu)

        self.main_section = QStackedWidget(self.MainWidget)
        self.main_section.setObjectName(u"main_section")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_section.sizePolicy().hasHeightForWidth())
        self.main_section.setSizePolicy(sizePolicy)
        self.main_section.setMinimumSize(QSize(480, 600))
        self.main_section.setMaximumSize(QSize(5000, 5000))
        font1 = QFont()
        font1.setFamilies([u"Fira Sans Semi-Light"])
        font1.setPointSize(10)
        font1.setKerning(True)
        self.main_section.setFont(font1)
        self.main_section.setStyleSheet(u"")
        self.main_section.setFrameShape(QFrame.NoFrame)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy1)
        self.login.setMinimumSize(QSize(480, 600))
        self.login.setMaximumSize(QSize(5000, 5000))
        self.login.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.login)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 0)
        self.login_label = QLabel(self.login)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMinimumSize(QSize(0, 40))
        self.login_label.setMaximumSize(QSize(5000, 40))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.login_label.setFont(font2)
        self.login_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.login_label, 0, Qt.AlignTop)

        self.groupBox = QGroupBox(self.login)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_label = QLabel(self.groupBox)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.username_label.setFont(font3)
        self.username_label.setStyleSheet(u"")
        self.username_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.username_label)

        self.username_text = QLineEdit(self.groupBox)
        self.username_text.setObjectName(u"username_text")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(16)
        self.username_text.setFont(font4)
        self.username_text.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.username_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.username_text)

        self.password_label = QLabel(self.groupBox)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(16777215, 30))
        self.password_label.setFont(font3)

        self.verticalLayout_4.addWidget(self.password_label)

        self.password_text = QLineEdit(self.groupBox)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setFont(font4)
        self.password_text.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.password_text.setCursorPosition(0)
        self.password_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.password_text)

        self.message = QLabel(self.groupBox)
        self.message.setObjectName(u"message")
        self.message.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.verticalLayout_4.addWidget(self.message)

        self.login_button = QPushButton(self.groupBox)
        self.login_button.setObjectName(u"login_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy2)
        self.login_button.setMinimumSize(QSize(0, 40))
        self.login_button.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.login_button.setFont(font5)
        self.login_button.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"")
        self.login_button.setFlat(False)

        self.verticalLayout_4.addWidget(self.login_button)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.main_section.addWidget(self.login)
        self.job_list = QWidget()
        self.job_list.setObjectName(u"job_list")
        self.job_list.setMinimumSize(QSize(480, 600))
        self.job_list.setMaximumSize(QSize(5000, 5000))
        self.job_list.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.job_list)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.job_list_label = QLabel(self.job_list)
        self.job_list_label.setObjectName(u"job_list_label")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(24)
        self.job_list_label.setFont(font6)
        self.job_list_label.setStyleSheet(u"")
        self.job_list_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.job_list_label)

        self.job_list_message = QLabel(self.job_list)
        self.job_list_message.setObjectName(u"job_list_message")
        self.job_list_message.setFont(font4)
        self.job_list_message.setStyleSheet(u"color: rgb(224, 27, 36);")
        self.job_list_message.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.job_list_message)

        self.job_area = QScrollArea(self.job_list)
        self.job_area.setObjectName(u"job_area")
        self.job_area.setStyleSheet(u"")
        self.job_area.setWidgetResizable(True)
        self.job_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.job_area_contents = QWidget()
        self.job_area_contents.setObjectName(u"job_area_contents")
        self.job_area_contents.setGeometry(QRect(0, 0, 814, 625))
        self.job_area_contents.setStyleSheet(u"")
        self.job_area.setWidget(self.job_area_contents)

        self.verticalLayout_2.addWidget(self.job_area)

        self.main_section.addWidget(self.job_list)
        self.job_details = QWidget()
        self.job_details.setObjectName(u"job_details")
        self.job_details.setMinimumSize(QSize(480, 600))
        self.job_details.setMaximumSize(QSize(5000, 5000))
        self.verticalLayout_5 = QVBoxLayout(self.job_details)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.job_details_label = QLabel(self.job_details)
        self.job_details_label.setObjectName(u"job_details_label")
        self.job_details_label.setMinimumSize(QSize(0, 30))
        self.job_details_label.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(18)
        font7.setBold(False)
        self.job_details_label.setFont(font7)
        self.job_details_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.job_details_label)

        self.job_details_area = QWidget(self.job_details)
        self.job_details_area.setObjectName(u"job_details_area")
        font8 = QFont()
        font8.setPointSize(14)
        self.job_details_area.setFont(font8)
        self.horizontalLayout_2 = QHBoxLayout(self.job_details_area)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.job_info_layout = QVBoxLayout()
        self.job_info_layout.setObjectName(u"job_info_layout")
        self.job_info_layout.setContentsMargins(0, -1, -1, -1)
        self.job_id_label = QLabel(self.job_details_area)
        self.job_id_label.setObjectName(u"job_id_label")
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(11)
        self.job_id_label.setFont(font9)

        self.job_info_layout.addWidget(self.job_id_label)

        self.job_id_text = QLabel(self.job_details_area)
        self.job_id_text.setObjectName(u"job_id_text")
        self.job_id_text.setMinimumSize(QSize(0, 16))
        self.job_id_text.setFont(font8)
        self.job_id_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.job_id_text.setMargin(2)

        self.job_info_layout.addWidget(self.job_id_text)

        self.material_label = QLabel(self.job_details_area)
        self.material_label.setObjectName(u"material_label")
        self.material_label.setFont(font9)

        self.job_info_layout.addWidget(self.material_label)

        self.material_text = QLabel(self.job_details_area)
        self.material_text.setObjectName(u"material_text")
        self.material_text.setMinimumSize(QSize(0, 16))
        self.material_text.setFont(font8)
        self.material_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.material_text.setMargin(2)

        self.job_info_layout.addWidget(self.material_text)

        self.quantity_label = QLabel(self.job_details_area)
        self.quantity_label.setObjectName(u"quantity_label")
        self.quantity_label.setFont(font9)

        self.job_info_layout.addWidget(self.quantity_label)

        self.quantity_text = QLabel(self.job_details_area)
        self.quantity_text.setObjectName(u"quantity_text")
        self.quantity_text.setMinimumSize(QSize(0, 16))
        self.quantity_text.setFont(font8)
        self.quantity_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.quantity_text.setMargin(2)

        self.job_info_layout.addWidget(self.quantity_text)

        self.good_quantity_label = QLabel(self.job_details_area)
        self.good_quantity_label.setObjectName(u"good_quantity_label")
        self.good_quantity_label.setFont(font9)

        self.job_info_layout.addWidget(self.good_quantity_label)

        self.good_quantity_text = QLabel(self.job_details_area)
        self.good_quantity_text.setObjectName(u"good_quantity_text")
        self.good_quantity_text.setMinimumSize(QSize(0, 16))
        self.good_quantity_text.setFont(font8)
        self.good_quantity_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.good_quantity_text.setMargin(2)

        self.job_info_layout.addWidget(self.good_quantity_text)

        self.reject_quantity_label = QLabel(self.job_details_area)
        self.reject_quantity_label.setObjectName(u"reject_quantity_label")
        self.reject_quantity_label.setFont(font9)

        self.job_info_layout.addWidget(self.reject_quantity_label)

        self.reject_quantity_text = QLabel(self.job_details_area)
        self.reject_quantity_text.setObjectName(u"reject_quantity_text")
        self.reject_quantity_text.setMinimumSize(QSize(0, 16))
        self.reject_quantity_text.setFont(font8)
        self.reject_quantity_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.reject_quantity_text.setMargin(2)

        self.job_info_layout.addWidget(self.reject_quantity_text)

        self.date_label = QLabel(self.job_details_area)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font9)

        self.job_info_layout.addWidget(self.date_label)

        self.date_text = QLabel(self.job_details_area)
        self.date_text.setObjectName(u"date_text")
        self.date_text.setMinimumSize(QSize(0, 16))
        self.date_text.setFont(font8)
        self.date_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.date_text.setMargin(2)

        self.job_info_layout.addWidget(self.date_text)

        self.status_label = QLabel(self.job_details_area)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font9)

        self.job_info_layout.addWidget(self.status_label)

        self.status_text = QLabel(self.job_details_area)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setMinimumSize(QSize(0, 16))
        font10 = QFont()
        font10.setPointSize(12)
        self.status_text.setFont(font10)
        self.status_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.status_text.setMargin(2)

        self.job_info_layout.addWidget(self.status_text)

        self.instructions_label = QLabel(self.job_details_area)
        self.instructions_label.setObjectName(u"instructions_label")
        self.instructions_label.setFont(font9)

        self.job_info_layout.addWidget(self.instructions_label)

        self.instruction_text = QTextBrowser(self.job_details_area)
        self.instruction_text.setObjectName(u"instruction_text")
        font11 = QFont()
        font11.setFamilies([u"Roboto"])
        font11.setPointSize(12)
        self.instruction_text.setFont(font11)
        self.instruction_text.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.job_info_layout.addWidget(self.instruction_text)

        self.job_info_layout.setStretch(15, 1)

        self.horizontalLayout_2.addLayout(self.job_info_layout)

        self.job_actions_layout = QVBoxLayout()
        self.job_actions_layout.setSpacing(24)
        self.job_actions_layout.setObjectName(u"job_actions_layout")
        self.start_job_btn = QPushButton(self.job_details_area)
        self.start_job_btn.setObjectName(u"start_job_btn")
        self.start_job_btn.setMinimumSize(QSize(0, 40))
        self.start_job_btn.setFont(font11)
        self.start_job_btn.setStyleSheet(u"background-color: rgb(26, 95, 120);")

        self.job_actions_layout.addWidget(self.start_job_btn)

        self.progress_btn = QPushButton(self.job_details_area)
        self.progress_btn.setObjectName(u"progress_btn")
        self.progress_btn.setMinimumSize(QSize(0, 40))
        self.progress_btn.setFont(font11)
        self.progress_btn.setStyleSheet(u"background-color: rgb(26, 95, 120);")

        self.job_actions_layout.addWidget(self.progress_btn)

        self.rejects_btn = QPushButton(self.job_details_area)
        self.rejects_btn.setObjectName(u"rejects_btn")
        self.rejects_btn.setMinimumSize(QSize(0, 40))
        self.rejects_btn.setFont(font11)
        self.rejects_btn.setStyleSheet(u"background-color: rgb(26, 95, 120);")

        self.job_actions_layout.addWidget(self.rejects_btn)

        self.complete_job_btn = QPushButton(self.job_details_area)
        self.complete_job_btn.setObjectName(u"complete_job_btn")
        self.complete_job_btn.setMinimumSize(QSize(0, 40))
        self.complete_job_btn.setFont(font11)
        self.complete_job_btn.setStyleSheet(u"background-color: rgb(26, 95, 120);")
        self.complete_job_btn.setFlat(False)

        self.job_actions_layout.addWidget(self.complete_job_btn)

        self.job_list_btn = QPushButton(self.job_details_area)
        self.job_list_btn.setObjectName(u"job_list_btn")
        self.job_list_btn.setMinimumSize(QSize(0, 40))
        self.job_list_btn.setFont(font11)
        self.job_list_btn.setStyleSheet(u"background-color: rgb(26, 95, 120);")

        self.job_actions_layout.addWidget(self.job_list_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.job_actions_layout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.job_actions_layout)


        self.verticalLayout_5.addWidget(self.job_details_area)

        self.main_section.addWidget(self.job_details)

        self.verticalLayout.addWidget(self.main_section)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        self.main_section.setCurrentIndex(1)
        self.complete_job_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IndusWorks", None))
        self.profileButton.setText("")
        self.current_value_text.setText("")
        self.settingsButton.setText("")
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Login to IndusWorks", None))
        self.groupBox.setTitle("")
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.username_text.setPlaceholderText("")
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.password_text.setInputMask("")
        self.password_text.setPlaceholderText("")
        self.message.setText("")
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.job_list_label.setText(QCoreApplication.translate("MainWindow", u"Job List", None))
        self.job_list_message.setText("")
        self.job_details_label.setText(QCoreApplication.translate("MainWindow", u"Job Details", None))
        self.job_id_label.setText(QCoreApplication.translate("MainWindow", u"Job ID:", None))
        self.job_id_text.setText("")
        self.material_label.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.material_text.setText("")
        self.quantity_label.setText(QCoreApplication.translate("MainWindow", u"Target Quantity:", None))
        self.quantity_text.setText("")
        self.good_quantity_label.setText(QCoreApplication.translate("MainWindow", u"Good Quantity:", None))
        self.good_quantity_text.setText("")
        self.reject_quantity_label.setText(QCoreApplication.translate("MainWindow", u"Reject Quantity:", None))
        self.reject_quantity_text.setText("")
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Target Start Date:", None))
        self.date_text.setText("")
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Current Status:", None))
        self.status_text.setText("")
        self.instructions_label.setText(QCoreApplication.translate("MainWindow", u"Instructions:", None))
        self.instruction_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.start_job_btn.setText(QCoreApplication.translate("MainWindow", u"Start Job", None))
        self.progress_btn.setText(QCoreApplication.translate("MainWindow", u"Report Progress", None))
        self.rejects_btn.setText(QCoreApplication.translate("MainWindow", u"Report Rejects", None))
        self.complete_job_btn.setText(QCoreApplication.translate("MainWindow", u"Complete Job", None))
        self.job_list_btn.setText(QCoreApplication.translate("MainWindow", u"Job List", None))
    # retranslateUi
