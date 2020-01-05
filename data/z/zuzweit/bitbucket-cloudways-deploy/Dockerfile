FROM alpine:3.9
RUN apk update && apk add bash
RUN apk add openssh
RUN mkdir ~/.ssh
RUN echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
RUN apk add sshpass
COPY pipe /
RUN chmod +x pipe.sh
ENTRYPOINT ["/pipe.sh"]