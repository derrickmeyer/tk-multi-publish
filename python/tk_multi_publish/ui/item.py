# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created: Tue Apr  2 23:53:15 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Item(object):
    def setupUi(self, Item):
        Item.setObjectName("Item")
        Item.resize(286, 38)
        self.horizontalLayout = QtGui.QHBoxLayout(Item)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_cb = QtGui.QCheckBox(Item)
        self.select_cb.setMinimumSize(QtCore.QSize(0, 0))
        self.select_cb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_cb.setText("")
        self.select_cb.setObjectName("select_cb")
        self.verticalLayout.addWidget(self.select_cb)
        spacerItem = QtGui.QSpacerItem(10, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.details_label = QtGui.QLabel(Item)
        self.details_label.setMinimumSize(QtCore.QSize(0, 0))
        self.details_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.details_label.setMargin(1)
        self.details_label.setObjectName("details_label")
        self.horizontalLayout.addWidget(self.details_label)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Item)
        QtCore.QMetaObject.connectSlotsByName(Item)

    def retranslateUi(self, Item):
        Item.setWindowTitle(QtGui.QApplication.translate("Item", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.details_label.setText(QtGui.QApplication.translate("Item", "<b>Item Name</b><br>Description...", None, QtGui.QApplication.UnicodeUTF8))

