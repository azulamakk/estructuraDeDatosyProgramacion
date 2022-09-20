import matplotlib.pyplot as plt
import numpy as np

signalTime = np.arange(0,100,0.5)
signalAmplitud=np.sin(signalTime)

plt.plot(signalTime, signalAmplitud, color='violet', linewidth=3)

plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title(label='Senal', loc='right')

plt.show()