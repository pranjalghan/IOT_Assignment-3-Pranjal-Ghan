README for IoT Environmental Monitoring System-

This README document provides an overview and instructions for a collection of scripts designed to simulate an environmental monitoring system using IoT technology. The system involves publishing simulated sensor data to ThingSpeak using MQTT and retrieving this data for visualization and analysis. There are three main components:

1.) Python Script for Publishing Sensor Data
2.) MATLAB Script for Displaying the Latest Sensor Data
3.) MATLAB Script for Displaying Sensor Data Over the Last Five Hours

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

a.) ThingSpeak Setup: Before using these scripts, you must have a ThingSpeak account and a channel set up with fields configured for temperature, humidity, and CO2 levels.
API Keys: Keep your API keys confidential to prevent unauthorized access to your channel.
b.) Data Publishing Frequency: The ThingSpeak free account has a rate limit for data publishing. Ensure the Python script's publishing frequency complies with these limits to avoid data loss.


1. Python Script for Publishing Sensor Data
Overview
This Python script simulates an IoT device that generates random data for temperature, humidity, and CO2 levels, then publishes this data to a ThingSpeak channel using MQTT.

Requirements
1.) Python 3.x
2.) Paho MQTT library (Install via pip install paho-mqtt)


Setup and Usage
1.)Install the required Paho MQTT library.
2.)Configure the channel_id, write_api_key, mqtt_username, mqtt_clientId, and mqtt_password with your ThingSpeak channel and MQTT credentials.
3.) Run the script. It will continuously publish random data at 2-second intervals.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. MATLAB Script for Displaying the Latest Sensor Data
Overview
This MATLAB script fetches and displays the latest data for all sensors (temperature, humidity, CO2 levels) from the specified ThingSpeak channel.

Requirements
1.)MATLAB environment with Internet connectivity.
Setup and Usage
1.)Ensure the channelID and readAPIKey variables match your ThingSpeak channel's settings.
2.)Run the script in MATLAB. It will display the latest readings from the sensors.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. MATLAB Script for Displaying Sensor Data Over the Last Five Hours
Overview
This MATLAB script displays data from the specified sensor (temperature, humidity, CO2) received during the last five hours from a ThingSpeak channel.

Requirements
1.) MATLAB environment with Internet connectivity.
Setup and Usage
1.)Select the field number for the desired environmental metric (1 for Temperature, 2 for Humidity, 3 for CO2 levels) by adjusting the fieldNum variable.
2.)Ensure channelID and readAPIKey are set to your ThingSpeak channel details.
3.)Run the script in MATLAB. It will list available metrics, highlight the selected one, and display the sensor data values received over the last five hours.
