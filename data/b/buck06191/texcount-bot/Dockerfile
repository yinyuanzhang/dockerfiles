FROM node:latest

ENV PORT=80


WORKDIR /code
COPY package*.json ./
RUN npm install
RUN curl -o /tmp/ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip /tmp/ngrok.zip

RUN  curl -o texcount.zip https://app.uio.no/ifi/texcount/download.php?file=texcount_3_1_1.zip \
    && unzip texcount.zip && rm texcount.zip && rm -r Doc

COPY . /code

RUN mkdir data

EXPOSE ${PORT}
CMD [ "npm", "start" ]


