FROM golang:1.12-alpine
RUN apk add --no-cache graphviz git
RUN go get -u golang.org/x/lint/golint
RUN go get github.com/mdempsky/maligned
RUN go get -u github.com/nickng/dingo-hunter
RUN go get -u github.com/360EntSecGroup-Skylar/goreporter
