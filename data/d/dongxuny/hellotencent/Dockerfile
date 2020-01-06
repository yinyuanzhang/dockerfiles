# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/tencent.com/dongxuny/hello-tencent

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go install tencent.com/dongxuny/hello-tencent

ADD ./content /content

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/hello-tencent
