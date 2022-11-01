import os

import cv2
from PIL import Image

import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5 import uic


class Image_Show:

    def __init__(self):
        # 动态加载UI文件
        self.ui = uic.loadUi('show_pic.ui')
        self.FileDirectory = ''
        self.file_list = []
        # 按钮绑定
        self.ui.pic_button.clicked.connect(self.show_img)
        self.ui.pics_button.clicked.connect(self.show_imgs)
        self.ui.down_pic.clicked.connect(self.down_img)
        self.ui.up_pic.clicked.connect(self.up_img)
        # 图片计数器
        self.count = 0
        # 图片总数
        self.pic_num = 0

    def show_img(self):
        """
        显示单张图像
        :return:
        """
        # 选择图片文件
        image_file, _ = QFileDialog.getOpenFileName(None, '选择图片', 'C:/',
                                                    'Image files (*.jpg *.gif *.png *.jpeg *.jfif)')

        # 自适应显示图片
        frame = QPixmap(image_file)
        self.ui.label.setScaledContents(True)
        # 设置标签图像
        self.ui.label.setPixmap(frame)
        # 设置进度条
        self.ui.pics_progressBar.setValue(100)

    def show_imgs(self):
        """
        显示多张图像
        :return:
        """
        # 选择文件夹
        FileDirectory = QFileDialog.getExistingDirectory(None, "选择图片文件夹", "C:/")
        # 获取目录列表
        file_list = [i for i in os.listdir(FileDirectory) if i.endswith('jpg') or i.endswith('png') or
                     i.endswith('gif') or i.endswith('jpeg') or i.endswith('.jfif')]

        if len(file_list) != 0:
            self.FileDirectory = FileDirectory
            self.file_list = file_list
            # 显示第一张图像
            first_file_path = os.path.join(FileDirectory, file_list[0])
            self.show_path_img(first_file_path)
            # 图片总数
            self.pic_num = len(file_list) + 1
            # 进度值
            progress = int((self.count + 1) / (self.pic_num - 1) * 100)
            # 更新进度条
            self.ui.pics_progressBar.setValue(progress)
        else:
            pass

    def down_img(self):
        """
        切换下一张图像
        :return:
        """
        if self.pic_num != 0 and self.count < len(self.file_list) - 1:
            self.count += 1
            now_file_path = os.path.join(self.FileDirectory, self.file_list[self.count])
            self.show_path_img(now_file_path)
            # 进度值
            progress = int((self.count + 1) / (self.pic_num-1) * 100)
            # 更新进度条
            self.ui.pics_progressBar.setValue(progress)
        else:
            pass

    def up_img(self):
        """
        切换上一张图像
        :return:
        """
        if self.count > 0:
            self.count -= 1
            now_file_path = os.path.join(self.FileDirectory, self.file_list[self.count])
            self.show_path_img(now_file_path)
            # 进度值
            progress = int((self.count + 1) / (self.pic_num-1) * 100)
            # 更新进度条
            self.ui.pics_progressBar.setValue(progress)
        else:
            pass

    def show_path_img(self, path):
        """
        显示路径图像
        :param path: 文件路径
        :return:
        """
        frame = QPixmap(path)
        # 自适应显示图片
        self.ui.label.setScaledContents(True)
        # 设置标签图像
        self.ui.label.setPixmap(frame)


app = QApplication([])
Image_Show = Image_Show()
Image_Show.ui.show()
app.exec_()
