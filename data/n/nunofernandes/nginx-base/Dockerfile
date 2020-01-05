
FROM nginx:mainline-alpine

## Make the project README available for `usage`
COPY README.md /

RUN apk --no-cache add bash 

ENV CONFD_VERSION=0.16.0
ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 /usr/bin/confd
COPY entrypoint.sh /usr/local/bin/

COPY nginx.conf.tmpl /etc/confd/templates/nginx.tmpl
COPY nginx.toml /etc/confd/conf.d/nginx.toml

## Rewrite our template file with our ENV-based parameters
## See README.md to know which vars are required
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
