from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"     

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__" 

class Product_PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productphoto
        fields = "__all__"            


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"  


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"  

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"  


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"  
        


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"   


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Blogs
        fields = "__all__" 


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = "__all__" 


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__" 



class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
        
class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = "__all__" 



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__" 



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__" 



class CardSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Card
        fields = "__all__"         


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Wishlist
        fields = "__all__"  



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = "__all__"  


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = OrderItem
        fields = "__all__"          