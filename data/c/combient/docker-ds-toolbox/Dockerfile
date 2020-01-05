#Start from the base image Ubuntu 18.04
FROM ubuntu:18.04

#R install script specific to 18.04 Bionic --- Change that if changing the base image!
COPY install_R_ubuntu1804.sh /install_R.sh

#Define a few environement variables
ENV PORT 8888
ENV SCALA_VERSION 2.11.11
ENV SPARKVERSION spark-2.2.0-bin-hadoop2.7

# the following (especially the first) are needed to deal with .deb package
# tzdata, which otherwise would ask for input from the terminal
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="/usr/share/zoneinfo/Europe/Stockholm"
RUN echo $TZ > /etc/timezone

### Install .deb packages 
# apt_packages.list must contain one package per line with an optional comment. The package name *** must be followed by a TAB *** before the comment
COPY apt_packages.list /

RUN apt-get update 1>/dev/null && apt-get install -y `cat /apt_packages.list | awk -F'\t'  '($1!~/^#/) && ($1!~/^$/) {print $1}' ` 1> /dev/null && apt-get clean && rm -rf /var/lib/apt/lists/*

#Install Scala
RUN curl -sO http://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb && dpkg -i scala-${SCALA_VERSION}.deb && rm -rf scala-${SCALA_VERSION}.deb

#Install Spark 
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/$SPARKVERSION.tgz | tar -xzf -

#Install Python and Jupyter
### Note: We install both Python 2 and 3. Jupyter is installed under Python 3 and offers a Python 2 kernel
RUN python2 -m pip install --upgrade pip setuptools packaging
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install --upgrade pyzmq
RUN python3 -m pip install jupyterlab 

#Install the Python2 and Python3 kernels
RUN python2 -m pip install ipykernel && python3 -m pip install ipykernel && python3 -m ipykernel install && python2 -m ipykernel install 

###To be fixed later: try to get the Toree kernel to support Scala
#RUN pip install -i https://pypi.anaconda.org/hyoon/simple toree && jupyter toree install --spark_home=/$SPARKVERSION/ --spark_opts='--master=local[4]' --interpreters=Scala,PySpark,SparkR,SQL 

#Install extra python packages defined in the list
# python_packages.list describes one package per line with a structure "name_pkg-TAB-[Python2/Python3/*empty]-TAB-#Comment"
# An empty second columns means the package is installed in both Python2 and Python3. 
# Python2 in the second column means that the package should be installed in python2 only. 
# Python2 in the second column means that the package should be installed in python2 only. 
COPY python_packages.list /
RUN python3 -m pip install --upgrade `cat /python_packages.list | awk -F'\t'  '($1!~/^#/) && ($1!~/^$/) && (($2=="") || ($2=="Python3")) {print $1}' `
RUN python2 -m pip install --upgrade `cat /python_packages.list | awk -F'\t'  '($1!~/^#/) && ($1!~/^$/) && (($2=="") || ($2=="Python2")) {print $1}' `



### Install the latest version of R available for the distribution from the Rstudio repo
RUN bash ./install_R.sh


#Install R packages 
COPY R_packages.list /R_packages.list

#### Do better than this at some point!!!! 
RUN echo `cat /R_packages.list | awk -F'\t'  'BEGIN {print "R -e install.packages(c(" } ($1!~/^#/) && ($1!~/^$/) {print "\47" $1 "\47,"} END {print "),repos=\47http://cran.r-project.org\47)" }' ` | sed 's/, )/)/;s/R -e /R -e "/;s/)$/)"/' | bash


# Finally, run any bash script that is placed in the post_install_scripts folder. 
# Note that the order of execution of the script is non necessarily deterministic (but, as far as I know, the scripts are not executed in parallel)
COPY post_install_scripts /post_install_scripts
RUN chmod 755 /post_install_scripts/* && sync && sleep 1 && /bin/run-parts /post_install_scripts/
 
 
#Jupyter will be run chrooted into that folder - mount whatever the user needs into that folder
RUN mkdir /data && mkdir /Templates_from_ds_toolbox

#Fix some folders and permissions so that the container can be run as non-root
RUN mkdir /.jupyter && mkdir /.local && chmod 777 /.jupyter && chmod 777 /.local

#Get the Templates inside the Docker image
COPY Templates/* /Templates_from_ds_toolbox/


#The command to run it all
#TO DO: set the right variables to get SparkR working
ENV SPARK_HOME /$SPARKVERSION/
ENV PYSPARK_SUBMIT_ARGS "--master local[6]  pyspark-shell"

CMD cd /data && cp -R /Templates_from_ds_toolbox /data/ && /usr/local/bin/jupyter lab --port=$PORT --ip=0.0.0.0 --no-browser --allow-root 
