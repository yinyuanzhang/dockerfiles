FROM golang AS build
COPY . .
RUN go build -o envy

FROM scratch
COPY --from=build /go/envy /
VOLUME /config
CMD ["/envy"]
