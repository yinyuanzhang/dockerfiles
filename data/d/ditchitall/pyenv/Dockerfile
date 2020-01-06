FROM python:2.7-alpine3.8

ENV PYENV_ROOT=/opt/pyenv \
    PYENV_PKG_VERSION=1.2.6

ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

COPY scripts/install-builddeps.sh /tmp/scripts/install-builddeps.sh
COPY scripts/install-pyenv.sh /tmp/scripts/install-pyenv.sh

RUN set -x \
    && chmod +x /tmp/scripts/* \
    && /tmp/scripts/install-builddeps.sh \
    && /tmp/scripts/install-pyenv.sh \
    && rm -rf /tmp/scripts \
    && find ${PYENV_ROOT} -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +;

WORKDIR ${PYENV_ROOT}

ARG PYTHON2_VERSION=2.7.15
ARG PYTHON34_VERSION=3.4.8
ARG PYTHON35_VERSION=3.5.5
ARG PYTHON36_VERSION=3.6.6

ENV PYTHON2_VERSION=${PYTHON2_VERSION} \
    PYTHON34_VERSION=${PYTHON34_VERSION} \
    PYTHON35_VERSION=${PYTHON35_VERSION} \
    PYTHON36_VERSION=${PYTHON36_VERSION}

RUN set -x \
    && pyenv install "$PYTHON2_VERSION" \
    && pyenv install "$PYTHON34_VERSION" \
    && pyenv install "$PYTHON35_VERSION" \
    && pyenv install "$PYTHON36_VERSION" \
    && find ${PYENV_ROOT} -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +;

COPY scripts/install-pycryptography.sh /tmp/scripts/install-pycryptography.sh

ENV CRYPTOGRAPHY_VERSION=2.3 \
    OPENSSL_VERSION=1.1.0h \
    OPENSSL_GPG_KEY=8657ABB260F056B1E5190839D9C4D26D0E604491

RUN set -x \
    && chmod +x /tmp/scripts/* \
    && for py_version in $(pyenv versions --bare --skip-aliases); \
        do \
            pyenv global $py_version; \
            pip install -U pip; \
            /tmp/scripts/install-pycryptography.sh; \
            find ${PYENV_ROOT} -depth \
            \( \
                \( -type d -a \( -name test -o -name tests \) \) \
                -o \
                \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
            \) -exec rm -rf '{}' +; \
            pyenv rehash; \
        done \
    && rm -rf /tmp/scripts

RUN pyenv global system "$PYTHON2_VERSION" "$PYTHON36_VERSION" "$PYTHON35_VERSION" "$PYTHON34_VERSION"

RUN set -x \
    && apk add --update su-exec \
    && pip install tox \
    && rm -rf /var/cache/apk/*

COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
