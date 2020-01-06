FROM hiono/texlive

MAINTAINER ABCanG <abcang1015@gmail.com>

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository -y ppa:webupd8team/java

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections

RUN apt-get update && \
    apt-get -y install curl git make ruby wget oracle-java8-installer oracle-java8-set-default && \
    apt-get -y upgrade

RUN version=$(curl -sI https://github.com/redpen-cc/redpen/releases/latest | awk -F'/' '/^Location:/{print $NF}' | tr -d '\r\n') && \
    curl -SL https://github.com/redpen-cc/redpen/releases/download/$version/$version.tar.gz | tar xz && \
    ln -s $PWD/$(ls redpen-distribution-*/bin/redpen) /usr/local/bin/redpen

CMD ["/bin/bash"]
