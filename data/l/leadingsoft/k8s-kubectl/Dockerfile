FROM alpine

LABEL maintainer="LeadingSoft <leadingsoft.jp@gmail.com>"

ENV KUBE_LATEST_VERSION="v1.11.1"

ADD ./pks /usr/local/bin/pks
ADD ./pks_login.sh /usr/local/bin/pks_login.sh
RUN apk add --update ca-certificates curl jq expect \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/pks \
 && chmod +x /usr/local/bin/pks_login.sh

WORKDIR /root
CMD ["/bin/sh"]
