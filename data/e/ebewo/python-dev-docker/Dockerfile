# the base miniconda3 image
FROM continuumio/miniconda3:latest

# load in the environment.yml file - this file controls what Python packages we install
ADD environment.yml /

# install the Python packages we specified into the base environment
RUN conda update -n base conda -y && conda env update

# download the coder binary, untar it, and allow it to be executed
RUN curl -s https://api.github.com/repos/cdr/code-server/releases/latest \
| grep "browser_download_url.*linux-x64.tar.gz" \
| cut -d : -f 2,3 | tr -d \" \
| wget -qi - && tar -xzvf code-server* && chmod +x code-server*/code-server

COPY docker-entrypoint.sh /usr/local/bin/

ADD ./code /code

ENTRYPOINT ["docker-entrypoint.sh"]