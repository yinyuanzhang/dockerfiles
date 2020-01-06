FROM openjdk:8-jre

RUN mkdir -p /opt/shinyproxy/
RUN wget https://www.shinyproxy.io/downloads/shinyproxy-2.0.2.jar -O /opt/shinyproxy/shinyproxy.jar

WORKDIR /opt/shinyproxy/
RUN mkdir app_yml

COPY ./start_shinyproxy.sh ./start_shinyproxy.sh

CMD ["bash", "start_shinyproxy.sh"]
