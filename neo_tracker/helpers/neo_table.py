import django_tables2 as tables


# the object name, size estimate, time and distance of the closest encounter
class NeoTable(tables.Table):
    name = tables.Column()

    class Meta:
        template_name = "django_tables2/bootstrap.html"
