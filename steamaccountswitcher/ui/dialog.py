# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(196, 177)
        Dialog.setMaximumSize(QSize(360, 240))
        icon = QIcon()
        iconThemeName = u"steam"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.accountEdit = QLineEdit(Dialog)
        self.accountEdit.setObjectName(u"accountEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountEdit.sizePolicy().hasHeightForWidth())
        self.accountEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.accountEdit, 2, 0, 1, 1)

        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout.addWidget(self.addButton, 2, 1, 1, 1)

        self.loginButton = QPushButton(Dialog)
        self.loginButton.setObjectName(u"loginButton")

        self.gridLayout.addWidget(self.loginButton, 1, 0, 1, 1)

        self.accountsBox = QComboBox(Dialog)
        self.accountsBox.setObjectName(u"accountsBox")

        self.gridLayout.addWidget(self.accountsBox, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.removeButton = QPushButton(Dialog)
        self.removeButton.setObjectName(u"removeButton")

        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        QWidget.setTabOrder(self.accountsBox, self.loginButton)
        QWidget.setTabOrder(self.loginButton, self.removeButton)
        QWidget.setTabOrder(self.removeButton, self.accountEdit)
        QWidget.setTabOrder(self.accountEdit, self.addButton)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Steam Account Switcher", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.removeButton.setText(QCoreApplication.translate("Dialog", u"Remove", None))
    # retranslateUi

