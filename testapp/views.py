from django.shortcuts import render,redirect,HttpResponse
from testapp.models import Student,Submarks,Emp,Post,Friendlist,Hotel
from django.db.models import Max,Min,Avg,Count,Sum,FloatField,IntegerField
# Create your views here.
import random,json
from django.db import connection



#this is new commit
#this is branch commit

def jointable(request):
    #cursor=connection.cursor()
    #cursor.execute("select * from Student")
    #result=cursor.fetchall()
    #emp=Student.objects.exclude(marks=400)
    #emp=Student.objects.filter(marks=500)|Student.objects.filter(marks=100)
    #emp = Student.objects.filter(marks=500) & Student.objects.filter(marks=480)
    #sql="SELECT * FROM testapp_student"
    #sql = "SELECT id,name FROM testapp_student"
    #sql = "SELECT id,name FROM testapp_student WHERE name='srinu'"
    #emp = Student.objects.raw("SELECT testapp_student.id,testapp_student.name FROM testapp_student INNER JOIN testapp_emp ON testapp_student.marks=testapp_emp.marks")
    lmt=5
    name="name"
    #emp = Student.objects.raw("SELECT id,marks FROM testapp_student order by marks desc limit 2")
    #emp = Student.objects.raw("SELECT id,%s FROM testapp_student limit %s",[name,lmt])
    #emp = Student.objects.raw("SELECT testapp_student.id,testapp_student.name, testapp_emp.marks FROM testapp_student LEFT JOIN testapp_emp ON testapp_student.marks=testapp_emp.marks")
    emp1 = Student.objects.distinct().values('marks')
    #emp = Student.objects.raw("SELECT id,COUNT(DISTINCT('name')) FROM testapp_student")
    emp=Student.get_students().aggregate(maxprice=Max('marks',output_field=IntegerField()) - Avg('marks',output_field=IntegerField()))
    emp2=Student.objects.annotate(num_marks=Min('marks'),num_marks2=Max('marks'))
    #emp=Student.objects.select_related('name')
    #emp=Student.objects.order_by('marks')[lmt]
    #emp3=Student.objects.raw("select id, name from testapp_student")
    emp3=Student.objects.all().values('name').distinct()
    return render(request,'jointable.html',{'result':emp['maxprice'],'result2':emp1,'result3':emp2,'result4':emp3})







def home1(request):
    print(request.user.is_authenticated)
    student=Student.objects.all()
    max_marks=Student.objects.all().aggregate(Sum('marks'))
    submarks = Student.objects.get(id=1)
    AvgMarks= Student.objects.order_by('-marks')[2]
    name=AvgMarks.name
    filname=Student.objects.filter(name__startswith='s')

    duplicates = Student.objects.values(
        'name'
    ).annotate(name_count=Count('name')).filter(name_count__gt=1)

    records=Student.objects.values('name').distinct()

    max_id = Student.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)

    randname=Student.objects.get(pk=pk).name
    Emps=Emp.objects.all()

    counting=Student.objects.all().count()


    return render(request,'home.html',{'student':student,'max_marks':max_marks,'submarks':submarks,'AvgMarks':AvgMarks,
                                       'name':name,'filname':filname,'duplicates':duplicates,'records':records,'randname':randname,
                                       'counting':counting,'Emps':Emps})
import random
from testapp.models import Company
from django.utils.crypto import get_random_string

def iftest(request):
    companylist = Company.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        number = request.POST['number']
        randnum = get_random_string(8, '0123456789')
        error=None
        if Company.objects.filter(number=number):
            error = "we found number Exist"
            return render(request, 'iftest.html', {'company': companylist, "error": error})
        elif Company.objects.filter(name=name):
            error = "we found name Exist"
            return render(request, 'iftest.html', {'company': companylist, "error": error})
        else:
            comp=Company(name=name,number=number,randnum=randnum).save()
            return render(request,'iftest.html',{'company':companylist})

    else:
        return render(request,'iftest.html',{'company':companylist})


from django.shortcuts import render, redirect
from django.http import HttpResponse


