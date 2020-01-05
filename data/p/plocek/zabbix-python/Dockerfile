FROM zabbix/zabbix-server-mysql:ubuntu-latest
MAINTAINER Sebastian Plocek <sebastian@plocek.at>

# Update
RUN apt-get update && apt-get install -y \
  curl \
  python-pip

# Install dependencies
RUN pip install \
  requests \
  --upgrade pip