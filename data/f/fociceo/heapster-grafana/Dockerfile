FROM java:8u111-alpine

RUN apk add --no-cache \
      git  \
&&  git clone https://github.com/albertogoffi/toradocu.git \
&&  cd toradocu \
&&  ./gradlew shadowJar

CMD [ 'ls -l']
