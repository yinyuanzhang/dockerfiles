FROM sumologic/sumologic-prometheus-scraper:2.5.0

WORKDIR /opt/sumo

COPY . /opt/sumo/

CMD ["python", "./sumologic_kubernetes_container_metrics.py"]