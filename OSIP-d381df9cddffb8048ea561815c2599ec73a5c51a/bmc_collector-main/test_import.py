#!/usr/bin/env python3
# 测试导入
import sys

print("Python version:", sys.version)

try:
    from flask import Flask
    print("✓ Flask imported successfully")
except Exception as e:
    print(f"✗ Flask import failed: {e}")

try:
    from flask_sqlalchemy import SQLAlchemy
    print("✓ Flask-SQLAlchemy imported successfully")
except Exception as e:
    print(f"✗ Flask-SQLAlchemy import failed: {e}")

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    print("✓ APScheduler imported successfully")
except Exception as e:
    print(f"✗ APScheduler import failed: {e}")

try:
    from cryptography.fernet import Fernet
    print("✓ Cryptography imported successfully")
except Exception as e:
    print(f"✗ Cryptography import failed: {e}")

try:
    import requests
    print("✓ Requests imported successfully")
except Exception as e:
    print(f"✗ Requests import failed: {e}")

try:
    import paramiko
    print("✓ Paramiko imported successfully")
except Exception as e:
    print(f"✗ Paramiko import failed: {e}")

print("\nAll imports tested!")
