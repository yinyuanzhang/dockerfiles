FROM python:alpine

WORKDIR /app
COPY . /app
ENV TZ=Asia/Shanghai

RUN \
    apk update && \
    apk upgrade && \
    apk add --no-cache ffmpeg wget yarn npm nodejs yarn libstdc++ tzdata && \
    pip install pipenv && \
    pip install --no-cache-dir you-get youtube-dl && \
    rm -rf /var/cache/apk/* && \
    yarn;

EXPOSE 3000
CMD ["npm", "run", "start"]