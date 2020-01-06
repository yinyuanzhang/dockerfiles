FROM alpine

LABEL author="Sebastian Wegert <swe@covis.de>"

ENV K8S_VERSION="v1.14.8"

RUN apk add --update ca-certificates \
&& apk add --update -t deps curl \
&& curl -L https://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
&& chmod +x /usr/local/bin/kubectl \
&& apk del --purge deps \
&& rm /var/cache/apk/*

#ENTRYPOINT ["kubectl"]
#CMD ["version"] 
