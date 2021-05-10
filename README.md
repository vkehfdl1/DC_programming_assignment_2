# DC_programming_assignment_2
경희대학교 SWCON22100 Datacenter Programming의 Assignment #2를 위한 repo입니다.

이 repo에는 두 가지의 docker image build를 위한 Dockerfile, 그리고 docker-compose를 위한 yaml 파일로 구성이 되어있습니다. 
이를 통하여 짧은 데이터를 influxdb container로 전송할 수 있습니다. 

	docker-compose up -d

명령어를 통하여 두 컨테이너를 실행할 수 있습니다. 두 컨테이너는 같은 docker network 상에서 움직이기 때문에 서로 접속할 수 있습니다. 전송한 데이터를 확인하는 방법은 다음과 같습니다.

	docker exec -it <container name> /bin/bash
	influx
	use mydb
	select * from cpu_load_short

데이터가 표시되면 data_to_influxdb 컨테이너에서 influxdb로 데이터가 잘 전송이 된 것입니다. 


### Links
- [data_to_influxdb](https://hub.docker.com/r/markervkehfdl1/data_to_influxdb)
- [influxdb_grafana_get_update](https://hub.docker.com/r/markervkehfdl1/influxdb_grafana_get_update)
