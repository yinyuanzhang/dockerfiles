FROM anapsix/alpine-java:8_jdk

RUN apk add --no-cache bash
RUN apk --no-cache add curl
RUN mkdir -p /opt/services/logs
ENV CONFIG_SERVER=http://localhost:8888
ENV PROFILE=docker
COPY wait-for-it.sh /
RUN chmod +x wait-for-it.sh
ENV ATM_BO_PORT=5400
ENV ATM_PS_PORT=5401
ENV ATM_LOG_PORT=5402
EXPOSE 5400
EXPOSE 5401
EXPOSE 5402
COPY start.sh /
RUN chmod +x start.sh
COPY siac-ms-ps-atm.jar /opt/services/
COPY siac-ms-ps-log-autorizacion.jar /opt/services/
COPY siac-ms-bo-atm.jar /opt/services/
CMD ./start.sh 
