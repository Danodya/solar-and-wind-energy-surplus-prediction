# Brighton Solar and Wind Energy Surplus Prediction Project  
**By – Danodya Weerasinghe**

## Project Overview  
Build a system that reliably predicts energy surplus at least 24 hours in advance for local clients near renewable energy sources. This allows the company to send customers an alert to opt into the slots so that the company can provide free energy when there is a surplus of energy in Brighton.

## Data  
The given dataset includes historical weather data in Brighton from 2010 to 2024. The dataset includes various factors contributing to solar and wind energy such as:  
- Temperature  
- Humidity  
- Cloud cover  
- Solar radiation  
- UV index  
- Wind speed  
- Wind direction  

## Goals  
The goal is to create a model that can predict, at least 24 hours in advance, whether there will be a surplus of energy in Brighton and answer the CEO’s questions about the company’s cost of false positives and the feasibility of model deployment in May 2024.

## Summary of Modelling and Testing Methods  
1. Loaded the cleaned training dataset from assignment 1 and validation/test datasets.
2. Created a separate Python script called `preprocessaModule` with the following functions:  
   - `preprocess()`: includes all the cleaning and preprocessing steps.  
   - `wind_energy()`: wind energy calculation steps.  
   - `solar_energy()`: solar energy calculation steps.  
   - `determine_surplus()`: uses average hourly energy consumption in Brighton as the threshold to decide if there is a surplus.  
3. Applied preprocessing steps for validation and test sets.  
4. Calculated solar and wind energy in validation and test sets.  
5. Defined a baseline for solar and wind energy on the validation set.  
6. Feature selection for modeling.  
7. Scaled features and targets for modeling.  
8. Trained a model for solar and wind energy forecasting.  
9. Made predictions for solar and wind energy on validation set and evaluated.  
10. Made predictions for solar and wind energy on training set.  
11. Analyzed predicted solar and wind energy for surplus forecasting.  
12. Confusion matrix and false positives analysis.  
13. Analyzed loss incurred from false positives.  
14. Calculated model performance (R² score) over the months on test set.  
15. Further analysis on actual and predicted total energy and surplus.

## Assumptions  

**Wind Energy Calculation Assumptions**:  
- Air density: 1.225 kg/m³ (typical air density at sea level).  
- Rotor diameter of the turbine: 30m.  
- Number of windmills in Brighton that contribute to wind energy: 116.

**References for wind energy calculation**:  
- [Penn State]([https://openai.com](https://www.e-education.psu.edu/emsc297/node/649#:%7E:text=We'll%20start%20with%20a,kW%20(8%20times%20as%20large)))
- [ICE](https://www.ice.org.uk/engineering-resources/briefing-sheets/wind-energy)  
- [Rampion Offshore Wind Farm](https://rampionoffshorewindfarm.co.uk/key-facts/#:%7E:text=The%20Rampion%20Offshore%20Wind%20Farm,foundation%20fixed%20into%20the%20seabed.) 

**Solar Energy Calculation Assumptions**:  
- Efficiency of the PV panel: 20%.  
- Energy percentage after considering all factors contributing to reduction of the panel output: 75%.  
- Panel area: 30m².  
- Number of panels: 369 * 4 (considering 4 panels installed in each of the 369 houses and shops in Brighton).  

**References for solar energy calculation**:  
- [EcoFlow](https://blog.ecoflow.com/us/how-to-calculate-solar-panel-output/)  
- [RayMaps](https://www.raymaps.com/index.php/how-to-calculate-the-area-required-by-solar-panels/)  
- [Brighton & Hove](https://www.brighton-hove.gov.uk/news/2023/hundreds-council-homes-switch-solar-power)  

**Electricity Surplus Threshold**:  
- 95.48 MW of average hourly demand is taken as the threshold to define energy surplus.  

**Reference to define energy surplus**:  
- [Utility Bidder](https://www.utilitybidder.co.uk/compare-business-energy/what-is-the-average-household-energy-usage/#:%7E:text=What%20is%20the%20average%20electricity,factors%20that%20affect%20this%20figure)
- 114,479 houses in Brighton [(Brighton & Hove)](https://www.brighton-hove.gov.uk/sites/default/files/migrated/subject/inline/downloads/citystats/4_Housing.pdf)  
- Consumer behavior factor: 2  

**Model Selection Reference**:  
- RNN model with LSTM architecture [source](https://www.scielo.org.mx/pdf/cys/v22n4/1405-5546-cys-22-04-1085.pdf)

**Electricity Cost per Megawatt Assumption**:  
- Cost per Megawatt: £60 [reference](https://www.utilitybidder.co.uk/business-electricity/price-of-1-mwh-electricity/)

## Steps to Run the Code  

### Prerequisites  
Make sure the following are installed before running Jupyter Notebook:
- Python (3.x recommended)  
- Jupyter Notebook  

### Running Jupyter Notebook  
1. Start the Jupyter Notebook server.  
2. Navigate to the `notebooks/` directory and open the notebooks named:  
   - `data_exploration.ipynb`  
   - `modeling_and_testing.ipynb`  
3. Place the `preprocessingModule.py` script inside the same directory.  
4. Change the `csv_path` to the path where your Brighton dataset is located and `output_file_path` to any location where you want to save the file.  
5. Create a folder called `model` to save solar and wind energy forecasting models.  
6. Run the cells one by one or all at once using the ‘Run All’ option in the Run menu in the following order:  
   - First: `data_exploration.ipynb`  
   - Second: `modeling_and_testing.ipynb`  
