#Add import statements
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Assign the dataframe to this variable.
# Load the data
bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv")
x_values = bmi_life_data[["BMI"]]
y_values = bmi_life_data[["Life expectancy"]]
# Make and fit the linear regression model
#Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(x_values, y_values)



plt.scatter(x_values, y_values)
plt.plot(x_values, bmi_life_model.predict(x_values))
plt.show()
# Mak a prediction using the model
# Predict life expectancy for a BMI value of 21.07931 is 60.315647164
#laos_life_exp = bmi_life_model.predict(21.07931)
