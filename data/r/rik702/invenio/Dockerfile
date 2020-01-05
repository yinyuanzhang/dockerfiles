FROM rik702/invenio:ivo-r-base

MAINTAINER Richard Roe "rik702@btinternet.com"

# Set the working directory to
WORKDIR /usr/local/src

# Copy the current directory contents into the container at /app
# The files to copy over are
# IVORDataWatchAPI_??.tgz - the latest version of built binary of R Package DataWatch API, consisting of the Ref Class IVORDataWatchAPI
# IVORIntermittent_??.tgz - the latest version of built binary of R Package for the Intermittent Calculation, consisting of Ref Class IVORIntermittent
# ivointermittentman.R - script that uses the above Ref Classes to do Intermittenet Calculations from the DataWatch DB
# ivointermittentman.sh - bash script to repeat the above calculation for as long as data requires Intermittent Analysis performed ("pending" state Logger Data Uploads in IvoLoggerDataUploadPort).
# this script will also provide the security required... 
ADD . /usr/local/src

RUN echo 'install.packages(c("IVORDataWatchAPI_0.0.0.9000.tgz"), repos=NULL, dependencies=TRUE, verbose=TRUE)' > /tmp/packages.R
RUN echo 'install.packages(c("IVORIntermittent_0.0.0.9000.tgz"), repos=NULL, dependencies=TRUE, verbose=TRUE)' >> /tmp/packages.R
RUN Rscript /tmp/packages.R

RUN chmod 755 ./ivointermittentman.sh

