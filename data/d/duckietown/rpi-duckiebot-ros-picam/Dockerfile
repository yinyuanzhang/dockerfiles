FROM duckietown/rpi-duckiebot-base:master18

RUN [ "cross-build-start" ]

ENV READTHEDOCS True
RUN pip install --upgrade picamera==1.13

RUN [ "cross-build-end" ]


COPY run_picamera.sh .
COPY run_watchtower_picamera.sh .

CMD [ "./run_picamera.sh" ]
