import sys
from math import pi

import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    MAX_ROWS = 100
    VISIBLE_ROWS = 10
    

    def __init__(self) -> None:
        super().__init__()

        self.X_values =[]

        self.setWindowTitle("Data Viewer")

        content = QWidget()
        layout = QHBoxLayout(content)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self.load_button = QPushButton("Load data")
        self.load_button.clicked.connect(self.load_data)
        left_layout.addWidget(self.load_button)

        self.table = QTableWidget(self.MAX_ROWS, 2)
        self.table.setHorizontalHeaderLabels(["x", "y"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        row_height = self.table.verticalHeader().defaultSectionSize()
        table_height = (
            row_height * self.VISIBLE_ROWS
            + self.table.horizontalHeader().height()
            + self.table.frameWidth() * 2
        )
        self.table.setFixedHeight(table_height)
        left_layout.addWidget(self.table)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout.addWidget(left_panel)
        layout.addWidget(self.canvas, stretch=1)
        self.setCentralWidget(content)

        self.draw_sine_wave()

    def load_data(self) -> None:
        pass

    def set_data(self, x_values: list[int | float], y_values: list[int | float]) -> None:
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length")
        if len(x_values) > self.MAX_ROWS:
            raise ValueError(f"Data cannot contain more than {self.MAX_ROWS} rows")

        self.table.clearContents()
        for row, (x_value, y_value) in enumerate(zip(x_values, y_values)):
            self.table.setItem(row, 0, QTableWidgetItem(str(x_value)))
            self.table.setItem(row, 1, QTableWidgetItem(str(y_value)))

    def draw_sine_wave(self) -> None:
        self.figure.clear()
        axes = self.figure.add_subplot(111)
        x_values = np.linspace(0, 2 * pi, 200)
        axes.plot(x_values, np.sin(x_values))
        axes.set_xlabel("x")
        axes.set_ylabel("y")
        axes.set_title("Sine wave")
        axes.grid(True)
        self.figure.tight_layout()
        self.canvas.draw()


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()
