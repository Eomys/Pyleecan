# -*- coding: utf-8 -*-

# File generated according to SimuWidget.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SimuWidget(object):
    def setupUi(self, SimuWidget):
        if not SimuWidget.objectName():
            SimuWidget.setObjectName(u"SimuWidget")
        SimuWidget.resize(685, 564)
        self.Start = QPushButton(SimuWidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(280, 240, 131, 31))
        self.LoadMotor = QGroupBox(SimuWidget)
        self.LoadMotor.setObjectName(u"LoadMotor")
        self.LoadMotor.setGeometry(QRect(30, 10, 231, 111))
        self.Motor = QLineEdit(self.LoadMotor)
        self.Motor.setObjectName(u"Motor")
        self.Motor.setGeometry(QRect(20, 30, 191, 20))
        self.Open = QPushButton(self.LoadMotor)
        self.Open.setObjectName(u"Open")
        self.Open.setGeometry(QRect(20, 60, 191, 28))
        self.Open.setToolTipDuration(-7)
        self.ChooseSimu = QGroupBox(SimuWidget)
        self.ChooseSimu.setObjectName(u"ChooseSimu")
        self.ChooseSimu.setGeometry(QRect(30, 130, 231, 121))
        self.FindNom = QRadioButton(self.ChooseSimu)
        self.FindNom.setObjectName(u"FindNom")
        self.FindNom.setGeometry(QRect(10, 30, 201, 20))
        self.FindNom.setChecked(True)
        self.SpecificRPM = QRadioButton(self.ChooseSimu)
        self.SpecificRPM.setObjectName(u"SpecificRPM")
        self.SpecificRPM.setGeometry(QRect(10, 90, 141, 20))
        self.TorqueSlip = QRadioButton(self.ChooseSimu)
        self.TorqueSlip.setObjectName(u"TorqueSlip")
        self.TorqueSlip.setGeometry(QRect(10, 60, 181, 20))
        self.InputBox = QGroupBox(SimuWidget)
        self.InputBox.setObjectName(u"InputBox")
        self.InputBox.setGeometry(QRect(280, 10, 361, 221))
        self.TorqueBullet = QRadioButton(self.InputBox)
        self.TorqueBullet.setObjectName(u"TorqueBullet")
        self.TorqueBullet.setGeometry(QRect(10, 150, 111, 20))
        self.TorqueBullet.setChecked(True)
        self.RPMInput = QLineEdit(self.InputBox)
        self.RPMInput.setObjectName(u"RPMInput")
        self.RPMInput.setEnabled(False)
        self.RPMInput.setGeometry(QRect(120, 90, 113, 20))
        self.FreqInput = QLineEdit(self.InputBox)
        self.FreqInput.setObjectName(u"FreqInput")
        self.FreqInput.setGeometry(QRect(120, 60, 113, 20))
        self.label_8 = QLabel(self.InputBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 180, 71, 16))
        self.PowerBullet = QRadioButton(self.InputBox)
        self.PowerBullet.setObjectName(u"PowerBullet")
        self.PowerBullet.setGeometry(QRect(10, 180, 101, 20))
        self.TorqueInput = QLineEdit(self.InputBox)
        self.TorqueInput.setObjectName(u"TorqueInput")
        self.TorqueInput.setGeometry(QRect(120, 150, 113, 20))
        self.label_7 = QLabel(self.InputBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 150, 21, 16))
        self.label_15 = QLabel(self.InputBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 90, 91, 16))
        self.PowerInput = QLineEdit(self.InputBox)
        self.PowerInput.setObjectName(u"PowerInput")
        self.PowerInput.setEnabled(False)
        self.PowerInput.setGeometry(QRect(120, 180, 113, 20))
        self.label_2 = QLabel(self.InputBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 91, 16))
        self.label_3 = QLabel(self.InputBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 30, 21, 16))
        self.label_4 = QLabel(self.InputBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 60, 21, 16))
        self.VoltageInput = QLineEdit(self.InputBox)
        self.VoltageInput.setObjectName(u"VoltageInput")
        self.VoltageInput.setGeometry(QRect(120, 30, 113, 20))
        self.label_5 = QLabel(self.InputBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 90, 71, 16))
        self.label = QLabel(self.InputBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.label_16 = QLabel(self.InputBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 120, 331, 16))
        self.Save = QPushButton(SimuWidget)
        self.Save.setObjectName(u"Save")
        self.Save.setEnabled(False)
        self.Save.setGeometry(QRect(510, 240, 131, 31))
        self.OutputBox = QGroupBox(SimuWidget)
        self.OutputBox.setObjectName(u"OutputBox")
        self.OutputBox.setGeometry(QRect(30, 280, 241, 251))
        self.label_12 = QLabel(self.OutputBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 30, 81, 16))
        self.label_9 = QLabel(self.OutputBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 90, 55, 16))
        self.label_10 = QLabel(self.OutputBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 120, 81, 16))
        self.label_11 = QLabel(self.OutputBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 150, 91, 16))
        self.label_6 = QLabel(self.OutputBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 55, 16))
        self.PowerOut = QLabel(self.OutputBox)
        self.PowerOut.setObjectName(u"PowerOut")
        self.PowerOut.setGeometry(QRect(120, 30, 81, 16))
        self.SpeedOut = QLabel(self.OutputBox)
        self.SpeedOut.setObjectName(u"SpeedOut")
        self.SpeedOut.setGeometry(QRect(120, 120, 81, 16))
        self.SlipOut = QLabel(self.OutputBox)
        self.SlipOut.setObjectName(u"SlipOut")
        self.SlipOut.setGeometry(QRect(120, 90, 55, 16))
        self.StatorCurOut = QLabel(self.OutputBox)
        self.StatorCurOut.setObjectName(u"StatorCurOut")
        self.StatorCurOut.setGeometry(QRect(120, 150, 81, 16))
        self.TorqueOut = QLabel(self.OutputBox)
        self.TorqueOut.setObjectName(u"TorqueOut")
        self.TorqueOut.setGeometry(QRect(120, 60, 55, 16))
        self.label_19 = QLabel(self.OutputBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(190, 30, 81, 16))
        self.label_20 = QLabel(self.OutputBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(190, 120, 81, 16))
        self.label_21 = QLabel(self.OutputBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(190, 90, 55, 16))
        self.label_22 = QLabel(self.OutputBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(190, 150, 81, 16))
        self.label_23 = QLabel(self.OutputBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(190, 60, 55, 16))
        self.label_25 = QLabel(self.OutputBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 210, 101, 16))
        self.OhmicLossOut = QLabel(self.OutputBox)
        self.OhmicLossOut.setObjectName(u"OhmicLossOut")
        self.OhmicLossOut.setGeometry(QRect(120, 210, 81, 16))
        self.label_29 = QLabel(self.OutputBox)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(190, 210, 81, 16))
        self.RotorCurOut = QLabel(self.OutputBox)
        self.RotorCurOut.setObjectName(u"RotorCurOut")
        self.RotorCurOut.setGeometry(QRect(120, 180, 81, 16))
        self.label_38 = QLabel(self.OutputBox)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(20, 180, 81, 16))
        self.label_39 = QLabel(self.OutputBox)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(190, 180, 81, 16))
        self.EECBox = QGroupBox(SimuWidget)
        self.EECBox.setObjectName(u"EECBox")
        self.EECBox.setGeometry(QRect(300, 280, 291, 191))
        self.label_35 = QLabel(self.EECBox)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(220, 30, 81, 16))
        self.EECRr = QLabel(self.EECBox)
        self.EECRr.setObjectName(u"EECRr")
        self.EECRr.setGeometry(QRect(150, 60, 81, 16))
        self.label_43 = QLabel(self.EECBox)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 120, 141, 16))
        self.EECLr = QLabel(self.EECBox)
        self.EECLr.setObjectName(u"EECLr")
        self.EECLr.setGeometry(QRect(150, 120, 81, 16))
        self.EECLs = QLabel(self.EECBox)
        self.EECLs.setObjectName(u"EECLs")
        self.EECLs.setGeometry(QRect(150, 90, 81, 16))
        self.label_37 = QLabel(self.EECBox)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 90, 131, 16))
        self.label_42 = QLabel(self.EECBox)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(220, 120, 81, 16))
        self.label_41 = QLabel(self.EECBox)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(220, 90, 81, 16))
        self.label_31 = QLabel(self.EECBox)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 30, 131, 16))
        self.label_32 = QLabel(self.EECBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 60, 141, 16))
        self.EECRs = QLabel(self.EECBox)
        self.EECRs.setObjectName(u"EECRs")
        self.EECRs.setGeometry(QRect(150, 30, 81, 16))
        self.label_33 = QLabel(self.EECBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(220, 60, 81, 16))
        self.label_51 = QLabel(self.EECBox)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 150, 141, 16))
        self.EECLm = QLabel(self.EECBox)
        self.EECLm.setObjectName(u"EECLm")
        self.EECLm.setGeometry(QRect(150, 150, 81, 16))
        self.label_53 = QLabel(self.EECBox)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(220, 150, 81, 16))
        self.Error = QLabel(SimuWidget)
        self.Error.setObjectName(u"Error")
        self.Error.setGeometry(QRect(290, 240, 351, 16))
        QWidget.setTabOrder(self.Motor, self.Open)
        QWidget.setTabOrder(self.Open, self.FindNom)
        QWidget.setTabOrder(self.FindNom, self.TorqueSlip)
        QWidget.setTabOrder(self.TorqueSlip, self.SpecificRPM)
        QWidget.setTabOrder(self.SpecificRPM, self.VoltageInput)
        QWidget.setTabOrder(self.VoltageInput, self.FreqInput)
        QWidget.setTabOrder(self.FreqInput, self.RPMInput)
        QWidget.setTabOrder(self.RPMInput, self.TorqueBullet)
        QWidget.setTabOrder(self.TorqueBullet, self.PowerBullet)
        QWidget.setTabOrder(self.PowerBullet, self.TorqueInput)
        QWidget.setTabOrder(self.TorqueInput, self.PowerInput)
        QWidget.setTabOrder(self.PowerInput, self.Start)
        QWidget.setTabOrder(self.Start, self.Save)

        self.retranslateUi(SimuWidget)

        QMetaObject.connectSlotsByName(SimuWidget)
    # setupUi

    def retranslateUi(self, SimuWidget):
        SimuWidget.setWindowTitle(QCoreApplication.translate("SimuWidget", u"SimuWidget", None))
        self.Start.setText(QCoreApplication.translate("SimuWidget", u"Start", None))
        self.LoadMotor.setTitle(QCoreApplication.translate("SimuWidget", u"Load motor design", None))
        self.Motor.setText("")
        self.Open.setText(QCoreApplication.translate("SimuWidget", u"Load", None))
        self.ChooseSimu.setTitle(QCoreApplication.translate("SimuWidget", u"Choose Simulation", None))
        self.FindNom.setText(QCoreApplication.translate("SimuWidget", u"Find nominal speed", None))
        self.SpecificRPM.setText(QCoreApplication.translate("SimuWidget", u"Specific speed", None))
        self.TorqueSlip.setText(QCoreApplication.translate("SimuWidget", u"Make torque/power curve", None))
        self.InputBox.setTitle(QCoreApplication.translate("SimuWidget", u"Input", None))
        self.TorqueBullet.setText(QCoreApplication.translate("SimuWidget", u"Torque", None))
        self.label_8.setText(QCoreApplication.translate("SimuWidget", u"kW", None))
        self.PowerBullet.setText(QCoreApplication.translate("SimuWidget", u"Power", None))
        self.label_7.setText(QCoreApplication.translate("SimuWidget", u"Nm", None))
        self.label_15.setText(QCoreApplication.translate("SimuWidget", u"Speed", None))
        self.label_2.setText(QCoreApplication.translate("SimuWidget", u"Frequency", None))
        self.label_3.setText(QCoreApplication.translate("SimuWidget", u"V", None))
        self.label_4.setText(QCoreApplication.translate("SimuWidget", u"Hz", None))
        self.label_5.setText(QCoreApplication.translate("SimuWidget", u"rpm", None))
        self.label.setText(QCoreApplication.translate("SimuWidget", u"Voltage", None))
        self.label_16.setText(QCoreApplication.translate("SimuWidget", u"Desired Torque or Power", None))
        self.Save.setText(QCoreApplication.translate("SimuWidget", u"Save results", None))
        self.OutputBox.setTitle(QCoreApplication.translate("SimuWidget", u"Output", None))
        self.label_12.setText(QCoreApplication.translate("SimuWidget", u"Power:", None))
        self.label_9.setText(QCoreApplication.translate("SimuWidget", u"Slip:", None))
        self.label_10.setText(QCoreApplication.translate("SimuWidget", u"Speed:", None))
        self.label_11.setText(QCoreApplication.translate("SimuWidget", u"Stator current:", None))
        self.label_6.setText(QCoreApplication.translate("SimuWidget", u"Torque:", None))
        self.PowerOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.SpeedOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.SlipOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.StatorCurOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.TorqueOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_19.setText(QCoreApplication.translate("SimuWidget", u"kW", None))
        self.label_20.setText(QCoreApplication.translate("SimuWidget", u"rpm", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("SimuWidget", u"A", None))
        self.label_23.setText(QCoreApplication.translate("SimuWidget", u"Nm", None))
        self.label_25.setText(QCoreApplication.translate("SimuWidget", u"Ohmic loss:", None))
        self.OhmicLossOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_29.setText(QCoreApplication.translate("SimuWidget", u"kW", None))
        self.RotorCurOut.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_38.setText(QCoreApplication.translate("SimuWidget", u"Rotor current:", None))
        self.label_39.setText(QCoreApplication.translate("SimuWidget", u"A", None))
        self.EECBox.setTitle(QCoreApplication.translate("SimuWidget", u"EEC parameters", None))
        self.label_35.setText(QCoreApplication.translate("SimuWidget", u"Ohm", None))
        self.EECRr.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_43.setText(QCoreApplication.translate("SimuWidget", u"Lr:", None))
        self.EECLr.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.EECLs.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_37.setText(QCoreApplication.translate("SimuWidget", u"Ls:", None))
        self.label_42.setText(QCoreApplication.translate("SimuWidget", u"H", None))
        self.label_41.setText(QCoreApplication.translate("SimuWidget", u"H", None))
        self.label_31.setText(QCoreApplication.translate("SimuWidget", u"Rs:", None))
        self.label_32.setText(QCoreApplication.translate("SimuWidget", u"Rr:", None))
        self.EECRs.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_33.setText(QCoreApplication.translate("SimuWidget", u"Ohm", None))
        self.label_51.setText(QCoreApplication.translate("SimuWidget", u"Lm:", None))
        self.EECLm.setText(QCoreApplication.translate("SimuWidget", u"-", None))
        self.label_53.setText(QCoreApplication.translate("SimuWidget", u"H", None))
        self.Error.setText("")
    # retranslateUi

