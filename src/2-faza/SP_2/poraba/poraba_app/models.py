from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from datetime import datetime
import numpy as np

# Create your models here.

class Avtomobil(models.Model):
    ime_vozila = models.CharField(max_length=200)

    #tip_goriva_izbira = (('B', 'Bencin'), ('D', 'Diezel'), ('E', 'Elektrika'))
    #tip_goriva = models.CharField(max_length=1, choices=tip_goriva_izbira, default='B')
    tip_goriva = models.CharField(max_length=45, default='Bencin 95')

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'ID: %d Avto: %s Gorivo: %s' % (self.id, self.ime_vozila, self.tip_goriva)

    def povprecna_poraba(self):
        p = Poraba.objects.filter(avto_id=self)
        avg = np.mean([x.poraba for x in p])
        return ("%.2f" % avg)

    def povprecna_poraba1(self):
        p = Poraba.objects.filter(avto_id=self)
        avg = np.mean([x.poraba for x in p])
        return avg


class Poraba(models.Model):
    poraba = models.DecimalField(max_digits=4, decimal_places=1)
    avto_id = models.ForeignKey(Avtomobil, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    datum = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Avtomobil: %s, User: %s , Poraba: %f' % (self.avto_id.ime_vozila, self.user_id.username, self.poraba)
