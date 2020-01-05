FROM funkypenguin/grinpool-mwdockerbase

# Good docker practice, plus we get microbadger badges
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/grinpool.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

WORKDIR /services

COPY grinbase/ /usr/local/bin/grinbase/
COPY grinlib/ /usr/local/bin/grinlib/
COPY services/*.py /usr/local/bin/
COPY services/config.ini /usr/local/bin/
COPY services/config.ini /services/
COPY api/ /usr/local/bin/api/
COPY api/MWGP_payout.py /content/

CMD ["/bin/sh"]
