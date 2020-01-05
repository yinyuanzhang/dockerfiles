FROM dclong/lubuntu-jdk

RUN add-apt-repository ppa:mmk2410/intellij-idea \
    && apt-get update \
    && apt-get install -y intellij-idea-community \
    && apt-get autoremove \
    && apt-get autoclean

COPY settings /settings
COPY scripts /scripts

