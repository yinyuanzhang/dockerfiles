FROM python:3.6.8

LABEL Name=surveillance Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

# Using pip:
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN wget https://pjreddie.com/media/files/yolov3.weights --output-document=/app/yolo-coco/yolov3.weights


CMD ["python3","/app/surveillance.py"]
