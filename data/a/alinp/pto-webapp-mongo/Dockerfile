# Dockerfile-mongo

FROM mongo:4.0.6-xenial

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pymongo
RUN pip3 install werkzeug

ADD mongo/ /docker-entrypoint-initdb.d

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 27017
CMD ["mongod"]