# Tristan Wong
# 2/12/2024
# test functions for the code of water_flow
# a test function for the kPa to Psi function is added to test if the values are correctly converted

from water_flow import water_column_height, pressure_gain_from_water_height, \
    pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, \
    pressure_loss_from_pipe_reduction, kpa_to_psi
from pytest import approx
import pytest

def test_water_column_height():
    '''Tests the water_column_height function
        
        Parameters: none
        Return: none'''
    
    # 4 test runs
    # Parameters: tower_height, tank_height
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9


def test_pressure_gain_from_water_height():
    '''Tests the pressure_gain_from_water_height function,
        with an approximate absolute tolerance of 0.001
        
        Parameters: none
        Return: none'''
    
    # 3 test runs
    # Parameter: height
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.0001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe():
    '''Tests the pressure_loss_from_pipe function,
        with an approximate absolute tolerance of 0.001
        
        Parameters: none
        Return: none'''
    
    # 7 test runs
    # Parameters: pipe_diameter, pipe_length, friction_factor, fluid_velocity
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)
    

def test_pressure_loss_from_fittings():
    '''Tests the pressure_loss_from_fttings function,
        with an approximate absolute tolerance of 0.001
        
        Parameters: none
        Return: none'''
    
    # 5 tests runs
    # Parameters: fluid_velocity, quantity_fittings
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
    '''Tests the reynolds_number function,
        with an approximate absolute tolerance of 1
        
        Parameters: none
        Return: none'''
    
    # 5 tests runs
    # Parameters: hydraulic_diamter, fluid_velocity
    assert reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.28687, 1.75) == approx(500318, abs=1)


def test_pressure_loss_from_pipe_reduction():
    '''Tests the pressure_loss_from_pipe_reduction,
        with an approximate absolute tolerance of 0.001
    
        Parameters: none
        Return: none'''
    
    # 3 test runs
    # Parameters: larger_diamter, fluid_velocity, reynolds_number, smaller_diameter
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)


def test_kpa_to_psi():
    '''Tests the kpa_to_psi function, 
        with an approximate absolute tolerance of 0.001
        
        Parameters: none
        Return: none'''
    
    # 7 test runs
    # Parameters: kpa
    assert kpa_to_psi(44) == approx(6.382, abs=0.001)
    assert kpa_to_psi(59.2) == approx(8.586, abs=0.001)
    assert kpa_to_psi(96.6) == approx(14.011, abs=0.001)
    assert kpa_to_psi(121.47) == approx(17.618, abs=0.001)
    assert kpa_to_psi(145.83) == approx(21.151, abs=0.001)
    assert kpa_to_psi(194.472) == approx(28.206, abs=0.001)
    assert kpa_to_psi(208.1639) == approx(30.192, abs=0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])