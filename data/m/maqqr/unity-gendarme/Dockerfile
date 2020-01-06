FROM gableroux/unity3d:2019.1.4f1

# Install misc tools
RUN apt update -y
RUN apt install -y zip curl

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt update -y
RUN apt install -y git-lfs
RUN git lfs install

# Add mono to apt repositories
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
#RUN apt install -y apt-transport-https ca-certificates
#RUN echo "deb https://download.mono-project.com/repo/ubuntu stable-xenial main" | tee /etc/apt/sources.list.d/mono-official-stable.list
#RUN apt update -y

#RUN apt install -y gendarme
