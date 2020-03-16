from django.db import models

# by defining classes, I am defining tables in my database
    # by defining attributes (in the classes), I am defining columns (in those tables)

class Entry(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'Entries'
        
        
class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.text
    
class Quote(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.text
        
class Rumi(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    key = "Rumi"
     
    def __str__(self):
        return "Rumi's #{}".format(self.id)
     
    class Meta():
        verbose_name_plural = 'Rumi\'s Quotes'
        
class Mooji(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    key = "Mooji"
     
    def __str__(self):
        return "Mooji's #{}".format(self.id)
     
    class Meta():
        verbose_name_plural = 'Mooji\'s Quotes'
        
        
        
        
        
class Topic(models.Model):
    text = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.text

    
class Topic_item(models.Model):
    item = models.ForeignKey(Topic, on_delete=models.CASCADE)
    more = models.TextField(max_length = 1000)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return '{} ¬ {} ~ id{}'.format(self.item, self.more, self.id)

    