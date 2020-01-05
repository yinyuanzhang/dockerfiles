FROM golang:1.8 as compiler
MAINTAINER brian.wojtczak@1and1.co.uk
ARG drone_git_ref=v0.7.3
WORKDIR /go/src/github.com/drone/drone/
RUN \
  git clone https://github.com/drone/drone.git --branch $drone_git_ref --single-branch . && \
  go get -u github.com/drone/drone-ui/dist && \
  go get -u golang.org/x/tools/cmd/cover && \
  go build -ldflags '-extldflags "-static" -X github.com/drone/drone/version.VersionDev=1and1' -o release/drone github.com/drone/drone/drone

FROM 1and1internet/ubuntu-16
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files/ /
RUN \
  apt-get update -q && \
  apt-get install -y inotify-tools && \
  apt-get clean -q -y && \
  rm -rf /var/lib/apt/lists/* && \
  cd /usr/share/ca-certificates/ && \ 
  mkdir 1and1 && \ 
  cd 1and1 && \ 
  wget http://pub.pki.1and1.org/pukirootca1.crt && \
  wget http://pub.pki.1and1.org/pukiissuingca1.crt && \
  openssl x509 -noout -in pukirootca1.crt -fingerprint -sha256 >a && \
  echo "SHA256 Fingerprint=6B:DE:2B:46:BA:BF:52:1E:09:45:41:16:AE:CD:73:65:DE:79:EB:D9:49:FE:B3:9C:E9:F1:1C:2B:46:60:C0:CD" | diff a - && \
  openssl x509 -noout -in pukiissuingca1.crt -fingerprint -sha256 >b && \
  echo "SHA256 Fingerprint=E1:99:91:7B:7F:DE:02:AF:00:AC:D0:65:0D:7B:E0:42:2A:A6:8E:E4:C1:53:BA:12:EF:15:3D:DB:62:A2:9A:DC" | diff b - && \
  rm a b && \
  cd .. && \ 
  ls -1 1and1/* >>  /etc/ca-certificates.conf && \ 
  update-ca-certificates && \
  ln -s /usr/bin/drone-server /usr/bin/server && \
  ln -s /usr/bin/drone-agent /usr/bin/agent && \
  chmod -R 777 /hooks/supervisord-pre.d/ /etc/supervisor/conf.d/

COPY --from=compiler /go/src/github.com/drone/drone/release/drone /opt/drone/drone

EXPOSE 8000 80 443
