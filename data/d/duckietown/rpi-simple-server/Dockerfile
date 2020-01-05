FROM duckietown/rpi-duckiebot-raspberrypi3-python:master18

ENV QEMU_EXECVE 1

EXPOSE 8082
VOLUME /data
WORKDIR /data

CMD python -m SimpleHTTPServer 8082
