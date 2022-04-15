FROM python:3.9.1

WORKDIR "/app"

COPY [".", "/app"]
RUN pip install -r requirements.txt

ENV FLASK_APP=api.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]
