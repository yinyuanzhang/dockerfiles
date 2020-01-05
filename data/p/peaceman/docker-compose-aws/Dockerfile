FROM docker:stable

RUN apk -v --update add \
        python py-pip bash  \
    && pip install awscli docker-compose \
    && apk -v --purge del py-pip \
    && rm /var/cache/apk/*
    
