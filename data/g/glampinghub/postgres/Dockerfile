FROM mdillon/postgis:9.4-alpine

LABEL \
    version="2.0" \
    maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"

RUN apk add --no-cache gnupg \
    && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing aws-cli \
    && sed -i '/exec "$@"/i\[ -d /docker-entrypoint.d ] && for f in /docker-entrypoint.d/*; do\n\tcase "$f" in\n\t\t*.sh) echo "$0: running $f"; . "$f";;\n\t\t*.sql) echo "$0: running $f"; "${psql[@]}" -f "$f"; echo;;\n\t\t*.sql.gz) echo "$0: running $f"; gunzip -c "$f" | "${psql[@]}"; echo;;\n\t\t*) if [ -x "$f" ]; then echo "$0: running $f"; "$f"; else echo "$0: ignoring $f"; fi;;\n\tesac\n\techo\ndone\n' /usr/local/bin/docker-entrypoint.sh
