from django.db import models

# Create your models here.
class TopicModel(models.Model):
    topic_name=models.CharField(max_length=205,unique=True)
    class Meta:
        ordering=('id',)
        db_table='topic_tbl'
    def __str__(self):
        return self.id

class ContentModel(models.Model):
    content_name=models.CharField(max_length=205)
    topic_id=models.ForeignKey(TopicModel,related_name='content',on_delete=models.CASCADE)
    class Meta:
        ordering=('id',)
        db_table='topic_content_tbl'
    def __str__(self):
        return self.content_name                


class ContentQuestionsModel(models.Model):
    content_id=models.ForeignKey(ContentModel,related_name='questions',on_delete=models.CASCADE)
    question=models.CharField(max_length=255)
    option_1=models.CharField( max_length=205)
    option_2=models.CharField( max_length=205)
    option_3=models.CharField( max_length=205)
    option_4=models.CharField( max_length=205)
    currect_option=models.IntegerField()
    class Meta:
        ordering=('id',)
        db_table='content_question_tbl'
    def __str__(self):
        return self.question 
    
class CandidateModel(models.Model):
    candidate_name=models.CharField(max_length=100)
    candidate_gender=models.CharField(max_length=20)
    candidate_email=models.CharField(unique=True,max_length=100)
    contact_number=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    class Meta:
        ordering=('id',)
        db_table='candidate_student_tabl'
    def __str__(self):
        return self.candidate_name
# ----------------------------------------------------------------------------------------------------------
class CandidateExamModel(models.Model):
    candidate_id=models.ForeignKey(CandidateModel,related_name='candidate',on_delete=models.CASCADE)  
    exam_date=models.CharField(max_length=100)
    exam_start_time=models.CharField(max_length=100) 
    exam_end_time=models.CharField(max_length=100)
    exam_status=models.CharField(max_length=100)
    class Meta: 
        ordering=('id',)
        db_table='candidate_exam_details'
    def __str__(self):
        return self.exam_id 


class ExamQuestionModel(models.Model):
    exam_id=models.ForeignKey(CandidateExamModel,related_name='exam',on_delete=models.CASCADE)
    question_id=models.ForeignKey(ContentQuestionsModel,related_name='exam',on_delete=models.CASCADE)
    submit_option_number=models.IntegerField()
    class Meta:
        ordering=('id',)
        db_table='exam_quesion_result'  
    def __str__(self):
        return self.exam_question_id
#-------------------------------------------------------------------------------------------------------------   
class DashboardModelMaster(models.Model):
    dashbord_discription = models.CharField(max_length=255) 
    class Meta: 
        ordering=('id',)
        db_table='Dashboard'
    def __str__(self):
        return self.dashbord_discription              
        
        
# --------------------------------------------------------------------------------------------------------------   
class TutorialModel(models.Model):
    tutorial_topics=models.CharField(max_length=255)
    class Meta:
        ordering =('id',)
        db_table = "tbl_tutorials"
    def __str__(self):
        return self.tutorial_topics    
         
class TutorialContentModel(models.Model):
    tutorial_content = models.CharField(max_length=255)
    tutorial_id=models.ForeignKey(TutorialModel,related_name="tutorialsContent",on_delete=models.CASCADE)
    class Meta:
        ordering = ('id',)
        db_table="tbltutorials_Content"   
    def __str__(self):
        return self.tutorial_content

class TutorialsData(models.Model):
    tutorial_headings = models.CharField(max_length=255)
    tutorial_data = models.CharField(max_length=255)
    tutorial_content_id=models.ForeignKey(TutorialContentModel,related_name="tutorialdata",on_delete=models.CASCADE)
    class Meta:
        ordering =('id',)
        db_table = 'tutorialdata_tbl'   
    def __str__ (self):
        return self.tutorial_data
# ---------------------------------------------------------------------------------------------

class VedioModel(models.Model):
    VedioModel=models.CharField(max_length=255)
    vedio_caption=models.CharField(max_length=255)
    tutorial_content_id=models.ForeignKey(TutorialContentModel,related_name="vedio",on_delete=models.CASCADE)
    class Meta:
        ordering = ('id',)
        db_table = 'vedios'
    def __str__(self):
        return self.vedio