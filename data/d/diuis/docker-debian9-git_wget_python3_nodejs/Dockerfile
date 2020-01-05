FROM diuis/docker-debian9-git_wget_python3:v1.0.4

RUN apt-get update && \
    wget -O - https://deb.nodesource.com/setup_10.x | bash && \
    apt-get install -y nodejs && \
    apt-get autoremove && apt-get clean
