FROM ubuntu:16.04 AS build

LABEL maintainer="kyontan <kyontan@monora.me>"

RUN sed -i.bak -e "s%http:[^ ]\+%http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu/%g" /etc/apt/sources.list

RUN apt update
RUN apt install -y build-essential gcc-5-multilib g++-5-multilib

ADD . /cacti

WORKDIR /cacti

RUN make DBG=-static

FROM scratch

COPY --from=build /cacti/cacti /cacti
COPY --from=build /cacti/*.cfg /

ENTRYPOINT ["/cacti"]
