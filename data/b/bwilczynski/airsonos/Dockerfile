FROM node:8
EXPOSE 5000-5050

RUN apt-get -q update && apt-get install -qy \
    libavahi-compat-libdnssd-dev \
    libasound2-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json .
RUN npm install
COPY . .

CMD service dbus start && service avahi-daemon start && npm start
