# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from SciDataTool import DataTime, Data1D, DataLinspace, VectorField

from pyleecan.Classes.SolutionData import SolutionData
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Classes.SolutionVector import SolutionVector


@pytest.mark.MeshSol
@pytest.mark.METHODS
class Test_get_field(TestCase):
    """ Tests for get_field method from Solution classes"""

    def test_SolutionMat(self):
        DELTA = 1e-10

        solution = SolutionMat()
        solution.field = np.array([[1, 2, 3], [2, 3, 4]])
        solution.axis_name = ["time", "indice"]
        solution.axis_size = [2, 3]

        field = solution.get_field()

        correction = np.array([[1, 2, 3], [2, 3, 4]])
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        field = solution.get_field("time[0]", "indice[1,2]")

        correction = np.array([[2, 3]])
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

    def test_SolutionVector(self):
        DELTA = 1e-10

        Indices_Cell = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=1,
            number=10,
        )

        H = np.ones((10, 4, 2))

        # Store the results for H
        componentsH = {}

        Hx_data = DataTime(
            name="Magnetic Field Hx",
            unit="A/m",
            symbol="Hx",
            axes=[Time, Indices_Cell],
            values=H[:, :, 0],
        )
        componentsH["comp_x"] = Hx_data

        Hy_data = DataTime(
            name="Magnetic Field Hy",
            unit="A/m",
            symbol="Hy",
            axes=[Time, Indices_Cell],
            values=H[:, :, 1],
        )
        componentsH["comp_y"] = Hy_data
        vecH = VectorField(name="Magnetic Field", symbol="H", components=componentsH)
        solution = SolutionVector(field=vecH, type_cell="triangle", label="H")

        field = solution.get_field()

        correction = np.ones((10, 4, 2))
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        field = solution.get_field("time[0]", "indice[1,2]")

        correction = np.ones((2, 2))
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

    def test_SolutionData(self):
        DELTA = 1e-10

        Indices_Cell = Data1D(name="indice", values=[0, 1, 2, 4], is_components=True)
        Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=1,
            number=10,
        )

        # Store the results for H
        H = DataTime(
            name="Magnetic Field Hx",
            unit="A/m",
            symbol="Hx",
            axes=[Time, Indices_Cell],
            values=np.ones((10, 4)),
        )

        solution = SolutionData(field=H, type_cell="triangle", label="H")

        field = solution.get_field()

        correction = np.ones((10, 4))
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)

        field = solution.get_field("time[0]", "indice[1,2]")

        correction = correction[0, 1:3]
        result = np.sum(np.abs(correction - field))
        msg = "Wrong result: returned " + str(field) + ", expected: " + str(correction)
        self.assertAlmostEqual(result, 0, msg=msg, delta=DELTA)
