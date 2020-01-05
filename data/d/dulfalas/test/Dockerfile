FROM alpine:3.5 as build 
RUN apk update && \ 
      apk add --update alpine-sdk 
RUN mkdir /app 
RUN mkdir /app2 
WORKDIR /app 
COPY hello.c /app 
RUN mkdir bin 
RUN gcc -Wall hello.c -o bin/hello 
CMD /app/bin/hello

FROM alpine:3.5
COPY --from=build /app/bin/hello /app/hello
CMD /app/hello
