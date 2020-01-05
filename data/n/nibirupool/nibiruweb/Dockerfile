FROM ubuntu
RUN apt update && apt -y upgrade
RUN apt install -y uwsgi python-flask build-essential python-dev uwsgi-plugin-python python-pip
RUN apt install -y libmysqlclient-dev
RUN pip install influxdb
RUN pip install MySQL-python
COPY website /app
COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh
ENTRYPOINT /root/start.sh

