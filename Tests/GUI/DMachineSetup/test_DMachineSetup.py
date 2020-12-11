# -*- coding: utf-8 -*-

from os.path import join, isfile
from os import remove
import sys

import mock  # for unittest of raw_input
from PySide2 import QtWidgets

from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from Tests import save_gui_path as save_path

from pyleecan.GUI.Dialog.DMachineSetup.SMachineType.SMachineType import SMachineType
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.SMagnet import SMagnet
from pyleecan.GUI.Dialog.DMachineSetup.SWindParam.SWindParam import SWindParam
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.SWindCond import SWindCond
from pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar import SBar
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.SWSlot import SWSlot
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
import matplotlib.pyplot as plt
from Tests import TEST_DATA_DIR

load_test = list()
load_test.append(  # 1
    {"type": "SCIM", "index": 0, "name": "SCIM_001", "p": 1, "count": 11}
)
load_test.append(  # 2
    {"type": "DFIM", "index": 1, "name": "DFIM_001", "p": 2, "count": 13}
)
load_test.append(  # 3
    {"type": "SyRM", "index": 2, "name": "SynRM_001", "p": 2, "count": 10}
)
load_test.append(  # 4
    {"type": "SPMSM", "index": 3, "name": "SPMSM_001", "p": 4, "count": 10}
)
load_test.append(  # 5
    {"type": "SIPMSM", "index": 4, "name": "SIPMSM_008", "p": 4, "count": 10}
)
load_test.append(  # 6
    {"type": "IPMSM", "index": 5, "name": "machine_IPMSM_A", "p": 5, "count": 10}
)
load_test.append(  # 7
    {"type": "WRSM", "index": 6, "name": "WRSM_001", "p": 6, "count": 13}
)
load_test.append(  # 8
    {"type": "SRM", "index": 7, "name": "SRM_test_load", "p": 10, "count": 10}
)
from PySide2.QtCore import Qt

ENABLE_ITEM = Qt.ItemIsSelectable | Qt.ItemIsEnabled


import pytest


matlib_path = join(TEST_DATA_DIR, "Material")


@pytest.mark.GUI
class TestDMachineSetup(object):
    """Test that the widget DMachineSetup behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        # MatLib widget
        matlib = MatLib(matlib_path)
        dmatlib = DMatLib(matlib=matlib)
        widget = DMachineSetup(
            dmatlib=dmatlib, machine_path=join(TEST_DATA_DIR, "Machine")
        )

        yield {"widget": widget}

        self.app.quit()

    @pytest.mark.parametrize("test_dict", load_test)
    def test_load(self, setup, test_dict):
        """Check that you can load a machine"""

        return_value = (
            join(join(TEST_DATA_DIR, "Load_GUI"), test_dict["name"] + ".json"),
            "Json (*.json)",
        )
        with mock.patch(
            "PySide2.QtWidgets.QFileDialog.getOpenFileName", return_value=return_value
        ):
            # To trigger the slot
            setup["widget"].b_load.clicked.emit()
        setup["widget"].nav_step.setCurrentRow(0)
        # To remember to update when adding a new machine type
        assert setup["widget"].w_step.c_type.count() == 8
        # Check load MachineType
        assert type(setup["widget"].w_step) == SMachineType
        assert setup["widget"].w_step.c_type.currentIndex() == test_dict["index"]
        assert setup["widget"].w_step.c_type.currentText() == test_dict["type"]
        assert setup["widget"].w_step.si_p.value() == test_dict["p"]
        assert setup["widget"].w_step.le_name.text() == test_dict["name"]
        # Check that the nav_step is correct
        assert setup["widget"].nav_step.count() == test_dict["count"]

    def test_set_save_machine_type(self, setup):
        """Check that the Widget allow to change the machine type and save"""
        # Check that all the machine type are available
        assert setup["widget"].w_step.c_type.count() == 8
        # DFIM
        setup["widget"].w_step.c_type.setCurrentIndex(1)
        assert setup["widget"].w_step.c_type.currentText() == "DFIM"
        assert type(setup["widget"].machine) == MachineDFIM
        save_function(setup["widget"], "test_dfim_save")
        # SyRM
        setup["widget"].w_step.c_type.setCurrentIndex(2)
        assert setup["widget"].w_step.c_type.currentText() == "SyRM"
        assert type(setup["widget"].machine) == MachineSyRM
        save_function(setup["widget"], "test_syrm_save")
        # SPMSM
        setup["widget"].w_step.c_type.setCurrentIndex(3)
        assert setup["widget"].w_step.c_type.currentText() == "SPMSM"
        assert type(setup["widget"].machine) == MachineSIPMSM
        save_function(setup["widget"], "test_spmsm_save")
        # SIPMSM
        setup["widget"].w_step.c_type.setCurrentIndex(4)
        assert setup["widget"].w_step.c_type.currentText() == "SIPMSM"
        assert type(setup["widget"].machine) == MachineSIPMSM
        save_function(setup["widget"], "test_sipmsm_save")
        # IPMSM
        setup["widget"].w_step.c_type.setCurrentIndex(5)
        assert setup["widget"].w_step.c_type.currentText() == "IPMSM"
        assert type(setup["widget"].machine) == MachineIPMSM
        save_function(setup["widget"], "test_ipmsm_save")
        # WRSM
        setup["widget"].w_step.c_type.setCurrentIndex(6)
        assert setup["widget"].w_step.c_type.currentText() == "WRSM"
        assert type(setup["widget"].machine) == MachineWRSM
        save_function(setup["widget"], "test_wrsm_save")
        # SRM
        setup["widget"].w_step.c_type.setCurrentIndex(7)
        assert setup["widget"].w_step.c_type.currentText() == "SRM"
        assert type(setup["widget"].machine) == MachineSRM
        save_function(setup["widget"], "test_srm_save")
        # SCIM
        setup["widget"].w_step.c_type.setCurrentIndex(0)
        assert setup["widget"].w_step.c_type.currentText() == "SCIM"
        assert type(setup["widget"].machine) == MachineSCIM


def save_function(widget, file_name):
    """Function to save a machine from the GUI"""
    file_path = join(save_path, file_name + ".json")

    # Check that the file didn't already exist
    if isfile(file_path):
        remove(file_path)
    assert not isfile(file_path)

    return_value = (file_path, "Json (*.json)")
    with mock.patch(
        "PySide2.QtWidgets.QFileDialog.getSaveFileName", return_value=return_value
    ):
        # To trigger the slot
        widget.b_save.clicked.emit()

    # Check that the file now exist => delete for next test
    assert isfile(file_path)
    remove(file_path)
    # Check that the GUI have been updated
    assert type(widget.w_step) == SMachineType
    assert widget.w_step.le_name.text() == file_name
