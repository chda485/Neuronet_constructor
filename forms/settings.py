# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Form.setPalette(palette)
        self.list = QtWidgets.QComboBox(Form)
        self.list.setGeometry(QtCore.QRect(160, 20, 121, 22))
        self.list.setObjectName("list")
        self.list_label = QtWidgets.QLabel(Form)
        self.list_label.setGeometry(QtCore.QRect(20, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.list_label.setFont(font)
        self.list_label.setObjectName("list_label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 50, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.par1_label = QtWidgets.QLabel(Form)
        self.par1_label.setGeometry(QtCore.QRect(20, 74, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par1_label.setFont(font)
        self.par1_label.setObjectName("par1_label")
        self.par2_label = QtWidgets.QLabel(Form)
        self.par2_label.setGeometry(QtCore.QRect(20, 110, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par2_label.setFont(font)
        self.par2_label.setObjectName("par2_label")
        self.par1 = QtWidgets.QLineEdit(Form)
        self.par1.setGeometry(QtCore.QRect(190, 73, 91, 20))
        self.par1.setObjectName("par1")
        self.par2 = QtWidgets.QLineEdit(Form)
        self.par2.setGeometry(QtCore.QRect(190, 109, 91, 20))
        self.par2.setObjectName("par2")
        self.par3 = QtWidgets.QLineEdit(Form)
        self.par3.setGeometry(QtCore.QRect(190, 149, 91, 20))
        self.par3.setObjectName("par3")
        self.buttons = QtWidgets.QDialogButtonBox(Form)
        self.buttons.setGeometry(QtCore.QRect(110, 460, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttons.setFont(font)
        self.buttons.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttons.setObjectName("buttons")
        self.par3_label = QtWidgets.QLabel(Form)
        self.par3_label.setGeometry(QtCore.QRect(20, 150, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par3_label.setFont(font)
        self.par3_label.setObjectName("par3_label")
        self.par4_label = QtWidgets.QLabel(Form)
        self.par4_label.setGeometry(QtCore.QRect(20, 190, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par4_label.setFont(font)
        self.par4_label.setObjectName("par4_label")
        self.par5_label = QtWidgets.QLabel(Form)
        self.par5_label.setGeometry(QtCore.QRect(20, 230, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par5_label.setFont(font)
        self.par5_label.setObjectName("par5_label")
        self.par4 = QtWidgets.QLineEdit(Form)
        self.par4.setGeometry(QtCore.QRect(190, 189, 91, 20))
        self.par4.setObjectName("par4")
        self.par5 = QtWidgets.QLineEdit(Form)
        self.par5.setGeometry(QtCore.QRect(190, 229, 91, 20))
        self.par5.setObjectName("par5")
        self.par6 = QtWidgets.QLineEdit(Form)
        self.par6.setGeometry(QtCore.QRect(190, 269, 91, 20))
        self.par6.setObjectName("par6")
        self.par6_label = QtWidgets.QLabel(Form)
        self.par6_label.setGeometry(QtCore.QRect(20, 270, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par6_label.setFont(font)
        self.par6_label.setObjectName("par6_label")
        self.par7_label = QtWidgets.QLabel(Form)
        self.par7_label.setGeometry(QtCore.QRect(20, 310, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par7_label.setFont(font)
        self.par7_label.setObjectName("par7_label")
        self.bool_check1 = QtWidgets.QCheckBox(Form)
        self.bool_check1.setGeometry(QtCore.QRect(225, 110, 16, 17))
        self.bool_check1.setText("")
        self.bool_check1.setObjectName("bool_check1")
        self.par8_label = QtWidgets.QLabel(Form)
        self.par8_label.setGeometry(QtCore.QRect(20, 350, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par8_label.setFont(font)
        self.par8_label.setObjectName("par8_label")
        self.par8 = QtWidgets.QLineEdit(Form)
        self.par8.setGeometry(QtCore.QRect(190, 349, 91, 20))
        self.par8.setObjectName("par8")
        self.par9_label = QtWidgets.QLabel(Form)
        self.par9_label.setGeometry(QtCore.QRect(20, 390, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par9_label.setFont(font)
        self.par9_label.setObjectName("par9_label")
        self.par9 = QtWidgets.QLineEdit(Form)
        self.par9.setGeometry(QtCore.QRect(190, 389, 91, 20))
        self.par9.setObjectName("par9")
        self.par7 = QtWidgets.QLineEdit(Form)
        self.par7.setGeometry(QtCore.QRect(190, 309, 91, 20))
        self.par7.setObjectName("par7")
        self.bool_check2 = QtWidgets.QCheckBox(Form)
        self.bool_check2.setGeometry(QtCore.QRect(225, 150, 16, 17))
        self.bool_check2.setText("")
        self.bool_check2.setObjectName("bool_check2")
        self.bool_check3 = QtWidgets.QCheckBox(Form)
        self.bool_check3.setGeometry(QtCore.QRect(225, 190, 16, 17))
        self.bool_check3.setText("")
        self.bool_check3.setObjectName("bool_check3")
        self.fun_button = QtWidgets.QToolButton(Form)
        self.fun_button.setGeometry(QtCore.QRect(220, 73, 25, 19))
        self.fun_button.setObjectName("fun_button")
        self.par10 = QtWidgets.QLineEdit(Form)
        self.par10.setGeometry(QtCore.QRect(190, 429, 91, 20))
        self.par10.setObjectName("par10")
        self.par10_label = QtWidgets.QLabel(Form)
        self.par10_label.setGeometry(QtCore.QRect(20, 430, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.par10_label.setFont(font)
        self.par10_label.setObjectName("par10_label")
        self.par4.raise_()
        self.bool_check3.raise_()
        self.par7.raise_()
        self.list.raise_()
        self.list_label.raise_()
        self.line.raise_()
        self.par1_label.raise_()
        self.par2_label.raise_()
        self.par1.raise_()
        self.par2.raise_()
        self.par3.raise_()
        self.buttons.raise_()
        self.par3_label.raise_()
        self.par4_label.raise_()
        self.par5_label.raise_()
        self.par5.raise_()
        self.par6.raise_()
        self.par6_label.raise_()
        self.par7_label.raise_()
        self.bool_check1.raise_()
        self.par8_label.raise_()
        self.par8.raise_()
        self.par9_label.raise_()
        self.par9.raise_()
        self.bool_check2.raise_()
        self.fun_button.raise_()
        self.par10.raise_()
        self.par10_label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.list_label.setText(_translate("Form", "<Список>"))
        self.par1_label.setText(_translate("Form", "<Parameter1>"))
        self.par2_label.setText(_translate("Form", "<Parameter2>"))
        self.par3_label.setText(_translate("Form", "<Parameter3>"))
        self.par4_label.setText(_translate("Form", "<Parameter4>"))
        self.par5_label.setText(_translate("Form", "<Parameter5>"))
        self.par6_label.setText(_translate("Form", "<Parameter6>"))
        self.par7_label.setText(_translate("Form", "<Parameter7>"))
        self.par8_label.setText(_translate("Form", "<Parameter8>"))
        self.par9_label.setText(_translate("Form", "<Parameter9>"))
        self.fun_button.setText(_translate("Form", "..."))
        self.par10_label.setText(_translate("Form", "<Parameter10>"))

