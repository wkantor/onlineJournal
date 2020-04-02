from django.db import models
from django.contrib.auth.models import User, auth

# by defining classes, I am defining tables in my database
    # by defining attributes (in the classes), I am defining columns (in those tables)

 

class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.TextField(null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} - {} -{}'.format(self.author, self.topic,  self.date)
    
    class Meta:
        verbose_name_plural = 'Entries'
        
        
class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length = 2000, null = True)
    
    def __str__(self):
        return self.text
    
    
class Quote(models.Model):
    text = models.CharField(max_length = 200)
    comment = models.TextField(max_length = 2000, null = True)
    
    def __str__(self):
        return self.text
        
        
class Quote_item(models.Model):
    item = models.ForeignKey(Quote, on_delete=models.CASCADE)
    more = models.TextField(max_length = 1000)
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length = 2000, null = True)
    
    def __str__(self):
        return '{} ~ {}'.format(self.item, self.more)  
        
        
class Topic(models.Model):
    text = models.CharField(max_length = 200)
    comment = models.TextField(max_length = 2000, null = True)
    
    def __str__(self):
        return self.text

    
class Topic_item(models.Model):
    item = models.ForeignKey(Topic, on_delete=models.CASCADE)
    more = models.TextField(max_length = 1000)
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length = 2000, null = True)

    
    def __str__(self):
        return '{} ~ {}'.format(self.item, self.more)
    
class Topic_item2(models.Model):
    parent = models.ForeignKey(Topic_item, on_delete=models.CASCADE)
    content = models.TextField(max_length = 2000)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return '{} ¬ {} ~ id{}'.format(self.parent, self.content, self.id)
    
    class Meta:
        verbose_name_plural = 'Topic_items2'
    
    
class Shadow(models.Model):
    text = models.CharField(max_length = 200)
    comment = models.TextField(max_length = 2000, null = True)

    
    def __str__(self):
        return self.text

class Shadow_item(models.Model):
    item = models.ForeignKey(Shadow, on_delete=models.CASCADE)
    more = models.TextField(max_length = 1000)
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length = 2000, null = True)

    
    def __str__(self):
        return '{} ~ {}'.format(self.item, self.more)
    
class Plunge(models.Model):
    text = models.CharField(max_length = 200)
    comment = models.TextField(max_length = 2000, null = True)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.text
