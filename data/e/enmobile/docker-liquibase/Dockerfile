FROM java

MAINTAINER SequenceIq

# download liquibase from https://github.com/liquibase/liquibase/releases/download/liquibase-parent-3.5.3/liquibase-3.5.3-bin.tar.gz
COPY lib/liquibase-3.5.3-bin.tar.gz /tmp/liquibase-3.5.3-bin.tar.gz

# Create a directory for liquibase
RUN mkdir /opt/liquibase

# Unpack the distribution
RUN tar -xzf /tmp/liquibase-3.5.3-bin.tar.gz -C /opt/liquibase
RUN chmod +x /opt/liquibase/liquibase

# Symlink to liquibase to be on the path
RUN ln -s /opt/liquibase/liquibase /usr/local/bin/

# Get the oracle JDBC driver from http://www.oracle.com/technetwork/database/features/jdbc/jdbc-drivers-12c-download-1958347.html
COPY lib/ojdbc6.jar /opt/jdbc_drivers/

RUN ln -s /opt/jdbc_drivers/ojdbc6.jar /usr/local/bin/

# Add command scripts
ADD scripts /scripts
RUN chmod -R +x /scripts

VOLUME ["/changelogs"]

WORKDIR /

ENTRYPOINT ["/scripts/liquibase_command.sh"]
