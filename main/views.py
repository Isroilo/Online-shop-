from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from .serializer import *



@api_view(['GET'])
def category_view(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subcategory_view(request):
    category = request.GET.get("category")
    c = Subcategory.objects.filter(category=category)
    serializer = SubcategorySerializer(c, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_product_by_subcategory(request,pk):
    subcategory = Subcategory.objects.get(id=pk)
    product = Product.objects.filter(subcategory=subcategory)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def product_view(request):
    product = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def information_view(request):
    information = Information.objects.last()
    serializer = InformationSerializer(information)
    return Response(serializer.data)


@api_view(['GET'])
def service_view(request):
    service = Service.objects.all().order_by('-id')[:4]
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def faq_view(request):
    faq = Faq.objects.all()
    serializer = FaqSerializer(faq, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def partner_view(request):
    partner = Partner.objects.all()
    serializer = PartnerSerializer(partner, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_category(request,pk):
    category = Categoriya.objects.get(id=pk)
    product = Product.objects.filter(subcategory__category=category)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_product_by_subcategory(request,pk):
    subcategory = Subcategory.objects.get(id=pk)
    product = Product.objects.filter(subcategory=subcategory)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_product(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    subcategory = request.POST.get('subcategory')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    bonus_persent = request.POST.get('bonus_persent')
    brand = request.POST.get('brand')
    advantage = request.POST.getlist('advantage')
    info = request.POST.getlist('info')
    is_active = request.POST.get('is_active')
    img = request.FILES.getlist("img")
    tags = request.POST.getlist("tag")
    new_product =  Product.objects.create(
            name=name,
            description=description,
            subcategory_id=subcategory,
            brand_id=brand,
            quantity=quantity,
            price=price,
            bonus_persent=bonus_persent,
            is_active=is_active,
            )
    try:        
            for photo in img:
                img = Newsphoto.objects.create(
                        img=photo
                    )
                new_product.img.add(img)
                new_product.save()
    except:
        pass
    try:
            for tag in tags:
                tags=Tags.objects.create(
                    tags = tag
                )    
                new_product.tags.add(tags)
                new_product.save()
    except:
        pass     
    try:
            for i in info:
                info=Info.objects.create(
                    info = i
                )    
                new_product.info.add(info)
                new_product.save()
    except:
        pass
    try:
            for x in advantage:
                advantage=Advantage.objects.create(
                    advantage = i
                )    
                new_product.advantage.add(advantage)
                new_product.save()
    except:
        pass               
    return Response({"message":"create success"})


@api_view(['POST'])
def create_blog(request):
        title = request.POST['title']
        text = request.POST['text']
        is_active = request.POST['is_active']
        img = request.FILES.getlist('img')
        new_blog = Blogs.objects.create(
            title=title,
            text=text,
            is_active=is_active,
        )
        try:
            for photo in img:
                img = Blogphoto.objects.create(
                    img=photo
                )
                new_blog.img.add(img)
                new_blog.save()
        except:
            pass
        ser = BlogsSerializer(new_blog)
        return Response(ser.data)



@api_view(['GET'])
def blog_view(request):
    blog = Blogs.objects.all()
    serializer = BlogsSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_subscribers(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscribers = Subscribers.objects.create(
            email=email,
        )
        ser = SubscribersSerializer(subscribers)
        return Response(ser.data)


@api_view(['GET'])
def get_product(request,pk):
    product = Product.objects.get(id=pk)
    ser = ProductSerializer(product)
    return Response(ser.data)


@api_view(['GET'])
def get_blog(request,pk):
    blog = Blogs.objects.get(id=pk)
    ser = BlogsSerializer(blog)
    return Response(ser.data)


@api_view(['GET'])
def banner_view(request):
    product = Product.objects.filter(in_slider=True).order_by('-id')[:3]
    ser = ProductSerializer(product ,many=True)
    return Response(ser.data)


@api_view(['GET'])
def recomended_product_view(request):
    product = Product.objects.filter(is_recommended=True).order_by('-id')[:6]
    ser = ProductSerializer(product ,many=True)
    return Response(ser.data)


@api_view(['GET'])
def product_bunus_persent(request):
    product = Product.objects.filter(bonus_persent__gt=0)
    ser = ProductSerializer(bonus_products ,many=True)
    return Response(ser.data)



@api_view(['GET'])
def top_product_view(request):
    product = Product.objects.filter(is_top=True).order_by('-id')[:6]
    ser = ProductSerializer(product ,many=True)
    return Response(ser.data)        




@api_view(['POST'])
def create_comment(request,pk):
    blog = Blogs.objects.get(pk=pk)
    izox = request.POST['izox']
    Comment.objects.create(
                text=izox,
                user=request.user,
                blog=blog,
            )
    ser = CommentSerializer(Comment ,many=True)        
    return Response(ser.data)
    


@api_view(['POST'])
def reply_comment(request,pk):
    reply = request.POST['izox']
    blog = Blogs.objects.get(pk=pk)
    reply_comment=Comment.objects.get(pk=pk)
    Comment.objects.create(
        text=reply,
        user=request.user,
        blog=blog,
        reply_comment=reply_comment.user,
        )
    ser = CommentSerializer(Comment ,many=True)        
    return Response(ser.data)




@api_view(['GET'])
def adress_view(request):
    adress = Adress.objects.all()
    ser = AdressSerializer(adress, many=True)
    return Response(ser.data)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_card(request):
    user = request.user
    product = request.POST.get('product')
    quantity = request.POST.get('quantity')
    card = Card.objects.create(
        user = user,
        product_id = product,
        quantity = quantity
        )
    ser = CardSerializer(card)
    return Response(ser.data)



@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_card(request,pk):
    product = request.POST.get('product')
    quantity = request.POST.get('quantity')
    card = Card.objects.get(pk=pk)
    card.quantity = quantity
    card.product_id = product
    card.save()
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def card_view(request):
    user = request.user
    card = Card.objects.filter(user=user)
    ser = CardSerializer(card, many=True)
    return Response(ser.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()        
    return Response("Deleted succes")


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def card_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()        
    return Response("Deleted succes")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_wishlist(request):
    user = request.user
    product = request.POST.get('product')
    wishlist = Wishlist.objects.create(
        user = user,
        product_id = product
        )
    ser = WishlistSerializer(wishlist)
    return Response(ser.data)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_view(request):
    request.user
    wishlist = Wishlist.objects.filter(user=user)
    ser = WishlistSerializer(wishlist, many=True)
    return Response(ser.data)



@api_view(['POST'])
def signin_view(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usrs = User.objects.get(username=username)
            usr = authenticate(username=username, password=password)
            try:
                if usr is not None:
                    status = 200
                    token, created = Token.objects.get_or_create(user=usrs)
                    data = {
                        'username': username,
                        'user_id': usrs.id,
                        'token': token.key,
                    }
                else:
                    status = 403
                    message = " Username yoki parol noto'g'ri ! "    
                    data={
                        'status':status,
                        'message':message,
                    }
            except User.DoesNotExist:
                status = 404
                message = ' Bunday foydalanuvchi mavjud emas! '    
                data = {
                    'status': status,
                    'message': message,
                }       
            return Response(data)    
        except Exception as err:
            return Response(f'{err}')


@api_view(['POST'])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username=username,password=password,email=email)
    ser = UserSerializer(user)        
    return Response(ser.data)
    


def logout_view(request):
    logout(request)       
    return Response("logout")            


@api_view(['GET'])
def search_product_name(request):
    name = request.GET.get("name")
    product = Product.objects.filter(name__icontains=name)
    ser = ProductSerializer(product ,many=True)        
    return Response(ser.data)


@api_view(['POST'])
def filter_product_price(request):
    price = request.GET.get("price")
    product = Product.objects.filter(price__lt=price)
    ser = ProductSerializer(product,many=True)        
    return Response(ser.data) 



@api_view(['POST'])
def search_blog_name(request):
    title = request.GET.get("title")
    blog = Blogs.objects.filter(title__icontains=title)
    ser = BlogsSerializer(blog ,many=True)        
    return Response(ser.data)    


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    country = request.POST.get('country')
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    address = request.POST.get('address')
    address_1 = request.POST.get('address_1')
    city = request.POST.get('city')
    zipcode = request.POST.get('zipcode')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    order = Order.objects.create(
            user = user,
            country =country,
            f_name =f_name,
            l_name =l_name,
            address =address,
            address_1 =address_1,
            city =city,
            zipcode =zipcode,
            email =email,
            phone = phone
    )
    card = Card.objects.filter(user=user)
    for i in card:
        orderitem = OrderItem.objects.create(
            order = order,
            product = i.product,
            price = i.product.price,
            quantity = i.quantity,
            total = i.product.price*i.quantity
        )
        product = Product.objects.get(id=i.product.id)  
        product.quantity -= i.quantity
        product.save()
    card = Card.objects.filter(user=user).delete()
    ser = OrderSerializer(order)    
    return Response(ser.data)    




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_orderitem(request, pk):
    user = request.user
    order = Order.objects.get(pk=pk)
    if user.id == order.user.id:
        orderitems = OrderItem.objects.filter(order=order)   
        ser = OrderItemSerializer(orderitems,many=True)     
        return Response(ser.data)    
    else:
        return Response({"message" : "sizda bunday raqamli order mavjud emas"})    



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_client_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)   
    ser = OrderSerializer(orders,many=True)     
    return Response(ser.data)
