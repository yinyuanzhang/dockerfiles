FROM python:3
COPY . /
RUN pip install numpy google-cloud-storage
ENTRYPOINT  [ "python", "./TrafficSimulation.py" ]