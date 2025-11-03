from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():

    weather_data = {}

    if request.method == 'POST':
        city = request.form['city']
        API_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=ddd94c9e165ea915557125e2adf5821f"
        response = requests.get(API_url)
        data = response.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            sky = data['weather'][0]['main']
            pressure=data['main']['pressure']
            humidity=data['main']['humidity']
            wind_speed=data['wind']['speed']

            weather_data = {
                'city': city,
                'temperature': temp,
                'sky': sky,
                'pressure': pressure,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
        #ERROR HANDLING

    return render_template('index.html', **weather_data)

if __name__=="__main__":
    app.run(debug=True)


