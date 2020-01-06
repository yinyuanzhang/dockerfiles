FROM iganbold/seleniumgrid:v2
MAINTAINER ITGEL GANBOLD
ENV DIRPATH /home/selenium
WORKDIR $DIRPATH
RUN pwd
RUN apt-get update
RUN apt-get upgrade -y

# Selenium Grid hub
EXPOSE 4444

# Selenium Grid Extra
EXPOSE 3000

# Selenium Grid node
EXPOSE 5555

ENTRYPOINT ["./start_grid_extras.sh"]
