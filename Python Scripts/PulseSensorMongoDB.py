from pulsesensor import Pulsesensor
import pymongo
import datetime
import time

conn_str = "mongodb+srv://katiehanj:katiehan@cluster0.tnb5u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["censor_app"]
collection = db["CurrentData"]
patient_location = "Patient Room 2A 125"

p = Pulsesensor()
p.startAsyncBPM()


while 1:
    try:

        bpm = p.BPM

        # If we received a measurement, print it and send it to MongoDB.
        if bpm:
            bpm > 0
            bpm_c = int(bpm)
            doc_id = collection.insert_one({'bpm': bpm_c,
                                             'datetime': datetime.datetime.now(),
                                             'location': patient_location}).inserted_id
            
            print (doc_id)
            print(int(bpm_c))
            print(patient_location)


    except KeyboardInterrupt:
        print('Error! Could not read the Pulse Value from unit')
    except ValueError:
        print('Error! Could not convert Pulse to int')
    finally:
        time.sleep(1)
