FROM ubuntu:latest

RUN apt-get update \
        && apt-get install software-properties-common -y \
        && add-apt-repository ppa:neovim-ppa/unstable \
        && apt-get update \
        && apt-get install -y git neovim ctags python-pip

# maybe additions
RUN pip install flake8 \
    && pip install autopep8



RUN mkdir /nvim-home/.local -p -m 0777

ENV HOME=/nvim-home

RUN git clone https://git@github.com/ibejohn818/neovim.git /nvim-home/vim # Last update 2017/09/10 1:30

RUN /bin/bash -c "cd /nvim-home/vim && ./local-setup.sh"

ENTRYPOINT ["nvim"]
