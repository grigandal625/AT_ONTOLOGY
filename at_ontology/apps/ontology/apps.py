from django.apps import AppConfig


class OntologyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "at_ontology.apps.ontology"
    label = "ontology"
    verbose_name = "Онтологии"
