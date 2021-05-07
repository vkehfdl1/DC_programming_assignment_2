from influxdb import InfluxDBClient, DataFrameClient
import pandas as pd
import threading
import time

# Server data
myhost = 'influxdb' # InfluxDB address without port number
myuser = 'root' # InfluxDB user name
mypass = 'root' # InfluxDB password
mydatabase = 'myDB' # InfluxDB database name

client = InfluxDBClient(host=myhost, port=8086, username=myuser, password=mypass, database=mydatabase)
client.create_database(mydatabase) # list에 없다면 database 생성
client.switch_database(mydatabase)
df = pd.read_csv('./NAB_data/art_daily_jumpsup.csv') # data csv file 경로 입력
df = df.value.values


def write_point(num):
    json_body = [
        {
            "measurement": "test",
            "tags": {
                "data": "jumpsup",
            },
            "fields": {
                "value": num,
                "anomalies": False
            },
        }
    ]
    client.write_points(json_body)

for j in range (10):
    for i in range(len(df)):
        write_point(df[i])
        time.sleep(1)