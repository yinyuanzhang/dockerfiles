FROM cultureamp/docker-elixir:latest
MAINTAINER Larry Liang <larry@cultureamp.com>

ENV WORK_DIR /usr/src/myapp
WORKDIR $WORK_DIR

COPY . $WORK_DIR/
RUN $WORK_DIR/bld

ENTRYPOINT ["mix", "phoenix.server"]
