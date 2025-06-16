from django.db import models

class FitnessClass(models.Model):
    CLASS_CHOICES = [('Yoga', 'Yoga'), ('Zumba', 'Zumba'), ('HIIT', 'HIIT')]
    name = models.CharField(max_length=50, choices=CLASS_CHOICES)
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    available_slots = models.PositiveIntegerField()

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)