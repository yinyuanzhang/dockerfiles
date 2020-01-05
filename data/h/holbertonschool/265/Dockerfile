# Container for project 265 

FROM holbertonschool/265-0
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>

RUN apt-get update

RUN apt-get install -y ssh 
RUN apt-get install -y openssh-server
RUN apt-get install -y curl

RUN mkdir -p /var/run/sshd

ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh

# start run!
CMD ["./tmp/run.sh"]
