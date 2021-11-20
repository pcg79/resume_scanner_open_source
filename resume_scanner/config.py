proj_directory = "/Users/patrickgeorge/dev/personal/resume_scanner_open_source"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = [

'*'

]

##### Local database #####

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_scanner',
        'USER': 'resume_scanner_user',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
