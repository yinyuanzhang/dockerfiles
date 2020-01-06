FROM puyuantech/dtl-base:latest
LABEL name="puyuantech/surfing"
LABEL maintainer="puyuan<github@puyuan.tech>"

ENV PYPI_MIRROR="https://mirrors.aliyun.com/pypi/simple/"
COPY python /surf/python
COPY bin /surf/bin

RUN cd /surf/python && python3 -m pip install -r requirements.txt -i ${PYPI_MIRROR} && python3 -m pip install --extra-index-url https://rquser:ricequant99@py.ricequant.com/simple/ rqdatac -i "https://mirrors.aliyun.com/pypi/simple" && pip install rqdatac -U && python3 setup.py install
RUN python3 -m pip install awscli -i "https://mirrors.aliyun.com/pypi/simple"
ENV RQDATAC2_CONF="rqdata://license:DcD0vxqM3m3glk2643x0hDzZ4EnEJdYU2FKcgsQaFFcAFLkhqdGb61GGbKqDEqQ3EHSsy1l7fiVILzeY6ZHOlibP47sXVuwmct1uxPH2XrE4Eon6vD5xKEBSRSau-6AUJotBDd6HxaDZnq5sjhZGmOUPF-pcjpttAOZXmRG4d5g=QMRAmyrM6kXQrO9g1jFfJDn5vDmcNraKPU3RVlFpng-21Y1F25htD_ZvvGvDLKDZVKxlkP95uDvA5NbgxIcGx_hHR2_xvSJUiB3yyWR1agf70GhOvMfgud8ZHVyWjDq0klSNCAfZuNP6ksI1CPVw8IV5Z_oOsmucPGjd4x_cHSY=@rqdatad-pro.ricequant.com:16011" 

WORKDIR /surf/bin
