from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Assessment, Submission, CustomUser
from .serializers import AssessmentSerializer, SubmissionSerializer, AdminCreateStudentSerializer
from .permissions import IsAdminUser, IsStudentUser

# Create your views here.
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAdminUser] 

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsStudentUser]

    def perform_create(self, serializer):
        assessment = serializer.validated_data['assessment']
        answers = serializer.validated_data['answers']
        score = 1 if answers == assessment.correct_answers else 0
        serializer.save(student=self.request.user, score=score)

class AdminCreateStudentViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminCreateStudentSerializer
    permission_classes = [IsAdminUser]