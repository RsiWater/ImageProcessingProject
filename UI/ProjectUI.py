# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1918, 1080)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.greylevelbutton = QtWidgets.QPushButton(self.centralwidget)
        self.greylevelbutton.setGeometry(QtCore.QRect(270, 900, 150, 45))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.greylevelbutton.setFont(font)
        self.greylevelbutton.setObjectName("greylevelbutton")
        self.loadfilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadfilebutton.setGeometry(QtCore.QRect(110, 900, 150, 45))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.loadfilebutton.setFont(font)
        self.loadfilebutton.setObjectName("loadfilebutton")
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setGeometry(QtCore.QRect(1700, 30, 150, 45))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.savebutton.setFont(font)
        self.savebutton.setObjectName("savebutton")
        self.showvideo = QtWidgets.QGraphicsView(self.centralwidget)
        self.showvideo.setGeometry(QtCore.QRect(320, 30, 1280, 720))
        self.showvideo.setObjectName("showvideo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 830, 92, 24))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1320, 870, 670, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 780, 500, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.greenLevel = QtWidgets.QSlider(self.centralwidget)
        self.greenLevel.setGeometry(QtCore.QRect(740, 830, 370, 22))
        self.greenLevel.setMinimum(50)
        self.greenLevel.setMaximum(200)
        self.greenLevel.setSingleStep(1)
        self.greenLevel.setProperty("value", 100)
        self.greenLevel.setOrientation(QtCore.Qt.Horizontal)
        self.greenLevel.setObjectName("greenLevel")
        self.blueLevel = QtWidgets.QSlider(self.centralwidget)
        self.blueLevel.setGeometry(QtCore.QRect(740, 860, 370, 22))
        self.blueLevel.setMinimum(50)
        self.blueLevel.setMaximum(200)
        self.blueLevel.setSingleStep(1)
        self.blueLevel.setProperty("value", 100)
        self.blueLevel.setOrientation(QtCore.Qt.Horizontal)
        self.blueLevel.setObjectName("blueLevel")
        self.redLevel = QtWidgets.QSlider(self.centralwidget)
        self.redLevel.setGeometry(QtCore.QRect(740, 800, 370, 22))
        self.redLevel.setMinimum(50)
        self.redLevel.setMaximum(200)
        self.redLevel.setSingleStep(100)
        self.redLevel.setProperty("value", 100)
        self.redLevel.setOrientation(QtCore.Qt.Horizontal)
        self.redLevel.setObjectName("redLevel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1150, 800, 300, 24))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1150, 830, 300, 24))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1150, 860, 300, 24))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1320, 760, 571, 151))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.filterBox = QtWidgets.QComboBox(self.centralwidget)
        self.filterBox.setGeometry(QtCore.QRect(1150, 900, 150, 45))
        self.filterBox.setEditable(False)
        self.filterBox.setObjectName("filterBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(740, 760, 130, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widthlevel = QtWidgets.QSpinBox(self.centralwidget)
        self.widthlevel.setGeometry(QtCore.QRect(280, 830, 100, 33))
        self.widthlevel.setMaximum(3840)
        self.widthlevel.setSingleStep(10)
        self.widthlevel.setProperty("value", 800)
        self.widthlevel.setObjectName("widthlevel")
        self.heightlevel = QtWidgets.QSpinBox(self.centralwidget)
        self.heightlevel.setGeometry(QtCore.QRect(480, 830, 100, 33))
        self.heightlevel.setMaximum(2160)
        self.heightlevel.setSingleStep(10)
        self.heightlevel.setProperty("value", 480)
        self.heightlevel.setObjectName("heightlevel")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 830, 92, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 830, 92, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Applybutton = QtWidgets.QPushButton(self.centralwidget)
        self.Applybutton.setGeometry(QtCore.QRect(430, 900, 150, 45))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(7)
        self.Applybutton.setFont(font)
        self.Applybutton.setObjectName("Applybutton")
        self.redLabel = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.redLabel.setGeometry(QtCore.QRect(1220, 790, 78, 33))
        self.redLabel.setMinimum(0.5)
        self.redLabel.setMaximum(2.0)
        self.redLabel.setSingleStep(0.01)
        self.redLabel.setProperty("value", 1.0)
        self.redLabel.setObjectName("redLabel")
        self.greenLabel = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.greenLabel.setGeometry(QtCore.QRect(1220, 825, 78, 33))
        self.greenLabel.setMinimum(0.5)
        self.greenLabel.setMaximum(2.0)
        self.greenLabel.setSingleStep(0.01)
        self.greenLabel.setProperty("value", 1.0)
        self.greenLabel.setObjectName("greenLabel")
        self.blueLabel = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.blueLabel.setGeometry(QtCore.QRect(1220, 860, 78, 33))
        self.blueLabel.setMinimum(0.5)
        self.blueLabel.setMaximum(2.0)
        self.blueLabel.setSingleStep(0.01)
        self.blueLabel.setProperty("value", 1.0)
        self.blueLabel.setObjectName("blueLabel")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(1700, 100, 150, 45))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.about = QtWidgets.QMenuBar(MainWindow)
        self.about.setGeometry(QtCore.QRect(0, 0, 1918, 36))
        self.about.setObjectName("about")
        self.menuabout = QtWidgets.QMenu(self.about)
        self.menuabout.setObjectName("menuabout")
        self.menuFile = QtWidgets.QMenu(self.about)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.about)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.about)
        self.successful = QtWidgets.QStatusBar(MainWindow)
        self.successful.setObjectName("successful")
        MainWindow.setStatusBar(self.successful)
        self.actionaboutus = QtWidgets.QAction(MainWindow)
        self.actionaboutus.setObjectName("actionaboutus")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionTwo_Level = QtWidgets.QAction(MainWindow)
        self.actionTwo_Level.setObjectName("actionTwo_Level")
        self.actionChoke_a_dick = QtWidgets.QAction(MainWindow)
        self.actionChoke_a_dick.setObjectName("actionChoke_a_dick")
        self.menuabout.addAction(self.actionaboutus)
        self.menuabout.addAction(self.actionChoke_a_dick)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionTwo_Level)
        self.about.addAction(self.menuFile.menuAction())
        self.about.addAction(self.menuEdit.menuAction())
        self.about.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.greylevelbutton.setText(_translate("MainWindow", "Grey On"))
        self.loadfilebutton.setText(_translate("MainWindow", "Load File"))
        self.savebutton.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Scale"))
        self.label_2.setText(_translate("MainWindow", "Copyright © 1999-2019 4NUKing Inc.All rights reserved."))
        self.label_3.setText(_translate("MainWindow", "Origin Width:Height:"))
        self.label_4.setText(_translate("MainWindow", "Red"))
        self.label_5.setText(_translate("MainWindow", "Green"))
        self.label_6.setText(_translate("MainWindow", "Blue"))
        self.label_7.setText(_translate("MainWindow", "MultiMedia Process Tool"))
        self.filterBox.setCurrentText(_translate("MainWindow", "無濾鏡"))
        self.label_8.setText(_translate("MainWindow", "Color Level"))
        self.label_9.setText(_translate("MainWindow", "Width"))
        self.label_10.setText(_translate("MainWindow", "Height"))
        self.Applybutton.setText(_translate("MainWindow", "Apply"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.menuabout.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionaboutus.setText(_translate("MainWindow", "aboutus"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionTwo_Level.setText(_translate("MainWindow", "Two Level"))
        self.actionChoke_a_dick.setText(_translate("MainWindow", "Choke a dick"))
