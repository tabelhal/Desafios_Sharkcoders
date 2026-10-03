import tkinter as tk
from tkinter import messagebox
import python_weather
import asyncio
import aiohttp

def weather_api():
    city = city_entry.get().strip()

    if city == '':
        messagebox.showerror("Erro", "O campo da cidade está vazio. Por favor insira uma cidade")
        return

    async def main() -> None:
        async with python_weather.Client(
            unit=python_weather.METRIC,
            locale=python_weather.Locale.PORTUGUESE,
        ) as client:
            weather = await client.get(city)
            temp_label.config(text=f'Temperatura - {weather.temperature}ºC')
            desc_label.config(text=weather.description)

    try:
        asyncio.run(main())
    except (aiohttp.ClientError, asyncio.TimeoutError, OSError):
        messagebox.showerror(
            "Erro de ligação",
            "Não foi possível ligar à internet. Verifique a sua ligação e tente novamente."
        )
    except Exception:
        messagebox.showerror(
            "Erro",
            "Não foi possível obter o tempo. Verifique o nome da cidade e tente novamente."
        )

root = tk.Tk()
root.title('Weather API')
root.geometry('250x150')

label = tk.Label(root, text='Insira a sua cidade')
label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

button = tk.Button(root, text='Pesquisar', command=weather_api)
button.pack()

desc_label = tk.Label(root)
desc_label.pack()

temp_label = tk.Label(root)
temp_label.pack()

root.mainloop()