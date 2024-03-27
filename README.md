# IoT Environmental Monitoring System README

This README document provides an overview and setup instructions for a suite of scripts designed to simulate an environmental monitoring system leveraging IoT technology. The system is centered around publishing simulated sensor data to ThingSpeak using MQTT and retrieving this data for visualization and analysis. The suite consists of three main components:

1. **Python Script for Publishing Sensor Data**
2. **MATLAB Script for Displaying the Latest Sensor Data**
3. **MATLAB Script for Displaying Sensor Data Over the Last Five Hours**

## Pre-requisites

### ThingSpeak Setup
- **Account and Channel:** Ensure you have a ThingSpeak account and a channel configured with fields for temperature, humidity, and CO2 levels.
- **API Keys:** Keep your API keys confidential to prevent unauthorized channel access.

### Data Publishing Frequency
- **Rate Limit:** The ThingSpeak free account imposes a data publishing rate limit. Adhere to this limit with the Python script to avoid data loss.

## 1. Python Script for Publishing Sensor Data

### Overview
Simulates an IoT device that generates and publishes random data for temperature, humidity, and CO2 levels to a ThingSpeak channel using MQTT.

### Requirements
1. Python 3.x
2. Paho MQTT library (`pip install paho-mqtt`)

### Setup and Usage
1. Install the Paho MQTT library.
2. Configure `channel_id`, `write_api_key`, `mqtt_username`, `mqtt_clientId`, and `mqtt_password` with your ThingSpeak channel and MQTT credentials.
3. Run the script to continuously publish random data at 2-second intervals.

## 2. MATLAB Script for Displaying the Latest Sensor Data

### Overview
Fetches and displays the latest sensor data (temperature, humidity, CO2 levels) from the specified ThingSpeak channel.

### Requirements
- MATLAB environment with Internet connectivity.

### Setup and Usage
1. Ensure `channelID` and `readAPIKey` match your ThingSpeak channel's settings.
2. Run the script in MATLAB to display the latest sensor readings.

## 3. MATLAB Script for Displaying Sensor Data Over the Last Five Hours

### Overview
Displays data for a specified sensor (temperature, humidity, CO2) received during the last five hours from a ThingSpeak channel.

### Requirements
- MATLAB environment with Internet connectivity.

### Setup and Usage
1. Select the desired environmental metric (1 for Temperature, 2 for Humidity, 3 for CO2 levels) by adjusting the `fieldNum` variable.
2. Ensure `channelID` and `readAPIKey` are set to your ThingSpeak channel details.
3. Run the script in MATLAB. It lists available metrics, highlights the selected one, and displays the sensor data values received over the last five hours.