def test(request):
    breakfast = Student.objects.get(name='jagadeesh')

    # Direct access
    friendpost = Post.objects.filter(stupost=breakfast).get(id=3)
    return render(request,'test.html',{'friendpost':friendpost})


# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        id=request.session['id']
        data=Student.objects.get(id=id)
        stuid=data.id
        stumarks=data.marks
        friendlist = Friendlist.objects.filter(friend=data)
        friendlist1 = Friendlist.objects.filter(friend=data)
        for friendlist1 in friendlist1:
            friendid=friendlist1.friendid
            print(friendid)
            friendpost = Student.objects.get(id=friendid)




        #param = {'current_user': current_user,'stuid':stuid,'stumarks':stumarks,'post':data,'friendlist':friendlist,'friendpost':friendpost}
        return render(request, 'base.html', {'current_user': current_user, 'stuid': stuid, 'stumarks': stumarks, 'post': data,
                 'friendlist': friendlist})
    else:
        return redirect('login')
    return render(request, 'base.html')





def login(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pwd = request.POST.get('password')

        check_user = Student.objects.filter(name=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            user=Student.objects.get(name=uname)
            request.session['id'] = user.id
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


def post(request):
    if request.method == 'POST':
        posttitle = request.POST.get('posttitle')
        postbody = request.POST.get('postbody')
        if 'user' in request.session:
            current_user = request.session['user']
            id = request.session['id']
            data = Student.objects.get(id=id)
            Post(post_title=posttitle,post_body=postbody,stupost=data).save()

            return redirect('home')
        return redirect('home')
    return render(request, 'post.html')

def updatepost(request,id):
    postupdate=Post.objects.get(id=id)
    postupdate.post_title="post title updated"
    postupdate.post_body = "post body updated"
    postupdate.save()
    return redirect('home')

def deletepost(request,id):
    Post.objects.get(id=id).delete()

    return redirect('home')




def testapi(request,id):
    student = Student.objects.all()
    try:
        student = Student.objects.get(id=id)
        stuname=student.name
        stumarks=student.marks
        studentdic={'name':stuname,'marks':stumarks}
        stujson=json.dumps(studentdic)
        return HttpResponse(stujson)
    except:
        studentdic = {'user': 'none', 'marks': 'none'}
        stujson=json.dumps(studentdic)
        return HttpResponse(stujson)

def testapiupdate(request,id):
    student = Student.objects.get(id=id)
    student.name="numbersonly"
    student.save()
    return HttpResponse("name updated successfully")

def testapical(request,id,id2,id3):
    sum=id+id2+id3
    return HttpResponse("your api code is : {code}".format(code=sum))



from django.views import View
class home2(View):
    def get(self,request):
        return render(request,'signin.html')

from django.http import JsonResponse

def sampleapiall(request):
    MAX_OBJECTS = 20
    polls = Student.objects.all()[:MAX_OBJECTS]
    #data = {"results": list(polls.values("id", "name", "password", "marks"))}
    data = list(polls.values("id", "name", "password", "marks"))
    return JsonResponse(data, safe=False)

def sampleapi(request,id):
    print(len(Student.objects.all()))
    objcount=len(Student.objects.all())
    if id<objcount+1:
        polls = Student.objects.filter(id=id)
        data = {"results": list(polls.values("id","name", "password", "marks"))}
        return JsonResponse(data,safe=False)
    else:
        status={'status':"user does not exist"}
        data=json.dumps(status)
        return JsonResponse(data,safe=False)
def samplepost(request,name,password,marks):
    stu=Student(name=name,password=password,marks=marks).save()
    status = {'status': "post data successfully"}
    data = json.dumps(status)
    return JsonResponse(data, safe=False)

def samplepostdelete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    status = {'status': "post deleted successfully"}
    data = json.dumps(status)
    return JsonResponse(data, safe=False)

def samplepostupdate(request,id,name,password,marks):
    student=Student.objects.get(id=id)
    student.name=name
    student.password=password
    student.marks=marks
    student.save()
    status = {'status': "post updated successfully"}
    data = json.dumps(status)
    return JsonResponse(data, safe=False)


def hotelapiall(request):
    MAX_OBJECTS = 20
    polls = Hotel.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("id", "name", "file"))}
    return JsonResponse(data)

