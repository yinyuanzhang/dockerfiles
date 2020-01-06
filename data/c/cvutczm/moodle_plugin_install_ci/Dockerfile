FROM alpine 

LABEL maintainer Jiri Fryc <jirifryc.cz@jirifryc.cz>

RUN apk --update add git openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*    
