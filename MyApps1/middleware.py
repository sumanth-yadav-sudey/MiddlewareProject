class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!! for ExecutionFlowMiddleware")
        self.get_response = get_response
    def __call__(self, request):
        print('This line added by __call__ at pre-processing of before-view-request')
        response = self.get_response(request)
        print('This line added by __call__ at post-processing of after-view-response')
        return response

from django.http import HttpResponse
class AppMaintananceMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called...for AppMaintananceMiddleware");
        self.get_response = get_response
    def __call__(self, request):
        return HttpResponse('<h1>Currently Application under maintenance...<br /><br />Plz try after 6am..!!</h1><hr />')

from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        print("init() is called for error-app ErrorMessageMiddleware");
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self, request, exception):
        print("Server is printing exception")
        return HttpResponse('<h1> Currently we are facing some technical problems..(Exception)<br/><br /> plz try after some time !!!</h1><hr /><h2>Raised Exception:{}</h2><h3>Exception Message : {}</h3>'.format(exception.__class__.__name__, exception));


class FirstMiddleware(object):
    def __init__(self, get_response):
        print("init() executed for FirstMiddleware")
        self.get_response = get_response
    def __call__(self, request):
        print('This line printed by FirstMiddleware at pre-processing of request');
        response = self.get_response(request)
        print('This line printed by FirstMiddleware at post-processing of request')
        return response;

class SecondMiddleware(object):
    def __init__(self, get_response):
        print("init() executed for SecondMiddleware")
        self.get_response = get_response
    def __call__(self, request):
        print('This line printed by SecondMiddleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by SecondMiddleware at post-processing of request')
        return response

