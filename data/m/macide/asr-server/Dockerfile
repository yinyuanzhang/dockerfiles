FROM golbin/kaldi:latest
ENV build_date 2018-09-19 001


RUN apt-get update -y
RUN apt-get install -y zlib1g \
    make \
    automake \
    autoconf \
    sox \
    subversion \
    python3 \
    zlib1g-dev \
    python \
    unzip \
    libtool \
    g++ \
    git \
    bash \
    libfcgi \
    libfcgi-dev \
    spawn-fcgi \
    wget

WORKDIR /home
RUN git clone https://github.com/api-ai/asr-server asr-server
RUN wget https://github.com/api-ai/api-ai-english-asr-model/releases/download/1.0/api.ai-kaldi-asr-model.zip
RUN unzip api.ai-kaldi-asr-model.zip

WORKDIR /home/asr-server
RUN /home/asr-server/configure
RUN make 1> /dev/null




COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 9000

CMD /run.sh
