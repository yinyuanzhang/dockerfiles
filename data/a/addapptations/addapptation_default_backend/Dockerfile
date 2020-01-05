# Builder

FROM golang:1.8 as builder
COPY . .
RUN make


# Runner

FROM scratch
COPY --from=builder / /
COPY /www /www
ENTRYPOINT ["/"]