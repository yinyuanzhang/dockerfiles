FROM ubuntu:bionic

RUN mkdir /var/run/sshd

ENV DEBIAN_FRONTEND noninteractive # Allows tzdata to be installed noninteractively

RUN apt-get update && \
    apt-get install -y git python3 python3-pip nano emacs-nox vim \
    openssh-server software-properties-common curl unzip && \
    pip3 install pyyaml pytz requests grequests python-dateutil && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache

# This lets us exit sshd cleanly
COPY /gradescope-base/dumb-init_1.2.0_amd64.deb /tmp
RUN dpkg -i /tmp/dumb-init_1.2.0_amd64.deb

# Create root's ssh config directory
RUN mkdir -p /root/.ssh && \
    touch /root/.ssh/authorized_keys && \
    chmod 644 /root/.ssh/authorized_keys

COPY /gradescope-base/sshd_config /etc/ssh/sshd_config

RUN mkdir /autograder
COPY /harness/update_harness.py /autograder/update_harness.py
COPY /harness/update_and_run_harness.sh /autograder/update_and_run_harness.sh
COPY /harness/harness.py /autograder/harness.py

COPY /gradescope-base/start_sshd.sh /usr/local/sbin/start_sshd.sh
COPY /gradescope-base/ssh_wrapper.sh /usr/local/sbin/ssh_wrapper.sh

COPY /gradescope-base/motd /etc/motd

# Set the locale to UTF-8 to ensure that Unicode output is encoded correctly
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/autograder/update_and_run_harness.sh"]
