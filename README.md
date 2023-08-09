1. Requirements and run:
    Install requirements using: pip install -r requirements.txt
    Directly run from terminal: python app.py

2. weather.py: 
    Makes an API call to OpenWeatherMap to fetch the weather of a given city. Only the values of temperature, humidity, and pressure are stored.

3. Functionality: 
    The basic idea is to simulate readings of a sensor that keeps fluctuating because the immediate surroundings of a sensor, especially home sensors, might get affected even by opening windows.

    Simulating sensors basic idea: 
    To do this, the program gets information on temperature, pressure, and humidity from OpenWeatherMap (https://openweathermap.org/). Now, to add fluctuations of a sensor, a random number generator is being used, which adds a 10% randomness value to the original values of parameters. Finally, a Flask instance is used as a back-end to display the dashboard to client in form of a web app.

    Multiple users:
    To add multiple users, a button is used which corresponds to different cities. For e.g., for User 1, the API call is made to fetch weather info of city='Miami' and a randomness is added to each parameter to simulate sensor readings. Similarly, for User 2, a different city can be used, e.g., city='Seattle', and then the same process of adding randomness is followed. The number of users can be increased or decreased based on requirements.

    Outlook:
    A login form with a database can be used to make a more secure interface and a registration procedure can be used to add new users.

4. UI:
    The homepage of (a very basic) UI asks you to choose your User ID and takes you to your dashboard where you can see the readings from your setup. The page automatically refreshes every 30 seconds to update readings and it also be refreshed manually optionally.