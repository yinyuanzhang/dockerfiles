FROM codercom/code-server

ENV PATH /usr/local/bin:$PATH

# Install ZSH
RUN set -eux; \
	sudo apt-get update; \
	sudo apt-get install -y zsh; \
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" "" --unattended \
	sudo rm -rf /var/lib/apt/lists/*

# Install GO
ENV GOLANG_VERSION 1.12.7
ENV GOPATH /go
RUN set -eux; \
	dpkgArch="$(dpkg --print-architecture)"; \
	case "${dpkgArch##*-}" in \
		amd64) goRelArch='linux-amd64'; goRelSha256='66d83bfb5a9ede000e33c6579a91a29e6b101829ad41fffb5c5bb6c900e109d9' ;; \
		armhf) goRelArch='linux-armv6l'; goRelSha256='48edbe936e9eb74f259bfc4b621fafca4d4ec43156b4ee7bd0d979f257dcd60a' ;; \
		arm64) goRelArch='linux-arm64'; goRelSha256='4da1f7198a8fa0c4067852656b6c10153a4eca5a26aca28ef02ae9f4a7939ba5' ;; \
		i386) goRelArch='linux-386'; goRelSha256='ae2424b7ff557a708be12d3141f25b645966489ca49af1ad10b4fbe4c97d4c41' ;; \
		ppc64el) goRelArch='linux-ppc64le'; goRelSha256='8eda20600d90247efbfa70d116d80056e11192d62592240975b2a8c53caa5bf3' ;; \
		s390x) goRelArch='linux-s390x'; goRelSha256='3374ac3d646555e50be790091b51849319cfcb176904048458c7f4252337fce8' ;; \
		*) goRelArch='src'; goRelSha256='95e8447d6f04b8d6a62de1726defbb20ab203208ee167ed15f83d7978ce43b13'; \
			echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a corresponding Go binary release; will be building from source"; echo >&2 ;; \
	esac; \
	\
	url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
	wget -O go.tgz "$url"; \
	echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
	sudo tar -C /usr/local -xzf go.tgz; \
	rm go.tgz; \
	export PATH="/usr/local/go/bin:$PATH"; \
	go version;

# Install Python
RUN set -eux; \
	sudo apt-get update; \
	sudo apt-get install -y python3 python3-pip; \
	sudo rm -rf /var/lib/apt/lists/*

# Install Conda
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         ca-certificates \
         libjpeg-dev \
         libpng-dev && \
     sudo rm -rf /var/lib/apt/lists/* && \
    curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x ~/miniconda.sh && \
    sudo ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh && \
    sudo /opt/conda/bin/conda install -y python=3.7 numpy pyyaml scipy ipython mkl mkl-include ninja cython typing && \
    sudo /opt/conda/bin/conda install -y python=3.7 -c pytorch && \
    sudo /opt/conda/bin/conda clean -ya

COPY settings.json /home/coder/.local/share/code-server/User/settings.json
RUN sudo chown -R coder.coder /home/coder/

ENV PATH $GOPATH/bin:/usr/local/go/bin:/opt/conda/bin:$PATH
