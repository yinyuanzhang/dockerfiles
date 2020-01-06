FROM maven:3.5.0-jdk-8

ENV MAVEN_HOME ""
ENV MAVEN_CONFIG ".m2"

RUN apt-get update && apt-get install -y \
  zip \
  unzip \
  && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash --user-group builder

WORKDIR /home/builder

RUN chown -R builder:builder /home/builder
USER builder
RUN mkdir -p .m2

CMD ["mvn"]
