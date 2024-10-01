# import necessary modules
import pandas as pd
import numpy as np

def preprocess(weather_data):
    # Convert 'datetime' column to datetime type if it's not already in datetime format in train, validation and test datasets
    weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])
    # make the datetime column the index of the X_train_weather dataframe for easier slicing
    weather_data.set_index('datetime', inplace=True)
    # keep only the first row of the duplicated rows
    weather_data_filled = weather_data[~weather_data.index.duplicated(keep='first')]
    
    # Generate a reference datetime range spanning the entire period of the X_train_weather data
    start_date = weather_data.index.min().floor('H')  # Rouning  down to the nearest hour
    end_date = weather_data.index.max().ceil('H')     # Rounding up to the nearest hour
    datetime_reference_range = pd.date_range(start=start_date, end=end_date, freq='H')

    # Fill missing hours
    weather_data_filled = weather_data_filled.reindex(datetime_reference_range)
    weather_data_filled.index.name = 'datetime'
    # drop solarenergy and preciptype column from the dataframe
    weather_data_filled.drop(columns=['solarenergy', 'preciptype'], inplace=True)
    # fill missing values
    data_interpolate = weather_data_filled
    linear_interpolate_columns = data_interpolate.columns.values
    
    # Perform linear interpolation
    weather_data_filled[linear_interpolate_columns] = data_interpolate[linear_interpolate_columns].interpolate(method='linear')
    return weather_data_filled


# function to calculate wind energy
def wind_energy(wind_speed):
    # Define parameters
    air_density = 1.225  # kg/m^3 (typical air density at sea level)
    swept_area =  np.pi * (15**2) # m^2 (assuming rotor diameter of the turbine is 30m, the swept area of the turbine)
    no_of_wind_mills = 116 # assuming there are 116 wind mills in Brigthon that produce wind energy
    # print(swept_area)
    
    # Calculate wind energy in MW using the equation for each wind speed value
    wind_energy = (((0.5 * air_density * swept_area * (wind_speed * (1000 / 3600)) ** 3)/1000) * 100)/1000
    return round(wind_energy, 2)


# function to calculate solar energy
def solar_energy(solar_radiation):
    
    # Define constants
    efficiency = 0.20  # 20%
    reduction_factor = 0.75  # 75% (percentage after considering all the factors(cloudcover, panel degradation) contributing to reduction of the panel output)
    panel_area = 30  # in square meters
    num_panels = 369 * 4 # considering 4 panels are installed in each 369 house and shops in brighton
    
    # Calculate solar energy in MW
    solar_energy = (solar_radiation* efficiency * reduction_factor * panel_area * num_panels)/1000000
    return round(solar_energy, 2)

# function to determine surplus
def determine_surplus(total_energy):
    if total_energy > (0.417/1000)*114479*2:
        return 1
    else:
        return 0