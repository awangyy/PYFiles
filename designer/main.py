#将.ui文件转换为.py文件
#方法一：
# python -m PyQt5.uic.pyuic demo.ui -o demo.py

#方法二：
#pyuic5



#尺寸策略（sizepolicy）
#sizeHint(期望尺寸)
#对于大多数控件来说，sizeHint的值是只读的

#读取期望尺寸
#self.pushButton.sizeHint().width()     //77
#self.pushButton.sizeHint().height()    //32

#QPushButton width:77 height:32
#QTextEdit width:256 height:192

#最小期望尺寸
#self.pushButton.minimumsizeHint().width()
#self.pushButton.minimumsizeHint().height()

#QTextEdit 78 78
#QPushButton 77 32