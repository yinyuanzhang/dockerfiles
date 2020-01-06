FROM reyad010/gem5:base

# Source & dependancies update
RUN apt-get update
RUN apt-get -y upgrade
WORKDIR /usr/local/src/gem5
RUN git config --global user.name "GitHub Bot"
RUN git config --global user.email "bot@github.com"
RUN git remote add upstream https://gem5.googlesource.com/public/gem5
RUN git fetch --all --prune
RUN git reset --hard origin/master
RUN git pull --rebase upstream master

# build it
RUN scons build/X86/gem5.opt -j$(( $(nproc) + 1 ))
CMD ["zsh"]
