FROM ruby:2.2

ENV HELPY_VERSION=1.2.1 \
    RAILS_ENV=production \
    HELPY_HOME=/user/helpy \
    HELPY_USER=helpyuser \
    HELPY_SLACK_INTEGRATION_ENABLED=true

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y nodejs postgresql-client imagemagick --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN useradd --home /user/$HELPY_USER -m -U -s /bin/bash web
#allow some limited sudo commands for user `web`
RUN echo 'Defaults !requiretty' >> /etc/sudoers; \
    echo 'web ALL= NOPASSWD: /usr/sbin/dpkg-reconfigure -f noninteractive tzdata, /usr/bin/tee /etc/timezone, /bin/chown -R $HELPY_USER\:$HELPY_USER /var/www, /bin/chown -R $HELPY_USER\:$HELPY_USER /home/$HELPY_USER' >> /etc/sudoers;
RUN chown -R $HELPY_USER:$HELPY_USER $HELPY_HOME /usr/local/lib/ruby /usr/local/bundle

WORKDIR $HELPY_HOME

USER $HELPY_USER

RUN git clone --branch $HELPY_VERSION --depth=1 https://github.com/helpyio/helpy.git .

# modify Gemfile to remove the line which says 'ruby "2.2.1"' to use a newer ruby version
RUN sed -i '/ruby "2.2.1"/d' $HELPY_HOME/Gemfile

# add the slack integration gem to the Gemfile if the HELPY_SLACK_INTEGRATION_ENABLED is true
# use `test` for sh compatibility, also use only one `=`. also for sh compatibility
RUN test "$HELPY_SLACK_INTEGRATION_ENABLED" = "true" && sed -i '$ a\gem "helpy_slack", git: "https://github.com/helpyio/helpy_slack.git", branch: "master"' $HELPY_HOME/Gemfile

RUN echo 'gem "breadcrumbs_on_rails"' >> $HELPY_HOME/Gemfile

RUN bundle install

RUN touch /helpy/log/production.log && chmod 0664 /helpy/log/production.log

# Due to a weird issue with one of the gems, execute this permissions change:
RUN chmod +r /usr/local/bundle/gems/griddler-mandrill-1.1.3/lib/griddler/mandrill/adapter.rb

# manually create the /helpy/public/assets folder and give the helpy user rights to it
# this ensures that helpy can write precompiled assets to it
RUN mkdir -p $HELPY_HOME/public/assets && chown $HELPY_USER $HELPY_HOME/public/assets

COPY database.yml $HELPY_HOME/config/database.yml
COPY run.sh $HELPY_HOME/run.sh

CMD ["./run.sh"]
