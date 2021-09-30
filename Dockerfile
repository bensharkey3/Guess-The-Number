# dockerfile, image, container

FROM python:3.8

ADD sourcecode.py .

RUN pip install pandas matplotlib 

CMD ["python", "./sourcecode.py"]
