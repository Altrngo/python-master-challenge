from PySide2 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.c = currency_converter.CurrencyConverter()
    self.setWindowTitle("Convertisseur de Devises")
    self.setup_ui()
    self.set_default_values()
    self.setup_connections()
    self.setup_css()
    self.resize(500, 50)
  
  def setup_ui(self):
    self.layaout = QtWidgets.QHBoxLayout(self)
    self.cbb_deviseFrom = QtWidgets.QComboBox()
    self.spn_montant = QtWidgets.QSpinBox()
    self.cbb_deviseTo = QtWidgets.QComboBox()
    self.spn_montantConverti = QtWidgets.QSpinBox()
    self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
  
  def set_default_values(self):
    self.cbb_deviseFrom.addItems(sorted(list(self.c.currencies)))
    self.cbb_deviseTo.addItems(sorted(list(self.c.currencies)))
    self.cbb_deviseFrom.setCurrentText("EUR")
    self.cbb_deviseTo.setCurrentText("EUR")
    
    self.spn_montant.setValue(100)
    self.spn_montantConverti.setValue(100)
    self.spn_montantConverti.setRange(1, 1000000)
    
  def setup_connections(self):
    self.cbb_deviseFrom.activated.connect(self.compute)
    self.cbb_deviseTo.activated.connect(self.compute)
    self.spn_montant.valueChanged.connect(self.compute)
    self.btn_inverser.clicked.connect(self.inverser_devises)
  
  def setup_css(self):
    self.setStyleSheet("""
                       background-color: rgb(30, 30, 30);
                       color: rgb(240, 240, 240);
                       border: none;
                       """)
  
  
  def compute(self):
    montant = self.spn_montant.value()
    devise_from = self.cbb_deviseFrom.currentText()
    devise_To = self.cbb_deviseTo.currentText()
    try:
      resultat = self.c.convert(montant, devise_from, devise_To)
    except currency_converter.currency_converter.RateNotFoundError:
      print("La conversion n'a pas fonctionné.")
    else:
      self.spn_montantConverti.setValue(resultat)
  
  def inverser_devises(self):
    devise_from = self.cbb_deviseFrom.currentText()
    devise_To = self.cbb_deviseTo.currentText()
    self.cbb_deviseFrom.currentText(devise_To)
    self.cbb_deviseTo.currentText(devise_from)
  
    self.compute()
  
  
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()