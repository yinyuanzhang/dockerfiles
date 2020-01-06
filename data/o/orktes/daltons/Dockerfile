FROM orktes/go-vowpal-wabbit

COPY . /src/
RUN cd /src/cmd/decisionservice/ && go build -o /app/decisionservice

# Clean src dir
RUN rm -Rf /src

# TODO create a multi stage build
ENTRYPOINT ["/app/decisionservice"]
