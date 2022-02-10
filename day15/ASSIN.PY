#Creating Graph with the help of Matplotlib With CSV
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/home/arun/Desktop/tibil/cars.csv")
print(df)
print("histogram PLOT FOR CAR VS displacement")
plt.hist(df['Car'], df['Model'])
plt.title("PLOT FOR CAR VS Model")
plt.xlabel("Car")
plt.ylabel("Model")
plt.show()


