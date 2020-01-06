FROM alpine:3.10
LABEL maintainer="Lukas f. Paluch <fluktuid@gmail.com>"

RUN apk update
RUN apk add hunspell=1.7.0-r0

VOLUME ["/source"]
WORKDIR /source

COPY de_DE de_DE/
RUN chmod -R 0666 de_DE/

CMD ["sh"]

