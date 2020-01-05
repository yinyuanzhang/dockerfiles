FROM hedlund/java:6
MAINTAINER henrik@hedlund.im

# Install Maven. Doing it this way is a bit blunt - we have no way to control the exact version,
# but as of this writing it's 3.0.5, which suits us perfectly...
RUN apt-get -y install maven

# Export the dependencies directories as a volume
RUN mkdir -p /root/.m2
VOLUME [ "/root/.m2" ]

# Create working directory
RUN mkdir -p /code
VOLUME [ "/code" ]
WORKDIR /code

ENTRYPOINT [ "mvn" ]
