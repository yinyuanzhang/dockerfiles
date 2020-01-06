FROM homeassistant/home-assistant:latest
LABEL maintainer="Niels Ardts <nardts@gmail.com>"

RUN apt-get update && \
    apt-get -y install socat ser2net  && \
    apt-get clean
RUN mkdir /runwatch

# Copy all the run and check files
COPY runwatch/* /runwatch/
CMD [ "bash","/runwatch/run.sh" ]
