FROM atlassian/pipelines-awscli:1.16.18

LABEL maintainer="github@lugana707"

WORKDIR /src
ADD pipe.sh .
ENTRYPOINT [ "/src/pipe.sh" ]
