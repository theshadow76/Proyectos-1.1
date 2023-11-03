import sys
from PyQt6.QtGui import QIcon, QColor
import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6
import PyQt6.QtCore
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QHBoxLayout, QFrame

def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setStyleSheet = ("""
        QWidget{
            background-color: white;
        }
    """)
    pn1 = QFrame
    pn1.styleSheet = ("""
        QWidget{
            background-color: #468EC7;
        }
    """)
    pn1.width = 100
    pn1.height = 7
    pn1.move(widget, 0, 0)
    pn1.show(widget)

    widget.setGeometry(50, 50, 1000, 800)

    widget.setWindowTitle("Shadow Task Manager")
    widget.show()

    sys.exit(app.exec())
if __name__ == '__main__':
    window()