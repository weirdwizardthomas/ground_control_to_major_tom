from dataclasses import dataclass
from datetime import datetime


@dataclass
class NearEarthObject:
    id: int
    neo_reference_id: int
    name: str
    nasa_jpl_url: dict
    absolute_magnitude_h: float
    close_approach_date: datetime
    orbiting_body: bool
    relative_velocity_dictionary: dict
    miss_distance_dictionary: dict
    estimated_diameter_dictionary: dict
    is_potentially_hazardous_asteroid: bool
    is_sentry_object: dict
    links: dict

    def relative_velocity(self, units='kilometers_per_second'):
        return float(self.pick_value_by_unit(self.relative_velocity_dictionary, units, 'relative velocity'))

    def estimated_diameter(self, units='kilometers'):
        return self.pick_value_by_unit(self.estimated_diameter_dictionary, units, 'diameter')

    def miss_distance(self, units='kilometers'):
        return float(self.pick_value_by_unit(self.miss_distance_dictionary, units, 'miss distance'))

    @staticmethod
    def pick_value_by_unit(dictionary, units, attribute_name):
        if units not in dictionary.keys():
            raise ValueError(f'Invalid units for {attribute_name}. Possible values: {dictionary.keys()}')

        return dictionary[units]

    @staticmethod
    def from_dictionary(data_dictionary):
        # The JSON always contains a single item list of close approach data, hence the squash from list to the item
        close_approach_data = data_dictionary['close_approach_data'][0]

        return NearEarthObject(id=data_dictionary['id'],
                               neo_reference_id=data_dictionary['neo_reference_id'],
                               name=data_dictionary['name'],
                               nasa_jpl_url=data_dictionary['nasa_jpl_url'],
                               absolute_magnitude_h=data_dictionary['absolute_magnitude_h'],
                               close_approach_date=datetime.strptime(close_approach_data['close_approach_date_full'],
                                                                     '%Y-%b-%d %H:%M'),
                               orbiting_body=close_approach_data['orbiting_body'],
                               relative_velocity_dictionary=close_approach_data['relative_velocity'],
                               miss_distance_dictionary=close_approach_data['miss_distance'],
                               estimated_diameter_dictionary=data_dictionary['estimated_diameter'],
                               is_potentially_hazardous_asteroid=data_dictionary['is_potentially_hazardous_asteroid'],
                               is_sentry_object=data_dictionary['is_sentry_object'],
                               links=data_dictionary['links']
                               )
