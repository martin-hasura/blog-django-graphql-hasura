FROM python:3
ENV PIP_NO_CACHE_DIR=1
RUN pip install --upgrade pip && pip install 'django<4' \
        'django-graphql-jwt<1' \
        'djangorestframework<4' \
        'gunicorn<21'
WORKDIR /code
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]