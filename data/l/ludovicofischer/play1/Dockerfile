FROM openjdk:8
LABEL maintainer="Ludovico Fischer <livrerie@gmail.com>"
RUN groupadd -r play && useradd --no-log-init -r -g play -m play
WORKDIR /home/play
USER play
RUN wget https://downloads.typesafe.com/play/1.5.2/play-1.5.2.zip && unzip play-1.5.2.zip && rm play-1.5.2.zip && mv play-1.5.2 play1
ENTRYPOINT ["/home/play/play1/play"]
EXPOSE 9000
