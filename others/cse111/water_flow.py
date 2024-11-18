# Tristan Wong
# 2/12/2024
'''3 functions calculating water column height, pressure gain from water height,
    and pressure loss from pipe'''
'''Constants are defined outside of functions and used in the formulas instead of inputting numbers,
    a kPa to Psi function is added, and 1 output in kPa and 1 output in Psi will be displayed'''


# defining the constants ρ, g, and μ
density_constant = 998.2
g_constant = 9.80665
μ_constant = 0.0010016


def water_column_height(tower_height, tank_height):
    '''Calculates the water column height through the given formula:
        h = t + 3w/4.
        
        h is height of the water column
        t is the height of the tower
        w is the height of the walls of the tank that is on top of the tower
        
        Parameters: tower_height, tank_height
        Return: height of the water column'''
        
    water_column_height = tower_height + tank_height * (3 / 4)
    
    return water_column_height


def pressure_gain_from_water_height(height):
    '''Calculates the pressure caused by Earth's gravity
        through the given formula:
        P = ρgh / 1000
        
        P is the pressure in kilopascals (kPa)
        ρ is the density of water (998.2 kilogram / meter^3)
        g is the acceleration from Earths gravity (9.80665 meter / second^2)
        h is the height of the water column in meters
        
        Parameters: height (h)
        Return: pressure in kilopascals (kPa)'''
    
    pressure_kpa = density_constant * g_constant * height / 1000
    
    return pressure_kpa


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    '''Calculates the pressure loss from friction within a pipe
        through the given formula:
        P = -fLρv^2 / 2000d
        
        P is the lost pressure in kilopascals (kPa)
        f is the pipe's friction factor
        L is the length of the pipe in meters
        ρ is the density of water (998.2 kilogram / meter^3)
        v is the velocity of the water flowing through the pipe in meters / second
        d is the diameter of the pipe in meters
        
        Parameters: pipe_diameter, pipe_length, friction_factor, fluid_velocity
        Return: pressure loss from friction within a pipe'''

    pressure_loss_pipe_kpa = - (friction_factor * pipe_length * density_constant * (fluid_velocity ** 2)) \
        / (2000 * pipe_diameter)
    
    return pressure_loss_pipe_kpa


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    '''Calculates the pressure loss from pipe fittings through the given formula:
        P = -0.04ρ(v^2)n / 2000
        
        P is the lost pressure in kilopascals (kPa)
        ρ is the density of water (998.2 kilogram / meter^3)
        v is the velocity of the water flowing through the pipe in meters / second
        n is the quantity of fittings
        
        Parameters: fluid_velocity, quantity_fittings
        Return: pressure loss from pipe fittings'''

    pressure_loss_fittings_kpa = - (0.04 * density_constant * (fluid_velocity ** 2) * quantity_fittings) \
        / 2000
    
    return pressure_loss_fittings_kpa


def reynolds_number(hydraulic_diameter, fluid_velocity):
    '''Calculates the Reynolds number through the given formula:
        R = ρdv / μ
        
        R is the Reynolds number
        ρ is the density of water (998.2 kilogram / meter^3)
        d is the hydraulic diameter of a pipe in meters. For a round pipe,
            the hydraulic diameter is the same as the pipe’s inner diameter.
        v is the velocity of the water flowing through the pipe in meters / second
        μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
        
        Parameters: hydraulic_diameter, fluid_velocity
        Return: Reynolds number'''

    reynolds_number = (density_constant * hydraulic_diameter * fluid_velocity) / μ_constant
    
    return reynolds_number


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity,
    reynolds_number, smaller_diameter):
    '''Calculates the pressure loss from a rounded reduction in a pipe's diameter
        through the given formulas:
        k = (0.1 + 50 / R)((D / d)^4 - 1)
        P = -kρv^2 / 2000
        
        k is a constant computed by the first formula and used in the second formula
        R is the Reynolds number that corresponds to the pipe with the larger diameter
        D is the diameter of the larger pipe in meters
        d is the diameter of the smaller pipe in meters
        P is the lost pressure kilopascals (kPa)
        ρ is the density of water (998.2 kilogram / meter^3)
        v is the velocity of the water flowing through the larger diameter pipe in meters / second
        
        Parameters: larger_diameter, fluid_velocity, reynolds_number, smaller_diameter
        Return: pressure loss from a rounded reduction in a pipe's diameter'''

    # 1st formula
    k_constant = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    # 2nd formula
    pressure_loss_pipe_reduction_kpa = - k_constant * density_constant * (fluid_velocity ** 2) \
        / 2000
    
    return pressure_loss_pipe_reduction_kpa


def kpa_to_psi(kpa):
    '''Converts kPa to Psi
        1 kPa = 0.1450377377 Psi
        
        kPa = Kilopascal
        Psi = Pound-force per square inch
        
        Parameters: kpa
        Return: psi'''
    
    psi = kpa * 0.1450377377
    
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    # convert pressure in kPa to psi
    pressure_psi = kpa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} Psi")


if __name__ == "__main__":
    main()