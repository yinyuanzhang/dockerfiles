FROM python:3
LABEL authors="relent0r, dwtaylornz"

WORKDIR /usr/src/app

COPY *.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" "-a","(a)","-u","(u)","-p","(p)","-c","(c)","-i","(i)","-x","(x)","-o","(o)","-b","(b)","-t","(t)"]
