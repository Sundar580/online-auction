from django.db import models

# class UserSaved(models.Model):
   
class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=220)
    user_name=models.CharField(max_length=220)
    mail=models.CharField(max_length=220)
    password=models.CharField(max_length=100)
    phnum=models.IntegerField(max_length=20)
    address=models.CharField(max_length=800)
    userImage=models.ImageField(upload_to='images/')

class CarModel(models.Model):
    car_id=models.AutoField(primary_key=True)
    seller_id=models.IntegerField()
    Model=models.CharField(max_length=100)
    Engine=models.CharField(max_length=200)
    Year=models.CharField(max_length=100)
    Color=models.CharField(max_length=300)
    OrginalPrice=models.CharField(max_length=100)
    StartingPrice=models.CharField(max_length=100)
    FuelType=models.CharField(max_length=300)
    FuelEfficiency=models.CharField(max_length=300)
    Features=models.CharField(max_length=300)
    Safety=models.CharField(max_length=300)
    InsuranceValidDate=models.CharField(max_length=100)
    PUCCValidDate=models.CharField(max_length=100)
    FitnessValidDate=models.CharField(max_length=100)
    frount_image=models.ImageField(upload_to='images/')
    decription = models.TextField()
    checkBox=models.BooleanField(default=False)
    finishing_time=models.DateTimeField()
    starting_date= models.DateTimeField(auto_now_add=True)

class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    car_id=models.IntegerField()


# ------------------
class Biddings(models.Model):
   seller_id=models.IntegerField()
   seller_startig_bid=models.CharField(max_length=100)
   starting_bid_time=models.DateTimeField()
   car_id=models.IntegerField()
   

class bids(models.Model):
    bidding_user=models.CharField(max_length=220)
    last_bidding_total=models.IntegerField()
    car_id=models.IntegerField()
# ++++++++++++++++++++++++++++++++



