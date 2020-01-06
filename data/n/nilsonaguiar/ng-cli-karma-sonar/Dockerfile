FROM trion/ng-cli-karma:8.0.3

# Creates the directory and all the parents (if they don’t exist)
RUN mkdir -p /usr/share/man/man1 \
    && apt-get update \
    && apt-get install -y openjdk-8-jre
