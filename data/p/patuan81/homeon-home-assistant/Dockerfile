FROM alpine:latest

COPY homeon-mqtt /
#enviroment variables
#ENV PORT 
#ENV PG_USER camera
#ENV PG_PASSWORD 123cameraDB
#ENV PG_ADDRESS localhost
#ENV PG_PORT 5432
#ENV PG_DB camera

#EXPOSE $PORT

RUN mkdir -p /config

ENTRYPOINT /homeon-mqtt