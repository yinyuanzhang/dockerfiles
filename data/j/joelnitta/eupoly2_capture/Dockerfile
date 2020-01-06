FROM rocker/tidyverse:3.5.2

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
# Dependencies for drake
  libudunits2-dev \
  libzmq3-dev \
# Dependecies for googledrive
  xdg-utils \
  links2 \
  elinks \
  links \
  lynx \
  w3m \
# Astral (also needs default-jre, which is already installed)
  default-jdk \
# Other dependencies
  bioperl \
  bwa \
  default-jre \
  exonerate \
  fasttree \
  libparallel-forkmanager-perl \
  mafft \
  muscle \
  ncbi-blast+ \
  parallel \
  python-pip \
  raxml \
  samtools \
  time \
  unzip \
  wget \
  wise \
  && apt-get clean && apt-get purge \
# Python libraries
  && pip install biopython

# Install CRAN packages with packrat
# (From R, run packrat::init() the first to set up packrat,
# and install_packages.R any time packages should be updated)
COPY packrat/packrat.lock packrat/

RUN Rscript -e 'packrat::restore()'

# Install github packages (packrat fails to download on restore,
# so install separately).

RUN Rscript -e 'devtools::install_github("joelnitta/jntools", lib = "/packrat/lib/x86_64-pc-linux-gnu/3.5.2")'

# .Rprofile doesn't get parsed by Rstudio, so modify Rprofile.site instead
# This is needed so R uses packrat libraries by default
RUN echo '.libPaths("/packrat/lib/x86_64-pc-linux-gnu/3.5.2")' >> /usr/local/lib/R/etc/Rprofile.site

# Install other software

ENV APPS_HOME=/apps
RUN mkdir $APPS_HOME
WORKDIR $APPS_HOME

# AlignWise
ENV APP_NAME=AlignWise
ENV DEST=$APPS_HOME/$APP_NAME
RUN git clone https://github.com/TeriForey/$APP_NAME.git \
  && printf '#!/bin/bash\n' > alignwise \
  && echo $DEST/AlignWise.pl' $*' >> alignwise \
  && chmod +x alignwise \
  && mv alignwise /bin

# Trimmomatic
ENV APP_NAME=Trimmomatic
ENV VERSION=0.38
ENV DEST=$APPS_HOME/$APP_NAME
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/$APP_NAME-$VERSION.zip \
  && unzip $APP_NAME-$VERSION.zip \
  && rm $APP_NAME-$VERSION.zip \
  && mkdir -p $DEST \
  && mv $APP_NAME-$VERSION $DEST/$VERSION \
  && printf '#!/bin/bash\njava -Xmx6g -jar ' > trimmomatic \
  && echo $APPS_HOME/$APP_NAME/$VERSION/trimmomatic-$VERSION.jar' $*' >> trimmomatic \
  && chmod +x trimmomatic \
  && mv trimmomatic /bin

# SPAdes
# This is also available as a package on Debian,
# but that version doesn't work for HybPiper.
ENV APP_NAME=SPAdes
ENV VERSION=3.13.0
ENV DEST=$APPS_HOME/$APP_NAME
RUN wget http://cab.spbu.ru/files/release$VERSION/$APP_NAME-$VERSION-Linux.tar.gz \
  && tar xf $APP_NAME-$VERSION-Linux.tar.gz \
  && rm $APP_NAME-$VERSION-Linux.tar.gz \
  && mkdir -p $DEST \
  && mv $APP_NAME-$VERSION-Linux $DEST/$VERSION
ENV PATH="$PATH:$DEST/$VERSION/bin/"

# HybPiper
# Use my fork until PR gets submitted and merged (or chmod won't work).
ENV APP_NAME=HybPiper
ENV DEST=$APPS_HOME/$APP_NAME
RUN git clone https://github.com/joelnitta/$APP_NAME.git \
  && chmod +x $DEST/*.py
ENV PATH="$PATH:$DEST/"

# Silence parallel citation warning
RUN mkdir /root/.parallel \
  && touch /root/.parallel/will-cite

# ASTRAL
ENV APP_NAME=ASTRAL
ENV VERSION=5.6.3
ENV DEST=$APPS_HOME/$APP_NAME

RUN git clone https://github.com/smirarab/$APP_NAME.git
WORKDIR $DEST
RUN bash make.sh
WORKDIR $APPS_HOME
RUN printf '#!/bin/bash\njava -Xmx6g -jar ' > astral \
	&& echo $APPS_HOME/$APP_NAME/astral.$VERSION.jar' $*' >> astral \
	&& chmod +x astral \
	&& mv astral /bin

# PartitionFinder
ENV APP_NAME=partitionfinder
ENV VERSION=2.1.1
ENV DEST=$APPS_HOME/$APP_NAME

RUN pip install numpy \
  pandas \
  tables \
  pyparsing \
  scipy \
  sklearn

RUN wget https://github.com/brettc/$APP_NAME/archive/v$VERSION.zip \
  && unzip v$VERSION.zip \
  && rm v$VERSION.zip \
  && mkdir -p $DEST \
  && mv $APP_NAME-$VERSION $DEST/$VERSION \
  && chmod +x $DEST/$VERSION/*.py
ENV PATH="$PATH:$DEST/$VERSION/"

WORKDIR /home/rstudio
