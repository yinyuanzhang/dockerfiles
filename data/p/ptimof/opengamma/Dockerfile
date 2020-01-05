# docker build -t ptimof/opengamma .

FROM ubuntu:14.04

RUN apt-get update \
 && apt-get install -y git maven openjdk-7-jdk \
 && apt-get autoremove -y \
 && apt-get clean -y

# Get source
WORKDIR /srv
RUN git clone --depth 1 https://github.com/OpenGamma/OG-Platform.git

# Build
WORKDIR OG-Platform
RUN mvn install

# Set up for simulated server
WORKDIR examples/examples-simulated
RUN mvn opengamma:server-init -Dconfig=fullstack

# Run the demo
EXPOSE 8080
CMD [ "mvn", "opengamma:server-run", "-Dconfig=fullstack" ]
