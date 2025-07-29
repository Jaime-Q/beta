import pandas as pd

#Read file
file = pd.read_excel("Ventas_2050.xlsx")

#Excel to dictionary
ventas = file.to_dict(orient="records")

#Show data
print(ventas)

for venta in ventas:
    print(venta)