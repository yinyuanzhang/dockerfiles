FROM prima/elixir-official:1.9.1-1

COPY files/apt/99defaultrelease /etc/apt/apt.conf.d/99defaultrelease
COPY files/apt/stable.list /etc/apt/sources.list.d/stable.list
COPY files/apt/testing.list /etc/apt/sources.list.d/testing.list

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.6" > "/etc/apt/sources.list.d/postgresql.list" && \
    curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install -qqy postgresql-client-9.6 libreoffice software-properties-common && \
    add-apt-repository ppa:ubuntuhandbook1/apps -y && \
    apt-get install -qqy mupdf mupdf-tools && \
    add-apt-repository -r ppa:ubuntuhandbook1/apps -y && \
    apt-get -t testing install -qqy ghostscript imagemagick && \
    rm -rf /var/lib/apt/lists/*

# temporary downgrade to pdftk 2.02
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -s -- && \
    apt-get update && \
    apt-get install -y wget

RUN wget http://launchpadlibrarian.net/340410966/libgcj17_6.4.0-8ubuntu1_amd64.deb \
    http://launchpadlibrarian.net/337429932/libgcj-common_6.4-3ubuntu1_all.deb \
    https://launchpad.net/ubuntu/+source/pdftk/2.02-4build1/+build/10581759/+files/pdftk_2.02-4build1_amd64.deb \
    https://launchpad.net/ubuntu/+source/pdftk/2.02-4build1/+build/10581759/+files/pdftk-dbg_2.02-4build1_amd64.deb && \
    echo -e "Packages for pdftk downloaded\n\n" && \
    # install packages
    echo -e "\n\n Installing pdftk: \n\n" && \
    apt-get install -y ./libgcj17_6.4.0-8ubuntu1_amd64.deb \
    ./libgcj-common_6.4-3ubuntu1_all.deb \
    ./pdftk_2.02-4build1_amd64.deb \
    ./pdftk-dbg_2.02-4build1_amd64.deb && \
    echo -e "\n\n pdftk installed\n" && \
    echo -e "   try it in shell with: > pdftk \n" &&\
    # delete deb files in /tmp directory
    rm ./libgcj17_6.4.0-8ubuntu1_amd64.deb &&\
    rm ./libgcj-common_6.4-3ubuntu1_all.deb &&\
    rm ./pdftk_2.02-4build1_amd64.deb &&\
    rm ./pdftk-dbg_2.02-4build1_amd64.deb

COPY files/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
