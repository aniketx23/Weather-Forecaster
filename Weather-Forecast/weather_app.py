#ANANYA

import tkinter as tk
from PIL import Image,ImageTk
import requests
import json
from datetime import datetime





def time_from_utc_with_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

#AKSHAT

def weather(forcastopedia):
    api_key = "a646474c361bcce126909cc0b153c2cf"
    city = textField.get()

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

    response = requests.get(weather_url)

    weather_data = response.json()

    # SAMPLE DATA: {'coord': {'lon': 78.4744, 'lat': 17.3753}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}],
    # 'base': 'stations', 'main': {'temp': 293.04, 'feels_like': 293.44, 'temp_min': 291.15, 'temp_max': 294.82, 'pressure': 1015, 'humidity': 72},
    # 'visibility': 6000, 'wind': {'speed': 1.58, 'deg': 163}, 'clouds': {'all': 0}, 'dt': 1614196800, 'sys': {'type': 1, 'id': 9213, 'country': 'IN',
    # 'sunrise': 1614215239, 'sunset': 1614257484}, 'timezone': 19800, 'id': 1269843, 'name': 'Hyderabad', 'cod': 200}
    # weather_data['cod'] == '404' means city not found



    kelvin = 273.15
    temp = int(weather_data['main']['temp'] - kelvin)
    feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed'] * 3.6
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    timezone = weather_data['timezone']
    cloudy = weather_data['clouds']['all']
    description = weather_data['weather'][0]['description']

    sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
    sunset_time = time_from_utc_with_timezone(sunset + timezone)


#ANIKET

    final_info = description.capitalize() + "\n" + str(temp) + "°C"

    final_data = "\n" + "Sunrise: " + str(sunrise_time) + " AM" +"\n" + "Sunset: " + str(sunset_time) + " PM" + "\n" + "Feels Like: " + str(feels_like_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + " Pa" + "\n" + "Humidity: " + str(
                humidity)+ "%" + "\n" + "Wind Speed: " + str(round(wind_speed,2)) + " Km/h" + "\n" + "Cloudy: " + str(cloudy) + "%"
    
    label1.config(text=final_info)
    label2.config(text=final_data)



forcastopedia= tk.Tk()
forcastopedia.geometry("600x500")
forcastopedia.title("Weather Forcaster")


img = Image.open('./main.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg = tk.Label(forcastopedia,image=img_photo)
bg.place(x=0,y=0,width=600,height=500)


f = ("Aerial", 15, "bold")
t = ("Aerial", 35, "bold")




textField = tk.Entry(forcastopedia, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', weather)



label1 = tk.Label(forcastopedia, font=t)
label1.pack()
label2 = tk.Label(forcastopedia, font=f)
label2.pack()
forcastopedia.mainloop()