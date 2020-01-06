FROM ubuntu:latest
USER root
RUN apt update && \
    apt -y install \
      software-properties-common \
      ffmpeg \
      shntool \
      cuetools \
      vim && \
    add-apt-repository -y ppa:flacon && \
    apt -y install flacon
ADD https://raw.githubusercontent.com/ysegorov/dotfiles/master/bin/cuesplit.sh /usr/local/bin/.
RUN chmod +x /usr/local/bin/cuesplit.sh
