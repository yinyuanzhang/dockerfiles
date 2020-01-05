FROM jacobalberty/firebird:2.5.8-sc

ENV DEBIAN_FRONTEND=noninteractive
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list && \
    sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-psycopg2 locales locales-all build-essential libssl-dev libffi-dev python3-dev && \
    apt-get clean && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8 && \
    pip3 install psycopg2 fdb typing

ENV LANG en_US.UTF-8
ENV LC_ALL C.UTF-8
