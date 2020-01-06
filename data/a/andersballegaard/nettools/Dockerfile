FROM ubuntu:18.04

COPY . .

RUN apt-get update

RUN apt-get install python3 python3-pip -y
RUN apt-get install python python-pip -y
RUN apt-get install ansible -y
RUN apt-get install curl wget -y
RUN apt-get install net-tools iproute2 -y
RUN apt-get install iputils-ping traceroute -y
RUN apt-get install nmap -y
RUN apt-get install tcpdump -y
RUN apt-get install iperf3 -y
RUN apt-get install dnsutils -y
RUN apt-get install git -y
RUN apt-get install telnet -y
RUN apt-get install tmux -y

RUN pip3 install -r config/requirements.txt
RUN pip install -r config/requirements-py2.txt

RUN echo "root:admin" | chpasswd

