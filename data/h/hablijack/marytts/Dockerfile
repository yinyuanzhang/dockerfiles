FROM anapsix/alpine-java:latest

RUN wget -O marytts.zip 'https://github.com/marytts/marytts/releases/download/v5.2/marytts-5.2.zip'
RUN mkdir marytts && unzip -d marytts marytts.zip && rm marytts.zip

RUN wget -O /marytts/marytts-5.2/voice-bits3-hsmm-5.2.zip 'https://github.com/marytts/voice-bits3-hsmm/releases/download/v5.2/voice-bits3-hsmm-5.2.zip'
RUN unzip -o -d /marytts/marytts-5.2/ /marytts/marytts-5.2/voice-bits3-hsmm-5.2.zip && rm /marytts/marytts-5.2/voice-bits3-hsmm-5.2.zip

RUN ls -l

CMD /marytts/marytts-5.2/bin/marytts-server

EXPOSE 59125
