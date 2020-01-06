FROM python:3.6.7-slim
ADD requirements.txt /
RUN pip install -r /requirements.txt && apt update && apt install wget -y 

RUN wget https://github.com/gamegos/cesi/releases/download/v2.6.2/cesi-extended.tar.gz -O /cesi.tar.gz &&  tar -xvf cesi.tar.gz
WORKDIR "/cesi"
ENTRYPOINT ["python" ,"/cesi/cesi/run.py"]
CMD ["--config-file", "/opt/cesi.conf", "--auto-reload"]