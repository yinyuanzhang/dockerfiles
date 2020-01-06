FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip build-essential
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]