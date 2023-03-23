FROM python:3.7

WORKDIR /opt/app

COPY ./requirements/requirements.txt /opt/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/app

ENV PYTHONPATH /opt/app

CMD ["python", "./tgboost/train_pipeline.py"]