# Man Hei Tristan Wong
# 4/4/2024
# Testing Functions for Final Project

import pytest
from pytest import approx
from final_project import heat_transfer

# Values input for temperature are displayed in Celsius / SI units
def test_heat_transfer_ice():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of ice with an absolute approximate tolerance of 1e-4 (0.0001)
        
        Parameters: none
        Return: none"""
    
    # tests for ice to ice
    assert heat_transfer("ice", "ice", 2.5, -32, -1) == approx(161975, abs=1e-4)
    assert heat_transfer("ice", "ice", 17, -47, -19) == approx(994840, abs=1e-4)
    assert heat_transfer("ice", "ice", 7.2, -83.44, -9.08) == approx(1118969.28, abs=1e-4)
    assert heat_transfer("ice", "ice", 0.26, -94.5, -91.3) == approx(1738.88, abs=1e-4)
    assert heat_transfer("ice", "ice", 5.234, -54.655, -13.618) == approx(448906.2052, abs=1e-4)


def test_heat_transfer_water():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of water with an absolute approximate tolerance of 1e-4 (0.0001)
        or 1e-6 (0.000001) for results with more than 4 decimal places
        
        Parameters: none
        Return: none"""
    
    # tests for water to water
    assert heat_transfer("water", "water", 8.2, 3, 12) == approx(308926.8, abs=1e-4)
    assert heat_transfer("water", "water", 11, 54, 57) == approx(138138, abs=1e-4)
    assert heat_transfer("water", "water", 0.1, 43.25, 65.26) == approx(9213.386, abs=1e-4)
    assert heat_transfer("water", "water", 0.346, 22.356, 25.677) == approx(4809.990276, abs=1e-6)
    assert heat_transfer("water", "water", 23.263, 74.635, 78.715) == approx(397305.9854, abs=1e-4)


def test_heat_transfer_steam():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of steam with an absolute approximate toleranceof 1e-4 (0.0001)
        or 1e-6 (0.000001) for results with more than 4 decimal places
        
        Parameters: none
        Return: none"""
    
    # tests for steam to steam
    assert heat_transfer("steam", "steam", 1.6, 110, 142) == approx(103782.4, abs=1e-4)
    assert heat_transfer("steam", "steam", 0.21, 166.6, 178.4) == approx(5022.906, abs=1e-4)
    assert heat_transfer("steam", "steam", 0.031, 178.13, 192.168) == approx(882.105806, abs=1e-6)
    assert heat_transfer("steam", "steam", 0.0054, 138.468, 159.168) == approx(226.57806, abs=1e-6)
    assert heat_transfer("steam", "steam", 0.00168, 153.362, 168.591) == approx(51.86022744, abs=1e-6)


def test_heat_transfer_ice_water():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of ice to water or water to ice with an absolute approximate tolerance
        of 1e-4 (0.0001) or 1e-6 (0.000001) for results with more than 4 decimal places
        
        Paramters: none
        Return: none"""
    
    # tests for ice to water
    assert heat_transfer("ice", "water", 1.2, -14, 31) == approx(591631.2, abs=1e-4)
    assert heat_transfer("ice", "water", 0.51, -7.1, 48.3) == approx(281021.628, abs=1e-4)
    assert heat_transfer("ice", "water", 0.449, -41.11, 2.82) == approx(193844.2646, abs=1e-4)
    assert heat_transfer("ice", "water", 0.018, -69.812, 5.871) == approx(9080.695548, abs=1e-6)
    assert heat_transfer("ice", "water", 0.0064, -66.015, 79.318) == approx(5145.577587, abs=1e-6)
    
    # tests for water to ice
    assert heat_transfer("water", "ice", 2.7, 81, -33) == approx(2003497.2, abs=1e-4)
    assert heat_transfer("water", "ice", 0.44, 33.1, -7.5) == approx(214821.904, abs=1e-4)
    assert heat_transfer("water", "ice", 0.117, 15.89, -64.49) == approx(62630.05788, abs=1e-6)
    assert heat_transfer("water", "ice", 0.584, 32.47, -20.11) == approx(298978.4029, abs=1e-4)
    assert heat_transfer("water", "ice", 0.0079, 2.099, -7.108) == approx(2825.372859, abs=1e-6)


def test_heat_transfer_water_steam():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of water to steam or steam to water with an absolute approximate
        tolerance of 1e-4 (0.0001) or 1e-6 (0.000001) for results with more than
        4 decimal places.
        
        Parameters: none
        Return: none"""
    
    # tests for water to steam
    assert heat_transfer("water", "steam", 3, 13, 124) == approx(8018490, abs=1e-4)
    assert heat_transfer("water", "steam", 1.7, 51.2, 111.1) == approx(4227520.05, abs=1e-4)
    assert heat_transfer("water", "steam", 0.26, 34.21, 170.87) == approx(696553.1118, abs=1e-4)
    assert heat_transfer("water", "steam", 0.05, 72.89, 104.287) == approx(119108.6105, abs=1e-4)
    assert heat_transfer("water", "steam", 0.0023, 97.354, 102.896) == approx(5236.9766, abs=1e-4)
    
    # tests for steam to water
    assert heat_transfer("steam", "water", 1, 142, 23) == approx(2667456, abs=1e-4)
    assert heat_transfer("steam", "water", 1.7, 145.2, 10.4) == approx(4635366.2, abs=1e-4)
    assert heat_transfer("steam", "water", 0.96, 135.64, 65.68) == approx(2376869.568, abs=1e-4)
    assert heat_transfer("steam", "water", 0.365, 138.583, 2.351) == approx(1002642.756, abs=1e-4)
    assert heat_transfer("steam", "water", 0.0135, 102.416, 93.512) == approx(30942.756, abs=1e-4)


def test_heat_transfer_ice_steam():
    """Test that the heat_transfer function returns the correct results for energy
        transfer of ice to steam or steam to ice with an absolute approximate
        tolerance of 1e-4 (0.0001) or 1e-6 (0.000001) for results with more than
        4 decimal places.
        
        Parameters: none
        Return: none"""
    
    # tests for ice to steam
    assert heat_transfer("ice", "steam", 2, -19, 145) == approx(6287050, abs=1e-4)
    assert heat_transfer("ice", "steam", 0.1, -3, 101) == approx(302089.7, abs=1e-4)
    assert heat_transfer("ice", "steam", 0.057, -1.68, 108.17) == approx(172862.292, abs=1e-4)

    # tests for steam to ice
    assert heat_transfer("steam", "ice", 1, 111, -1) == approx(3036987, abs=1e-4)
    assert heat_transfer("steam", "ice", 0.2, 101, -4) == approx(604597.4, abs=1e-4)
    assert heat_transfer("steam", "ice", 0.036, 143.63, -6.381) == approx(112117.4748, abs=1e-4)


pytest.main(["-v", "--tb=line", "-rN", __file__])