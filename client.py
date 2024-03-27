import paho.mqtt.client as mqtt
import random
import time

# ThingSpeak Channel Settings
channel_id = "2483890"
write_api_key = "IO9W203Q6WP1RYVA"

# MQTT Credentials provided
mqtt_username = "FC0wIyIQBi4FNzsNJQ0DICQ"
mqtt_clientId = "FC0wIyIQBi4FNzsNJQ0DICQ"
mqtt_password = "IL9ZLVf+ica8KQCNEOkz7zLR"

# MQTT Topic
topic = f"channels/{channel_id}/publish"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id=mqtt_clientId)
client.username_pw_set(username=mqtt_username, password=mqtt_password)

client.on_connect = on_connect

client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_start()


try:
    while True:
        # Generate random sensor data
        temperature = random.uniform(-50, 50)
        humidity = random.uniform(0, 100)
        co2 = random.uniform(300, 2000)

        # Publishing data
        payload = f"field1={temperature}&field2={humidity}&field3={co2}"
        result = client.publish(topic, payload)
        time.sleep(2)
        if result.is_published():
            print(f"Sent to topic {topic}: {payload}")
        else:
            print(f"Failed to send message to topic {topic}")
            time.sleep(15)  # Respect ThingSpeak's publishing rate limit
        

except Exception as e:
    print(f"An error occurred: {e}")

except KeyboardInterrupt:
    print("Stopped by User")
    client.loop_stop()
    client.disconnect()