FROM alpine:3.7

RUN apk add --no-cache bash \
  curl \
  zsh \
  py-pip \
  python \
  git

# install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

RUN mkdir -p /home/h/repos
RUN mkdir -p /home/h/bin
ENV PATH="/home/h/bin:${PATH}"

# @TODO:
# INSTALL HASHCAT

# sqlmap - https://github.com/sqlmapproject/sqlmap.git
RUN git clone https://github.com/sqlmapproject/sqlmap.git /home/h/repos/sqlmap
RUN chmod +x /home/h/repos/sqlmap/sqlmap.py
RUN ln -s /home/h/repos/sqlmap/sqlmap.py /home/h/bin/sqlmap

# sublist3r - https://github.com/aboul3la/Sublist3r.git
RUN git clone https://github.com/aboul3la/Sublist3r.git /home/h/repos/sublist3r
RUN cd /home/h/repos/sublist3r && pip install -r requirements.txt
RUN chmod +x /home/h/repos/sublist3r/sublist3r.py
RUN ln -s /home/h/repos/sublist3r/sublist3r.py /home/h/bin/sublister

# truffleHog - https://github.com/dxa4481/truffleHog.git
RUN pip install truffleHog
