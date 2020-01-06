FROM lambci/lambda:build-python3.7
RUN pip install boto3
COPY main.py main.py
ENTRYPOINT ["python3", "main.py"]