FROM alpine as builder
RUN apk update && apk add alpine-sdk git ncurses-dev
RUN git clone https://github.com/abishekvashok/cmatrix.git
WORKDIR /cmatrix
RUN ./configure && make
ENTRYPOINT ["ash"]

FROM alpine
#apk update &&
RUN apk add --no-cache ncurses
WORKDIR /root
COPY --from=builder /cmatrix/cmatrix .
CMD ["./cmatrix"]

