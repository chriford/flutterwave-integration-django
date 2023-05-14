from .models import Hotel
from faker import Faker

faker = Faker()

def create_hotel_data(n):
    for i in range(1, n):
        Hotel.objects.create(
            name = faker.name(),
            description = '''Libraries, Libraries, Oh Libraries, so much knowledge in them guess why? Because of too many books. This library could be your dream libray.''',
        )