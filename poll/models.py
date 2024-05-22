from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def agree_rate(self):
        total_votes = self.agree + self.disagree
        if total_votes > 0:
            return self.agree / total_votes * 100
        else: 
            return 0
    def disagree_rate(self):
        total_votes = self.agree + self.disagree
        if total_votes > 0:
            return self.disagree/total_votes * 100
        else:
            return 0
    