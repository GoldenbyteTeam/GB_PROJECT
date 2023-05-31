# Goldenbyte
## Goldenbyte.it - Shared IT knowledge

The purpose of this project is to provide a centralized notebook to share  CLI's command references and clipboards.

[Goldenbyte](https://goldenbyte.it) is built in [Django](https://www.djangoproject.com/) and pages are been published using [Notion](https://www.notion.so/) 
and [Fruitionsite](https://fruitionsite.com/Fruition-Free-Open-Source-Toolkit-for-Building-Websites-with-Notion-771ef38657244c27b9389734a9cbff44).

Goldenbyte.it is an open project. But, it can be deployed privately among teams members based on specific catalogues.

---
### Configuration requirements
Install all requirements
`pip install -r requirements.txt`
All the configurations are stored in these files:
- .env
  ```
    SENDGRID_API_KEY=<Token>
    # SendGrid Sender Identity
    FROM_EMAIL=<sender_mail>
  ```
* gb/local_settings.py
  ```
    SECRET_KEY = <django-key>

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = [<IP_SRV>]

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #postgresDB
        'NAME': <DBname>,
        'USER': <DBuser>,
        'PASSWORD':<DBpassword>,
        'HOST': <DBhost>
    }
  }
  ```
+ quotes_config.ini (Optional)
  ```
  [postgres]
  host = <IP_SRV_DB>
  db = <DBname> #It should be different from mainDB
  user = <DBuser>
  psw = <DBpassword>

  ```
  
