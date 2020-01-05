FROM apluslms/service-base:django-1.7

COPY rootfs /

# Set container related configuration via environment variables
ENV CONTAINER_TYPE="grader" \
    GRADER_LOCAL_SETTINGS="/srv/grader-cont-settings.py" \
    GRADER_SECRET_KEY_FILE="/local/grader/secret_key.py" \
    GRADER_AJAX_KEY_FILE="/local/grader/ajax_key.py"

ARG BRANCH=v1.6rc1
RUN : \
 && apt_install \
      apt-transport-https \
      jq \
      # temp
      gnupg curl \
      libmagic1 \
      libxml2-dev \
      libxslt1-dev \
      zlib1g-dev \
  # install docker-ce
 && curl -LSs https://download.docker.com/linux/debian/gpg | apt-key add - >/dev/null 2>&1 \
 && echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" > /etc/apt/sources.list.d/docker.list \
 && apt_install docker-ce \
\
  # create user
 && adduser --system --no-create-home --disabled-password --gecos "MOOC-Grader webapp server,,," --home /srv/grader --ingroup nogroup grader \
 && mkdir /srv/grader && chown grader.nogroup /srv/grader \
\
 && cd /srv/grader \
\
  # clone. patch and prebuild .pyc files
 && git clone --quiet --single-branch --branch $BRANCH https://github.com/Aalto-LeTech/mooc-grader.git . \
 && (echo "On branch $(git rev-parse --abbrev-ref HEAD) | $(git describe)"; echo; git log -n5) > GIT \
 && rm -rf .git \
 && patch -p1 < /srv/cors.patch \
 && python3 -m compileall -q . \
\
  # install requirements, remove the file, remove unrequired locales and tests
 && pip_install -r requirements.txt \
 && rm requirements.txt \
 && find /usr/local/lib/python* -type d -regex '.*/locale/[a-z_A-Z]+' -not -regex '.*/\(en\|fi\|sv\)' -print0 | xargs -0 rm -rf \
 && find /usr/local/lib/python* -type d -name 'tests' -print0 | xargs -0 rm -rf \
\
  # default course link
 && mkdir -p /srv/grader/courses/ \
 && mkdir -p /srv/courses/default \
 && ln -s -T /srv/courses/default /srv/grader/courses/default \
 && chown -R grader.nogroup \
    /srv/courses \
    /srv/grader \
\
  # clean
 && rm -rf $GRADER_SECRET_KEY_FILE $GRADER_AJAX_KEY_FILE \
 && rm -rf /etc/init.d/ /tmp/* \
 && apt_purge \
      gnupg curl \
      libxml2-dev \
      libxslt1-dev \
      zlib1g-dev \
 && :


VOLUME /srv/courses/default
WORKDIR /srv/grader/
EXPOSE 8080
CMD [ "manage", "runserver", "0.0.0.0:8080" ]
