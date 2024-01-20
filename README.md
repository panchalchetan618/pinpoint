# Introduction
This project shows the configuration for AWS Pinpoint for SMS Services

## Features
- Request OTP for phone number
- Verify OTP for phone number

## How to setup?
### Clone the Repo
```bash
git clone https://github.com/panchalchetan618/pinpoint.git
cd pinpoint/
```

### Create Virtual environment
For Windows
- ```bash
  pip install veritualenv
  virtualenv venv
  ```
For Linux & Mac
- ```bash
  python3 -m venv venv

### Install requirements
```bash
pip install -r requirements.txt
```

### Setup .env file
- Create a file in root directory named as `.env`.
- Copy content from `.env.example` & paste in `.env`.
- Then add your keys & IDs etc...

### Runserver
```bash
python manage.py runserver
```
