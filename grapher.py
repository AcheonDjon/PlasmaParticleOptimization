import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('lengths.csv',header=0)
x = df['num_particles']
y= df['length']*1e3
plt.scatter(x,y)
plt.title("Number of Charged Particles vs Equilibriium Distance")
plt.xlabel("Number of Particles")
plt.ylabel("Equilibrium Distance(mm)")
plt.grid(True)
plt.show()