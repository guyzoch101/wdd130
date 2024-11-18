# Man Hei Tristan Wong
# 4/4/2024
# Final Project

from scipy import constants

# 2 modes for the code
heat_transfers = 1
gas_laws = 2


# Heat Transfers
def heat_transfer(initial_state, final_state, mass, initial_t, final_t):
    """This function takes in the states of the substance (water) that the user input,
        and uses the appropriate formulas to calculate the energy.
        
        Formulas:
            Heat transfer within 1 state: E = mcΔT
            Heat transfer when states are changing: E = m(lv) or m(lf)
            
            E = Energy in joules (J)
            m = mass of the substance in kg
            c = specific heat capacity of the substance in J kg^-1 C^-1
            ΔT = change in temperature in Celsius or Kelvin
                Kelvin = 273.15 + Celsius
            
            lv = latent heat of vaporization
            lf = latent heat of fusion
        
        Parameters:
            initial_state
            final_state
            mass = mass of substance
            initial_state = initial state of the substance
            final_state = final state of the subtance
        
        Return:
            total energy of the heat transfer process"""
        # only SI units can be used in this function
    
    # defining constants
    c_water = 4186
    lf = 334000
    lv = 2260000
    c_ice = 2090
    c_steam = 2027
    
    # lambda functions for the 3 formulas of heat transfer
    internal_energy_change = lambda m, c, t1, t2: m * c * (t2 - t1)
    ice_water = lambda m: m * lf
    water_steam = lambda m: m * lv
    
    # energy change without involving change of state
    if initial_state == final_state:
        if initial_state == final_state == "ice":
            c = c_ice
        
        elif initial_state == final_state == "water":
            c = c_water
        
        elif initial_state == final_state == "steam":
            c = c_steam
        
        energy = internal_energy_change(mass, c, initial_t, final_t)
    
    # energy change involving change of state
    elif initial_state != final_state:
        if (initial_state == "ice" and final_state == "water") \
            or (initial_state == "water" and final_state == "ice"):
            
            t1 = initial_t
            t2 = final_t
            
            if initial_state == "water" and final_state == "ice":
                # flipping the temperature
                t1 = final_t
                t2 = initial_t
            
            energy = internal_energy_change(mass, c_ice, t1, 0) + ice_water(mass) \
                + internal_energy_change(mass, c_water, 0, t2)
        
        elif (initial_state == "water" and final_state == "steam") \
            or (initial_state == "steam" and final_state == "water"):
            
            t1 = initial_t
            t2 = final_t
            
            if initial_state == "steam" and final_state == "water":
                # flipping the temperature
                t1 = final_t
                t2 = initial_t
                
            energy = internal_energy_change(mass, c_water, t1, 100) + water_steam(mass) \
                + internal_energy_change(mass, c_steam, 100, t2)
        
        elif (initial_state == "ice" and final_state == "steam") \
            or (initial_state == "steam" and final_state == "ice"):
            
            t1 = initial_t
            t2 = final_t
            
            if initial_state == "steam" and final_state == "ice":
                # flipping the temperature
                t1 = final_t
                t2 = initial_t
            
            energy = internal_energy_change(mass, c_ice, t1, 0) + ice_water(mass) \
                + internal_energy_change(mass, c_water, 0, 100) + water_steam(mass) \
                    + internal_energy_change(mass, c_steam, 100, t2)

    
    return energy


def ideal_gas(pressure, volume, moles, temperature):
    """This function takes in various variables to calculate certain characteristics of an
        ideal gas.
        
        Ideal gas:
            1. Negligible volume of gas molecules
            2. No intermolecular forces
            3. Random motion
            4. Elastic collisions
            5. Kinetic energy is directly proportional to temperature
        
        Formulas:
            Ideal Gas Law: pV = nRT
            
            p = Pressure in pascals (Pa)
            V = Volume of the ideal gas in m^3
            n = number of moles
            R = Ideal gas constant (8.314 J mol^-1 K^-1)
            T = Temperature in Kelvin
        
        Parameters:
            Pressure
            Volume
            Number of moles
            Temperature
            
        Return:
        One of the paremeters"""
    
    # defining constants
    R = constants.gas_constant

    if pressure == "P":
        pressure_pa = (moles * R * temperature) / volume
        
        unknown = pressure_pa
    
    elif volume == "V":
        volume_m3 = (moles * R * temperature) / pressure
        
        unknown = volume_m3
    
    elif moles == "N":
        moles_mol = (pressure * volume) / (R * temperature)
        
        unknown = moles_mol
    
    elif temperature == "T":
        temperature_k = (pressure * volume) / (moles * R)
        
        unknown = temperature_k
    
    
    return unknown


