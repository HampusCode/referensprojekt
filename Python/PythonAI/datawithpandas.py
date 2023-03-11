import pandas as pd
import matplotlib.pyplot as plt

leVsGdp = pd.read_csv("life-expectancy-vs-gdp-per-capita.csv")
# Look at data from 2018
leVsGdp = leVsGdp.loc[leVsGdp['Year'] == 2018]
# Reduce size of markers to better visulize data
plt.scatter(leVsGdp['GDP per capita'], leVsGdp[
'Life expectancy at birth (historical)'], s=2)
plt.title("life expectancy vs gdp per capita 2018", fontsize=15)
plt.xlabel("GDP per capita", fontsize=15)
plt.ylabel("Life expectancy", fontsize=15)
# Set x limit to 75000 to remove outlier and focus on majority of markers
plt.xlim(0, 75000)
plt.show()



leVsGdp = pd.read_csv("life-expectancy-vs-gdp-per-capita.csv")
# Look at data from 2018
leVsGdp = leVsGdp.loc[leVsGdp['Year'] == 2018]
# remove where gdp or le is NaN
leVsGdp = leVsGdp.dropna(subset=['GDP per capita'])
leVsGdp = leVsGdp.dropna(subset=['Life expectancy at birth (historical)'])
# Extract mean and std using describe()
desc = leVsGdp.describe()
mean = desc.loc['mean']['Life expectancy at birth (historical)']
std = desc.loc['std']['Life expectancy at birth (historical)']
# Filter out countries where le is bigger than mean+std
desc = leVsGdp.loc[leVsGdp['Life expectancy at birth (historical)'] >
mean+std]
# Print the countries and le
print(desc[['Entity', 'Life expectancy at birth (historical)']])
desc[['Entity', 'Life expectancy at birth (historical)',]]


leVsGdp = pd.read_csv("life-expectancy-vs-gdp-per-capita.csv")
# Look at data from 2018
leVsGdp = leVsGdp.loc[leVsGdp['Year'] == 2018]
leVsGdp = leVsGdp.dropna(subset=['GDP per capita'])
leVsGdp = leVsGdp.dropna(subset=['Life expectancy at birth (historical)'])
# Adding new column GDP
leVsGdp["GDP"] = leVsGdp["GDP per capita"] * leVsGdp["Population (historical estimates)"]
# Calculating median for gdp and median for life expectancy
medianGFP = leVsGdp['GDP'].median()
medianLE = leVsGdp['Life expectancy at birth (historical)'].median()
# Makes a table of the cases where the life expectancy exceeds median life, and gdp is lower than the median
desc = leVsGdp.loc[(leVsGdp['Life expectancy at birth (historical)'] >
medianLE) & (leVsGdp['GDP'] < medianGFP)]
# Only shows the rows that we are interested in
desc = desc[['Entity','Life expectancy at birth (historical)','GDP']]
# Prints what we are interested in
print(desc)



leVsGdp = pd.read_csv("life-expectancy-vs-gdp-per-capita.csv")
leVsGdp = leVsGdp.loc[leVsGdp['Year'] == 2018]
# Drop bad data
leVsGdp = leVsGdp.dropna(subset=['GDP per capita'])
leVsGdp = leVsGdp.dropna(subset=['Life expectancy at birth (historical)'])
medianGDP = leVsGdp['GDP per capita'].median()
medianLE = leVsGdp['Life expectancy at birth (historical)'].median()
# Look at data where LE is above median and GDP per capita is less than median
desc = leVsGdp.loc[(leVsGdp['Life expectancy at birth (historical)']> medianLE) & (leVsGdp['GDP per capita'] < medianGDP)]
print(desc[['Entity', 'GDP per capita', 'Life expectancy at birth (historical)']])
