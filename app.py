from flask import Flask, render_template, request
from weather import main as get_weather
import random

app = Flask(__name__)

def get_values(x):
    return round(x+0.1*x*random.random(),2)

@app.route('/', methods=['GET','POST'])
def index():
    temp = get_weather('Miami', '', '').temperature
    pressure = 0.001*get_weather('Miami', '', '').pressure
    humidity = get_weather('Miami', '', '').humidity

    data = {'lr_temp': get_values(temp), 'lr_hum': get_values(humidity),'lr_pressure': get_values(pressure),
    'br_temp': get_values(temp), 'br_hum': get_values(humidity),'br_pressure': get_values(pressure),
    'g_temp': get_values(temp), 'g_hum': get_values(humidity),'g_pressure': get_values(pressure)}

    return render_template('index.html',x=data)






if __name__ == '__main__':
    app.run(debug=True)