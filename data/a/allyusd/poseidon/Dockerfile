FROM allyusd/python3-cpp

ARG user=ci
ARG group=ci
ARG uid=1738552204
ARG gid=1738539521

ENV HOME /home/${user}
RUN groupadd -g ${gid} ${group}
RUN useradd -l -c "ci user" -d $HOME -u ${uid} -g ${gid} -m ${user}

RUN pip install conan
RUN apt-get update && apt-get install curl subversion git -y

# 32-bit compiler toolchain
RUN apt-get update && apt-get install libc6-i386 gcc-multilib g++-multilib libc6-dev-i386 libzip-dev lib32ncurses5 lib32z1 libasound2-plugins lib32gcc1 lib32ncurses5 lib32stdc++6 lib32z1 libc6 libcanberra-gtk-module -y

# for mosquitto
RUN apt-get update && apt-get install xsltproc docbook-xsl -y
