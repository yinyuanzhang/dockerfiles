FROM ubuntu:latest
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

ARG API_USER
ARG API_PASS

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       ca-certificates \
       git \
       libpq-dev \
       nodejs

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
    && curl -sSL https://get.rvm.io | bash -s stable --ruby

RUN useradd -m -s /bin/bash -g rvm runner 

USER runner

WORKDIR /home/runner

RUN echo 'source /etc/profile.d/rvm.sh' >> ~/.bashrc

RUN /bin/bash -l -c "rvm install 2.1.8"

RUN /bin/bash -l -c "rvm use 2.1.8 && gem install bundler"

RUN git clone https://github.com/git/git-scm.com 

RUN /bin/bash -l -c "cd git-scm.com \
                     && rvm use 2.1.8 \
                     && bundle install"

ENV GIT_REPO .git

RUN cp git-scm.com/config/database.yml.example git-scm.com/config/database.yml \
    && /bin/bash -l -c "cd git-scm.com \
                        && rvm use 2.1.8 \
                        && rake db:migrate \
                        && rake local_index"

RUN /bin/bash -l -c "cd git-scm.com \
                     && rvm use 2.1.8 \
                     && rake remote_genbook"
    
EXPOSE 8080

CMD /bin/bash -l -c "cd git-scm.com \
                     && rails server -b 0.0.0.0 -p 8080"
