from django.shortcuts import render,HttpResponse,redirect
from .models import UserModel, CartModel, CarModel,Biddings,bids
from django.contrib import messages
from datetime import datetime 

def nav(request):
    return render(request,"base.html")
def Home(request):
    home_obj=CarModel.objects.all()
    return render(request,"home.html",{"Data":home_obj})


def signup(request):
    if request.method =="GET":                                              
        return render(request,"registration.html")
    elif request.method =="POST":
        signup_first_name=request.POST.get("first_name")
        signup_user_name=request.POST.get("User_name")
        signup_mail=request.POST.get("e_mail")
        signup_password=request.POST.get("password")

        if signup_first_name=="":
          messages.error(request,"Enter your name")
          return render(request,"registration.html")
        elif signup_user_name=="":
           messages.error(request,"Enter User name")
           return render(request,"registration.html")
        elif signup_mail=="":
            messages.error(request,"Enter E-mail")
            return render(request,"registration.html")
        elif signup_password=="":
           messages.error(request,"Enter Password")
           return render(request,"registration.html")
        else:
            registration_obj=UserModel(first_name=signup_first_name,
            user_name=signup_user_name,
            mail=signup_mail,
            password=signup_password,
            phnum=0000)
            registration_obj.save()
            return render(request,"login.html")   

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method =="POST":
        mail=request.POST.get("mail")
        password=request.POST.get("Login_password")
        user_form_db=UserModel.objects.filter(mail=mail).first()

        if user_form_db is not None:
            if user_form_db.password== password:
                request.session["mail"]=mail
                request.session["password"]=password
                request.session["user_id"]= user_form_db.user_id
                return redirect("home")
            else:
                messages.error(request,"Incorect E-mail or pasword") 
                return render(request,"login.html") 
                
        else:
             messages.error(request,"Incorect E-mail or pasword") 
             return render(request,"login.html")   

def logout(request):
    request.session.clear()
    return render(request,"login.html")

def view(request):
    return render(request,"new1.html")
def home(request):
    return render(request, 'new1.html')  

def view(request):
    return render(request,"view_info_item.html")
      
def view_items(request,ides):
    ides=int(ides)
    print(ides)
    one_person=CarModel.objects.get(pk=ides)
    return render(request,"view_info_item.html",{'data':one_person})
  
def add(request):
    return render(request, 'add_info.html')
def Register(request):
    if request.method =="GET":
        return render(request, 'add_info.html')   
    elif request.method == "POST":
        Model=request.POST.get("CarModel")
        Engine=request.POST.get("Engine")
        Year=request.POST.get("Year")
        Color=request.POST.get("Color")
        OrginalPrice=request.POST.get("OrginalPrice")
        StartingPrice=request.POST.get("StartingPrice")
        FuelType=request.POST.get("FuelType")
        FuelEfficiency=request.POST.get("FuelEfficiency")
        Features=request.POST.get("Features")
        Safety=request.POST.get("Safety")
        InsuranceValidDate=request.POST.get("InsuranceValidDate")
        PUCCValidDate=request.POST.get("PUCCValidDate")
        FitnessValidDate=request.POST.get("FitnessValidDate")
        frount_image=request.FILES['frount_image']
        finishing_time=request.POST.get("finishing_time")
        input_datetime = datetime.strptime(finishing_time, "%Y-%m-%dT%H:%M")
        seller_id=request.session["user_id"]

        InfoOfCar_obj=CarModel( Model = Model,
            Engine = Engine,
            Year = Year,
            Color = Color,
            OrginalPrice = OrginalPrice,
            StartingPrice=StartingPrice,
            FuelType = FuelType,
            FuelEfficiency = FuelEfficiency,
            Features = Features,
            Safety = Safety,
            InsuranceValidDate = InsuranceValidDate,
            PUCCValidDate = PUCCValidDate,
            FitnessValidDate = FitnessValidDate,
            frount_image=frount_image,
            finishing_time=input_datetime,
            seller_id=seller_id )
       
        InfoOfCar_obj.save()
        car_id=(InfoOfCar_obj.car_id)
        
        bidding_obj=Biddings(seller_id=seller_id,seller_startig_bid=StartingPrice,
                             starting_bid_time=input_datetime,car_id=car_id)
        bidding_obj.save()
        return redirect('home')

