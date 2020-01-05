From jrowen/dcaret

RUN apt-get update
RUN apt-get install -y python git curl

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -qq update
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN apt-get install -y nodejs npm
RUN npm install -g npm

RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('MICE')"
RUN Rscript -e "install.packages('yhatr')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('PARTY')"
RUN Rscript -e "install.packages('svm')"
RUN Rscript -e "install.packages('reshape2')"
RUN Rscript -e "install.packages('stringr')"
RUN Rscript -e "install.packages('lubridate')"
RUN Rscript -e "install.packages('cleaner')"
RUN Rscript -e "install.packages('rjson')"
RUN Rscript -e "install.packages('Metrics')"
RUN Rscript -e "install.packages('encryptr')"

WORKDIR /

RUN mkdir app
RUN mkdir /iexec
COPY ./app /app
WORKDIR /app
RUN npm install
RUN chmod +x entrypoint.sh

ARG PINATA_API_KEY=PINATA_API_KEY
ARG PINATA_SECRET_API_KEY=PINATA_SECRET_API_KEY

ENV PINATA_API_KEY=${PINATA_API_KEY}
ENV PINATA_SECRET_API_KEY=${PINATA_SECRET_API_KEY}

RUN chmod +x genkeys.R
RUN ./genkeys.R
RUN cat id_rsa.pub

ENTRYPOINT ["./entrypoint.sh"]