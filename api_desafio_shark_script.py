from tkinter import *
import tkinter as tk
import python_weather
  import asyncio

  def weather_api():
    city = city_entry.get()
    async def main() -> None:
      async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        temp = weather.temperature
        desc = weather.description
        temp_label = tk.Label(root, text=f'Temperatura: {temp}ºC')
        temp_label.pack()
        desc_label = tk.Label(root, text=desc)
        desc_label.pack()

  if __name__ == '__main__':
    asyncio.run(main())


root = tk.Tk()
root.title("Weather API")
root.geometry("500x500")
city_entry = tk.Entry(root)
button = tk.Button(root, text="Weather API", command=weather_api)
button.pack()
city_entry.pack()


root.mainloop()