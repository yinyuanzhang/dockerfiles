FROM golang as build
RUN CGO_ENABLED=0 go get -u github.com/coyove/goflyway/cmd/goflyway
ENTRYPOINT ["bash"]

FROM scratch
MAINTAINER Ryan Lieu <github-benzBrake@woai.ru>
COPY --from=build /go/bin/goflyway /goflyway
COPY --from=build /go/src/github.com/coyove/goflyway/chinalist.txt /chinalist.txt
EXPOSE 8100 8101 8102
ENTRYPOINT ["/goflyway"]