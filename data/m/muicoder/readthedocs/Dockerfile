FROM ubuntu:16.04

ENV APP=rtd \
    GIT=github.com \
    GIT_USER=rtfd \
    GIT_REPO=readthedocs.org \
    USERNAME=admin \
    PASSWORD=admin

SHELL ["/bin/bash", "-c"]

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y \
    curl wget unzip git \
        build-essential \
        python-dev python-pip python-setuptools \
        libxml2-dev libxslt1-dev zlib1g-dev \
\
    && pip install --no-cache-dir --upgrade --force-reinstall pip \
    && pip install --no-cache-dir --upgrade --force-reinstall setuptools \
    && pip install --no-cache-dir --upgrade --force-reinstall virtualenv \
\
    && mkdir $APP && cd $APP \
    && cd /tmp/ && git clone git://$GIT/$GIT_USER/$GIT_REPO.git && mv $GIT_REPO/* /$APP ; cd - \
\
    && sed -i 's/pip==/pip>=/g' requirements/*.txt \
    && sed -i 's/setuptools==/setuptools>=/g' requirements/*.txt \
    && sed -i 's/virtualenv==/virtualenv>=/g' requirements/*.txt \
\
    && pip install -r requirements/pip.txt \
    && python manage.py migrate \
    && echo "from django.contrib.auth.models import User; User.objects.create_superuser('${USERNAME:-admin}', '${USERNAME:-admin}@localhost', '${PASSWORD:-admin}')" | python manage.py shell \
    && python manage.py collectstatic --noinput \
\
    && apt-get clean \
    && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /var/log/* /tmp/* ~/.[^.]*

WORKDIR /$APP

EXPOSE 80

CMD ["python", "./manage.py", "runserver", "0.0.0.0:80"]
