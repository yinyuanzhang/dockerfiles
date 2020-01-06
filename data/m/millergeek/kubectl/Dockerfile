FROM alpine as curl
RUN apk add --no-cache curl
WORKDIR /downloads
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/\
$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)\
/bin/linux/amd64/kubectl
RUN chmod +x /downloads/kubectl

FROM scratch
COPY --from=curl /downloads/kubectl /kubectl
ENTRYPOINT [ "/kubectl" ]
