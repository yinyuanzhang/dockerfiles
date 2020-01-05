FROM node:8

RUN mkdir /streamboard-wa
WORKDIR /streamboard-wa

COPY . /streamboard-wa
RUN npm install superstatic -g

EXPOSE 8080

CMD superstatic public --port 8080 --host 0.0.0.0