def home(request):
       
        full_info=CarModel.objects.all()
        info={"key":full_info}
        return render(request, 'new1.html',info)
    
def myitems(request):
    user_id=request.session["user_id"]
    CarModel_obj=CarModel.objects.filter(seller_id=user_id)
    dis={"key":CarModel_obj}
    return render(request,"saved_items_list.html",dis)

def usersaved(request,carid):
    carid=int(carid)
    user_id=request.session["user_id"]
    cart_model_obj=CartModel.objects.filter(car_id=carid).first()
    if cart_model_obj is None: 
        Cart_obj=CartModel(user_id= user_id, car_id= carid)
        Cart_obj.save()
        return redirect('home')
    else:
        res=f"""
        <script>
        window.alert("The item is already saved")
        window.location.href='/home '
        </script>"""
        return HttpResponse(res)

def cartlist(request):
    user_id=request.session["user_id"]
    cartlist_obj=CartModel.objects.filter(user_id=user_id)
    CardDataList= []
    for i in cartlist_obj:
        carid=(i.car_id)
        print("fdf")
        carmodel_obj=CarModel.objects.get(pk=carid)
        print("")
        CardData={
            "car_id":carmodel_obj.car_id,
            "Model":carmodel_obj.Model,
            "Features":carmodel_obj.Features,
            "frount_image":carmodel_obj.frount_image,
            "user_id":user_id
            } 
        CardDataList.append(CardData)
    return render(request,"user_saved_item_list.html",{"Data": CardDataList})

def liveauction(request):
    return render(request,"live_auction.html")


def bidding(request,carid,value=None):
        CardDataList= []
        sold="Avaliable"
        carmodel_obj=CarModel.objects.get(pk=carid)
        now_time=datetime.now()
        date1=now_time.date()
        date2=carmodel_obj.finishing_time.date()
        print(date1,date2)
        if date1 < date2:
            print("time avaliable")
            if value == None:
                print("1")
                CardData={
                "car_id":carmodel_obj.car_id,
                "Model":carmodel_obj.Model,
                "Features":carmodel_obj.Features,
                "frount_image":carmodel_obj.frount_image,
                "current_bid":carmodel_obj.StartingPrice,
                "time":carmodel_obj.finishing_time,
                 "status":sold
                } 
            else:   
                CardData={
                "car_id":carmodel_obj.car_id,
                "Model":carmodel_obj.Model,
                "Features":carmodel_obj.Features,
                "frount_image":carmodel_obj.frount_image,
                "current_bid":value,
                "time":carmodel_obj.finishing_time,
                 "status":sold
                } 

        elif date1 == date2:
            if value == None:
                CardData={
                "car_id":carmodel_obj.car_id,
                "Model":carmodel_obj.Model,
                "Features":carmodel_obj.Features,
                "frount_image":carmodel_obj.frount_image,
                "current_bid":carmodel_obj.StartingPrice,
                "time":carmodel_obj.finishing_time,
                 "status":sold
                } 
            else:
                CardData={
                "car_id":carmodel_obj.car_id,
                "Model":carmodel_obj.Model,
                "Features":carmodel_obj.Features,
                "frount_image":carmodel_obj.frount_image,
                "current_bid":value,
                "time":carmodel_obj.finishing_time,
                 "status":sold
                } 
        else:
            print("time not avaliable")
            sold="Not Avaliable"
            CardData={
                "car_id":carmodel_obj.car_id,
                "Model":carmodel_obj.Model,
                "Features":carmodel_obj.Features,
                "frount_image":carmodel_obj.frount_image,
                "current_bid":carmodel_obj.StartingPrice,
                "time":carmodel_obj.finishing_time,
                "status":sold
                } 

        CardDataList.append(CardData)
        return render(request,"live_auction.html",{"Data": CardDataList})
 
