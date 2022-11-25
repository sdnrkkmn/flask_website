from flask import Flask,render_template,flash,redirect,url_for,session,request,logging,Response
from flask_mysqldb import MySQL
from flask_uploads import configure_uploads,IMAGES, UploadSet
#from flask_wtf import FlaskForm
#from flask_wtf.file import FileField,FileRequired,FileAllowed
#import urllib.request
from werkzeug.utils import secure_filename
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
import os
import time

app = Flask(__name__)
app.secret_key="makromaden"
UPLOAD_FOLDER = 'uploads/image'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGHT']=16*1024*1024
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
app.config['UPLOADED_IMAGES_DEST']='uploads/image'

images=UploadSet('images',IMAGES)
configure_uploads(app,images)

class RegisterForm(Form):
    name=StringField("İsim Soyisim",validators=[validators.Length(min=6, max=30)])
    username = StringField("Kullanıcı adı",validators=[validators.Length(min=6, max=30)])
    email = StringField("E posta",validators=[validators.Email(message="Lütfen geçerli bir Email adresi giriniz...")])
    password = PasswordField("Parola",validators=[
        validators.DataRequired("Lütfen bir parola belirleyiniz"),
        validators.length(min=8),
        validators.EqualTo(fieldname="confirm",message="Parolanız Uyuşmuyor")        
    ])
    confirm=PasswordField("Parola Doğrula")

class LoginForm(Form):
    username=StringField("Kullanıcı adı")
    password=PasswordField("Parola")
    

class ProductForm(Form):
    title=StringField("Başlık",validators=[validators.Length(min=6, max=75)])
    category=StringField("Kategori",validators=[validators.Length(min=3, max=25)])
    content=TextAreaField("İçerik",validators=[validators.Length(min=8)])
    #image= FileField(
    #    validators=[
    #        FileAllowed(images, 'Only images are allowed'),
    #        FileRequired('File field should not be empty')
    #    ]
    #    )
    stock =StringField("Stok Durumu")
    price =StringField("Fiyatı")
class EditForm(Form):
    title=StringField("Başlık",validators=[validators.Length(min=6, max=75)])
    content=TextAreaField("İçerik",validators=[validators.Length(min=8)])

class SpecialOrderForm(Form):
    name = StringField("Başlık",validators=[validators.Length(min=6, max=75)])
    content=TextAreaField("İçerik",validators=[validators.Length(min=8)])
class CartOKForm(Form):
    name=StringField("İsim ",validators=[validators.Length(min=6, max=30)])
    surname = StringField("Soyisim",validators=[validators.Length(min=6, max=30)])
    adress = StringField("Adres",validators=[validators.Length(min=6, max=100)])
    email = StringField("E posta",validators=[validators.Email(message="Lütfen geçerli bir Email adresi giriniz...")])
    phone_number = StringField("Telefon numarası",validators=[validators.Length(11)])
    cart_info =  StringField("Kredi Kartı Numarası",validators=[validators.Length(16)])


def login_required(f):
    @wraps(f)
    def decorator_function(*args,**kwargs):
        if "logged_in" in session:
            return f(*args,**kwargs)
        else:
            flash("Bu sayfayı görüntülemek için giriş yapmanız lazım...","danger")
            return redirect(url_for("login"))
    return decorator_function


#Db bağlantı konfigürasyonu başladı
app.config["MYSQL_HOST"] ="localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "makromaden"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
#Db bağlantı konfigürasyonu bitti

def gen():
    i = 0

    while True:
        time.sleep(5)
        images = get_all_images()
        image_name = images[i]
        im = open('images/' + image_name, 'rb').read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')
        i += 1
        if i >= len(images):
            i = 0

def get_all_images():
    image_folder = 'images'
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    return images

