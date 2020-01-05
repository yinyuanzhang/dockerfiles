FROM python:2.7-onbuild
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]
