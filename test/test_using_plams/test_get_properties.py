from nose.plugins.attrib import attr
from qmflows import (templates, run, molkit, dftb, adf)


@attr('slow')
def test_dftb_props():
    """
    Get properties from DFTB freq calc
    """

    mol = molkit.from_smiles('F[H]')
    result = run(dftb(templates.freq, mol, job_name='dftb_FH'))
    expected_energy = -4.76
    assert abs(result.energy - expected_energy) < 0.01
    assert len(result.dipole) == 3
    expected_frequency = 3460.92
    assert abs(result.frequencies - expected_frequency) < 0.1
    assert len(result.charges) == 2
    assert abs(result.charges[0] + result.charges[1]) < 1e-6


@attr('slow')
def test_adf_props():
    """
    Get properties from ADF freq calc
    """

    mol = molkit.from_smiles('F[H]')
    result = run(adf(templates.freq, mol, job_name='adf_FH'))
    expected_energy = -0.30
    assert abs(result.energy - expected_energy) < 0.01
    assert len(result.dipole) == 3
    expected_frequency = 3480.90
    assert abs(result.frequencies[1] - expected_frequency) < 0.1
    assert len(result.charges) == 2
    assert abs(result.charges[0] + result.charges[1]) < 1e-6
