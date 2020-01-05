ARG cuda=cuda
FROM willthefrog/cuda-runtime:${cuda}
ARG cuda=cuda

ENV LD_LIBRARY_PATH=/home/opt/nvidia_lib/

COPY pacman.conf /pacman.conf

RUN pacman -Syu --noconfirm --config /pacman.conf ; \
        pacman -Scc --noconfirm

# `inetutils` is for `hostname`
RUN pacman -Sy --noconfirm --config /pacman.conf inetutils which awk wget tar129 jre7-openjdk-headless hadoop-client ; \
        pacman -Scc --noconfirm

RUN pacman -Sy --noconfirm --config /pacman.conf base-devel openssh vim rsync psmisc moreutils tmux git ; \
        pacman -Scc --noconfirm

RUN pacman -Sy --noconfirm --config /pacman.conf opencv-with-python2-support \
        python-tqdm python2-tqdm python-pycocotools-git python2-pycocotools-git \
        python-pillow-simd-git python2-pillow-simd-git python-dali-git python2-dali-git \
        python-scipy python2-scipy \
        python-nvidia-ml-py3-git python2-nvidia-ml-py3-git; \
        pacman -Scc --noconfirm

RUN pacman -Sy --noconfirm --config /pacman.conf python-paddle-${cuda}-git python2-paddle-${cuda}-git; \
        pacman -Scc --noconfirm

RUN rm /pacman.conf ; rm /var/lib/pacman/sync/*

RUN echo 'eval $START_CMD' > /root/start.sh ; \
        chmod +x /root/start.sh
CMD /root/start.sh

