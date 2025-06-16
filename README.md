# Fitness Booking API

## Setup

```bash
pip install django djangorestframework
python manage.py makemigrations booking
python manage.py migrate
python manage.py loaddata sample_classes_fixture.json
python manage.py runserver
```

## Endpoints

- GET /classes/
- POST /book/
- GET /bookings/?email=email@example.com