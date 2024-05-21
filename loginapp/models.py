from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
def validate_studentid(value):
    if len(str(value))!=8:
        raise ValidationError('STUDENT ID MUST BE 7 NUMBERS',
                              params={'value': value})
 
def validate_indexnum(value):
    if len(str(value))!=7:
        raise ValidationError("Index number must be 7 digitd",
                              params={'value': value})
    
class logininfo(models.Model):
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    indexnum=models.IntegerField(validators=[validate_indexnum])
    student_id=models.IntegerField(validators=[validate_studentid])
    
    def __str__(self):
        return self.username        
    def save(self, *args, **kwargs):
        self.full_clean()
        
        if self.pk is None or not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super(logininfo, self).save(*args, **kwargs)
    def clean(self):
        if not self.username:
            raise ValidationError('Username cannot be empty.')
        super(logininfo,self).clean()     
    def check_password(self, raw_password):
        return check_pwd(raw_password, self.password)    






         


     

    
    
