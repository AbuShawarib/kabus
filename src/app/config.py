import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    RECAPTCHA_PUBLIC_KEY = (
                            os.environ.get('RECAPTCHA_PUBLIC_KEY') or
                            '6LcGI80ZAAAAAPPTcxxxxxxxxxxxxxxxxxxxxxxxx'
                           )
    RECAPTCHA_PRIVATE_KEY = (
                             os.environ.get('RECAPTCHA_PRIVATE_KEY') or
                             '6LcGI80ZAAAAAEWJxxxxxxxxxxxxxxxxxxxxxxxx'
                            )
