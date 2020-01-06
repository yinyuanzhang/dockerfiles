FROM redmine:4.0.5
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"

ENV REDMINE_PATH=/usr/src/redmine \
    REDMINE_LOCAL_PATH=/var/local/redmine

# Install dependencies and plugins
RUN apt-get update -q \
 && apt-get install -y --no-install-recommends unzip graphviz vim python3-pip cron rsyslog python3-setuptools \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir -p ${REDMINE_LOCAL_PATH}/github \
 && git clone -b v0.8.0 https://github.com/tckz/redmine-wiki_graphviz_plugin.git ${REDMINE_PATH}/plugins/wiki_graphviz_plugin \
# && git clone -b Ver_0.3.0 https://github.com/masamitsu-murase/redmine_add_subversion_links.git ${REDMINE_PATH}/plugins/redmine_add_subversion_links \
# && git clone https://github.com/eea/redmine_github_hook.git ${REDMINE_PATH}/plugins/redmine_github_hook \
 && git clone https://github.com/bluezio/redmine_wiki_backlinks.git ${REDMINE_PATH}/plugins/redmine_wiki_backlinks \
 && cd ${REDMINE_PATH}/plugins/redmine_wiki_backlinks \
 && git checkout 62488fa341d21c9b46b27cbb787ee61b46266d0e \
 && cd .. \
 && git clone -b 0.2.0 https://github.com/akiko-pusu/redmine_banner.git ${REDMINE_PATH}/plugins/redmine_banner \
 && git clone -b 2.0.21 https://github.com/alphanodes/additionals.git ${REDMINE_PATH}/plugins/additionals \
 && git clone -b v0.9.0 https://github.com/mikitex70/redmine_drawio.git ${REDMINE_PATH}/plugins/redmine_drawio \
 && git clone  https://github.com/eea/redmine_ldap_sync.git ${REDMINE_PATH}/plugins/redmine_ldap_sync \
 && git clone https://github.com/eea/eea.redmine.theme.git ${REDMINE_PATH}/public/themes/eea.redmine.theme \
 && git clone https://github.com/eea/taskman.redmine.theme.git ${REDMINE_PATH}/public/themes/taskman.redmine.theme \
 && chown -R redmine:redmine ${REDMINE_PATH} ${REDMINE_LOCAL_PATH} 

# Install gems
RUN echo 'gem "dalli", "~> 2.7.6"' >> ${REDMINE_PATH}/Gemfile \
 && echo 'gem "acts-as-taggable-on", "~> 5.0"' >> ${REDMINE_PATH}/Gemfile


# Install eea cron tools
COPY crons/ ${REDMINE_LOCAL_PATH}/crons
COPY config/install_plugins.sh ${REDMINE_PATH}/install_plugins.sh
COPY plugins.cfg ${REDMINE_PATH}/plugins.cfg

# patches for plugins, to be removed when fixed
#banner plugin fix
COPY patches/projects_helper_patch.rb ${REDMINE_PATH}/plugins/redmine_banner/lib/banners/projects_helper_patch.rb
#wiki linkis "key not found" error
#Remove when fixed - https://github.com/bluezio/redmine_wiki_backlinks/issues/10
COPY patches/wiki_links_controller.rb  ${REDMINE_PATH}/plugins/redmine_wiki_backlinks/app/controllers/wiki_links_controller.rb

#SystemStackError (stack level too deep) with additionals/lib/additionals/patches/formatting_helper_patch.rb
COPY patches/textile_helper.rb ${REDMINE_PATH}/plugins/redmine_drawio/lib/redmine_drawio/helpers/textile_helper.rb


COPY redmine_jobs /var/redmine_jobs.txt

RUN sed -i '/#cron./c\cron.*                          \/proc\/1\/fd\/1'  /etc/rsyslog.conf \
 && sed -i 's/-\/var\/log\/syslog/\/proc\/1\/fd\/1/g'  /etc/rsyslog.conf 

RUN echo "export REDMINE_PATH=$REDMINE_PATH\nexport BUNDLE_PATH=$BUNDLE_PATH\nexport BUNDLE_APP_CONFIG=$BUNDLE_PATH\nexport PATH=$BUNDLE_PATH/bin:$PATH"  > ${REDMINE_PATH}/.profile \
 && chown redmine:redmine ${REDMINE_PATH}/.profile \
 && usermod -d ${REDMINE_PATH} redmine

# Send Redmine logs on STDOUT/STDERR
COPY config/additional_environment.rb ${REDMINE_PATH}/config/additional_environment.rb

# Add email configuration
COPY config/configuration.yml ${REDMINE_PATH}/config/configuration.yml

COPY start_redmine.sh /start_redmine.sh
RUN chmod 0766 /start_redmine.sh


ENTRYPOINT ["/start_redmine.sh"]

CMD []
