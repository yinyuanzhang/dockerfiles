FROM dcm4che/dcm4chee-arc-psql:5.15.0

COPY script_entrypoint.sh /script_entrypoint.sh

RUN groupadd -g 1010 ansible
RUN usermod -a -G ansible wildfly
RUN usermod -a -G ansible root

ENTRYPOINT ["/script_entrypoint.sh"]
CMD ["standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c", "dcm4chee-arc.xml" ]
