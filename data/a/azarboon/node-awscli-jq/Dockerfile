FROM node:9-alpine
RUN apk update && apk add jq && apk add py-pip && pip install awscli --upgrade --user

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /home

CMD ["sh"]
