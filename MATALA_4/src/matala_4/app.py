import sys
import csv
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class GradeAdjustmentWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = None

        self.setWindowTitle("Grade Adjustment Tool")
        self.resize(800, 620)
        self.create_widgets()
        self._load_stylesheet()
        self.update_table_from_lists()

    def create_widgets(self) -> None:
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)

        controls_layout = QHBoxLayout()
        self.load_file_button = QPushButton("Load File")
        self.load_file_button.clicked.connect(self.on_load_file_clicked)
        controls_layout.addWidget(self.load_file_button)

        controls_layout.addWidget(QLabel("Bonus points:"))
        self.bonus_spin_box = QSpinBox()
        self.bonus_spin_box.setRange(-100, 100)
        self.bonus_spin_box.setKeyboardTracking(False)
        self.bonus_spin_box.editingFinished.connect(self.on_bonus_changed)
        controls_layout.addWidget(self.bonus_spin_box)

        controls_layout.addStretch()

        self.update_file_button = QPushButton("Update File")
        self.update_file_button.clicked.connect(self.on_update_file_clicked)
        controls_layout.addWidget(self.update_file_button)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.on_about_clicked)
        controls_layout.addWidget(self.about_button)
        main_layout.addLayout(controls_layout)

        self.grades_table = QTableWidget(50, 3, self)
        self.grades_table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.grades_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.grades_table.setAlternatingRowColors(True)
        self.grades_table.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.grades_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.grades_table.verticalHeader().setVisible(False)
        main_layout.addWidget(self.grades_table)

        self.setCentralWidget(central_widget)

    def _load_stylesheet(self) -> None:
        stylesheet_path = Path(__file__).with_name("style.qss")
        stylesheet = stylesheet_path.read_text()
        self.setStyleSheet(stylesheet)

    def on_load_file_clicked(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "Select grades excel", "", "CSV Files (*.csv)")

        if not file_path:
            return
        self.selected_file = file_path

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(self.selected_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader,None)

            for row in reader:
                student_id = row[0]
                grade = int(row[1])

                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)

        self.update_table_from_lists()


    def on_bonus_changed(self) -> None:
        # TODO: my code
        pass

    def on_update_file_clicked(self) -> None:
        # TODO: my code
        pass

    def on_about_clicked(self) -> None:
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("About Grade Adjustment Tool")
        about_dialog.setMinimumWidth(400)

        layout = QVBoxLayout(about_dialog)
        layout.addWidget(QLabel("<h2>Grade Adjustment Tool</h2>"))
        layout.addWidget(QLabel("A desktop application for grade adjustments."))
        layout.addWidget(QLabel("Author: Alex Atlas"))

        repository_url = "[INSERT_YOUR_GITHUB_REPO_URL]"
        repository_link = QLabel(
            f'<a href="{repository_url}">{repository_url}</a>'
        )
        repository_link.setOpenExternalLinks(True)
        repository_link.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        layout.addWidget(repository_link)

        close_button = QPushButton("Close")
        close_button.clicked.connect(about_dialog.accept)
        layout.addWidget(close_button)
        about_dialog.exec()

    def update_table_from_lists(self) -> None:
        for row in range(50):
            values = (
                self.student_ids[row] if row < len(self.student_ids) else "",
                self.original_grades[row]
                if row < len(self.original_grades)
                else "",
                self.corrected_grades[row]
                if row < len(self.corrected_grades)
                else "",
            )
            for column, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.grades_table.setItem(row, column, item)


def open_file_cross_platform(file_path: str | Path) -> None:
    file_url = QUrl.fromLocalFile(str(Path(file_path).resolve()))
    if not QDesktopServices.openUrl(file_url):
        raise OSError(f"Could not open file: {file_path}")


def main() -> None:
    app = QApplication(sys.argv)
    window = GradeAdjustmentWindow()
    window.show()
    sys.exit(app.exec())
