FROM golang as build
COPY . /go/src/goflyway
WORKDIR /go/src/goflyway
RUN cd cmd/goflyway && go-wrapper download
RUN CGO_ENABLED=0 make build
ENTRYPOINT ["bash"]

FROM scratch
COPY --from=build go/src/goflyway/build/goflyway /goflyway
EXPOSE 8102 8100 8101
ENTRYPOINT ["/goflyway"]
