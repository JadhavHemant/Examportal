
# from django.contrib import admin
from django.urls import path
from ExamApp.Apis import TopicRestApi    
from ExamApp.Apis import ContentRestApi
from ExamApp.Apis import QuestionsRestApi
from ExamApp.Apis import AddStudentRestApi
from ExamApp.Apis import ExamRestApi
from ExamApp.Apis import StudentExamRestApi
# ============================================
from ExamApp.Apis import TutorialTopicApi
from ExamApp.Apis import TutorialContent
from ExamApp.Apis import TutorialDataRestApi,VedioRestApi
# ============================================
# from ExamApp.Apis import VedioTopic




# from ExamApp.Apis import TopicWiseConent
urlpatterns = [
    # path('admin/', admin.site.urls),
                #Tpoics URL's
    path("api/topic",TopicRestApi.TpoicApi.as_view()),
    path("api/topic/<int:pk>/",TopicRestApi.TopicUpdateDeleteApi.as_view()),
    path("api/topic/content/<int:topic_id>/",TopicRestApi.ContentWiseRestApi.as_view()),
              
                #Content URL's
    path("api/content",ContentRestApi.ContentApi.as_view()),
    path("api/content/<int:pk>/",ContentRestApi.ContentUpdateDeleteApi.as_view()),
    path("api/content/questions/<int:content_id>/",ContentRestApi.ContentWiseAPIView.as_view()),
              
                #Questions URL's
    path("api/questions",QuestionsRestApi.QuestionApi.as_view()),
    path("api/questions/<int:pk>/",QuestionsRestApi.QuestionUpdateDeleteApi.as_view()),  
               
                #Student URL's
    path("api/studentregi",AddStudentRestApi.AddStudentApi.as_view()),
    path("api/studentregi/update/delete/<int:pk>/",AddStudentRestApi.AddStudentUpdateDeleteApi.as_view()),
    path("api/login",AddStudentRestApi.StudentLoginApi.as_view()),  
    path("api/studentdata/<int:id>/",AddStudentRestApi.IdWiseStudentData.as_view()),  
                
                 #Student Exam URL's
    path("api/examanswer",ExamRestApi.ExamQuestionApi.as_view()),
    path("api/examanswer/id/<int:exam_id>/",ExamRestApi.ExamidWiseRestApi.as_view()), 
          
                #Exam URL's
    path("api/studexamdetails",StudentExamRestApi.StudentExamApi.as_view()),
    path("api/studexamdetails/<int:pk>/",StudentExamRestApi.StudentExamUpdateDeleteApi.as_view()), 
    
         #Tutorial Topic URL's
    path("api/tutorial",TutorialTopicApi.TutorialTopicApi.as_view()),
    path("api/tutorial/<int:pk>/",TutorialTopicApi.TutorialTopicUpdateDeleteApi.as_view()), 
    path("api/tutorial/content/<int:id>/",TutorialTopicApi.ContentWiseRestApi.as_view()),
 
        #  Tutorial Content URL's
    path("api/tutorial/tcontent",TutorialContent.TContentApi.as_view()),
    path("api/tutorial/tcontent/<int:pk>/",TutorialContent.TContentUpdateDeleteApi.as_view()), 
    path("api/tutorial/tcontent/tdata/<int:id>/",TutorialContent.TDataWiseRestApi.as_view()),
    path("api/tutorial/vediocontent/vedio/<int:id>/",TutorialContent.ContentWiseVedioRestApi.as_view()),
    
        #  Tutorial Content URL's   #
    path("api/tutorial/tcontent/data",TutorialDataRestApi.DataApi.as_view()),
    path("api/tutorial/tcontent/data/<int:pk>/",TutorialDataRestApi.DataUpdateDeleteApi.as_view()),

    path("api/vedios",VedioRestApi.VedioApi.as_view()),#VedioUpdateDeleteApi
    path("api/vedios/update/delete/<int:pk>/",VedioRestApi.VedioUpdateDeleteApi.as_view()),

]
