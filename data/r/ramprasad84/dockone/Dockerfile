

FROM ubuntu
RUN apt update
COPY src /datas

# Install prerequisites
RUN apt-get update && apt-get install -y \
curl
CMD /bin/bash

RUN apt -qq -y  install curl software-properties-common git
RUN echo "Data Loading.."
RUN curl -sL https://deb.nodesource.com/setup_12.x |bash -
RUN apt install -y nodejs
RUN git clone https://github.com/ramprasad84/gittwo;

#COPY . /Devops/gittwo/gittwo
RUN cd gittwo
WORKDIR gittwo
RUN npm install
EXPOSE 8000
#RUN npm start
CMD [ 'npm','start' ]

