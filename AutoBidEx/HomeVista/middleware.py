from django.shortcuts import redirect
class CheckUser:
    exclude_path=["/","/sign_up",]

    def __init__(self,get_response):
        self.response=get_response

    def __call__(self,request):
        if request.path_info not in self.exclude_path:
            if "username" in request.session:
                if request.session["username"] !="":
                    response=self.response(request)
                    return response
                    
                else:
                    return redirect('login')
            else:
                return redirect("login")
                     
        else:
            if "username" in request.session:
                if request.session["username"] !="":
                        
                        response=self.response(request)
                        return response
                else:
                    response=self.response(request)
                    return response
            else:
                response=self.response(request)
                return response
                
