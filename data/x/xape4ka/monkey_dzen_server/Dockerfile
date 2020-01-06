FROM ubuntu

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
RUN apt-get -y install locales
RUN apt -y upgrade

RUN apt install -y python3.7 python3-pip python3.7-dev
RUN python3.7 -m pip install --upgrade pip
COPY . /var/app/monkey_dzen_server
RUN cd /var/app/monkey_dzen_server && python3.7 setup.py build && python3.7 setup.py install
WORKDIR /var/app/monkey_dzen_server

ENTRYPOINT [ "python3.7", "bin/run.py"]
