FROM python:alpine

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY emby_exporter/emby_exporter.py emby_exporter.py
COPY emby_exporter/embypysessionextender.py embypysessionextender.py
COPY emby_exporter/prometheus_metrics prometheus_metrics

EXPOSE 9123

ENTRYPOINT ["/usr/local/bin/python3", "emby_exporter.py"]
