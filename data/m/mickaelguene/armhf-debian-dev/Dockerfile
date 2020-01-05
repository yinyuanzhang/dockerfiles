FROM mickaelguene/armhf-debian:jessie

MAINTAINER Mickael Guene <mickael.guene@st.com>

ADD build.sh /build.sh
RUN ["/usr/bin/umeq-arm", "-execve", "-0", "bash", "/bin/bash", "-c", "/build.sh"]

CMD ["/usr/bin/umeq-arm", "-execve", "-0", "bash", "/bin/bash"]
