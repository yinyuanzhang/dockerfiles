FROM python:3

WORKDIR /app

RUN wget https://kloudio-docker.s3-us-west-2.amazonaws.com/frontend/app.tar.gz

RUN tar -xvzf app.tar.gz

RUN mv dist/* .

RUN rm -rf app

RUN rm app.tar.gz

CMD [ "python3", "-m", "http.server", "8080" ]

EXPOSE 8080
