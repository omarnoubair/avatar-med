FROM python:3.9.18

WORKDIR /avatar

RUN pip install flask

COPY hello.py /avatar/hello.py 

CMD ["python3", "/avatar/hello.py"]
