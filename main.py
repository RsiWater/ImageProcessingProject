import sys
import cv2
import os.path 
import pathlib
import copy
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from UI import ProjectUI
from image_process_function import * 


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = ProjectUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = ''
        self.greyData = ''
        self.ori_data = ''
        self.ori_video = ''

        self.fps = 0
        
        self.isVideo = False
        self.alreadyDone = False
        self.clickedByGreyButton = True
        self.isGrey = False

        self.readImageFromPath("patrick.jpg")
        self.ori_data = copy.deepcopy(self.data)

        self.initFilterBox()

        self.ui.showvideo.setScene(self.showImage(self.data[0]))
        self.ui.label_3.setText("Origin: "+ str(self.ori_data[0].shape[1]) + "x" +str(self.ori_data[0].shape[0]))
        self.ui.actionNew.triggered.connect(self.loadEvent)
        self.ui.loadfilebutton.clicked.connect(self.loadEvent)
        self.ui.savebutton.clicked.connect(self.saveEvent)
        self.ui.actionSave.triggered.connect(self.saveEvent)
        self.ui.greylevelbutton.clicked.connect(self.setGrey)
        self.ui.redLevel.sliderReleased.connect(self.setRLabel)
        self.ui.greenLevel.sliderReleased.connect(self.setGLabel)
        self.ui.blueLevel.sliderReleased.connect(self.setBLabel)
        self.ui.redLabel.valueChanged.connect(self.setRLevel)
        self.ui.greenLabel.valueChanged.connect(self.setGLevel)
        self.ui.blueLabel.valueChanged.connect(self.setBLevel)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.Applybutton.clicked.connect(self.apply)


    def debug(self):
        print("Starburststream")
        print(self.ui.savebutton.setVisible(False))

    def initFilterBox(self):
        self.ui.filterBox.clear()

        self.ui.filterBox.addItem("自訂義")
        self.ui.filterBox.addItem("鄉愁黃")
        self.ui.filterBox.addItem("共產紅")
        self.ui.filterBox.addItem("星爆藍")
        self.ui.filterBox.addItem("魅力紫")
        self.ui.filterBox.addItem("出軌綠") 
        if not self.isVideo: # Image
            self.ui.filterBox.addItem("邊緣提取")
            self.ui.filterBox.addItem("邊緣增強")
            self.ui.filterBox.addItem("邊緣再增強")
            self.ui.filterBox.addItem("浮雕風")

    def setRLabel(self):
        self.ui.redLabel.setValue(self.ui.redLevel.value() / 100)
    def setGLabel(self):
        self.ui.greenLabel.setValue(self.ui.greenLevel.value() / 100)
    def setBLabel(self):
        self.ui.blueLabel.setValue(self.ui.blueLevel.value() / 100)

    def setRLevel(self):
        self.ui.redLevel.setValue(int(self.ui.redLabel.value() * 100))
    def setGLevel(self):
        self.ui.greenLevel.setValue(int(self.ui.greenLabel.value() * 100))
    def setBLevel(self):
        self.ui.blueLevel.setValue(int(self.ui.blueLabel.value() * 100))

    def reset(self):
        self.data = copy.deepcopy(self.ori_data)
        self.ui.redLevel.setValue(int(1 * 100))
        self.ui.greenLevel.setValue(int(1 * 100))
        self.ui.blueLevel.setValue(int(1 * 100))
        self.ui.redLabel.setValue(100 / 100)
        self.ui.greenLabel.setValue(100 / 100)
        self.ui.blueLabel.setValue(100 / 100)
        self.ui.showvideo.setScene(self.showImage(self.ori_data[0]))

    def apply(self):
        self.clickedByGreyButton = False
        self.data = copy.deepcopy(self.ori_data)
        if self.ui.filterBox.currentText() == "自訂義":
            self.data = self.modifyColor()
        else:
            self.data = self.modifyFilter()
        self.data = self.resizeImage()
        if self.isGrey:
            self.setGrey()
            self.ui.showvideo.setScene(self.showImage(self.greyData[0]))
        else:
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
        self.clickedByGreyButton = True
        

    def modifyFilter(self):
        filterType = self.ui.filterBox.currentText()
        temp_data = copy.deepcopy(self.data)

        if self.isVideo and not self.alreadyDone:
            temp_data = [temp_data[0]]

        if filterType == "鄉愁黃":
            temp_data = color(temp_data, 0.005, 0.499, 0.888)
        elif filterType == "共產紅":
            temp_data = color(temp_data, 0.114, 0.114, 0.887)
        elif filterType == "星爆藍":
            temp_data = color(temp_data, 0.587, 0.299, 0.114)
        elif filterType == "魅力紫":
            temp_data = color(temp_data, 0.299, 0.114, 0.587)
        elif filterType == "出軌綠":
            temp_data = color(temp_data, 0.114, 0.587, 0.229)
        elif filterType == "邊緣提取":
            temp_data = findEdge(temp_data)
        elif filterType == "邊緣增強":
            temp_data = edgeEnhance(temp_data)
        elif filterType == "邊緣再增強":
            temp_data = edgeEnMore(temp_data)
        elif filterType == "浮雕風":
            temp_data = emboss(temp_data)

        return temp_data

    def setGrey(self):
        if not self.isGrey or not self.clickedByGreyButton:
            img = copy.deepcopy(self.data)
            if (self.isVideo and self.alreadyDone) or not self.isVideo:
                img = grey(img)
            else:
                img = grey([img[0]])

            img = grey(img)
            self.ui.showvideo.setScene(self.showImage(img[0]))
            self.greyData = copy.deepcopy(img)
            if self.clickedByGreyButton:
                self.ui.greylevelbutton.setText("Grey Off")
                self.isGrey = True
        else:
            self.ui.showvideo.setScene(self.showImage(self.data[0]))
            self.ui.greylevelbutton.setText("Grey On")
            self.isGrey = False

    def resizeImage(self):
        # temp = cv2.cvtColor(self.data[0], cv2.COLOR_BGR2RGB)

        height, width , gar = self.data[0].shape

        # resize image
        temp_data = copy.deepcopy(self.data)
        if self.isVideo and not self.alreadyDone:
            img = size([temp_data[0]], ((self.ui.heightlevel.value() / height) * 100), ((self.ui.widthlevel.value() / width) * 100))
        else:
            img = size(temp_data, ((self.ui.heightlevel.value() / height) * 100), ((self.ui.widthlevel.value() / width) * 100))
        return img

    def modifyColor(self):
        temp_data = copy.deepcopy(self.data)
        
        R_Value = self.ui.redLevel.value() / 100
        G_Value = self.ui.greenLevel.value() / 100
        B_Value = self.ui.blueLevel.value() / 100

        if self.isVideo and not self.alreadyDone:
            temp_data = color([temp_data[0]], B_Value, G_Value, R_Value)
        else:
            temp_data = color(temp_data, B_Value, G_Value, R_Value)
        return temp_data

    def loadEvent(self):
        self.isGrey = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.readImageFromPath(fileName)
            self.initFilterBox()
            if len(self.data) == 1:
                self.ui.showvideo.setScene(self.showImage(self.data[0]))
            else:
                # set video to frame 0
                self.ui.showvideo.setScene(self.showImage(self.data[0]))
        
        self.ui.label_3.setText("Origin: "+ str(self.data[0].shape[1]) + "x" +str(self.data[0].shape[0]))

    def saveEvent(self):
        if self.isVideo:
            directory = str(QtWidgets.QFileDialog.getSaveFileName(self, ("Save F:xile"), "./untitled.mp4", ("Video (*.mp4)")))
        else:
            directory = str(QtWidgets.QFileDialog.getSaveFileName(self, ("Save F:xile"), "./untitled.jpg", ("Images (*.png *.jpg)")))
        savePath = directory.split("'")[1]

        if savePath != '':
            if savePath.split("/")[0] == "C:":
                savePath = os.path.relpath(savePath)

            if self.isGrey:
                tempData = copy.deepcopy(self.data)
                self.data = copy.deepcopy(self.greyData)

            if not self.isVideo: #Image
                write_image(savePath, self.data)
            else:
                self.alreadyDone = True
                self.apply()
                if self.isGrey:
                    write_video(savePath, self.greyData, self.fps)
                else:
                    write_video(savePath, self.data, self.fps)
                self.alreadyDone = False
        
        if self.isGrey:
            self.data = copy.deepcopy(tempData)
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("File saved!")
        msg.setWindowTitle("Notification")

        msg.exec_()

    def readImageFromPath(self, path):
        if path.split("/")[0] == "C:":
            if path.split("/")[-1].split('.')[1] == 'mp4':
                self.data, self.fps = get_video(os.path.relpath(path))
                self.ori_video = copy.deepcopy(self.data)
                self.isVideo = True
            else:
                self.data = get_image(os.path.relpath(path))
                self.isVideo = False
        else:
            self.data = get_image(path)
        self.ori_data = copy.deepcopy(self.data)
        
    def showImage(self, send_img):
        img = send_img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_height, img_width, gar = img.shape
        

        image_disp = QtGui.QImage(img, img_width, img_height, QtGui.QImage.Format_RGB888)

        pixMap = QtGui.QPixmap.fromImage(image_disp)
        item = QtWidgets.QGraphicsPixmapItem(pixMap)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)

        return scene


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()

sys.exit(app.exec_())
