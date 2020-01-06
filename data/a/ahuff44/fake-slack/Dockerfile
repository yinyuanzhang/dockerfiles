FROM golang:1.12

ENV APP_HOME /usr/src/app/
WORKDIR $APP_HOME

RUN useradd -u 1000 -M docker \
  && mkdir -p /messages/slack \
  && chown docker /messages/slack \
  && chown -R docker $GOPATH \
  && chown -R docker $APP_HOME \
  && true
# USER docker
# ^this causes problems during `go mod download` (later):
# failed to initialize build cache at /home/docker/.cache/go-build: mkdir /home/docker: permission denied

# download the app's dependencies early in the dockerfile (for caching)
COPY --chown=docker go.mod go.sum $APP_HOME
RUN go mod download

COPY --chown=docker . $APP_HOME
RUN go install -v ./...

EXPOSE 9393

CMD ["docker-fake-slack"]
