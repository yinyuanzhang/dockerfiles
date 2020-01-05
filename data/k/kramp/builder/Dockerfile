FROM golang:alpine AS BUILDER
RUN apk --no-cache add git
WORKDIR /go/src/github.com/kramphub/
RUN git clone https://github.com/kramphub/kiya.git
RUN CGO_ENABLED=0 go install ./kiya

FROM google/cloud-sdk:alpine
COPY --from=BUILDER /go/bin/kiya /usr/bin
RUN chmod 755 /usr/bin/kiya

#RUN gcloud components install --quiet kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/bin/kubectl
RUN chmod 755 /usr/bin/kubectl

RUN mkdir -p /root/.config/gcloud
