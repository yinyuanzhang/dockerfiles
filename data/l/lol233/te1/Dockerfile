FROM alpine

RUN apk update && apk add ca-certificates && update-ca-certificates && apk add wget
RUN wget https://raw.githubusercontent.com/calm04061/proxy-lantern/56f8a344d11c474b05bcec319f4c5f1cd5c5e9a6/lantern_linux_amd64 -O lantern
RUN chmod +x lantern
EXPOSE 8787
 
CMD ["/lantern", "--addr", "0.0.0.0:8787"]
