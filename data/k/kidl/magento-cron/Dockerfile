FROM google/cloud-sdk:slim

ENV PROJECT "dalema"
ENV COMPUTE_ZONE "europe-west1-b"
ENV CLUSTER_NAME "edelweiss-stage"
ENV SCHEDULE_EXPRESSION "* * * * *"
ENV LABEL "app"
ENV LABEL_VALUE "magento"
ENV COMMAND "php bin/magento cron:run"

RUN apt-get update && \
    apt-get install cron kubectl -y

COPY magento.sh /cron/magento.sh
COPY startup.sh /startup.sh

CMD ["bash", "-c", "/startup.sh"]
