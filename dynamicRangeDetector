mport matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv',header=None)
data.loc[:,0].plot()
plt.title('Dynamic range detector (Multiple samples)')
plt.xlabel("PWM rate (%)")
plt.ylabel("ADC (light sensor)")
plt.grid()
plt.xlim(0,100)
plt.ylim(0,4500)
plt.show()
