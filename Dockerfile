FROM python:3.12-slim

# /usr/local/bin/uv <- как переменные среды на windows что бы uv можно было вызывать в любом месте

ENV PROGRESS_NO_TRUNC=1
WORKDIR /app
COPY . .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
RUN uv sync

ENTRYPOINT ["uv", "run"] 
CMD ["main.py"]
