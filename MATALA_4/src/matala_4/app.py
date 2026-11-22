import sys
import csv
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
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
        self.bonus_spin_box.setRange(0, 100)
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

        bonus_points = self.bonus_spin_box.value()
        self.corrected_grades = []

        for grade in self.original_grades:
            new_grade = grade + bonus_points

            if new_grade >100:
                new_grade = 100

            self.corrected_grades.append(new_grade)

        self.update_table_from_lists()

        
    def on_update_file_clicked(self) -> None:

        if not self.selected_file:
            return

        with open(self.selected_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Grade"])

            for student_id, corrected_grade in zip(self.student_ids, self.corrected_grades):
                writer.writerow([student_id, corrected_grade])

        open_file_cross_platform(self.selected_file)
        

    def on_about_clicked(self) -> None:
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("About Grade Adjustment Tool")
        about_dialog.setObjectName("aboutDialog")
        about_dialog.resize(620, 420)
        about_dialog.setMinimumSize(580, 400)

        layout = QVBoxLayout(about_dialog)
        layout.setContentsMargins(32, 28, 32, 24)
        layout.setSpacing(16)

        title = QLabel("Grade Adjustment Tool")
        title.setObjectName("aboutTitle")
        layout.addWidget(title)

        subtitle = QLabel("A desktop application for grade adjustments.")
        subtitle.setObjectName("aboutSubtitle")
        layout.addWidget(subtitle)

        author = QLabel("Student: Alex Atlas")
        author.setObjectName("aboutAuthor")
        layout.addWidget(author)

        repository_url = "https://github.com/alexatlasidf-afk/Mecatronis"
        repository_panel = QWidget()
        repository_panel.setObjectName("repositoryPanel")
        repository_layout = QHBoxLayout(repository_panel)
        repository_layout.setContentsMargins(18, 14, 18, 14)
        repository_layout.setSpacing(18)

        image_path = Path(__file__).resolve().parents[2] / "GitHub-Logo.png"
        logo = QPixmap(str(image_path))
        logo_label = QLabel()
        logo_label.setObjectName("repositoryLogo")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setFixedSize(76, 76)
        logo_label.setPixmap(
            logo.scaled(
                68,
                68,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        repository_layout.addWidget(logo_label)

        repository_link = QLabel(
            f'<a href="{repository_url}">{repository_url}</a>'
        )
        repository_link.setObjectName("repositoryUrl")
        repository_link.setOpenExternalLinks(True)
        repository_link.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        repository_link.setWordWrap(True)
        repository_layout.addWidget(repository_link, 1)
        layout.addWidget(repository_panel)

        close_button = QPushButton("Close")
        close_button.setObjectName("aboutClose")
        close_button.clicked.connect(about_dialog.accept)
        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_layout.addWidget(close_button)
        layout.addLayout(close_layout)

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
