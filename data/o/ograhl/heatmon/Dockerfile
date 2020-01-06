FROM ubuntu:trusty

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
      python-pip \
      wget \
      ca-certificates \
      && \
    rm -r /var/lib/apt/lists/* && \
    pip install pyserial

ADD usbgpio8 /usbgpio8
ADD run.sh /run.sh
RUN chmod 755 /*.sh

ENV \
  GPIO_PORT="/dev/ttyACM0" \
  GPIO_CHANNEL=7 \
  GPIO_STATUS_ALIVE=1 \
  ALIVE_URL="please_set_environment_variable" \
  ALIVE_USERNAME="please_set_environment_variable" \
  ALIVE_PASSWORD="please_set_environment_variable" \
  QUERY_INTERVAL=1m

CMD ["/run.sh"]
