from django.db import models

class Ratings(models.Model):

    leaderboard_rank= models.IntegerField(null=True)
    username= models.CharField(max_length=100,null=True)
    name= models.CharField(max_length=100,null=True)
    country= models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    organization= models.CharField(max_length=100,null=True)
    rank_codeforces= models.IntegerField(null=True)
    rating_codeforces = models.IntegerField(null=True)
    links = models.CharField(max_length=100,null=True)
 
  
     
    def __str__(self):
        return self.username
    
