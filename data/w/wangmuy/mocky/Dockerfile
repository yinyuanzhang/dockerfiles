FROM hseeberger/scala-sbt
MAINTAINER wangmuy <wangmuy@gmail.com>

# COPY sbt.repositories /root/.sbt/repositories
COPY . /app

WORKDIR /app
# cache sbt
RUN sbt -Dsbt.override.build.repos=true -Dsbt.repository.secure=false dist

# TODO: use dist version
CMD ["sbt", "-Dsbt.override.build.repos=true", "-Dsbt.repository.secure=false", "run", "."]
