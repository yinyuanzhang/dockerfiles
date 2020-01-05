FROM golang:latest

RUN apt-get update && apt-get install -y --no-install-recommends libwebkit2gtk-4.0 \
	&& rm -rf /var/lib/apt/lists/*
  
RUN go get github.com/zserge/webview
