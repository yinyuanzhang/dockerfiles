FROM debian

RUN apt-get -y update
RUN apt-get install -y dos2unix
RUN mkdir -p /usr/share/man/man1
RUN apt-get -y install default-jdk
RUN javac -version

COPY /App /SemanticTurkey
COPY /entrypoint.sh /

RUN dos2unix /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 1979

#ENTRYPOINT ["/entrypoint.sh"]