# run: docker run -i cubeearth/puttygen  < id_rsa > id_rsa.ppk

FROM alpine

RUN apk --no-cache add putty openssh-keygen

COPY run.sh /usr/local/bin/

ENTRYPOINT [ "/usr/local/bin/run.sh" ]
