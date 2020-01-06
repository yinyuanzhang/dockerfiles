FROM alpine:latest

# Add dependencies and autosub
RUN apk add --no-cache python py-pip \
 && pip install \
    cheetah \
    six \
 && wget https://github.com/BenjV/autosub/archive/master.zip \
 && unzip master.zip \
 && rm master.zip \

 && mkdir -p \
    /series \
    /backup

EXPOSE 9960

WORKDIR /autosub-master

CMD ["python", "AutoSub.py", "-l"]
