# port number 3838
# script runs from /srv/shiny-server/
# logs stored at /var/log/shiny-server/
FROM ausvet/shinypy

ENV APPLICATION_LOGS_TO_STDOUT true
ENV LOCAL_DATA_PATH "/srv/data"
ENV R_DATA_FOLDER "/RData"
# TODO: [FD-56] update default remote path to a production setting.
ENV default_remote_path "/Shared/Divisions/AnimalHealth/FVG/Global/Fishvet_Dashboard/Scotland/dashboard_files"
ENV default_domain "bmk.egnyte.com"

# move install packages higher so it can be cached.
COPY ./src/installpackages.r /srv/installpackages.r
RUN Rscript /srv/installpackages.r

# install nginx
RUN apt-get install -y nginx
COPY ./proxy.nginx /etc/nginx/sites-available/default
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# setup pipenv
COPY ./Pipfile /srv/Pipfile
COPY ./Pipfile.lock /srv/Pipfile.lock
WORKDIR /srv
RUN pipenv install
COPY ./sync /srv/sync

## copy data
RUN mkdir $LOCAL_DATA_PATH
RUN chmod -R 777 $LOCAL_DATA_PATH
VOLUME $LOCAL_DATA_PATH

# copy scripts
RUN rm -R /srv/shiny-server/*
COPY src/. /srv/shiny-server/
RUN chown -R shiny:shiny /srv/shiny-server

# expose network ports
#EXPOSE 3838
EXPOSE 80

COPY ./docker_entrypoint.sh /srv/docker_entrypoint.sh
RUN chmod +x /srv/docker_entrypoint.sh
#ENTRYPOINT ["service", "nginx", "restart;"]
ENTRYPOINT ["/srv/docker_entrypoint.sh"]

# run server
CMD ["/usr/bin/shiny-server.sh"]
