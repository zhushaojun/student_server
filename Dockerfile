FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg2 dependencies
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
#    && apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev \
    # for pillow
#    && apk add --no-cache jpeg-dev zlib-dev \
#    && apk add --no-cache --virtual .build-deps build-base linux-headers

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip config set global.index-url https://pypi.douban.com/simple/  \
#    && pip install --upgrade pip \
    && pip install -r requirements.txt
#    && apk del build-deps

# Now copy in our code, and run it
COPY . /app

COPY ./entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]