@app.route('/slideshow')
def slideshow():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/images")
def images():
    return render_template("images.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
        cursor = mysql.connection.cursor()
        sorgu="Select * from edit where id = 1" 
        result = cursor.execute(sorgu)
        if result > 0: 
            edit = cursor.fetchone() 
            return render_template("about.html",edit=edit) 
        else: 
            return render_template("about.html")
@app.route("/aboutedit",methods=["GET","POST"])
@login_required
def aboutedit():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from edit where id =1"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Böyle bir ürün yok ","danger")
            session.clear()
            return redirect(url_for("admin"))
        else:
            data=cursor.fetchone()
            form =EditForm()
            session["id"] = data["id"]
            form.title.data = data["title"]
            form.content.data = data["content"]
            return render_template("aboutedit.html",form = form)
    else:
        form = EditForm(request.form)
        newtitle = form.title.data
        newcontent = form.content.data
        sorgu2="Update edit Set title = %s,content = %s where id=1"
        cursor= mysql.connection.cursor()
        cursor.execute(sorgu2,(newtitle,newcontent))
        mysql.connection.commit()
        flash("Hakkımızda başarılı bir şekilde güncellendi","success")
        return redirect(url_for("admin"))


@app.route("/contact")
def contact():
        cursor = mysql.connection.cursor()
        sorgu="Select * from edit where id = 2" 
        result = cursor.execute(sorgu)
        if result > 0: 
            edit = cursor.fetchone() 
            return render_template("contact.html",edit=edit) 
        else: 
            return render_template("contact.html")
@app.route("/contactedit",methods=["GET","POST"])
@login_required
def contactedit():
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from edit where id =2"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Böyle bir ürün yok ","danger")
            session.clear()
            return redirect(url_for("admin"))
        else:
            data=cursor.fetchone()
            form =EditForm()
            session["id"] = data["id"]
            form.title.data = data["title"]
            form.content.data = data["content"]
            return render_template("contactedit.html",form = form)
    else:
        form = EditForm(request.form)
        newtitle = form.title.data
        newcontent = form.content.data
        sorgu2="Update edit Set title = %s,content = %s where id=2"
        cursor= mysql.connection.cursor()
        cursor.execute(sorgu2,(newtitle,newcontent))
        mysql.connection.commit()
        flash("İletişim başarılı bir şekilde güncellendi","success")
        return redirect(url_for("admin"))

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if(request.method=="POST" and form.validate()):
        name=form.name.data
        username=form.username.data
        email=form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        sorgu= "Insert into user(name,email,username,password) VALUES(%s,%s,%s,%s) "
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla kayıt oldunuz...","success")
        return redirect(url_for("login"))

    else:
        return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    if(request.method=="POST"):
        username=form.username.data
        password = form.password.data
        cursor = mysql.connection.cursor()
        sorgu= "Select * from user where username = %s"
        result=cursor.execute(sorgu,(username,))

        if result>0:
            data=cursor.fetchone()
            real_passw=data["password"]
            if sha256_crypt.verify(password,real_passw):
                flash("Başarılı giriş yaptınız..","success")
                session["logged_in"] = True
                session["username"] = username
                session["id"] = data["id"]
                session["email"] = data["email"]
                session["name"] = data["name"]
                if data["id"]==1:
                    return redirect(url_for("admin"))
                else:
                    session["id"] = data["id"]
                    return redirect(url_for("index"))
            else:
                flash("Parolanızı yanlış girdiniz","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor...","danger")
            return redirect(url_for("login"))

    return render_template("login.html",form=form)
@app.route("/product/<string:id>")
def product(id):
    cursor=mysql.connection.cursor()
    sorgu="Select * from product where id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        product = cursor.fetchone()
        return render_template("product.html",product=product)
    else:
        return render_template("product.html")  

@app.route("/admin",methods=["GET","POST"])
@login_required
def admin():
    return render_template("admin.html")

