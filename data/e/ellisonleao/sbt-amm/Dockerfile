# Based of https://github.com/hseeberger/scala-sbt debian version , without the user creation,
# and using ammonite.io REPL instead
#
# To cache ivy2 sbt dependencies just call
# $ docker run -it --rm \
#     -v ~/.ivy2:/root/.ivy2 \
#     -v ~/.sbt:/root/.sbt \
#     -v $PWD:/app \
#     -w /app ellisonleao/sbt-amm \
#     sbt ...

FROM openjdk:14-slim-buster
LABEL maintainer "Ellison Leão <ellisonleao@gmail.com>"

ENV AMMONITE_VERSION 1.7.4
ENV SCALA_VERSION 2.12.10
ENV SBT_VERSION 1.3.2

# Install sbt
RUN \
  apt-get -q update && \
  apt-get -y -q --no-install-recommends install curl  && \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get -y -q --no-install-recommends install sbt  && \
  # cleanup package manager caches
  apt-get clean && \
  rm /var/lib/apt/lists/*_*

# Install ammonite repl
RUN curl -L https://github.com/lihaoyi/Ammonite/releases/download/$AMMONITE_VERSION/2.13-1.7.4 > \
        /usr/local/bin/amm && chmod +x /usr/local/bin/amm


# Prepare sbt (warm cache)
RUN \
  sbt sbtVersion && \
  mkdir -p project && \
  echo "scalaVersion := \"${SCALA_VERSION}\"" > build.sbt && \
  echo "sbt.version=${SBT_VERSION}" > project/build.properties && \
  echo "case object Temp" > Temp.scala && \
  sbt compile && \
  rm -r project && rm build.sbt && rm Temp.scala && rm -r target

COPY ./docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["sbt", "--version"]
