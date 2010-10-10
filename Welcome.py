import sys
from PyQt4 import QtGui

if __name__ == '__main__':
  application = QtGui.QApplication( sys.argv )
  window = QtGui.QWidget()
  window.setGeometry( 50, 50, 640, 480 )
  
  logo       = QtGui.QPixmap("welcome.png", "PNG")
  logo_label = QtGui.QLabel( parent = window )
  logo_label.setPixmap( logo )
  
  window.show()
  sys.exit( application.exec_() )