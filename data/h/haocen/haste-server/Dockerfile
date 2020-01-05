FROM node:carbon

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -yq \
    git

RUN git clone https://github.com/Haocen/haste-server.git /app
WORKDIR /app
RUN npm install

ADD ./app.sh /app/
RUN chmod 755 app.sh

EXPOSE 7777

ENV STORAGE_TYPE file

CMD [ "./app.sh" ]
