from django.http import HttpResponse 
# class AppMaintenanceMiddleware(object):
# class ErrorMessageMiddleware(object):
class FirstMiddleware(object):
    def __init__(self,get_response):
        print('init method execution')
        self.get_response=get_response

    def __call__(self,request):
        # print('preprocessing of request')
        print('This is printed by middleware-1 before processing request')
        response=self.get_response(request)
        # print('Post processing of request')
        print('This is printed by middleware-1 after processing request')
        return response
        # return HttpResponse('<h1>currently application under maitenance... kindly try in business hours</h1>')
 
class SecondMiddleware(object):
    def __init__(self,get_response):
        print('init method execution of second middleware')
        self.get_response=get_response

    def __call__(self,request):
        print('This is printed by middleware-2 before processing request')
        response=self.get_response(request)
        print('This is printed by middleware-2 after processing request')
        return response
        