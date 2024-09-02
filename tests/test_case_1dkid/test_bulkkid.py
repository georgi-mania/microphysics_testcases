"""
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: test_bulkkid.py
Project: test_case_1dkid
Created Date: Monday 2nd September 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Monday 2nd September 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# %% Function definitions
import numpy as np
from pathlib import Path
from PyMPDATA_examples.Shipway_and_Hill_2012 import si

from .perform_1dkid_test_case import perform_1dkid_test_case
from libs.thermo.thermodynamics import Thermodynamics
from libs.kid_bulk_microphysics.bulk_scheme_condensation import (
    MicrophysicsSchemeWrapper,
)

# TODO(CB): add documentation


def test_mock_py_0dparcel():
    """runs test of 1-D KiD rainshaft model using bulk scheme extracted from pyMPDATA for
    microphysics scheme.

    This function sets up initial conditions and parameters for running a 1-D KiD rainshaft
    test case using the bulk microphysics scheme for condensation from the Shipway and Hill 2012
    pyMPDATA-examples example (via a wrapper). It then runs the test case as specified.
    """
    ### label for test case to name data/plots with
    run_name = "bulkkid_microphys_1dkid"

    ### path to directory to save data/plots in after model run
    binpath = Path(__file__).parent.resolve() / "bin"  # i.e. [current directory]/bin/
    binpath.mkdir(parents=False, exist_ok=True)

    ### time and grid parameters
    z_delta = 25 * si.m
    z_max = 3200 * si.m
    timestep = 0.25 / 2 * si.s
    time_end = 15 * si.minutes

    ### initial thermodynamic conditions
    assert z_max % z_delta == 0, "z limit is not a multiple of the grid spacing."
    zeros = np.zeros(int(z_max / z_delta))
    thermo_init = Thermodynamics(
        zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros, zeros
    )

    ### microphysics scheme to use (within a wrapper)
    microphys_scheme = MicrophysicsSchemeWrapper()

    ### Perform test of 1-D KiD rainshaft model using chosen setup
    perform_1dkid_test_case(
        z_delta,
        z_max,
        time_end,
        timestep,
        thermo_init,
        microphys_scheme,
        binpath,
        run_name,
    )


# # %% Run 1-D KiD Model
# outputs = {}
# output = {
#     k: np.zeros((kiddyn.settings.nz, kiddyn.settings.nt + 1))
#     for k in ("qv", "S", "ql", "act_frac", "reldisp")
# }
# outputs[kiddyn.key] = output
# assert "t" not in output and "z" not in output
# output["t"] = np.linspace(
#     0, kiddyn.settings.nt * kiddyn.settings.dt, kiddyn.settings.nt + 1, endpoint=True
# )
# output["z"] = np.linspace(
#     kiddyn.settings.dz / 2,
#     (kiddyn.settings.nz - 1 / 2) * kiddyn.settings.dz,
#     kiddyn.settings.nz,
#     endpoint=True,
# )
# output["qv"][:, 0] = kiddyn.mpdata["qv"].advectee.get()

# [HERE runs model]

# output["ql"][:, t + 1] = ql
# output["qv"][:, t + 1] = qv
# output["S"][:, t + 1] = RH - 1


# # %% plot results
# cmap = "gray"
# rasterized = False
# figsize = (3.5, 3.5)
# print(kiddyn.key)

# kid.plot(
#     var="qv",
#     mult=1e3,
#     label="$q_v$ [g/kg]",
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap,
#     threshold=1e-3,
# )
# savename = binpath / "kid1d_qvap.png"
# plt.savefig(savename, bbox_inches="tight")

# kid.plot(
#     var="ql",
#     mult=1e3,
#     label="$q_l$ [g/kg]",
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap,
#     threshold=1e-3,
#     figsize=figsize,
# )
# savename = binpath / "kid1d_qcond.png"
# plt.savefig(savename, bbox_inches="tight")

# kid.plot(
#     var="S",
#     mult=1e2,
#     label="$S$ [%]",
#     rng=(-0.25, 0.75),
#     output=outputs[f"{kiddyn.key}"],
#     cmap=cmap + "_r",
#     figsize=figsize,
# )
# savename = binpath / "kid1d_supersat.png"
# plt.savefig(savename, bbox_inches="tight")
