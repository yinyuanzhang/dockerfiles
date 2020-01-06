FROM python:3.6-alpine3.6 as builder

RUN apk --no-cache upgrade && apk --no-cache add build-base tar musl-utils openssl-dev git
RUN pip3 install setuptools cx_Freeze==6.0b1

RUN git clone https://github.com/elastic/curator
WORKDIR /curator
RUN ln -s /lib/libc.musl-x86_64.so.1 ldd
RUN ln -s /lib /lib64
RUN pip3 install -r requirements.txt
#RUN python3 setup.py build_exe
RUN python3 setup.py install

#FROM alpine:3.6
#RUN apk --no-cache upgrade && apk --no-cache add ca-certificates && update-ca-certificates && apk --no-cache add wget
#COPY --from=builder curator/build/exe.linux-x86_64-3.6 /curator/
USER nobody:nobody
#ENTRYPOINT ["/curator/curator"]
ENTRYPOINT ["python3", "/curator/run_curator.py"]
