FROM alpine/socat

RUN wget -q -O - https://dl.k8s.io/v1.15.1/kubernetes-client-linux-amd64.tar.gz | tar xz && mv kubernetes/client/bin/kubectl /usr/bin/kubectl

COPY *.sh ./
ENTRYPOINT ["./listen.sh"]
EXPOSE 80
