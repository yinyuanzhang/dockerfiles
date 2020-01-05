FROM amazonlinux:2 as corretto8-al2

RUN bash -c "yes | amazon-linux-extras install docker" \
 && yum -y update \
 && yum -y install wget curl zip unzip git make which tar \
 && wget https://d3pxv6yz143wms.cloudfront.net/java-1.8.0-amazon-corretto-1.8.0_192.b12-1.amzn2.x86_64.rpm \
 && wget https://d3pxv6yz143wms.cloudfront.net/java-1.8.0-amazon-corretto-devel-1.8.0_192.b12-1.amzn2.x86_64.rpm \
 && rpm -K java-1.8.0-amazon-corretto-1.8.0_192.b12-1.amzn2.x86_64.rpm \
 && rpm -K java-1.8.0-amazon-corretto-devel-1.8.0_192.b12-1.amzn2.x86_64.rpm \
 && yum -y localinstall *.rpm \
 && rm java-1.8.0-amazon-corretto-1.8.0_192.b12-1.amzn2.x86_64.rpm \
       java-1.8.0-amazon-corretto-devel-1.8.0_192.b12-1.amzn2.x86_64.rpm \
 && bash -c 'curl -s "https://get.sdkman.io" | bash'

FROM corretto8-al2

RUN bash -c 'source "$HOME/.sdkman/bin/sdkman-init.sh"; sdk install sbt 1.2.6' && \
    ln -s $HOME/.sdkman/candidates/sbt/current/bin/sbt /usr/local/bin/sbt && \
    curl -L https://git.io/n-install | bash -s -- -y && \
    ln -s /root/n/bin/n /usr/local/bin/n
