FROM nvllsvm/emby-unlocked:latest

RUN apk add  --no-cache  --update curl
HEALTHCHECK --interval=15s --timeout=15s --start-period=30s CMD curl -f http://localhost:8096/emby/system/info/public?format=json || exit 1
