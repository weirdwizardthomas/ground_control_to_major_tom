import django_tables2 as tables


class NeoTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        order_by = 'miss_distance'

    name = tables.Column()
    close_approach_date = tables.Column()
    miss_distance = tables.Column()
    estimated_diameter_min = tables.Column(empty_values=())
    estimated_diameter_max = tables.Column(empty_values=())

    def render_estimated_diameter_min(self, record):
        return record.estimated_diameter()['estimated_diameter_min']

    def render_estimated_diameter_max(self, record):
        return record.estimated_diameter()['estimated_diameter_max']
