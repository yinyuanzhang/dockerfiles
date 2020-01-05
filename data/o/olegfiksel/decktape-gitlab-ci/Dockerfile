FROM debian:8.3

ENV TERM xterm-color

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    libfontconfig \
    ca-certificates

WORKDIR /decktape

# Copy each directory individually as Docker Hub does not take .dockerignore into account for the moment
# COPY . .
COPY libs libs/
COPY plugins plugins/
COPY decktape.js ./

RUN curl -f \
    -L https://github.com/astefanutti/decktape/releases/download/v1.0.0/phantomjs-linux-x86-64 \
    -o phantomjs && chmod +x phantomjs
