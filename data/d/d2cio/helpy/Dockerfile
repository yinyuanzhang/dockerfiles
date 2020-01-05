FROM helpy/helpy

COPY run.sh $HELPY_HOME/docker/run.sh
COPY database.yml $HELPY_HOME/config/database.yml
COPY seeds.rb $HELPY_HOME/db/seeds.rb
USER root
RUN chown -R $HELPY_USER:$HELPY_USER $HELPY_HOME
USER $HELPY_USER
