import factory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('email',)

    id = factory.Faker('uuid4')
    email = factory.Faker('email')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    name = factory.Faker('name')
    is_active = True
    is_staff = False
