from django.shortcuts import render
import sqlite3
# Create your views here.
def index(request):
    return render(request, "bday/index.html")
def details(request):
    na=request.POST.get("t1")
    da=request.POST.get("t2")
    kanika=False
    ansh=False
    if (na=="Kanika" or na=="kanika") and da=="03/12":
        kanika=True
    if (na=="Ansh" or na=="ansh") and da=="14/01":
        ansh=True
    if kanika :
        return render(request,"bday/kannu.html")
    if ansh :
        return render(request,"bday/ansh.html")
    else:
        d={"l": "Wrong details"}
        return render(request,"bday/index.html",d)
def kanika(request):
    name=request.POST['name']
    com=request.POST['com']
    f=open("/media/comments.txt","a+")
    f.write(name)
    f.write(" : ")
    f.write(com)
    f.write(",\n")
    #f.seek(0)
    #read=f.read()
    f.close()
    #dic={"comment": read}
    db=sqlite3.connect("/media/comments.db")
    cursor=db.cursor()
    cursor.execute("INSERT INTO COMMENTS(NAME,COMMENT) VALUES(?,?)",(name,com))
    db.commit()
    db.close()
    return render(request, "bday/kanika.html")
def ansh(request):
    name=request.POST['name']
    com=request.POST['com']
    f=open("/media/kanika.txt","a+")
    f.write(name)
    f.write(" : ")
    f.write(com)
    f.write(",\n")
    #f.seek(0)
    #read=f.read()
    f.close()
    #dic={"comment": read}
    db=sqlite3.connect("/media/comments.db")
    cursor=db.cursor()
    cursor.execute("INSERT INTO COMMENTS(NAME,COMMENT) VALUES(?,?)",(name,com))
    db.commit()
    db.close()
    return render(request, "bday/ansh.html")