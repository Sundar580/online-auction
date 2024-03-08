from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login ,name="login"),
    path('sign_up',views.signup,name="signup"),
    path('log_out',views.logout,name ="logout"),
    path('home',views.Home,name="home"),
    path('add_info/',views.add ,name="add_info"),
    path('Register/',views.Register, name="register"),
    path('my_items/',views.myitems,name="myitems"),
    path('view_items/<str:ides>',views.view_items,name="view_items"),
    path('user_saved/ <str:carid>',views.usersaved,name="usersaved"),
    path("cartlist",views.cartlist, name="cartlist"),
    path('live_auction/',views.liveauction,name="liveauction"),
    path('live_bidding/<str:carid>',views.bidding,name="bidding"),
    path('live_biddings/<str:carid>,<str:value>',views.bidding,name="bids"),
    path('live_bids/<str:carid>,<str:amt>,<str:num>',views.increase,name="increase_bid"),
    path('time',views.time),
    path('seller_info/<str:carid>',views.sellerInfo,name="sellerInfo"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),
    path('viewUserProfile/',views.Viewprofile,name="viewProfile"),
    path('user_items/<str:user_id>',views.user_items,name="user_items"),
    path('sellerInfo/<str:carid>',views.sellerInfo,name="sellerInfo"),
    path('search/',views.search,name="search"), 
    path('car_status/<str:carid>',views.car_status,name="car_status"),
    path('delete/<str:carid>',views.delete,name="delete"),
    path('item_delete/<str:carid>',views.item_delete,name="item_delete"),
    path('about_us/',views.about,name="about"),
    # path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_user_list/',views.admin_user,name="admin_user"),
    path('admin_user_del/<str:userid>',views.admin_user_delet,name="admin_user_delet"),
    path('admin_user_info/<str:userid>',views.admin_user_info,name="admin_user_info"),
   

]

    
#
   