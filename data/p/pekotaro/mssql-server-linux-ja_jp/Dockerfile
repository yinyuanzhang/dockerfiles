FROM mcr.microsoft.com/mssql/server:2017-latest-ubuntu

RUN apt-get update

# \¦¾êÆüÍ¾êðú{êü¯ÉÝè
RUN apt-get install -y locales 
RUN apt-get install -y language-pack-ja-base language-pack-ja 
RUN locale-gen ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8

# ^C][ðAsia/TokyoÉÏX
ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# bashÖWÌî{R}hðCXg[
RUN apt-get install -y bash-completion
RUN apt-get install -y less
RUN apt-get install -y vim
RUN apt-get install -y iputils-ping

# SQL ServerCXg[pÌftHgÝè
#   GfBVFDeveloper
#   úpX[hFP@ssw0rd
#   gp·é|[gF1433
#   ¾êFú{ê
ENV ACCEPT_EULA=Y
ENV MSSQL_PID=Developer
ENV MSSQL_SA_PASSWORD=P@ssw0rd
ENV MSSQL_TCP_PORT=1433
ENV MSSQL_LCID=1041

# SQL ServerÌR}hCc[ÉpXðÊ·
ENV PATH=$PATH:/opt/mssql-tools/bin
