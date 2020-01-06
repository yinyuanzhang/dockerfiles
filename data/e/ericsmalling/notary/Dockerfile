FROM alpine as notary
RUN wget https://github.com/theupdateframework/notary/releases/download/v0.4.3/notary-Linux-amd64 -O /notary
RUN chmod +x /notary

ENTRYPOINT /notary

