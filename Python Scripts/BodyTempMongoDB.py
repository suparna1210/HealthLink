#Collects sensor data and sends to MongoDB

import pymongo
from smbus2 import SMBus
from mlx90614 import MLX90614
import datetime
import time
import datetime

conn_str = "mongodb+srv://katiehanj:katiehan@cluster0.tnb5u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["censor_app"]
collection = db["BodyTemperature"]
#collection = client.database.collection
temperature_location = "Patient Room 2A 125"
partition = "_partition"
DHT_PIN = 0x5a

fixed_interval = 10
while 1:
    try:
        # Temperature value
        
        bus = SMBus(1)
        object_temp = MLX90614(bus, address=DHT_PIN)
        temp_string = object_temp.get_obj_temp()

        # If we received a measurement, print it and send it to MongoDB.
        if temp_string:
            temperature_c = float(temp_string)
            doc_id = collection.insert_one({'temperature': temperature_c,
                                             'datetime': datetime.datetime.now(),
                                             '_partition': partition,
                                             'location': temperature_location}).inserted_id
            
            print (doc_id)
            print(float(temperature_c))
            print(temperature_location)


    except KeyboardInterrupt:
        print('Error! Could not read the Temperature Value from unit')
    except ValueError:
        print('Error! Could not convert temperature to float')
    finally:
        time.sleep(fixed_interval)
