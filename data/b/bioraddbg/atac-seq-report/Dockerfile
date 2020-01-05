FROM ubuntu:18.10

MAINTAINER Bio-Rad Support <support@bio-rad.com>

# Requires Python 3 dev environment
RUN apt-get update && \
	apt-get install -y tzdata && \
    apt-get install -y python3 && \
    apt-get install -y python3-dev && \
    apt-get install -y libcurl4-openssl-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y python3-venv && \
    apt-get install -y r-base && \
    apt-get install -y pandoc && \
    apt-get install -y libxml2-dev && \
    apt-get install -y wget && \
    apt-get install -y fonts-freefont-ttf

RUN Rscript -e 'install.packages(c("dplyr", "knitr", "rmarkdown", "kableExtra", "data.table", "ggplot2", "plotly", "fastqcr", "rlist", "tinytex", "webshot"), repos = "http://cran.r-project.org")'

RUN Rscript -e 'tinytex::install_tinytex()'
RUN Rscript -e 'webshot::install_phantomjs()'

RUN python3 -m venv /multiqc_venv
RUN /multiqc_venv/bin/pip install multiqc

RUN Rscript -e 'tinytex::tlmgr_install(pkgs = c("xcolor", "colortbl", "multirow", "wrapfig", "float", "tabu", "varwidth", "threeparttable", "threeparttablex", "environ", "trimspaces", "ulem", "makecell"))'

RUN apt-get install -y texlive-xetex build-essential chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev

RUN wget https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/share
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin

COPY src/generate_report.sh /generate_report.sh
COPY src/quickQcReport.R /quickQcReport.R
COPY src/atacReport.R /atacReport.R
COPY src/generateRmdReport.R /generateRmdReport.R
COPY src/pdfReport.R /pdfReport.R
COPY src/vendor-logo.png /vendor-logo.png

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/generate_report.sh"]
