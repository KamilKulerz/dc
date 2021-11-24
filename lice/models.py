from django.db import models

# Create your models here.


class License(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=255)
    # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=50)
    # Field name made lowercase.
    license = models.CharField(
        db_column='License', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'License'
        # ordering = ['id']


class AppUser(models.Model):
    net_id = models.CharField(name='net_id', max_length=200)
    Name = models.CharField(max_length=200, blank=True)
    Surname = models.CharField(max_length=200, blank=True)
    Active = models.BooleanField(default=False)
    FullAccess = models.BooleanField(default=False)
    LicenseSignAccess = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.net_id} | Name: {self.Name} {self.Surname} | LicenseSignAccess: {self.LicenseSignAccess} | Active: {self.Active} | FullAccess: {self.FullAccess}'
