from rest_framework import serializers

from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    agree_rate = serializers.SerializerMethodField()
    disagree_rate = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'agree', 'disagree', 
                'agree_rate', 'disagree_rate', 'created_at']

    def get_agree_rate(self, obj):
        total = obj.agree + obj.disagree
        if total > 0:
            return obj.agree / total * 100
        else:
            return 0

    def get_disagree_rate(self, obj):
        total = obj.agree + obj.disagree
        if total > 0:
            return obj.disagree / total * 100
        else:
            return 0