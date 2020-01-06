FROM microsoft/aspnet:latest

COPY . /app
WORKDIR /app

RUN mkdir 'approot/src/WebController/Databases'

EXPOSE 1312
ENTRYPOINT ["sh", "web"]