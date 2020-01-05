FROM ubuntu:18.04

LABEL maintainer "kun(i@imux.top)"

ENV REFRESHED_AT 2019-03-26 \
    DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8"

RUN apt-get update && \
    apt-get install -y iverilog && \
    apt-get autoremove -y

ADD ./startup.sh / 
RUN chmod a+x /startup.sh

RUN mkdir ~/verilog

ENTRYPOINT ["/startup.sh"]
CMD ["output"]
