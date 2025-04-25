# django-starter-kit

## Prerequisites
- **Python 3.13.1** 이상
- **Docker Desktop** 설치

## Windows 환경에서 개발 서버 실행 방법
1. **컨트롤러 실행**  
   `controller_for_window/first-run-dev.bat` 파일을 실행합니다.

2. **서버 실행**  
   `open-dev-server.bat` 파일을 실행하면 서버가 시작됩니다.

## 인터프리터 설정 방법
first-run-dev.bat을 실행한 후 venv/Scripts/python.exe를 Select Existing으로 설정하면 됩니다.

## Window 환경에서 Production 서버 무중단 배포 방법
first-run-production.bat을 이미 실행한 후 상황에서  
수정사항이 생겼을 경우 아래 과정을 진행하면 됩니다.
1. **이미지 빌드**  
   `controller_for_window/build-server-image.bat` 실행
2. **컨테이너 순차적 재구동**  
   `controller_for_window/release-server.bat` 실행

