# -*- coding: utf-8 -*-
import pytest

from os.path import join
from numpy import (
    zeros,
    exp,
    pi,
    real,
    meshgrid,
    mean,
)
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path

DELTA = 1e-6

# Load machine
IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
# Prepare simulation
simu = Simu1(name="AC_IPMSM_plot", machine=IPMSM_A)

simu.input = InputCurrent(
    Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=4 * 2 ** 4, N0=1200
)

simu.elec = None

simu.mag = MagFEMM(
    type_BH_stator=1,
    type_BH_rotor=1,
    is_periodicity_a=False,
    is_periodicity_t=False,
)
simu.force = ForceMT(
    is_periodicity_a=False,
    is_periodicity_t=False,
)


@pytest.mark.validation
@pytest.mark.Force
@pytest.mark.long
def test_AC_IPMSM_AGSF_spectrum_no_sym():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Run simulation
    out = simu.run()

    # Test 1: No sym
    AGSF = out.force.AGSF

    arg_list = ["time", "angle"]
    result1 = AGSF.get_rphiz_along(*arg_list)
    Prad = result1["radial"]
    time = result1["time"]
    angle = result1["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    # Check time_to_freq reversibility
    AGSF_rad_freq = AGSF.components["radial"].time_to_freq()
    result_frq = AGSF_rad_freq.get_along(*arg_list)
    Prad_frq = result_frq["AGSF_r"]

    AGSF2 = AGSF_rad_freq.freq_to_time()
    result2 = AGSF2.get_along(*arg_list)
    Prad2 = result2["AGSF_r"]

    assert_array_almost_equal(Prad_frq, Prad, decimal=5)
    assert_array_almost_equal(Prad2, Prad, decimal=5)

    # Check time-space reconstruction
    arg_list = ["time", "angle"]
    result3 = AGSF.get_rphiz_along(*arg_list)
    Prad = result3["radial"]
    time = result3["time"]
    angle = result3["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    arg_list = ["freqs", "wavenumber"]
    result_freq = AGSF.get_rphiz_along(*arg_list)
    Prad_wr = result_freq["radial"]
    freqs_AGSF = result_freq["freqs"]
    wavenumber = result_freq["wavenumber"]
    Nf = len(freqs_AGSF)
    Nr = len(wavenumber)

    XP_rad1 = zeros(Prad.shape)

    # Since only positive frequency were extracted, the correct sum must be on the the real part
    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs_AGSF[ifrq]
            XP_rad1 = XP_rad1 + real(
                Prad_wr[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    # assert_array_almost_equal(XP_rad1, Prad, decimal=2)
    test = abs(XP_rad1 - Prad) / mean(XP_rad1)
    assert_array_almost_equal(test, 0, decimal=1)  # Less than 10% error

    return out


@pytest.mark.validation
@pytest.mark.Force
@pytest.mark.long
def test_AC_IPMSM_AGSF_spectrum_sym():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Test 2 : With sym
    simu2 = simu.copy()

    simu2.mag.is_periodicity_a = True
    simu2.mag.is_periodicity_t = True

    simu2.force.is_periodicity_a = True
    simu2.force.is_periodicity_t = True

    out = simu2.run()

    AGSF = out.force.AGSF

    arg_list = ["time", "angle"]
    result = AGSF.get_rphiz_along(*arg_list)
    Prad = result["radial"]
    time = result["time"]
    angle = result["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    # Check time_to_freq reversibility
    AGSF_rad_freq = AGSF.components["radial"].time_to_freq()
    result_frq = AGSF_rad_freq.get_along(*arg_list)
    Prad_frq = result_frq["AGSF_r"]

    AGSF2 = AGSF_rad_freq.freq_to_time()
    result2 = AGSF2.get_along(*arg_list)
    Prad2 = result2["AGSF_r"]

    assert_array_almost_equal(Prad_frq, Prad, decimal=5)
    assert_array_almost_equal(Prad2, Prad, decimal=5)

    # Check time-space reconstruction
    arg_list = ["freqs", "wavenumber"]
    result_freq = AGSF.get_rphiz_along(*arg_list)
    Prad_wr = result_freq["radial"]
    freqs_AGSF = result_freq["freqs"]
    wavenumber = result_freq["wavenumber"]
    Nf = len(freqs_AGSF)
    Nr = len(wavenumber)

    XP_rad1 = zeros(Prad.shape)

    # Since only positive frequency were extracted, the correct sum must be on the the real part
    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs_AGSF[ifrq]
            XP_rad1 = XP_rad1 + real(
                Prad_wr[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    # assert_array_almost_equal(XP_rad1, Prad, decimal=3)
    test = abs(XP_rad1 - Prad) / mean(XP_rad1)
    assert_array_almost_equal(test, 0, decimal=1)  # Less than 10% error

    return out


if __name__ == "__main__":

    out = test_AC_IPMSM_AGSF_spectrum_sym()
    out2 = test_AC_IPMSM_AGSF_spectrum_no_sym()

    out2.plot_2D_Data(
        "force.AGSF",
        "wavenumber",
        "freqs=160",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_AGSF_space_fft_freq160_no_sym.png"),
        is_show_fig=False,
    )
