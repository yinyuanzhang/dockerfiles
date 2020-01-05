FROM docker:19.03.5-dind

RUN apk --no-cache add make curl gettext git

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/usr/bin/env", "sh", "/entrypoint.sh" ]
