FROM datadog/agent:6.6.0

COPY requirements.txt /requirements.txt
RUN apt-get update \
    && apt-get install --no-install-recommends -y iproute2 net-tools iputils-ping \
    && pip install -r requirements.txt

COPY /checks.d/* /checks.d/
COPY /conf.d/* /conf.d/
COPY /cont-init.d/* /etc/cont-init.d/
