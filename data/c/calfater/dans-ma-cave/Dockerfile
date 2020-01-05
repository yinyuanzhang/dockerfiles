FROM node:8.2.1

#RUN apt-get update
#RUN apt-get install -y vim
#RUN apt-get install -y jq

ARG wd=/home/dans-ma-cave
ENV wd=$wd

WORKDIR $wd

COPY [".", "."]
RUN npm run build
RUN mv dist/data dist/data-origin
RUN mkdir /data
RUN ln -s /data dist/data

EXPOSE 3000

ENTRYPOINT ["./start.sh"]
COPY ["docker/start.sh", "start.sh"]
RUN ["chmod", "+x", "start.sh"]
