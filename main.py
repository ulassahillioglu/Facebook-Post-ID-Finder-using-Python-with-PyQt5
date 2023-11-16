from Extractor import FacebookPostLinkExtractor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QVBoxLayout, QWidget


class FacebookPostLinkExtractorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Facebook Post Link Extractor")
        self.setGeometry(300, 300, 500, 250)

        self.label = QLabel("Enter Facebook post link:", self)
        self.label.setGeometry(20, 20, 150, 30)

        self.link_input = QLineEdit(self)
        self.link_input.setGeometry(170, 20, 300, 30)

        self.extract_button = QPushButton("Extract", self)
        self.extract_button.setGeometry(200, 70, 100, 30)
        self.extract_button.clicked.connect(self.extract_post_link)

        self.result_label = QLabel("Result:", self)
        self.result_label.setGeometry(20, 120, 60, 30)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(90, 120, 380, 70)
        self.result_text.setReadOnly(True)

        self.copy_button = QPushButton("Copy", self)
        self.copy_button.setGeometry(200, 200, 100, 30)
        self.copy_button.clicked.connect(self.copy_result)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(320, 200, 100, 30)
        self.clear_button.clicked.connect(self.clear_fields)

    def extract_post_link(self):
        link = self.link_input.text().strip()

        extractor = FacebookPostLinkExtractor()
        result = extractor.get_facebook_post_link(link)

        self.result_text.setText(result)

    def copy_result(self):
        result = self.result_text.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(result)
        QMessageBox.information(self, "Copied", "Result copied to clipboard!")

    def clear_fields(self):
        self.link_input.clear()
        self.result_text.clear()





    


    
    
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FacebookPostLinkExtractorApp()
    window.show()
    sys.exit(app.exec_())