@app.route("/addproduct",methods=["GET","POST"])
@login_required
def addproduct():
    form=ProductForm(request.form)
    if request.method=="POST" and form.validate :
       
        title = form.title.data
        category = form.category.data
        content = form.content.data
        stock = int(form.stock.data)
        price = float(form.price.data)
        cursor = mysql.connection.cursor()
        sorgu="Insert into product (title,category,content,stock,price) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(title,category,content,stock,price))
        mysql.connection.commit()
        session["title"] = title
        session["stock"] = stock
        session["price"] = price
        cursor.close()
        flash("Ürün başarılı bir şekilde kaydedildi...","success")
        return redirect(url_for("dashboard"))
    return render_template("addproduct.html",form=form)
@app.route('/addproduct', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)
    image = request.files['file']
    if image.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('dashboard.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
@app.route("/deleteproduct/<string:id>")
@login_required
def delete(id):
    cursor=mysql.connection.cursor()
    sorgu="Select * from product where id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        sorgu2="Delete from product where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        flash("Ürün başarıyla silinmiştir.","success")
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir ürün yok ","danger")
        return redirect(url_for("dashboard"))
@app.route("/editproduct/<string:id>",methods=["GET","POST"])
@login_required
def edit(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        sorgu = "Select * from product where  id = %s  "
        result = cursor.execute(sorgu,(id,))
        if result == 0:
            flash("Böyle bir ürün yok ","danger")
            session.clear()
            return redirect(url_for("admin"))
        else:
            product=cursor.fetchone()
            form =ProductForm()
            form.title.data = product["title"]
            form.category.data = product["category"]
            form.content.data = product["content"]
            form.stock.data = product["stock"]
            form.price.data = product["price"]
            return render_template("update.html",form = form)
    else:
        form = ProductForm(request.form)
        newtitle = form.title.data
        newcategory = form.category.data
        newcontent = form.content.data
        newstock = form.stock.data
        sorgu2="Update product Set title = %s,category = %s, content = %s, stock = %s where id=%s"
        cursor= mysql.connection.cursor()
        cursor.execute(sorgu2,(newtitle,newcategory,newcontent,newstock,id))
        mysql.connection.commit()
        flash("Ürün Başarılı bir şekilde güncellendi","success")
        return redirect(url_for("dashboard"))

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from product "
    result = cursor.execute(sorgu)
    if result>0:
        products = cursor.fetchall()
        return render_template("dashboard.html",products=products)
    else:
        return render_template("dashboard.html")
@app.route("/products",methods=["GET","POST"])
def products():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from product "
    result = cursor.execute(sorgu)
    if result>0:
        products = cursor.fetchall()
        return render_template("products.html",products=products)
    else:
        return render_template("products.html")
@app.route("/products/bags",methods=["GET","POST"])
def bags():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from product where category = %s"
    result = cursor.execute(sorgu,("Çanta",))
    if result>0:
        products = cursor.fetchall()
        session["category"]=products[0]["category"]
        return render_template("bags.html",products=products)
    else:
        flash("Aradığınız kategori de ürünler bulunmamaktadır. Tüm ürünler listeleniyor.","warning")
        return redirect(url_for("products"))
    
@app.route("/products/home_product",methods=["GET","POST"])
def home_product():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from product where category = %s"
    result = cursor.execute(sorgu,("Ev Ürünleri",))
    if result>0:
        products = cursor.fetchall()
        session["category"]=products[1]["category"]
        return render_template("home_product.html",products=products)
    else:
        flash("Aradığınız kategori de ürünler bulunmamaktadır. Tüm ürünler listeleniyor.","warning")
        return redirect(url_for("products"))
            
@app.route("/products/sets",methods=["GET","POST"])
def sets():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from product where category = %s"
    result = cursor.execute(sorgu,("Kitler",))
    if result>0:
        products = cursor.fetchall()
        session["category"]=products[0]["category"]
        return render_template("sets.html",products=products)
    else:
        flash("Aradığınız kategori de ürünler bulunmamaktadır. Tüm ürünler listeleniyor.","warning")
        return redirect(url_for("products"))

@app.route("/cart",methods=["GET","Post"])
@login_required
def cart():
    if request.method =="POST":
        cursor = mysql.connection.cursor()
        sorgu="Select * from product " 
        result = cursor.execute(sorgu)
        if result > 0: 
            cart = cursor.fetchone()
            title = cart["title"]
            price = cart["price"]
            id = cart["id"]
            sorgu2 = "Insert into cart (id,title,price) values(%s,%s,%s)" 
            cursor.execute(sorgu2,(id,title,price))
            mysql.connection.commit()
            return render_template("cart.html",cart=cart)
        else: 
            return render_template("index.html")
    else:
        return render_template("cart.html")

@app.route("/cartdelete/<string:id>")
@login_required
def cartdelete(id):
    cursor=mysql.connection.cursor()
    sorgu="Select * from cart where id = %s"
    result = cursor.execute(sorgu,(id,))
    if result > 0:
        sorgu2="Delete from cart where id = %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("cart"))
    else:
        flash("Böyle bir ürün yok ","danger")
        return redirect(url_for("cart"))
@app.route("/costumermessages",methods=["GET","POST"])
def specialorder():
    cursor = mysql.connection.cursor()
    sorgu= "Select * from özelsipariş "
    result = cursor.execute(sorgu)
    if result>0:
        products = cursor.fetchone()
        return render_template("costumermesaj.html",products=products)
    else:
        return render_template("costumermesaj.html")
@app.route("/addmessages",methods=["GET","POST"])
@login_required
def addmessages():
    form=SpecialOrderForm(request.form)
    if request.method=="Post":
        name=form.name.data
        content = form.content.data
        cursor = mysql.connection.cursor()
        sorgu="Insert into özelsipariş (username,name,content) values(%s,%s,%s) " 
        cursor.execute(sorgu,(session["username"],name,content))
        mysql.connection.commit()
        flash("Siparişiniz satıcıya iletildi en kısa sürede fiyat bilgisi iletilecektir","success")
        return redirect(url_for("specialorder")) 
    return render_template("addmessages.html",form=form)  

@app.route("/adminmessages")
def order():
    cursor = mysql.connection.cursor()
    sorgu = "Select * from özelsipariş  "
    result=cursor.execute(sorgu)
    if result>0:
        products=cursor.fetchall()
        return render_template("adminmesaj.html",products=products)
    else:
        return render_template("adminmesaj.html")



@app.route("/search",methods=["GET","POST"])
def search():
    if request == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        sorgu = "Select * from product where title like '%" + keyword + "%' or content like '%" + keyword + "%'"
        result = cursor.execute(sorgu)
        if result == 0:
            flash("Aradığınız kelimeyi içeren ürün yok","warning")
            return redirect(url_for("products"))
        else:
            products=cursor.fetchall()
            return render_template("products.html",products=products)

@app.route("/cartok",methods=["Post","Get"])
def cartok():
    form=CartOKForm(request.form)
    if(request.method=="POST" and form.validate()):
        name=form.name.data
        surname=form.surname.data
        adress=form.adress.data
        phone_number=form.phone_number.data
        cart_info = sha256_crypt.encrypt(form.cart_info.data)
        cursor = mysql.connection.cursor()
        sorgu= "Insert into sipariş(name,surname,adress,email,phone_number,cart_info ) VALUES(%s,%s,%s,%s,%s,%s,%s) "
        cursor.execute(sorgu,(name,surname,adress,session["email"],phone_number,cart_info ))
        mysql.connection.commit()
        cursor.close()
        flash("Bilgileriniz iletiliyor...","success")
        return redirect(url_for("index"))

    else:
        return render_template("cartok.html",form=form)
    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('uploads', filename='image/' + filename), code=301)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ =="__main__":
    app.run(debug = True)