def mode_heat():
    # main function for heat transfers: mode 1

    print("States: ice, water, steam")
    # states of water
    initial_state = input("Please enter the initial state: ").lower()
    final_state = input("Please enter the final state: ").lower()
    
    # mass
    mass_pound = float(input("Please enter the mass in pound: "))
    
    # temperature
    initial_temperature_f = float(input("Please enter the initial temperature in Fahrenheit: "))
    final_temperature_f = float(input("Please enter the final temperature in Fahrenheit: "))
    
    # lambda functions to convert user input values into SI units
    # results are rounded to 3 decimal places
    pound_to_kg = lambda pound: round(pound * 0.453592, 3)
    fahrenheit_to_celsius = lambda f: round((f - 32) * (5/9), 3)
    
    # unit conversions
    mass_kg = pound_to_kg(mass_pound)
    initial_temperature_c = fahrenheit_to_celsius(initial_temperature_f)
    final_temperature_c = fahrenheit_to_celsius(final_temperature_f)
    
    # raising exceptions upon user input values do not agree with phsical properties
    if (initial_state == "ice" and initial_temperature_c > 0) \
        or (final_state == "ice" and final_temperature_c > 0):
        
        print()
        raise Exception("Temperature of ice must be lower than 32 degree Fahrenheit.")
        pass
    
    if (initial_state == "water" and (initial_temperature_c > 100 or initial_temperature_c < 0)) \
        or (final_state == "water" and (final_temperature_c > 100 or final_temperature_c < 0)):
        
        print()
        raise Exception("Temperature of water must be between 32 and 212 degree Fahrenheit.")
        pass
    
    if (initial_state == "steam" and initial_temperature_c < 100) \
        or (final_state == "steam" and final_temperature_c < 100):
        
        print()
        raise Exception("Temperature of steam must be higher than 212 degree Fahrenheit.")
        pass
    
    if mass_pound <= 0:
        
        print()
        raise Exception("Mass must not be negative or 0.")

    # calling the heat_transfers function to calculate the energy
    energy = heat_transfer(initial_state, final_state, mass_kg, \
        initial_temperature_c, final_temperature_c)
    
    # print the results, rounded to 3 deciaml places
    print(f"Energy = {round(energy, 3)} J")
    
    
    pass


def mode_gas_law():
    # main function for gas laws: mode 2
    print("Conside the formula PV = NRT")
    unknown = input("Please enter the unknown you would like to find: ").upper()
    
    # lambda functions for unit conversions, with results rounded to 3 decimal places
    psi_to_pa = lambda psi: round(psi * 6894.76, 3)
    in3_to_m3 = lambda in3: round(in3 * 1.63871 * (10 ** -5), 3)
    fahrenheit_to_kelvin = lambda f: round((f - 32) * (5/9) + 273.15, 3)
    
    if unknown == "P":
        
        volume_in3 = float(input("Please enter the volume in in^3: "))
        mole = float(input("Please enter the number of moles: "))
        temperature_f = float(input("Please enter the temperture in Fahrenheit: "))
        
        # converting into SI units
        volume_m3 = in3_to_m3(volume_in3)
        temperature_k = fahrenheit_to_kelvin(temperature_f)
        
        if any(value < 0 for value in (volume_m3, mole, temperature_k)):
            raise Exception("Values entered violated physical properties.")
            pass
        
        # calling gas_laws to calculate the unkown
        pressure_pa = ideal_gas(unknown, volume_m3, mole, temperature_k)
        pressure_psi = pressure_pa / 6894.76
        
        # printing the result
        print(f"Pressure = {round(pressure_pa, 3)} Pa")
    
    elif unknown == "V":
        
        pressure_psi = float(input("Please enter the pressure in psi: "))
        mole = float(input("Please enter the number of moles: "))
        temperature_f = float(input("Please enter the temperture in Fahrenheit: "))
        
        # converting into SI units
        pressure_pa = psi_to_pa(pressure_psi)
        temperature_k = fahrenheit_to_kelvin(temperature_f)
        
        if any(value < 0 for value in (pressure_pa, mole, temperature_k)):
            raise Exception("Values entered violated physical properties.")
            pass
        
        # calling gas_laws to calculate the unkown
        volume_m3 = ideal_gas(pressure_pa, unknown, mole, temperature_k)
        volume_in3 = volume_m3 * 31023.7
        
        # printing the result
        print(f"Volume = {round(volume_in3, 3)} in^3")
        
    
    elif unknown == "N":
        
        pressure_psi = float(input("Please enter the pressure in psi: "))
        volume_in3 = float(input("Please enter the volume in in^3: "))
        temperature_f = float(input("Please enter the temperture in Fahrenheit: "))
        
        # converting into SI units
        pressure_pa = psi_to_pa(pressure_psi)
        volume_m3 = in3_to_m3(volume_in3)
        temperature_k = fahrenheit_to_kelvin(temperature_f)
        
        if any(value < 0 for value in (pressure_pa, volume_m3, temperature_k)):
            raise Exception("Values entered violated physical properties.")
            pass
        
        # calling gas_laws to calculate the unkown
        mole = ideal_gas(pressure_pa, volume_m3, unknown, temperature_k)
        
        # printing the result
        print(f"Number of moles = {round(mole, 3)}")
            
    elif unknown == "T":
        
        pressure_psi = float(input("Please enter the pressure in psi: "))
        volume_in3 = float(input("Please enter the volume in in^3: "))
        mole = float(input("Please enter the number of moles: "))
        
        # converting into SI units
        pressure_pa = psi_to_pa(pressure_psi)
        volume_m3 = in3_to_m3(volume_in3)
        
        if any(value < 0 for value in (pressure_pa, volume_m3, mole)):
            raise Exception("Values entered violated physical properties.")
            pass
        
        # calling gas_laws to calculate the unkown
        temperature_k = ideal_gas(pressure_pa, volume_m3, mole, unknown)
        temperature_f = temperature_k * (9/5) - 459.67
        
        # printing the result
        print(f"Temperature = {round(temperature_f, 3)} F")
    
    
    pass


def main():
    
    print()
    print("Mode 0: Exit")
    print("Mode 1: Heat Transfers")
    print("Mode 2: Gas Laws")
    mode = int(input("Please select a mode: "))
    print()
    
    # if mode entered is in the range of 0 and 3 (0, 1, 2)
    if mode in range(0, 3):
        selector = True
    else:
        selector = False
    
    # if invalid mode numbers are entered
    while not selector:
        mode = int(input("Please select a mode: "))
        print()
    
    # calls the corresponding main function of a certain mode
    if mode == 1:
        mode_heat()
    elif mode == 2:
        mode_gas_law()

    
    pass


if __name__ == "__main__":
    main()