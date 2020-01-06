FROM ubuntu as builder
RUN apt-get update && apt-get install -y curl tar jq
WORKDIR /build
RUN curl -sLo hetzner.tar.gz $(curl --silent https://api.github.com/repos/JonasProgrammer/docker-machine-driver-hetzner/releases | jq -r '. | first | .assets[] | select(.name|contains("linux_amd64")).browser_download_url')
RUN tar xf hetzner.tar.gz && chmod +x docker-machine-driver-hetzner

FROM gitlab/gitlab-runner:latest
COPY --from=builder /build/docker-machine-driver-hetzner /usr/bin

