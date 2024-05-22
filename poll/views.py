from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Poll
from .serializers import PollSerializer

def get_poll_or_404(id):
    return get_object_or_404(Poll, id=id)

@api_view(['GET', 'POST'])
def list(request):
    if request.method == 'GET':
        polls = Poll.objects.order_by('-created_at')
        serializer = PollSerializer(polls, many=True)
        return Response({'message': '조회 성공', 'data': serializer.data}, status=200)
    
    if request.method == 'POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '등록 성공', 'data': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, id):
    poll = get_poll_or_404(id)

    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response({'message': '조회 성공', 'data': serializer.data}, status=200)
    
    if request.method == 'PUT':
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '수정 성공', 'data': serializer.data}, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        poll.delete()
        return Response({'message': '삭제 성공'}, status=204)

@api_view(['POST'])
def agree(request, id):
    poll = get_poll_or_404(id)
    poll.agree += 1
    poll.save()
    serializer = PollSerializer(poll)
    return Response({'message': '투표 성공', 'data': serializer.data}, status=200)

@api_view(['POST'])
def disagree(request, id):
    poll = get_poll_or_404(id)
    poll.disagree += 1
    poll.save()
    serializer = PollSerializer(poll)
    return Response({'message': '투표 성공', 'data': serializer.data}, status=200)