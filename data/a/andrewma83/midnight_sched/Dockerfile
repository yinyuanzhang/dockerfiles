FROM python:3.5

WORKDIR /opt/app
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir -p /opt/app/data

COPY sched.py /opt/app
COPY slideCtrlRemind.py /opt/app
COPY commUtils.py /opt/app
COPY nurseryReminder.py /opt/app
COPY welcomeRemind.py /opt/app
COPY requirements.txt /opt/app

RUN pip3 install -r /opt/app/requirements.txt

ENTRYPOINT ["python3", "/opt/app/sched.py"]

