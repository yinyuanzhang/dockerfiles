FROM alpine:3.4

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

CMD curl -sS https://build.bugsnag.com/ --header "Content-Type: application/json" --data "{ \
    \"apiKey\": \"${BUGSNAG_API_KEY}\", \
    \"appVersion\": \"${APP_VERSION}\", \
    \"releaseStage\": \"${RELEASE_STAGE}\", \
    \"sourceControl\": { \
        \"provider\": \"${SOURCE_CONTROL_PROVIDER}\", \
        \"repository\": \"${REPOSITORY_URL}\", \
        \"revision\": \"${APP_REVISION}\" \
    } \
}"