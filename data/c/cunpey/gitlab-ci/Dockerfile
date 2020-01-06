FROM node:10.16.1-alpine
RUN apk update -q && apk add --no-cache bash -q && apk add --no-cache openssh -q && apk add --no-cache lftp -q && apk add --no-cache tzdata -q && apk add --no-cache xclip -q
CMD ["/bin/bash"]