def increase(request,carid,amt,num):
    print(carid,num,amt)
    carid=int(carid)
    num= int(num)
    amt=int(amt)
    # print(carid,num,amt)
    user_id=request.session["user_id"]
    user_obj=UserModel.objects.filter(user_id=user_id).first()
    userName=user_obj.user_name
    bids_obj=bids.objects.filter(car_id=carid).first()
    if bids_obj is None:
        first_add=bids(bidding_user=userName,last_bidding_total=amt+num,car_id=carid)
        value=amt+num
        first_add.save()
        return redirect("bids",carid,value)
    
    else:
        value=bids_obj.last_bidding_total
        bids_obj.last_bidding_total=value+num
        value=bids_obj.last_bidding_total
        bids_obj.save()
        return redirect("bids",carid,value)
    
    
def time(request):
    ti=datetime.now()
    print(ti)

def Viewprofile(request):
        user_id=request.session["user_id"]
        usermodel_obj=UserModel.objects.get(pk=user_id)
        if usermodel_obj.userImage is None:

            pass
        else:
            return render(request,"view_user_profile.html",{"data":usermodel_obj})
        
def Editprofile(request):
    if  request.method =="GET":
        user_id=request.session["user_id"]
        usermodel_obj=UserModel.objects.get(pk=user_id)
        return render(request,"edit_profile.html" ,{"data":usermodel_obj})
    elif request.method =="POST":
        user_id=request.session["user_id"]
        user_profile_edit=UserModel.objects.filter(user_id=user_id).first()
        if user_profile_edit is  None:
            pass   
        else:
            UserImage=request.FILES['user_image']
            Firstname=request.POST.get("first_name")
            user_name=request.POST.get("user_name")
            address=request.POST.get("address")
            gmail=request.POST.get("gmail")
            phnum=request.POST.get("phnum")
            user_profile_edit.first_name=Firstname
            user_profile_edit.user_name= user_name
            user_profile_edit.mail= gmail
            user_profile_edit.phnum= phnum
            user_profile_edit.address=address
            user_profile_edit.userImage=UserImage

            user_profile_edit.save()
        
            return redirect("home" )
        
def sellerInfo(request,carid):
    carid=int(carid)
    carinfo=CarModel.objects.filter(car_id=carid).first()
    user=carinfo.seller_id
    user=int(user)
    user_info=UserModel.objects.filter(user_id=user).first()
    print(user_info)
    return render(request,"view_user_profile.html",{"data":user_info})

def user_items(request,user_id):
    user_id=int(user_id)
    user_items_obj=CarModel.objects.filter(seller_id=user_id)
    return render(request,"view_profile_items.html",{"data":user_items_obj})

def search(request):
    searchWord=request.POST.get("searchWord")
    car_model=CarModel.objects.filter(Model=searchWord)
    return render(request,"search_cars.html",{"Data":car_model})

def carstatus(request):
    return HttpResponse("ok")

def car_status(request, carid):
    carid=int(carid)
    carinfo=CarModel.objects.filter(car_id=carid).first()
    bidding_obj=bids.objects.filter(car_id=carid).first()
    userid=bidding_obj.bidding_user

    cardata={
        "model":carinfo.Model,
        "Features":carinfo.Features,
        "frount_image":carinfo.frount_image,
        "Finishing_bid":bidding_obj.last_bidding_total,
        "User":bidding_obj.bidding_user,
        "time":carinfo.finishing_time,
    }

    return render(request,"car_status.html",{"Data":cardata})

def delete(request,carid):
    carid= int(carid)
    cart_obj=CartModel.objects.filter(car_id=carid).first()
    print(cart_obj)
    cart_obj.delete()
    return render(request,"view_profile_items.html")


def item_delete(request,carid):
    carid= int(carid)
    print(carid)
    carinfo=CarModel.objects.filter(car_id=carid).first()
    carinfo.delete()
    return redirect("home")

def about(request):
    return render(request,"about_us.html")
# 11111111111111111111 admin
def admin_user_delet(request,userid):
    userid=int(userid)
    user_info=UserModel.objects.get(pk=userid)
    user_info.delete()
    return render(request,"user_list.html")
    
def admin_user(request):
    user_info=UserModel.objects.all()
    return render(request,"user_list.html",{"data":user_info})
def admin_user_info(request,userid):
    userid=int(userid)
    user_info=UserModel.objects.filter(user_id=userid).first()
    return render(request,"view_user_profile.html",{"data":user_info})
# def admin_home()