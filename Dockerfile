FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python3-dev libffi-dev

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash admin@gmail.com && chmod 777 /opt /run

WORKDIR /Test_Backend

RUN mkdir /Test_Backend/static && mkdir /Test_Backend/media && chown -R admin@gmail.com /Test_Backend/ && chmod 755 /Test_Backend

COPY --chown=admin@gmail.com:admin@gmail.com . .

RUN pip install -r requirements.txt

USER admin@gmail.com

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
