FROM python:2-alpine
RUN adduser -S backend
USER backend
COPY backend.py /

ENTRYPOINT ["python", "/backend.py"]
