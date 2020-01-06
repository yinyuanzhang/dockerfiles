FROM alpine

WORKDIR /usr/local/service

ENV DJANGO_SETTINGS_MODULE=estate.settings \
    PYTHONPATH=/usr/local/service \
    PATH=/usr/local/service/node_modules/.bin/:$PATH

ENV NODE_VERSION 6.14.3
COPY ./package.json /usr/local/service/package.json
COPY ./TERRAFORM_URL.txt /usr/local/service/TERRAFORM_URL.txt
COPY ./.babelrc /usr/local/service/.babelrc
COPY ./webpack /usr/local/service/webpack
COPY ./estate /usr/local/service/estate
COPY ./patches /usr/local/service/patches

RUN apk update && \
    apk add --no-cache gcc \
                       musl-dev \
                       ca-certificates \
                       libffi-dev \
                       yaml-dev \
                       libmemcached-dev \
                       zlib-dev \
                       postgresql-dev \
                       python2-dev \
                       openldap-dev \
                       unzip \
                       git \
                       patch \
                       curl \
                       nodejs \
                       npm \
                       && \
    mkdir -p /usr/local/service && \
    curl -slO https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install --ignore-installed -U chardet && \
    pip install ply && \
    curl -L --silent $(cat /usr/local/service/TERRAFORM_URL.txt) > /terraform.zip && \
    unzip /terraform.zip -d /bin/ && \
    rm /terraform.zip && \
    pip install coreapi \
                    boto3 \
                    dj-database-url \
                    Django \
                    django-auth-ldap \
                    django-braces \
                    django-crispy-forms \
                    django-cors-headers \
                    django-elasticache \
                    django-extensions \
                    django-filter==1.1.0 \
                    django-permanent \
                    django-rest-swagger \
                    django-simple-history \
                    django-storages \
                    django-webpack-loader \
                    djangorestframework==3.6.3 \
                    gevent \
                    gunicorn \
                    hvac \
                    Jinja2 \
                    markdown \
                    psycopg2-binary \
                    pyhcl \
                    python-consul \
                    python-memcached \
                    raven \
                    semantic_version \
                    structlog \
                    whitenoise \
                    chardet \
                    && \
        pip install --global-option="--with-libyaml" pyyaml && \
        npm install phantomjs-prebuilt && \
        npm install && \
        patch /usr/local/service/node_modules/react-jsonschema-form/lib/utils.js /usr/local/service/patches/utils.patch && \
        webpack --bail --config webpack/webpack.prod.config.js && \
        django-admin collectstatic --noinput

ENTRYPOINT ["sh", "estate/local.sh" ]
