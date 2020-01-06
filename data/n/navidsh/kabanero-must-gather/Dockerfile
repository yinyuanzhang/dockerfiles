FROM quay.io/openshift/origin-must-gather:4.2

# Save original gather script
RUN mv /usr/bin/gather /usr/bin/gather_original

# Copy all Kabanero scripts to /usr/bin
COPY gather-kabanero/* /usr/bin/

ENTRYPOINT /usr/bin/gather