def uploaded_file(f):  
    with open('ExamApp/static/vedio/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  