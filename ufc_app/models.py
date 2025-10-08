from django.db import models

class WeightClass(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    min_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    max_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.name

class Fighter(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80, blank=True)
    height = models.IntegerField(null=True, blank=True)
    reach = models.IntegerField(null=True, blank=True)
    stance = models.CharField(max_length=20, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.PROTECT, related_name='fighters')
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    city = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=80, blank=True)
    def __str__(self):
        return self.title

class Bout(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='bouts')
    fighter_red = models.ForeignKey(Fighter, on_delete=models.PROTECT, related_name='bouts_red')
    fighter_blue = models.ForeignKey(Fighter, on_delete=models.PROTECT, related_name='bouts_blue')
    result = models.CharField(max_length=50, blank=True)
    method = models.CharField(max_length=50, blank=True)
    round = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return f'{self.event_id}-{self.id}'