def hotelimage(request):
    polls = Hotel.objects.get(id=1)
    hotelcount = Student.objects.all().count()
    pic=polls.file.path
    return render(request,'hotelimage.html',{'hotelimage':polls,'pic':pic,'hotelcount':hotelcount})




#========================Class Based Views========================================================
from rest_framework.views import APIView, View
from .serializer import MoviesSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

class MovieApi(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            saved_movie = get_object_or_404(Hotel.objects.all(), pk=pk)
            serializer = MoviesSerializer(saved_movie)
            return Response({"Movie": serializer.data})

        movies = Hotel.objects.all()
        movies = MoviesSerializer(movies, many=True)
        return Response({'Movies': movies.data})
        # return HttpResponse({'Movies': movies.data})

    def post(self, request):

        serializer = MoviesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        parser_class = (FileUploadParser,)
        movie = get_object_or_404(Hotel.objects.all(), pk=pk)
        serializer = MoviesSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            movie_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(movie_saved.movie_name)})

    def delete(self, request, pk):
        # Get object with this pk
        movie = get_object_or_404(Hotel.objects.all(), pk=pk)
        movie.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)

class StudentApi(APIView):
    def get(self,request,**kwrgs):
        if kwrgs.get('pk'):
            pk=kwrgs.get('pk')
            studentdata=get_object_or_404(Student.objects.all(),pk=pk)
            stusepdata=StudentSerializer(studentdata)
            return Response({'studentdata':stusepdata.data})
        student=Student.objects.all()
        studata=StudentSerializer(student,many=True)
        return Response({'Studata':studata.data})
    def post(self,request):
        stuserializedata=StudentSerializer(data=request.data)
        if stuserializedata.is_valid():
            stuserializedata.save()
            return Response(stuserializedata.data, status=status.HTTP_201_CREATED)
        return Response(stuserializedata.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        student=get_object_or_404(Student.objects.all(),pk=pk)
        stuupdateseralizer=StudentSerializer(instance=student,data=request.data,partial=True)
        if stuupdateseralizer.is_valid(raise_exception=True):
            stuupdate=stuupdateseralizer.save()
        return Response({"success":"Article '{}' updated successfully".format(stuupdate.name)})
    def delete(self,request,pk):
        student=get_object_or_404(Student.objects.all(),pk=pk)
        student.delete()
        return Response({"status":"deleted successfully"})

from .forms import StudentRegistration,StudentForm1
from django.contrib import messages
from testapp.models import Student,Submarks,Emp,Post,Friendlist,Hotel,Contactor
from django.db.models import Q
from django.db.models import Avg,Min,Max,Count

def StudentForm(request):
    #stu=Student.objects.all()
    #stu = Student.objects.filter(marks=550)
    #stu = Student.objects.exclude(marks=550)
    #stu = Student.objects.order_by('name')
    #stu = Student.objects.order_by('id').reverse()[0:5]
    #stu = Student.objects.all()[0:5]
    #stu = Student.objects.values()
    #stu = Student.objects.values('id','name')
    q1 = Student.objects.values_list('id','name',named=True)
    q2=Emp.objects.values_list('id','name',named=True)
    #stu=q2.union(q1)
    #stu = q2.intersection(q1)
    #stu = q2.difference(q1)
    #stu = Student.objects.filter(marks=500)&Student.objects.filter(id=10)
    #stu=Student.objects.filter(Q(id=10)&Q(marks=500))
    #stu = Student.objects.filter(Q(id=10) | Q(marks=500))
    #stu = Student.objects.get(pk=6)
    #stu = Student.objects.first()
    #stu=Student.objects.order_by('name').first()
    #stu = Student.objects.last()
    # stu = Student.objects.latest('join_date')
    #stu = Student.objects.earliest('join_date')
    #stu = Student.objects.order_by('name').last()
    #stu = Student.objects.create(name='shivaji',password=125687,marks=564) it won't create return values, it is functioning value
    #stu = Student.objects.filter(id=6).update(name='updated',marks='1000') it won't create return values, it is functioning value
    #stu = Student.objects.get_or_create(name='kadhar', marks='900') it won't create return values, it is functioning value
    #stu = Student.objects.update_or_create(id=6,name='kadhar', marks='900',default={'name':'updated'})
    """obj=[
        Student(name='p',password='12345',marks=680),
        Student(name='q', password='12645', marks=670),
        Student(name='r', password='12845', marks=660),
        Student(name='e', password='12945', marks=650),
        Student(name='t', password='12745', marks=640),
    ]
    stu = Student.objects.bulk_create(obj)"""
    """stu1=Student.objects.all()
    for stu2 in stu1:
        stu2.password='12345'
    stu=Student.objects.bulk_update(stu1,['password'])"""

    #stu = Student.objects.get(id=6)
    #stu1=Student.objects.all()
    #count = stu1.count()
    #Student.objects.get(id=10).delete()

    #stu = Student.objects.filter(name__exact='shivaji')
    #stu = Student.objects.filter(name__contains='v')
    #stu = Student.objects.filter(name__contains='va')
    #stu = Student.objects.filter(name__startswith='v')
    #stu = Student.objects.filter(name__istartswith='k')
    #stu = Student.objects.filter(name__endswith='i')

    #stu = Student.objects.filter(id__in=[1,10,12])
    #stu = Student.objects.filter(marks__in=[550,660])
    #stu = Student.objects.filter(marks__gt=550)
    #stu = Student.objects.filter(marks__gte=550)
    #stu = Student.objects.filter(marks__lt=550)
    #stu = Student.objects.filter(marks__lte=550)

    #stu = Student.objects.filter(passdate__range=('2020-10-02','2020-12-31'))
    #stu = Student.objects.filter(passdate__year=2020)
    # stu = Student.objects.filter(passdate__year__gt=2020)
    # stu = Student.objects.filter(passdate__year__gte=2020)
    # stu = Student.objects.filter(passdate__month=4)
    #stu = Student.objects.filter(passdate__month__gt=4)
    # stu = Student.objects.filter(passdate__month__gte=4)
    # stu = Student.objects.filter(passdate__day=10)
    # stu = Student.objects.filter(passdate__day__gt=10)
    # stu = Student.objects.filter(passdate__day__gte=10)
    # stu = Student.objects.filter(passdate__week=10)
    # stu = Student.objects.filter(passdate__week__day=10)
    # stu = Student.objects.filter(passdate__quarter=10)
    #stu = Student.objects.filter(passtime__time=time(10,20))
    # stu = Student.objects.filter(passtime__time__gt=time(10,20))
    # stu = Student.objects.filter(passtime__hour=5)
    # stu = Student.objects.filter(passtime__minute=5)
    #stu = Student.objects.filter(password__isnull=False)

    #Avg=stu.aggregate(Max('marks'))

    #stu = Student.objects.all()[0:5]
    #stu = Student.objects.all()[5:9]

    from datetime import date
    # stu = Student.objects.filter(admitdate__date=date(2020,1,12))
    obj = [
        Contactor(name='p', age=28,salary=2000),
        Contactor(name='g', age=28,salary=6000),
        Contactor(name='f', age=28,salary=5000),
        Contactor(name='n', age=28,salary=7000),
        Contactor(name='l', age=28,salary=9000),
    ]

    stu=Contactor.objects.bulk_create(obj)

    context={'stu':stu}
    #print(stu)
    return render(request,'form.html',context)
    #return HttpResponse({'list':stu})

def getcookie(request):

        return render(request,'getcookie.html')

from django.contrib.auth.models import User,auth

def CreateUser(request):
    username='srinivas'
    password='Srinu@123'
    fname='srinivas'
    lname='putta'
    email='srinivas@gmail.com'
    User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password).save()
    return HttpResponse('user created successfully')



