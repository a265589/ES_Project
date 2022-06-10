import  pymysql
import base64
from pytz import timezone   
from datetime import datetime


def connect():
    try:
        global connection
        connection = pymysql.connect()
        print("successfully connect to database")
    except:
        print("cannot connect to database")

def enter(licensePlateNum, path):
    global connection
    tz = timezone('Asia/Taipei')
    timestamp = (datetime.now(tz)).strftime('%Y-%m-%d %H:%M:%S')   
    command = "INSERT INTO vehicle_data (license_plate_number,enter_time,inside, photo) VALUES(%s,%s,'Y',%s) ON DUPLICATE KEY UPDATE enter_time = %s, inside = 'Y', times = times+1, photo = %s"
    file = _convertToBinaryData(path)
    with connection.cursor() as cursor:
        cursor.execute(command,(licensePlateNum, timestamp, file, timestamp, file))
    connection.commit()

def leave(licensePlateNum):
    global connection
    tz = timezone('Asia/Taipei')
    timestamp = (datetime.now(tz)).strftime('%Y-%m-%d %H:%M:%S') 
    command = "UPDATE vehicle_data SET leave_time = %s, inside = 'N' WHERE license_plate_number = %s"
    with connection.cursor() as cursor:
        cursor.execute(command,( timestamp, 'abc123'))
    connection.commit()

def close():
    global connection
    connection.close()

def _convertToBinaryData(path):
    # Convert digital data to binary format
    with open(path, 'rb') as file:
        binaryData = file.read()
    return binaryData
