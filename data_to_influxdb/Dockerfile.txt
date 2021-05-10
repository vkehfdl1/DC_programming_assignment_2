FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y curl
CMD curl -i -XPOST http://influxdb:8086/query --data-urlencode "q=CREATE DATABASE mydb"
CMD curl -i -XPOST 'http://influxdb:8086/write?db=mydb' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'