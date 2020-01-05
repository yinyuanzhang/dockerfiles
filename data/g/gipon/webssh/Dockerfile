FROM alpine:3.7
MAINTAINER by Gipon
RUN apk update \
&& apk upgrade \
&& apk add --no-cache python \
    python-dev gcc make libc-dev \
    py-pip libffi-dev openssl-dev \
&& pip install webssh
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
EXPOSE 6080
CMD ["wssh", "--address=0.0.0.0", "--port=6080"]

