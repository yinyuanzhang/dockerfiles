FROM node:11.13.0-stretch-slim
MAINTAINER James Salvatore "jimmy.c.salvatore@gmail.com"

COPY . /src
WORKDIR /src

RUN apt-get update -y \
  && apt-get install libgl1-mesa-glx -y \
  && apt-get autoremove -y \
  && apt-get clean

RUN npm i -S

CMD ["npx", "gridsome", "serve"]
