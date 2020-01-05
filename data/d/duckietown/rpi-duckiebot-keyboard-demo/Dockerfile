FROM duckietown/rpi-gui-tools:master18

COPY run_keyboarddemo.sh .

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y python-pygame

CMD [ "./run_keyboarddemo.sh" ]
