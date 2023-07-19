FROM python:3.10

ADD scripts/docker-entrypoint.sh /etc/scripts/docker-entrypoint.sh
RUN chmod +x /etc/scripts/docker-entrypoint.sh

WORKDIR /app
COPY src/app.py .
COPY requirements.txt .
COPY src/templates ./templates
COPY src/static ./static
RUN pip install -r ./requirements.txt

ENTRYPOINT ["/etc/scripts/docker-entrypoint.sh"]
CMD ["python", "./app.py"]
