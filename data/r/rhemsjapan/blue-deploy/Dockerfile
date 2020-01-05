FROM alpine:3.9

RUN     apk add --no-cache vim \
                           bash \
                           curl \
                           python3 && \
        python3 -m ensurepip && \
        rm -r /usr/lib/python*/ensurepip && \
        pip3 install --upgrade pip setuptools && \
        if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

RUN     pip3 install redis \
        && pip3 install boto \
        && pip3 install ConfigParser \
        && pip3 install requests \
        && pip3 install supervisor \
        && pip3 install supervisor-stdout

RUN rm -r /root/.cache && mkdir -p /root/deploy

COPY hook.py /root/deploy
COPY receiver.py /root/deploy
COPY DeploySysFunc.py /root/deploy
COPY supervisord.conf /etc/supervisord.conf
COPY supervisord-rhems-deploy-system.conf /etc/supervisor.d/rhems-deploy-system.ini
RUN  chmod +x /root/deploy/receiver.py /root/deploy/hook.py
RUN  mkdir /deploy/ && touch /deploy/.done

ADD run.sh /run.sh
RUN chmod 755 /*.sh
#CMD ["/run.sh"]
CMD ["/usr/bin/supervisord"]
