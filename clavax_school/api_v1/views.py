from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, StudentClass
from .serializers import StudentSerializers, ClassSerializers
from rest_framework import routers
from .forms import StudentClassForm, StudentForm

"""Class Based Video"""


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentAPI(APIView):
    def get(self, request):
        try:
            students = Student.objects.all()
            student_serializer = StudentSerializers(students, many=True)
            return Response({
                'status': 200,
                'data': student_serializer.data
            })
        except Exception as Err:
            print(F"Error in Get {Err}")
            return Response({
                'status': 404,
                'data': "Something Went Wrong"
            })

    def post(self, request):
        try:
            data = request.data
            print(data)
            serializer = StudentSerializers(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': 403,
                    'message': 'Something Went Wrong',
                    'error': serializer.errors
                })

            serializer.save()
            return Response(
                {
                    'status': 200,
                    'payload': serializer.data,
                }
            )
        except Exception as Err:
            print(F"Error in Get {Err}")
            return Response({
                'status': 404,
                'data': F"Invalid Entries {Err}"
            })

    def put(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            data = request.data

            serializer = StudentSerializers(student, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': 403,
                    'message': 'Something Went Wrong',
                    'error': serializer.errors
                })

            serializer.save()
            return Response(
                {
                    'status': 200,
                    'payload': serializer.data,
                    'message': 'Success'
                }
            )
        except Exception as Err:
            print(Err)
            return Response({'status': 403, 'message': 'Invalid Entries'})

    def patch(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            data = request.data

            serializer = StudentSerializers(
                student, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': 403,
                    'message': 'Something Went Wrong',
                    'error': serializer.errors
                })

            serializer.save()
            return Response(
                {
                    'status': 200,
                    'payload': serializer.data,
                    'message': 'Success'
                }
            )
        except Exception as Err:
            print(Err)
            return Response({'status': 403, 'message': F'Invalid Entries {Err}'})

    def delete(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            student.delete()
            return Response({
                'status': 200,
                'message': 'Deleted'
            })
        except Exception as e:
            print(F"Error is : {e}")
            return Response({'status': 403, 'message': 'Invalid ID'})


"""Function Based View"""

# GUI Pages


def home_page(request):
    return render(request, 'index.html')


def add_new_student(request):
    print('Request in add_class')
    if request.method == 'POST':
        print('Post Request')
        form = StudentForm(request.POST, request.FILES)
        print("Form Submitting Start")
        print(form)
        if form.is_valid():
            form.save()
            print("Form Is Saved")
            # return redirect('gui_student')

            return HttpResponse("Form Submited")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = StudentForm()
    return render(request, 'student_forms.html', {'form': form})


def add_new_class(request):
    status = 0  # Do Nothing
    print('Request in add_class')
    if request.method == 'POST':
        print('Post Request')
        form = StudentClassForm(request.POST)
        print("Form Submitting Start")
        if form.is_valid():
            form.save()
            print("Form Is Saved")

            return HttpResponse("Form Submited")
            status = 2  # Form Submited
        else:
            status = 1  # Form Failed

            return HttpResponse("Invalid Form")

    else:
        form = StudentClassForm()
    return render(request, 'class_form.html', {'form': form, 'status': status},)


# API View
@ api_view(['GET'])
def all_class(request):
    student_class = StudentClass.objects.all()
    class_serializer = ClassSerializers(student_class, many=True)
    return Response({
        'status': 200,
        'data': class_serializer.data
    })


@ api_view(['GET'])
def home(request):
    students = Student.objects.all()
    student_serializer = StudentSerializers(students, many=True)
    return Response({
        'status': 200,
        'data': student_serializer.data
    })


@ api_view(['POST'])
def add_student(request):
    data = request.data
    print(data)
    serializer = StudentSerializers(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({
            'status': 403,
            'message': 'Something Went Wrong',
            'error': serializer.errors
        })

    serializer.save()
    return Response(
        {
            'status': 200,
            'payload': serializer.data,
        }
    )


@ api_view(['PUT'])
def update_student(request, id):
    # data = request.data
    try:
        student = Student.objects.get(id=id)
        data = request.data

        serializer = StudentSerializers(student, data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                'status': 403,
                'message': 'Something Went Wrong',
                'error': serializer.errors
            })

        serializer.save()
        return Response(
            {
                'status': 200,
                'payload': serializer.data,
            }
        )
    except Exception as Err:
        return Response({'status': 403, 'message': 'Invalid Entries'})


@ api_view(['PATCH'])
def update_student_patch(request, id):
    # data = request.data
    try:
        student = Student.objects.get(id=id)
        data = request.data
        # Partial May Be Issue
        serializer = StudentSerializers(
            student, data=request.data, partial=True)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                'status': 403,
                'message': 'Something Went Wrong',
                'error': serializer.errors
            })

        serializer.save()
        return Response(
            {
                'status': 200,
                'payload': serializer.data,
            }
        )
    except Exception as Err:
        return Response({'status': 403, 'message': 'Invalid Entries'})


@ api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response({
            'status': 200,
            'message': 'Deleted'
        })
    except Exception as e:
        print(F"Error is : {e}")
        return Response({'status': 403, 'message': 'Invalid ID'})
