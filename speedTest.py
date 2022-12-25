import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import speedtest

class SpeedTestWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to display the download speed
        self.download_label = QLabel("Download speed:")
        self.download_speed = QLabel("N/A")

        # Create a label to display the upload speed
        self.upload_label = QLabel("Upload speed:")
        self.upload_speed = QLabel("N/A")

        # Create a button to run the speed test
        self.test_button = QPushButton("Run speed test")
        self.test_button.clicked.connect(self.run_speed_test)

        # Create a layout to arrange the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.download_label)
        layout.addWidget(self.download_speed)
        layout.addWidget(self.upload_label)
        layout.addWidget(self.upload_speed)
        layout.addWidget(self.test_button)
        self.setLayout(layout)

    def run_speed_test(self):
        # Perform the speed test
        speed = speedtest.Speedtest()
        download_speed = speed.download()
        upload_speed = speed.upload()

        # Convert download and upload speeds to megabits per second (Mbps)
        download_speed_Mbps = download_speed / 1000000
        upload_speed_Mbps = upload_speed / 1000000

        # Update the labels with the results
        self.download_speed.setText(f"{download_speed_Mbps:.2f} Mbps")
        self.upload_speed.setText(f"{upload_speed_Mbps:.2f} Mbps")

if __name__ == '__main__':
    # Create the application and the main window
    app = QApplication(sys.argv)
    window = SpeedTestWindow()
    # Set the size and position of the window
    window.resize(400, 200)
    window.move(300, 300)

    # Display the window
    window.show()

    # Run the application loop
    sys.exit(app.exec_())


