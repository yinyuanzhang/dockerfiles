FROM python:3.7

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

EXPOSE 9184
COPY nexus_exporter.py /nexus_exporter.py

ENTRYPOINT ["/nexus_exporter.py"]
