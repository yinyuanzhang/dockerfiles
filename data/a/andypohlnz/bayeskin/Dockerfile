# Start with base r docker image
FROM r-base 

# update linux and install required MYSQL packages
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y libmysqlclient-dev libcurl4-openssl-dev libssl-dev 

# install jags
RUN apt-get install jags -y

# install R packages
RUN echo "install.packages(c('rjags', 'coda', 'DBI', 'RMariaDB', 'circular'), repos='http://cran.us.r-project.org', dependencies=TRUE)" > /tmp/packages.R \
	&& Rscript /tmp/packages.R

# Make a user with approiate permissions
RUN useradd --create-home --home-dir /home/user user && chown -R user:user $HOME  

WORKDIR /home/user/src
USER user

#Add the Code Directory.
CMD mkdir /home/user/src

COPY src/* /home/user/src/ 

# set the command
CMD ["Rscript","--no-save","/home/user/src/runner.r"]


