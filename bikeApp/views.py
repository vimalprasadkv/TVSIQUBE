from django.shortcuts import render,redirect
from .models import Cu_User,CustomUser,Iqube,Booking
from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    msg=""
    if request.POST:
        firstName=request.POST['fname']
        lastName=request.POST['lname']
        userName=request.POST['uname']
        password=request.POST['password']
        address=request.POST['address']
        mob=request.POST['phone']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        try:
            u=CustomUser.objects.create_user(username=userName,password=password,userType='Customer')
            u.save()
            user=Cu_User.objects.create(first_name=firstName,last_name=lastName,user_name=userName,password=password,address=address,mobile_number=mob,city=city,state=state,zip=zip,user=u)
            user.save()
        except:
            msg="Username already existed"
    return render(request,"regi.html",{"msg":msg})
def login_(request):
    msg=""
    if request.POST:
        uName=request.POST['uname']
        password=request.POST['password']
        user=authenticate(username=uName,password=password)
        if user is None:
            msg="Invalid login"
        else:
            login(request,user)
            if user.userType=="admin":
                request.session["id"]=user.id
                return redirect("/adminlogin")
            elif user.userType=="Customer":
                cust=Cu_User.objects.get(user_name=uName)
                request.session["id"]=cust.id
                return redirect("/customerlogin")

    return render(request,"login.html")
def adminlogin(request):
   
    return render(request,"adminlogin.html")
def customerlogin(request):
    custId=request.session["id"]
    if request.POST:
        firstName=request.POST['fname']
        customer=Cu_User.objects.get(id=custId)
        customer.first_name = firstName
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"customerlogin.html",{"cust":cust})
def spec(request):
    return render(request,"spec.html")
def color(request):
    vehicles=Iqube.objects.all()
    return render(request,"color.html",{"vehicles":vehicles})
def about(request):
    return render(request,"about.html")
def images(request):
    return render(request,"images.html")
@login_required(login_url='/')
def customer(request):
    user=Cu_User.objects.all()
    return render(request,"customer.html",{"usr":user})
@login_required(login_url='/')
def stockupdation(request):
    return render(request,"stockupdation.html")
@login_required(login_url='/')
def addvehicle(request):
    if request.POST:
        vehicle=request.POST['vmodel']
        vehicle_color=request.POST['vcolor']
        vehicle_desc=request.POST['vdesc']
        stock=request.POST['stock']
        rate=request.POST['rate']
        img=request.FILES['img']
        
        admin=Iqube.objects.create(vehicle=vehicle,vehicle_color=vehicle_color,vehicle_desc=vehicle_desc,stock=stock,rate=rate,status="Available",img=img)
        admin.save()
    return render(request,"addvehicle.html")
@login_required(login_url='/')
def bookingdetails(request):
    vehicles=Booking.objects.filter(status="pending")
    return render(request,"bookingdetails.html",{"vehicles":vehicles})
@login_required(login_url='/')
def approvereject(request):
    bid=request.GET['id']
    status=request.GET['status']

    bkg=Booking.objects.get(id=bid)

    
    bkg.status=status
    bkg.save()
    if status=="Approved":
        vid=bkg.vehicles.id
        veh=Iqube.objects.get(id=vid)
        stock=veh.stock
        sto=int(stock)-1
        veh.stock=sto
        veh.save()

    
    return redirect("/bookingdetails")
@login_required(login_url='/')
def viewvehicle(request):
    vehicles=Iqube.objects.all()
    return render(request,"viewvehicle.html",{"vehicles":vehicles})
@login_required(login_url='/')
def updateVeh(request):
    vid = request.GET['id']
    veh = Iqube.objects.get(id=vid)
    if request.POST:
        vehicle=request.POST['vmodel']
        vehicle_color=request.POST['vcolor']
        vehicle_desc=request.POST['vdesc']
        stock=request.POST['stock']
        rate=request.POST['rate']
        veh.vehicle=vehicle
        veh.vehicle_color=vehicle_color
        veh.vehicle_desc=vehicle_desc
        veh.rate=rate
        veh.stock=stock 
        veh.save()
        return redirect("/viewvehicle")
    return render(request, "updateVeh.html",{"veh":veh})
@login_required(login_url='/')
def profile(request):

    custId=request.session["id"]
    if request.POST:
        firstName=request.POST['fname']
        lastName=request.POST['lname']
        userName=request.POST['uname']
        address=request.POST['address']
        mob=request.POST['phone']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        customer=Cu_User.objects.get(id=custId)
        customer.first_name = firstName
        customer.last_name = lastName
        customer.user_name = userName
        customer.address = address
        customer.mobile_number =mob
        customer.city = city
        customer.state = state
        customer.zip = zip

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"profile.html",{"cust":cust})
def vehicle(request):
    vehicles=Iqube.objects.all()
    return render(request,"vehicle.html",{"vehicles":vehicles})
@login_required(login_url='/')
def booking(request):
    msg=""
    vid = request.GET['id']
    custId=request.session["id"]
    if request.POST:
        date=request.POST['date']
        id_proof=request.FILES['identity']
        cust=Cu_User.objects.get(id=custId)

        veh=Iqube.objects.get(id=vid)
        adm=Booking.objects.create(date=date,id_proof=id_proof,vehicles=veh,user=cust)
        adm.save()
        msg="Your Booking successfully"
    return render(request,"booking.html",{"msg":msg})

@login_required(login_url='/')
def logout_(request):
    if 'id' in request.session:
        request.session.flush()
    logout(request)
    return redirect('/')
@login_required(login_url='/')
def aprej(request):
    app=Booking.objects.filter(status="Approved")
    rej=Booking.objects.filter(status="Rejected")

    return render(request,"aprej.html",{"app":app,"rej":rej})
@login_required(login_url='/')

def status(request):
    
    custId=request.session['id']
    sta=Booking.objects.filter(user_id=custId)

    return render(request,"status.html",{"sta":sta})
def specc(request):
    return render(request,"specc.html")
def colorc(request):
    vehicles=Iqube.objects.all()
    return render(request,"colorc.html",{"vehicles":vehicles})
def imagesc(request):
    return render(request,"imagesc.html")
def aboutc(request):
    return render(request,"aboutc.html")
def aboutb(request):
    return render(request,"aboutc.html")
    
   