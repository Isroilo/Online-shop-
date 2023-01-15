from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Productphoto(models.Model):
    img=models.ImageField(upload_to='products_images/')


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Advantage(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Info(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    img = models.ManyToManyField(Productphoto,blank=True)
    tags = models.ManyToManyField(Tags,blank=True)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    bonus_persent = models.IntegerField(default=0)
    in_slider = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    is_recommended = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE) 
    advantage = models.ManyToManyField(Advantage,blank=True)
    info = models.ManyToManyField(Info,blank=True)

    def __str__(self):
        return self.name

# blog models
class Blogphoto(models.Model):
    img = models.ImageField(upload_to="blogphotos/")

class Blogs(models.Model):
    title = models.CharField(max_length=255)  
    text = models.TextField()  
    img = models.ManyToManyField(Blogphoto,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    reply_comment = models.ForeignKey('Comment', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username


class Adress(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Information(models.Model):
    logo = models.ImageField(upload_to="logo/")
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.ManyToManyField(Adress,blank=True)
    teleg = models.CharField(max_length=255)
    insta = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class Partner(models.Model):
    partner=models.ImageField(upload_to='partner/')


class Subscribers(models.Model):
    email = models.CharField(max_length=255) 


class Service(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="service_logo/")


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Card(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField() 



class Wishlist(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=255)      
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()    