import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from PyQt5.QtGui import QColor

dracula_style = """
    QWidget {
        background-color: #282a36;
        color: #f8f8f2;
    }

    QPlainTextEdit {
        background-color: #282a36;
        color: #f8f8f2;
        selection-background-color: #44475a;
        selection-color: #f8f8f2;
    }

    QLineEdit {
        background-color: #282a36;
        color: #f8f8f2;
        selection-background-color: #44475a;
        selection-color: #f8f8f2;
    }

    QTextEdit {
        background-color: #282a36;
        color: #f8f8f2;
        selection-background-color: #44475a;
        selection-color: #f8f8f2;
    }
    """

class CustomRichJupyterWidget(RichJupyterWidget):
    enter_pressed = pyqtSignal(str)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enter_pressed.emit(self.input.text)
            self.input.clear()
        else:
            super().keyPressEvent(event)

class PythonTerminal(QWidget):
    def __init__(self, parent=None):
        super(PythonTerminal, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Cria o console Python e o gerenciador de kernel
        self.console = CustomRichJupyterWidget()
        self.console.setStyleSheet(dracula_style)
        self.console.set_default_style(colors='Linux')
        self.console.in_prompt_color = QColor('#50fa7b')
        kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        # Conecta o console ao kernel
        self.console.kernel_manager = kernel_manager
        self.console.kernel_client = kernel_client
        self.console.exit_requested.connect(self.close)
        self.console.enter_pressed.connect(self.show_user_input)

        # Adiciona o console ao layout
        layout.addWidget(self.console)

    def show_user_input(self, user_input):
        self.console.append_plain_text(f'In [1]: {user_input}\n')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Python Terminal - Drácula")
        self.setCentralWidget(PythonTerminal())
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
