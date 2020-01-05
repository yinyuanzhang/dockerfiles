FROM node:8

EXPOSE 8080

WORKDIR /app
COPY . /app

RUN npm install

RUN useradd ebiiim
RUN chown -R ebiiim .

USER ebiiim
CMD bash -c "npm run build && npm run start"

