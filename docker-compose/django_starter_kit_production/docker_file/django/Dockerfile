# 1) Builder stage: 파이썬 패키지 설치만 미리 해두는 단계
FROM python:3.10-slim AS builder

# 환경 변수
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# requirements.txt 복사 & 의존성 설치
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 2) Final stage: 실제 코드만 복사해서 가볍게 실행
FROM python:3.10-slim

WORKDIR /app

# 빌더 단계에서 설치한 site-packages 복사
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY .. .

# Waitress 로 WSGI 애플리케이션 실행
CMD ["waitress-serve", "--listen=0.0.0.0:8200", "server.wsgi:application"]
