FROM archlinux/base
LABEL maintainer="bofhbug"
LABEL Description="This image is used to use the poppler on archlinux" Version="0.75.0"
#TAG latest
#TAG 0.75.0
#ADD https://raw.githubusercontent.com/finalduty/configs/master/.vimrc /root/
#ADD https://raw.githubusercontent.com/finalduty/configs/master/.bashrc /root/
#RUN pacman -Sy --noconfirm bash-completion vim lsof tcpdump poppler; pacman -Scc --noconfirm &>/dev/null
RUN pacman -Sy --noconfirm bash-completion poppler poppler-data; pacman -Scc --noconfirm &>/dev/null
#ENTRYPOINT ["/bin/bash"]
#CMD /bin/bash
ENV varBuild=done
