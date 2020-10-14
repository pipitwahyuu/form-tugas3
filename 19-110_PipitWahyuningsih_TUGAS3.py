from PyQt5.QtWidgets import*
import sys

#membuat fungsi untuk menentukan layout window
def window():
    #inisialisasi PyQt
    app = QApplication(sys.argv)
    window = QWidget()

    #menempelkan label pada window, setText, dan merubah tampilan pada text(bgcolor, fontcolor, size, menebalkan tulisan)
    labelku = QLabel(window)
    labelku.setText('Input Biodata')
    labelku.setStyleSheet("Font: Bold; color:#8B0000; background-color:#FF7F50;  font-size:24pt")

    #untuk menampilkan masukan form nama, alamat
    layout = QFormLayout()#dengan QFormLayout(kelas) kita bisa membagi layout menjadi 2 bagian. kiri untuk mengisi label, dan kanan untuk inputan
    layout.addRow(labelku)
    layout.addRow('Name', QLineEdit())
    layout.addRow('Address', QLineEdit())
    layout.addWidget(QLineEdit())

    #untuk menampilkan checkbox
    layout.addRow('Hobby', QCheckBox('Makan'))
    layout.addWidget(QCheckBox('Tidur'))
    layout.addWidget(QCheckBox('Main'))

    #untuk menampilkan radiobutton
    layout.addRow('Status', QRadioButton('Pelajar'))
    layout.addWidget(QRadioButton('Pegawai'))
    layout.addWidget(QRadioButton('Wiraswasta'))
    
    #menentukan ukuran window, Title, setLayout dan menampilkan
    window.setGeometry(400,100,700,500)
    window.setWindowTitle('Belajar PyQt5')
    window.show()
    window.setLayout(layout)
    sys.exit(app.exec_())

if __name__=='__main__':
    window()
