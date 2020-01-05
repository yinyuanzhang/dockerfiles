FROM ubuntu:rolling
RUN apt update
RUN apt-get dist-upgrade -y
RUN apt-get install git -y
RUN mkdir /repos
ADD Scripts/ /Scripts/
#RUN useradd -ms /bin/bash git
#USER git
CMD ["/Scripts/timer.sh"]
