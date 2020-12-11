# -*- coding: utf-8 -*-

import sys
from os import listdir, mkdir, remove
from os.path import abspath, basename, isdir, isfile, join
from shutil import copyfile, rmtree

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QDialogButtonBox

from pyleecan.Functions.load import load
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from Tests import TEST_DATA_DIR
from Tests import save_load_path as save_path


import pytest


@pytest.mark.GUI
class Testsave_load_matlib(object):
    """Test that the widget DMachineSetup and DMatLib can save/load the MatLib (old and new)"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        work_path = join(save_path, "Material")
        # Delete old test if needed
        if isdir(work_path):
            rmtree(work_path)
        mkdir(work_path)

        yield {"work_path": work_path}

        self.app.quit()

        rmtree(work_path)

    def test_load_save_several_file(self, setup):
        """Check that you can load/save several machine files"""
        # Copy the matlib
        mkdir(join(setup["work_path"], "Lamination"))
        mkdir(join(setup["work_path"], "Magnet"))
        copyfile(
            join(TEST_DATA_DIR, "Material", "Magnet1.json"),
            join(setup["work_path"], "Magnet", "Magnet1.json"),
        )
        cop_path = join(setup["work_path"], "Copper1.json")
        copyfile(join(TEST_DATA_DIR, "Material", "Copper1.json"), cop_path)
        copyfile(
            join(TEST_DATA_DIR, "Material", "Insulator1.json"),
            join(setup["work_path"], "Insulator1.json"),
        )
        lam_path = join(setup["work_path"], "Lamination", "M400-50A.json")
        copyfile(join(TEST_DATA_DIR, "Material", "M400-50A.json"), lam_path)
        nb_file = len(
            [
                name
                for name in listdir(setup["work_path"])
                if isfile(join(setup["work_path"], name)) and name[-5:] == ".json"
            ]
        )
        assert nb_file == 2

        # Start the GUI
        self.matlib = MatLib(setup["work_path"])
        self.mat_widget = DMatLib(matlib=self.matlib)
        self.widget = DMachineSetup(
            dmatlib=self.mat_widget, machine=None, machine_path=setup["work_path"]
        )
        # Check load of the matlib
        assert len(self.matlib.dict_mat["RefMatLib"]) == 4
        assert ["Copper1", "Insulator1", "M400-50A", "Magnet1"] == [
            mat.name for mat in self.matlib.dict_mat["RefMatLib"]
        ]

        assert self.matlib.dict_mat["RefMatLib"][0].elec.rho == 1.73e-8
        assert self.matlib.dict_mat["RefMatLib"][0].HT.alpha == 0.00393
        assert self.matlib.dict_mat["RefMatLib"][0].path == join(
            setup["work_path"], "Copper1.json"
        ).replace("\\", "/")

        assert self.matlib.dict_mat["RefMatLib"][2].mag.mur_lin == 2500
        assert self.matlib.dict_mat["RefMatLib"][2].struct.rho == 7650
        assert self.matlib.dict_mat["RefMatLib"][2].struct.Ex == 215000000000
        assert self.matlib.dict_mat["RefMatLib"][2].path == join(
            setup["work_path"], "Lamination", "M400-50A.json"
        ).replace("\\", "/")
        # Change value of materials
        self.matlib.dict_mat["RefMatLib"][0].elec.rho = 1.74e-8
        self.matlib.dict_mat["RefMatLib"][0].HT.alpha = 0.00555
        self.matlib.dict_mat["RefMatLib"][2].mag.mur_lin = 2501.2
        self.matlib.dict_mat["RefMatLib"][2].struct.rho = 76
        # Save matlib
        for mat in self.matlib.dict_mat["RefMatLib"]:
            mat.save(mat.path)
            mat2 = load(mat.path)
            assert mat.as_dict() == mat2.as_dict()


def compare_file(file_path1, file_path2):
    # name1 = basename(file_path1)
    # name2 = basename(file_path2)
    # if name1 != name2:
    #     return "Different file name: (" + name1 + ", " + name2 + ")"
    with open(file_path1) as file1:
        with open(file_path2) as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            if len(lines1) != len(lines2):
                return (
                    "Different file length: ("
                    + str(len(lines1))
                    + ", "
                    + str(len(lines2))
                    + ")"
                )
            for ii in range(len(lines1)):
                if lines1[ii] != lines2[ii]:
                    return (
                        "Different line "
                        + str(ii)
                        + ":\n"
                        + lines1[ii]
                        + "\n"
                        + lines2[ii]
                    )
    return None
