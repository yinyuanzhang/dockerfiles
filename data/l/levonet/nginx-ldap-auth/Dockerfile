FROM python:2-alpine

RUN apk --no-cache add openldap-dev \
    && apk --no-cache add --virtual build-dependencies build-base curl \
    && pip install python-ldap \
    && mkdir -p /usr/src/nginx-ldap-auth \
    && curl -fSL https://github.com/nginxinc/nginx-ldap-auth/archive/master.tar.gz -o /usr/src/nginx-ldap-auth.tar.gz \
    && tar -zxC /usr/src/nginx-ldap-auth -f /usr/src/nginx-ldap-auth.tar.gz --strip 1 \
    && cp /usr/src/nginx-ldap-auth/nginx-ldap-auth-daemon.py / \
    && rm -rf /usr/src/nginx-ldap-auth \
    && apk del build-dependencies

EXPOSE 8888

CMD ["python", "/nginx-ldap-auth-daemon.py", "--host", "0.0.0.0", "--port", "8888"]
