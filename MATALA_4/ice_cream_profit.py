import sys
import csv
from pathlib import Path

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT,
)
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class IceCreamProfitWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.temperatures = []
        self.profits = []
        self.selected_file = None

        self.setWindowTitle("Ice Cream Profit Tool")
        self.resize(1100, 760)
        self._create_widgets()
        self._load_stylesheet()
        self._draw_placeholder_plot()

    def _create_widgets(self) -> None:
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(26, 22, 26, 26)
        main_layout.setSpacing(18)

        header_layout = QHBoxLayout()
        title_block = QVBoxLayout()

        title = QLabel("Ice Cream Profit Tool")
        title.setObjectName("pageTitle")
        title_block.addWidget(title)

        subtitle = QLabel("Explore the relationship between temperature and profit.")
        subtitle.setObjectName("pageSubtitle")
        title_block.addWidget(subtitle)
        header_layout.addLayout(title_block)
        header_layout.addStretch()

        self.load_file_button = QPushButton("Load File")
        self.load_file_button.clicked.connect(self.on_load_file_clicked)
        header_layout.addWidget(self.load_file_button)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.clicked.connect(self.on_about_clicked)
        header_layout.addWidget(self.about_button)
        main_layout.addLayout(header_layout)

        plot_panel = QFrame()
        plot_panel.setObjectName("plotPanel")
        plot_layout = QVBoxLayout(plot_panel)
        plot_layout.setContentsMargins(10, 10, 10, 10)
        plot_layout.setSpacing(4)

        self.figure = Figure(figsize=(8, 5), tight_layout=True)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas, 1)
        main_layout.addWidget(plot_panel, 1)

        self.setCentralWidget(central_widget)

    def _load_stylesheet(self) -> None:
        stylesheet_path = Path(__file__).with_name("ice_cream_profit.qss")
        self.setStyleSheet(stylesheet_path.read_text())

    def on_load_file_clicked(self) -> None:

        file_path, _ = QFileDialog.getOpenFileName(self, "Select Ice Cream excel", "", "CSV Files (*.csv)")
        if not file_path:
            return

        self.selected_file = file_path
        self.temperatures = []
        self.profits = []

        with open(self.selected_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader,None)

            for row in reader:
                if not row:
                    continue
                temp = float(row[0])
                prof = float(row[1])

                self.temperatures.append(temp)
                self.profits.append(prof)

        self.plot_ice_cream_data()


    def plot_ice_cream_data(self) -> None:
        # TODO: my code
        pass

    def _draw_placeholder_plot(self) -> None:
        self.axes.clear()
        self.axes.set_title("Ice Cream Profit")
        self.axes.set_xlabel("Temperature")
        self.axes.set_ylabel("Profit")
        self.axes.text(
            0.5,
            0.5,
            "Load a data file to begin",
            horizontalalignment="center",
            verticalalignment="center",
            transform=self.axes.transAxes,
            color="#758397",
            fontsize=14,
        )
        self.axes.grid(True, color="#e7edf3", linewidth=0.8)
        self.canvas.draw_idle()

    def on_about_clicked(self) -> None:
        about_dialog = QDialog(self)
        about_dialog.setObjectName("aboutDialog")
        about_dialog.setWindowTitle("About Ice Cream Profit Tool")
        about_dialog.resize(680, 430)
        about_dialog.setMinimumSize(640, 400)
        about_dialog.setStyleSheet(self.styleSheet())

        dialog_layout = QVBoxLayout(about_dialog)
        dialog_layout.setContentsMargins(32, 28, 32, 24)
        dialog_layout.setSpacing(18)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(24)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(12)

        title = QLabel("Ice Cream Profit Tool")
        title.setObjectName("aboutTitle")
        text_layout.addWidget(title)

        description = QLabel(
            "A simple desktop tool for exploring how temperature relates to "
            "ice cream profits."
        )
        description.setObjectName("aboutDescription")
        description.setWordWrap(True)
        text_layout.addWidget(description)

        author = QLabel("Created by Alex Atlas")
        author.setObjectName("aboutAuthor")
        text_layout.addWidget(author)

        repository_caption = QLabel("GitHub repository")
        repository_caption.setObjectName("repositoryCaption")
        text_layout.addWidget(repository_caption)

        repository_url = "https://github.com/alexatlasidf-afk/Mecatronis"
        repository_link = QLabel(
            f'<a href="{repository_url}">{repository_url}</a>'
        )
        repository_link.setObjectName("repositoryUrl")
        repository_link.setOpenExternalLinks(True)
        repository_link.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        repository_link.setWordWrap(True)
        text_layout.addWidget(repository_link)
        text_layout.addStretch()

        content_layout.addLayout(text_layout, 1)

        illustration_path = (
            Path(__file__).resolve().parent / "ice_cream_illustration.png"
        )
        illustration = QLabel()
        illustration.setObjectName("aboutIllustration")
        illustration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        illustration.setFixedSize(220, 290)
        illustration.setPixmap(
            QPixmap(str(illustration_path)).scaled(
                210,
                280,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        content_layout.addWidget(illustration)
        dialog_layout.addLayout(content_layout, 1)

        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_button = QPushButton("Close")
        close_button.setObjectName("aboutCloseButton")
        close_button.clicked.connect(about_dialog.accept)
        close_layout.addWidget(close_button)
        dialog_layout.addLayout(close_layout)

        about_dialog.exec()


def main() -> None:
    app = QApplication(sys.argv)
    window = IceCreamProfitWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()