from ubuntu:latest 

env JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre
env GOROOT /usr/local/go
env GOPATH /root/git/go

run mkdir -p /tmp && \
    apt-get update && \
    apt-get install -y curl software-properties-common apt-transport-https && \
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    add-apt-repository ppa:openjdk-r/ppa && \
    add-apt-repository ppa:neovim-ppa/unstable && \
    apt-get update && \
    export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && \
    echo "tzdata tzdata/Areas select Europe" > /tmp/tzdata.txt && \
    echo "tzdata tzdata/Zones/Europe select London" >> /tmp/tzdata.txt && \
    debconf-set-selections /tmp/tzdata.txt && \
    curl -sL https://deb.nodesource.com/setup_11.x | bash - && \
    apt-get install -y wget jq build-essential dirmngr openjdk-8-jdk maven iputils-ping net-tools nodejs python python-dev python-pip neovim php php-cli git gawk autoconf automake bison libffi-dev libgdbm-dev libncurses5-dev libsqlite3-dev libtool libyaml-dev pkg-config sqlite3 zlib1g-dev libgmp-dev libreadline-dev libssl-dev netcat nmap vim tcpdump dnsutils groff zip unzip bsdtar && \
    touch /root/.bash_aliases && \
    chmod a+rwx /root/.bash_aliases && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)" && \
    echo ". /root/.bash_alises" >> .bash_profile && \
    echo "alias ll='ls -gAlFh'" >> /root/.bash_aliases.sh && \
    echo "alias tf='terraform'" >> /root/.bash_aliases.sh && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /bin && \
    npm install -g n && \
    n latest && \
    curl -fsSL get.docker.com | bash && \
    curl -sSL https://dl.google.com/go/go1.11.5.linux-amd64.tar.gz -o go.tar.gz && \
    tar -C /usr/local -xzf go.tar.gz && \
    rm -f go.tar.gz && \
    mkdir -p /root/go && \
    cd /tmp && \
    wget -O tf.zip https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip && \
    unzip tf.zip && \
    mv terraform /usr/local/bin/ && \
    chmod a+rx /usr/local/bin/terraform && \
    rm -rf /tmp/tf.zip && \
    cd /tmp && \
    wget -O packer.zip https://releases.hashicorp.com/packer/0.12.0/packer_0.12.0_linux_amd64.zip && \
    unzip packer.zip && \
    mv packer /usr/local/bin && \
    rm -rf /tmp/packer* && \
    chmod a+rx /usr/local/bin/packer && \
    wget -LqO- "https://github.com/joeabbey/diver/releases/download/0.4/diver-linux-0.4.zip" | bsdtar -xzf- && \
    cp diver /usr/local/bin && \
    chmod a+rx /usr/local/bin/diver && \
    pip install --upgrade --no-cache-dir --ignore-installed six awscli ansible boto && \
    curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get | bash && \
    mkdir -p ~/.jx/bin && \
    curl -L https://github.com/jenkins-x/jx/releases/download/v2.0.137/jx-linux-amd64.tar.gz | tar xzv -C ~/.jx/bin && \
    export PATH=$PATH:~/.jx/bin && \
    echo 'export PATH=$PATH:~/.jx/bin' >> ~/.bashrc && \
    rm -rf /root/.cache/* && \
    rm -rf /tmp/* && \
    apt autoclean && \
    apt-get clean && \
    apt autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    touch /root/.vimrc && \
    echo "nnoremap <F5> :let _s=@/<Bar>:%s/\s\+$//e<Bar>:let @/=_s<Bar><CR>" >> /root/.vimrc && \
    echo "highlight ws ctermbg=red guibg=red" >> /root/.vimrc && \
    echo "match ws /\s\+$/" >> /root/.vimrc && \
    echo "autocmd BufWinEnter *.log,*.service,*.sh,*.yaml,*.yml,*.json,*.java match ws / \+$/" >> /root/.vimrc && \
    echo "Complete"

