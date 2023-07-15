# Email Sender project
this project is meant to create an email sender

in the settings.py file
```python
# configuration for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@gmail.com'#THE EMAIL
EMAIL_HOST_PASSWORD = 'genertedPassword' 

DEFAULT_FROM_EMAIL = 'example@gmail.com'#very important
'''for the host password go to google security
    in the app security feature, let it generate the 
    password
'''
```