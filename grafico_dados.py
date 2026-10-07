import matplotlib.pyplot as plt

horas = ['07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
temp = [16.8, 17.0, 17.9, 19.7, 21.2, 22.6, 23.7, 23.3, 23.5, 23.2]

fig, ax = plt.subplots()
ax.plot(horas, temp)

ax.set(xlabel='Tempo (H)', ylabel='Temperatura (ºC)',title='Temperatura ao longo de 10 horas em Lisboa (7 de outubro)')

fig.savefig("gráfico.png")
plt.show()

