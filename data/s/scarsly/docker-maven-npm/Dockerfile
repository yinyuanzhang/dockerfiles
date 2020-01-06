FROM maven:3.6.0-jdk-11-slim

RUN apt-get update && apt-get install gnupg -y && curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
apt-get install nodejs -y

ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]
