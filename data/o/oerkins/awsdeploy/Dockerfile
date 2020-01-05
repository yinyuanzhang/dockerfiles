FROM golang:1.12-stretch as stage

WORKDIR /src
COPY . /src
RUN go build -o awsdeploy-app
EXPOSE 8082
CMD [ "./awsdeploy-app" ]