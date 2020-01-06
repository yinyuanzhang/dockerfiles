FROM agrf/exome_wdl_tools_base:2019.07

# Set path
ENV PATH=/opt/conda/bin:$PATH

# Change dir
WORKDIR /opt/

# Copy the repo to the container
RUN mkdir /opt/exome_wdl_tools
ADD scripts/ /opt/exome_wdl_tools/scripts/

# Ensure that exome_wdl_tools is an executable
RUN ls -lsrth /opt/exome_wdl_tools/scripts/exome_wdl_tools.sh
RUN chmod +x /opt/exome_wdl_tools/scripts/exome_wdl_tools.sh

# Create softlink to $PATH
RUN ln -s /opt/exome_wdl_tools/scripts/exome_wdl_tools.sh /opt/conda/bin/exome_wdl_tools

# Add tests
ADD tests/ /opt/tests/

# Ensure the run_tests.sh is an executable
RUN chmod +x /opt/tests/run_tests.sh

# Local only
RUN bash /opt/tests/run_tests.sh

# Create an entrypoint
ENTRYPOINT ["bash", "/opt/conda/bin/exome_wdl_tools"]
