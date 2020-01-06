FROM redmobile/base
EXPOSE 8080
ADD . /app
RUN cd /app; npm i
WORKDIR /app
ENTRYPOINT coffee index.coffee
