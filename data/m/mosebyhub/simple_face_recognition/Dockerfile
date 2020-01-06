FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

RUN pip3 install --upgrade pip
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
RUN apt-get install -y libglib2.0-0 libsm6 libxrender-dev libxext6

COPY models/ /app/models/
COPY src/ /app/src/
COPY serve_run_params.json /app/
COPY train_run_params.json /app/
ENTRYPOINT [ "python3","-m", "src.run" ]

