from django.apps import AppConfig

# The GamingConfig class is a subclass of AppConfig. It has a default_auto_field attribute that is set
# to 'django.db.models.BigAutoField'. It also has a name attribute that is set to 'gaming'
class GamingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gaming'
