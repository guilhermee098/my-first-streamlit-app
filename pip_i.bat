@echo off
.\venv\Scripts\activate
pip install %1
pip freeze > requirements.txt
