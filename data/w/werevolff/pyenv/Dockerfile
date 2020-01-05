FROM debian:bullseye-20190708

ENV DEBIAN_FRONTEND noninteractive

# Default variables
ARG PYENV_DEFAULT_LOCALE='ru_RU.UTF-8'
ENV PYENV_DEFAULT_LOCALE=$PYENV_DEFAULT_LOCALE
ARG PYENV_GENERATED_LOCALES='en_US.UTF-8 UTF-8, ru_RU.UTF-8 UTF-8'
ENV PYENV_GENERATED_LOCALES=$PYENV_GENERATED_LOCALES
ARG PYENV_LANGUAGE='ru_RU:ru'
ENV PYENV_LANGUAGE=$PYENV_LANGUAGE
ARG PYENV_INSTALL_PACKAGES='build-essential git libssl1.1 libssl-dev libreadline-dev libsqlite3-dev libpq-dev libjpeg-dev zlib1g-dev libpng-dev libjpeg-dev bzip2 libbz2-dev curl'
ENV PYENV_INSTALL_PACKAGES=$PYENV_INSTALL_PACKAGES
ARG PYENV_BUILD_DEP_PACKAGES='python3 python3-ndg-httpsclient python3-dev python3-pip'
ENV PYENV_BUILD_DEP_PACKAGES=$PYENV_INSTALL_PACKAGES
ENV PYENV_DOWNLOAD_URL='https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer'
ARG PYENV_INSTALL_DIR='/opt/pyenv'
ENV PYENV_INSTALL_DIR=$PYENV_INSTALL_DIR
ARG PYENV_ROOT='/var/pyenv_root'
ENV PYENV_ROOT=$PYENV_ROOT
ARG PYENV_VERSION='3.6.4'
ENV PYENV_VERSION=$PYENV_VERSION
ENV PATH $PATH:$PYENV_ROOT/bin
ENV PATH $PATH:$PYENV_ROOT/versions/$PYENV_VERSION/bin

# Set up locales
COPY sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y locales locales-all
RUN echo 'locales locales/default_environment_locale select $(PYENV_DEFAULT_LOCALE)' | debconf-set-selections
RUN echo 'locales locales/locales_to_be_generated multiselect $(PYENV_GENERATED_LOCALES)' | debconf-set-selections
RUN locale-gen --purge $PYENV_DEFAULT_LOCALE
RUN update-locale 'LC_ALL=$(PYENV_DEFAULT_LOCALE)'
RUN sed -i -e 's/# $(PYENV_GENERATED_LOCALES)/$(PYENV_GENERATED_LOCALES)/' /etc/locale.gen && locale-gen
ENV LANG $PYENV_DEFAULT_LOCALE
ENV LANGUAGE $PYENV_LANGUAGE
ENV LC_ALL $PYENV_DEFAULT_LOCALE

# Set up python packages
RUN apt-get install -y $PYENV_INSTALL_PACKAGES
RUN apt-get build-dep -y $PYENV_BUILD_DEP_PACKAGES

# Remove Directories
RUN if [ -d '$PYENV_INSTALL_DIR' ]; then rm -Rf $PYENV_INSTALL_DIR; fi
RUN if [ -d '$PYENV_ROOT' ]; then rm -Rf $PYENV_ROOT; fi
RUN mkdir -p $PYENV_INSTALL_DIR

# Download and install pyenv
RUN cd $PYENV_INSTALL_DIR && curl -L $PYENV_DOWNLOAD_URL | bash
RUN $PYENV_ROOT/bin/pyenv install $PYENV_VERSION
RUN $PYENV_ROOT/bin/pyenv global $PYENV_VERSION

# Update pip
RUN pip install --upgrade pip

ENV DEBIAN_FRONTEND teletype
