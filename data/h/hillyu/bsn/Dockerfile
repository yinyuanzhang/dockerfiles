From alpine:edge
RUN apk --update --no-cache add python3 py3-lxml&& \
	    python3 -m ensurepip && \
	    rm -r /usr/lib/python*/ensurepip && \
	    pip3 install --upgrade pip setuptools && \
        pip3 install flask && \
        pip3 install redis && \
	    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
	    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
	    rm -r /root/.cache
ADD flask_demo.py /root/
ADD configuration.py /root/
ADD checkconfig.py /root/
ADD parseConfig.sh /root/
ADD getrssi.sh /root/
ADD bsn_adapt_cali.py /root/
ADD logfiles /root/logfiles
COPY cron_pars_daily /etc/periodic/daily
#COPY cron_rssi_hourly /etc/periodic/hourly
ADD bod.py /root/
ADD bodModule.so /root/
ADD IC.py /root/
ADD intcalModule.so /root/
ADD setupLabel.py /root/
#COPY root /var/spool/cron/crontabs/root
WORKDIR "/root"
EXPOSE 10080
#RUN chmod +x /bin/myawesomescript
CMD crond -l 2 && python flask_demo.py
