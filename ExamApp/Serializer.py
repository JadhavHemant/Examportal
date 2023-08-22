from rest_framework import serializers
from ExamApp.models import *
from rest_framework.relations import PrimaryKeyRelatedField

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopicModel
        fields=['id','topic_name']
        
        
class ContentSerializer(serializers.ModelSerializer):
    topic_id=PrimaryKeyRelatedField(queryset=TopicModel.objects.all(),many=False)
    class Meta:
        model=ContentModel
        fields=['id','content_name','topic_id']


class ContentQuestionSerializer(serializers.ModelSerializer):
    content_id=PrimaryKeyRelatedField(queryset=ContentModel.objects.all(),many=False)
    class Meta:
        model=ContentQuestionsModel
        fields=['id','content_id','question','option_1','option_2','option_3','option_4','currect_option']
        
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CandidateModel
        fields=['id','candidate_name','candidate_gender','candidate_email','contact_number','password','city']

class CandidateExamSerializer(serializers.ModelSerializer):
    candidate_id=PrimaryKeyRelatedField(queryset=CandidateModel.objects.all(),many=False)
    class Meta:
        model=CandidateExamModel
        fields=['id','candidate_id','exam_date','exam_start_time','exam_end_time','exam_status']
 
class ExamSerializer(serializers.ModelSerializer):
    exam_id=PrimaryKeyRelatedField(queryset=CandidateExamModel.objects.all(),many=False)
    class Meta:
        model=ExamQuestionModel
        fields=["id","exam_id","question_id","submit_option_number"] 
       
        #dashBoard Details
         
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=DashboardModelMaster
        fields=["id","dashbord_discription"]        
        
         #Add Tutorial Topic Details
         
class TutorialTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model= TutorialModel  
        fields=["id","tutorial_topics"]

class TutorialContentSerializer(serializers.ModelSerializer):
    tutorial_id=PrimaryKeyRelatedField(queryset=TutorialModel.objects.all(),many=False)
    class Meta:
        model= TutorialContentModel  
        fields=["id","tutorial_content","tutorial_id"]  

class TutorialDataSerializer(serializers.ModelSerializer):
    tutorial_content_id=PrimaryKeyRelatedField(queryset=TutorialContentModel.objects.all(),many=False)
    class Meta:
        model= TutorialsData  
        fields=["id","tutorial_headings","tutorial_data","tutorial_content_id"]                     
             
#Veddio Tutorial Topic Detailss

class VedioDataSerializer(serializers.ModelSerializer):
    tutorial_content_id=PrimaryKeyRelatedField(queryset=TutorialContentModel.objects.all(),many=False)
    class Meta:
        model= VedioModel  
        fields=["id","VedioModel","vedio_caption","tutorial_content_id"]                           