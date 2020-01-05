FROM microsoft/powershell:ubuntu-16.04 as expand-crawler-template

RUN apt-get update              \
    && apt-get install -y rsync \
    && rm -rf /var/lib/apt/lists/*