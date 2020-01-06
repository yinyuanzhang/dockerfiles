FROM alpine:latest

RUN apk -v --no-cache add \
        python3 \
        ca-certificates \
        groff \
        less \
        bash \
        make \
        curl \
        wget \
        zip \
        git \
        && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade awscli && \
    pip3 install --upgrade troposphere>=2.0.0 && \
    update-ca-certificates

RUN git clone https://github.com/zaro0508/sceptre-stack-termination-protection-hook.git hooks/sceptre-stack-termination-protection-hook/

ADD resolvers /resolvers
ADD hooks /hooks
ADD sceptre /sceptre 

RUN pip3 install /resolvers/* 
RUN pip3 install /hooks/* 
RUN pip3 install /sceptre

VOLUME [ "/root/.aws" ]
VOLUME [ "/opt/app" ]
WORKDIR /opt/app

CMD ["sceptre", "--version"]
