FROM alpine
MAINTAINER "Florian Baader <florian.baader@selectcode.de>"
RUN apk add wget --no-cache
RUN wget https://github.com/reactiveops/polaris/releases/download/0.2.1/polaris_0.2.1_Linux_x86_64.tar.gz -O - | tar -xz -C /usr/local/bin/ && chmod +x /usr/local/bin/polaris
