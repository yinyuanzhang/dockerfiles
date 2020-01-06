FROM alpine as builder 
RUN apk update && apk add alpine-sdk openssl-dev
ADD main.cpp /
RUN gcc -o sha2 main.cpp -lssl -lcrypto
ENTRYPOINT ["ash"]

FROM alpine
#apk update && 
RUN apk add --no-cache openssl
COPY --from=builder /sha2 /
CMD ["/sha2"]

