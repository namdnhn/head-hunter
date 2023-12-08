# head-hunter
## Hướng dẫn cài đặt môi trường cho back-end
- Cần cài đặt Python và MySQL sẵn trong máy
- Truy cập vào folder app trong project, tạo một file .env có nội dung giống trong file .env example và sửa lại các thông tin tương ứng với máy của người dùng.
- Tạo môi trường ảo: ```python -m venv head-hunter-env```
- Kích hoạt môi trường ảo:
  + Với Windows: ```head-hunter-env\Scripts\activate```
  + Với MacOS và Linux: ```source head-hunter-env/bin/activate```
- Cài đặt các dependencies cho môi trường ảo: ```pip install -r requirements.txt```
- Chạy server trong local (di chuyển vào thư mục chứa file main.py): ```uvicorn main:app -reload```
- Tắt kích hoạt môi trường ảo: ```deactivate```
## Hướng dẫn cài đặt môi trường cho front-end
- Phiên bản sử dụng: NodeJS 14.18.0
- di chuyển vào thư mục front-end: ```cd view```
- Cài đặt môi trường cho front-end: ```yarn install```
- Chạy front-end: ```yarn run dev```
