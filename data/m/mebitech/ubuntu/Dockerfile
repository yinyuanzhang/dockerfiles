FROM ubuntu:16.04

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install curl wget unzip software-properties-common nano -y \
  && apt-get autoremove
  

CMD ["bash"]