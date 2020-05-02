from coworking.settings import *

DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "qj@*uxslwnu77y*@yv12$4@12$$7_5!)276&aohn$3c2kj=hjs"
NEVERCACHE_KEY = "_71ak9!4$&v$w2=*!3%^e!h9o4ac@^$gecykhf5-4%+t1=jn!k"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "fabrica",
        "USER": "root",
        "PASSWORD": "mk28to#$",
        "HOST": "database",
        "PORT": "3306",
    }
}
