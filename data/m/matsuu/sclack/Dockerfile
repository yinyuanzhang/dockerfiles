FROM alpine

RUN \
  apk update && \
  apk add libcaca python3 && \
  apk add --virtual=build git && \
  git clone https://github.com/haskellcamargo/sclack.git && \
  cd sclack && \
  pip3 install -r requirements.txt && \
  apk del --purge build

VOLUME /root
WORKDIR /sclack

ENTRYPOINT ["./app.py"]
