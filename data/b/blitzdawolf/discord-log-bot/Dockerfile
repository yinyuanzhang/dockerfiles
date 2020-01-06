FROM node

ENV TOKEN=None

#Port for the webserver
EXPOSE 3050

COPY ./src /var

RUN ls /var/bot

#RUN apt-get -y update && \
#    apt-get install -y nodejs && \
#    apt-get install -y npm

RUN cd /var/bot && \
    npm install

CMD [ "node", "/var/bot" ]