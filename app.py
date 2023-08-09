from flask import Flask, render_template, request, jsonify
from weather import main as get_weather
import random

app = Flask(__name__)

def get_values(x):
    #add randomness and round the digits
    return round(x+0.1*x*random.random(),2)

def get_data(city='Miami'):
    #get weather data from weather.py, defualt city value is set to 'Miami' to avoid running into error
    temp = get_weather(city, '', '').temperature
    pressure = 0.001*get_weather(city, '', '').pressure
    humidity = get_weather(city, '', '').humidity

    data = {'lr_temp': get_values(temp), 'lr_hum': get_values(humidity),'lr_pressure': get_values(pressure),
    'br_temp': get_values(temp), 'br_hum': get_values(humidity),'br_pressure': get_values(pressure),
    'g_temp': get_values(temp), 'g_hum': get_values(humidity),'g_pressure': get_values(pressure)}

    return data


@app.route('/')
def home():
    return render_template('home.html')


#button_id for different user_id (e.g, button1 for user1)
@app.route('/button1', methods=['GET','POST'])
def button1():
    x = get_data('Miami')
    x['user'] = 'User 1'
    return render_template('index.html', x=x)

@app.route('/button2', methods=['GET','POST'])
def button2():
    x = get_data('Seattle')
    x['user'] = 'User 2'
    return render_template('index.html', x=x)

@app.route('/button3', methods=['GET','POST'])
def button3():
    x = get_data('Washington')
    x['user'] = 'User 3'
    return render_template('index.html', x=x)



if __name__ == '__main__':
    app.run(debug=False)