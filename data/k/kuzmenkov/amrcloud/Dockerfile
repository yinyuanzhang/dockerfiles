FROM kuzmenkov/amrcloudbasic:mro_minicran
RUN sudo R -e "install.packages('stringi', repos='https://cran.amrcloud.net/')" \
&& R CMD javareconf \
&& R -e "install.packages(c('rJava', 'mailR', 'fst', 'shinytoastr', 'readxl', 'readr', 'shinyBS', 'future', 'uuid', 'fs', 'lubridate', 'curl', 'shinyWidgets', 'stringr', 'tools', 'rjson', 'htmlwidgets', 'utils', 'DT', 'promises', 'raster', 'sp', 'viridis', 'leaflet', 'leaflet.extras', 'ggrepel', 'leaflet.minicharts', 'rhandsontable', 'ipc', 'shinyAce', 'RSQLite', 'glue', 'highcharter', 'shinycssloaders', 'fmsb', 'visNetwork', 'igraph', 'formattable', 'mapview', 'timevis', 'shinyparticles', 'officer', 'flextable', 'qrencoder', 'rgdal', 'anytime', 'configr', 'Ruchardet', 'GetoptLong', 'qs', 'leafsync', 'GAlogger', 'waiter', 'shinybusy'), repos='https://cran.amrcloud.net/')"

VOLUME /home/dockerapp/data
VOLUME /home/dockerapp/app
VOLUME /home/dockerapp/cashe
VOLUME /home/dockerapp/deleted
EXPOSE 3838
USER dockerapp

CMD ["R", "-e shiny::runApp('/home/dockerapp/app',port=3838,host='0.0.0.0')"]
