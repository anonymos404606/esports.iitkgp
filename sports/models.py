from django.db import models

class mregistration(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      interest_game=models.CharField(max_length=200)
      skills=models.CharField(max_length=100)
      role=models.CharField(max_length=100)
      date=models.DateTimeField(auto_now_add=True)
      links=models.URLField(max_length=200)
      message=models.TextField()

      class Meta:
            ordering=['-date']
      def __str__(self):
            return self.name