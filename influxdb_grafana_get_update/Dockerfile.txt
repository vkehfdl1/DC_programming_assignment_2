From philhawthorne/docker-influxdb-grafana:latest
RUN apt-get update
RUN apt-get upgrade -y
CMD ["/run.sh"]