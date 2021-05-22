from app import app
from app.models import*
from app import db
import os
import random
from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import secure_filename

@app.route("/admin")
def admin_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    sliders=Slider.query.all()
    sliderbttns=SliderUrl.query.all()
    serviceheadings=ServiceTitle.query.all()
    serviceitems=ServiceItem.query.all()
    servicebttns=ServiceButton.query.all()
    reasonheadings=ServiceButton.query.all()
    reasonitems=ReasonItem.query.all()
    return render_template("admin/index.html",header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names, sliders=sliders, sliderbttns=sliderbttns,serviceheadings=serviceheadings, serviceitems=serviceitems , servicebttns=servicebttns, reasonheadings=reasonheadings, reasonitems=reasonitems)


# Header Contact Info start
@app.route("/admin/hcContactAdd", methods=['GET','POST'])
def hcContactAdd():
    header_contacts=HeaderContact.query.all()
    if request.method=='POST':
        header_contact=HeaderContact(
            hc_content=request.form['hc_content'],
            hc_icon_class=request.form['hc_icon_class'],
            hc_url=request.form['hc_url']
        )
        db.session.add(header_contact)
        db.session.commit()
        return redirect('/admin/hcContactAdd')
    return render_template("admin/hcContactAdd.html", header_contacts=header_contacts)

@app.route("/admin/hcContactUpdate/<id>",methods=['GET','POST'])
def hcContactUpdate(id):
    header_contact=HeaderContact.query.get(id)
    if request.method=='POST':
        header_contact.hc_content=request.form['hc_content']
        header_contact.hc_icon_class=request.form['hc_icon_class']
        header_contact.hc_url=request.form['hc_url']
        db.session.commit()
        return redirect('/admin/hcContactAdd')
    return render_template('admin/hcContactUpdate.html', header_contact=header_contact)

@app.route("/admin/hcContactDelete/<id>")
def hcContactDelete(id):
    header_contact=HeaderContact.query.get(id)
    db.session.delete(header_contact)
    db.session.commit()
    return redirect('/admin/hcContactAdd')
# Header Contact Info end

# Header Social icon start
@app.route("/admin/headerSocialIconAdd", methods=['GET','POST'])
def headerSocialIconAdd():
    headersocial_icons=HeaderSocialIcon.query.all()
    if request.method=='POST':
        headersocial_icon=HeaderSocialIcon(
            hsi_name=request.form['hsi_name'],
            hsi_css_class=request.form['hsi_css_class'],
            hsi_url=request.form['hsi_url']
        )
        db.session.add(headersocial_icon)
        db.session.commit()
        return redirect('/admin/headerSocialIconAdd')
    return render_template("admin/headerSocialIconAdd.html", headersocial_icons=headersocial_icons)

@app.route("/admin/headerSocialIconUpdate/<id>",methods=['GET','POST'])
def headerSocialIconUpdate(id):
    headersocial_icon=HeaderSocialIcon.query.get(id)
    if request.method=='POST':
        headersocial_icon.hsi_name=request.form['hsi_name']
        headersocial_icon.hsi_css_class=request.form['hsi_css_class']
        headersocial_icon.hsi_url=request.form['hsi_url']
        db.session.commit()
        return redirect('/admin/headerSocialIconAdd')
    return render_template('admin/headerSocialIconUpdate.html', headersocial_icon=headersocial_icon)

@app.route("/admin/headerSocialIconDelete/<id>")
def headerSocialIconDelete(id):
    headersocial_icon=HeaderSocialIcon.query.get(id)
    db.session.delete(headersocial_icon)
    db.session.commit()
    return redirect('/admin/headerSocialIconAdd')

# Header Socila icon End

# Header Meniu Logo start
@app.route("/admin/meniuLogoAdd", methods=['GET','POST'])
def meniuLogoAdd():
    logos=MeniuLogo.query.all()
    if request.method=='POST':
        file=request.files['logo_img']
        logo_img=file.filename
        randomlogo=random.randint(0,1000000089)
        logo_extention=logo_img.split(".")[-1]
        logoName=str(randomlogo)+"."+logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],logoName))
        logo=MeniuLogo(
            logo_title=request.form['logo_title'],
            logo_url=request.form['logo_url'],
            logo_alt=request.form['logo_alt'],
            logo_img=logoName
        )
        db.session.add(logo)
        db.session.commit()
        return redirect('/admin/meniuLogoAdd')
    return render_template("admin/meniuLogoAdd.html", logos=logos)

@app.route("/admin/meniuLogoUpdate/<id>",methods=['GET','POST'])
def meniuLogoUpdate(id):
    logo=MeniuLogo.query.get(id)
    if request.method=='POST':
        file=request.files['logo_img']
        logo_img=file.filename
        randomlogo=random.randint(0,10000)
        logo_extention=logo_img.split(".")[-1]
        logoName=str(randomlogo)+"."+logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],logoName))
        logo.logo_title=request.form['logo_title']
        logo.logo_url=request.form['logo_url']
        logo.logo_alt=request.form['logo_alt']
        logo.logo_img=logoName
        db.session.commit()
        return redirect('/admin/meniuLogoAdd')
    return render_template('admin/meniuLogoUpdate.html', logo=logo)

@app.route("/admin/meniuLogoDelete/<id>")
def meniuLogoDelete(id):
    logos=MeniuLogo.query.get(id)
    db.session.delete(logos)
    db.session.commit()
    return redirect('/admin/meniuLogoAdd')
# Header Meniu Logo end

# Header Meniu Name start
@app.route("/admin/meniuNameAdd", methods=['GET','POST'])
def meniuNameAdd():
    meniu_names=MeniuName.query.all()
    if request.method=='POST':
        meniu_name=MeniuName(
            meniu_title=request.form['meniu_title'],
            meniu_url=request.form['meniu_url'],
            meniu_icon=request.form['meniu_icon']
        )
        db.session.add(meniu_name)
        db.session.commit()
        return redirect('/admin/meniuNameAdd')
    return render_template("admin/meniuNameAdd.html", meniu_names=meniu_names)

@app.route("/admin/meniuNameUpdate/<id>",methods=['GET','POST'])
def meniuNameUpdate(id):
    meniu_name=MeniuName.query.get(id)
    if request.method=='POST':
        meniu_name.meniu_title=request.form['meniu_title']
        meniu_name.meniu_url=request.form['meniu_url']
        meniu_name.meniu_icon=request.form['meniu_icon']
        db.session.commit()
        return redirect('/admin/meniuNameAdd')
    return render_template('admin/meniuNameUpdate.html', meniu_name=meniu_name)

@app.route("/admin/meniuNameDelete/<id>")
def meniuNameDelete(id):
    meniu_name=MeniuName.query.get(id)
    db.session.delete(meniu_name)
    db.session.commit()
    return redirect('/admin/meniuNameAdd')
# Header Meniu Name end


# Slider Image Start
@app.route("/admin/sliderImageAdd", methods=['GET','POST'])
def sliderImageAdd():
    sliders=Slider.query.all()
    if request.method=='POST':
        file=request.files['slider_img']
        slider_img=file.filename
        randomslider=random.randint(0,1000000)
        slider_extention=slider_img.split(".")[-1]
        sliderImg=str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider=Slider(
            slider_title=request.form['slider_title'],
            slider_text=request.form['slider_text'],
            slider_alt=request.form['slider_alt'],
            slider_img=sliderImg
        )
        db.session.add(slider)
        db.session.commit()
        return redirect('/admin/sliderImageAdd')
    return render_template("admin/sliderImageAdd.html", sliders=sliders)

@app.route("/admin/sliderImageUpdate/<id>",methods=['GET','POST'])
def sliderImageUpdate(id):
    slider=Slider.query.get(id)
    if request.method=='POST':
        file=request.files['slider_img']
        slider_img=file.filename
        randomslider=random.randint(0,1000000)
        slider_extention=slider_img.split(".")[-1]
        sliderImg=str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider.slider_title=request.form['slider_title']
        slider.slider_text=request.form['slider_text']
        slider.slider_alt=request.form['slider_alt']
        slider.slider_img=sliderImg
        db.session.commit()
        return redirect('/admin/sliderImageAdd')
    return render_template('admin/sliderImageUpdate.html', slider=slider)

@app.route("/admin/sliderImageDelete/<id>")
def sliderImageDelete(id):
    slider=Slider.query.get(id)
    db.session.delete(slider)
    db.session.commit()
    return redirect('/admin/sliderImageAdd')
# Slider Image End

# Slider Button Start
@app.route("/admin/sliderBttnAdd", methods=['GET','POST'])
def sliderBttnAdd():
    sliderbttns=SliderUrl.query.all()
    if request.method=='POST':
        sliderbttn=SliderUrl(
            sliderurl_title=request.form['sliderurl_title'],
            sliderurl_icon=request.form['sliderurl_icon'],
            sliderurl_url=request.form['sliderurl_url']
        )
        db.session.add(sliderbttn)
        db.session.commit()
        return redirect('/admin/sliderBttnAdd')
    return render_template("admin/sliderBttnAdd.html", sliderbttns=sliderbttns)

@app.route("/admin/sliderBttnUpdate/<id>",methods=['GET','POST'])
def sliderBttnUpdate(id):
    sliderbttn=SliderUrl.query.get(id)
    if request.method=='POST':
        sliderbttn.sliderurl_title=request.form['sliderurl_title']
        sliderbttn.sliderurl_icon=request.form['sliderurl_icon']
        sliderbttn.sliderurl_url=request.form['sliderurl_url']
        db.session.commit()
        return redirect('/admin/sliderBttnAdd')
    return render_template('admin/sliderBttnUpdate.html', sliderbttn=sliderbttn)

@app.route("/admin/sliderBttnDelete/<id>")
def sliderBttnDelete(id):
    sliderbttn=SliderUrl.query.get(id)
    db.session.delete(sliderbttn)
    db.session.commit()
    return redirect('/admin/sliderBttnAdd')
# Slider Button End

# Service Heading Start

@app.route("/admin/serviceHeadingAdd", methods=['GET','POST'])
def serviceHeadingAdd():
    serviceheadings=ServiceTitle.query.all()
    if request.method=='POST':
        serviceheading=ServiceTitle(
            service_subheading=request.form['service_subheading'],
            service_title=request.form['service_title']
        )
        db.session.add(serviceheading)
        db.session.commit()
        return redirect('/admin/serviceHeadingAdd')
    return render_template("admin/serviceHeadingAdd.html", serviceheadings=serviceheadings)

@app.route("/admin/serviceHeadingUpdate/<id>",methods=['GET','POST'])
def serviceHeadingUpdate(id):
    serviceheading=ServiceTitle.query.get(id)
    if request.method=='POST':
        serviceheading.service_subheading=request.form['service_subheading']
        serviceheading.service_title=request.form['service_title']
        db.session.commit()
        return redirect('/admin/serviceHeadingAdd')
    return render_template('admin/serviceHeadingUpdate.html', serviceheading=serviceheading)

@app.route("/admin/serviceHeadingDelete/<id>")
def serviceHeadingDelete(id):
    serviceheading=ServiceTitle.query.get(id)
    db.session.delete(serviceheading)
    db.session.commit()
    return redirect('/admin/serviceHeadingAdd')
# Service Heading End

# Service Item start

@app.route("/admin/serviceItemAdd", methods=['GET','POST'])
def serviceItemAdd():
    serviceitems=ServiceItem.query.all()
    if request.method=='POST':
        serviceitem=ServiceItem(
            servitem_title=request.form['servitem_title'],
            servitem_text=request.form['servitem_text'],
            servitem_url=request.form['servitem_url'],
            servitem_icon=request.form['servitem_icon']
        )
        db.session.add(serviceitem)
        db.session.commit()
        return redirect('/admin/serviceItemAdd')
    return render_template("admin/serviceItemAdd.html", serviceitems=serviceitems)

@app.route("/admin/serviceItemUpdate/<id>",methods=['GET','POST'])
def serviceItemUpdate(id):
    serviceitem=ServiceItem.query.get(id)
    if request.method=='POST':
        serviceitem.servitem_title=request.form['servitem_title']
        serviceitem.servitem_text=request.form['servitem_text']
        serviceitem.servitem_url=request.form['servitem_url']
        serviceitem.servitem_icon=request.form['servitem_icon']
        db.session.commit()
        return redirect('/admin/serviceItemAdd')
    return render_template('admin/serviceItemUpdate.html', serviceitem=serviceitem)

@app.route("/admin/serviceItemDelete/<id>")
def serviceItemDelete(id):
    serviceitem=ServiceItem.query.get(id)
    db.session.delete(serviceitem)
    db.session.commit()
    return redirect('/admin/serviceItemAdd')
# Service Item End

# Service Button start
@app.route("/admin/serviceBttnAdd", methods=['GET', 'POST'])
def serviceBttnAdd():
    servicebttns=ServiceButton.query.all()
    if request.method== "POST":
        servicebttn=ServiceButton(
            servbttn_title=request.form['servbttn_title'],
            servbttn_icon=request.form['servbttn_icon'],
            servbttn_url=request.form['servbttn_url']
        )
        db.session.add(servicebttn)
        db.session.commit()
        return redirect('/admin/serviceBttnAdd')
    return render_template('admin/serviceBttnAdd.html', servicebttns=servicebttns)

@app.route("/admin/serviceBttnUpdate/<id>", methods=['GET','POST'])
def serviceBttnUpdate(id):
    servicebttn=ServiceButton.query.get(id)
    if request.method=='POST':
        servicebttn.servbttn_title=request.form['servbttn_title']
        servicebttn.servbttn_icon=request.form['servbttn_icon']
        servicebttn.servbttn_url=request.form['servbttn_url']
        db.session.commit()
        return redirect('/admin/serviceBttnAdd')
    return render_template('admin/serviceBttnUpdate.html', servicebttn=servicebttn)

@app.route("/admin/serviceBttnDelete/<id>")
def serviceBttnDelete(id):
    servicebttn=ServiceButton.query.get(id)
    db.session.delete(servicebttn)
    db.session.commit()
    return redirect('/admin/serviceBttnAdd')
# Service Button end

# Reason Heading start
@app.route("/admin/reasonHeadingAdd", methods=['GET', 'POST'])
def reasonHeadingAdd():
    reasonheadings=ReasonTitle.query.all()
    if request.method== "POST":
        reasonheading=ReasonTitle(
            reason_subheading=request.form['reason_subheading'],
            reason_title=request.form['reason_title']
        )
        db.session.add(reasonheading)
        db.session.commit()
        return redirect('/admin/reasonHeadingAdd')
    return render_template('admin/reasonHeadingAdd.html', reasonheadings=reasonheadings)

@app.route("/admin/reasonHeadingUpdate/<id>", methods=['GET','POST'])
def reasonHeadingUpdate(id):
    reasonheading=ReasonTitle.query.get(id)
    if request.method=='POST':
        reasonheading.reason_subheading=request.form['reason_subheading']
        reasonheading.reason_title=request.form['reason_title']
        db.session.commit()
        return redirect('/admin/reasonHeadingAdd')
    return render_template('admin/reasonHeadingUpdate.html', reasonheading=reasonheading)

@app.route("/admin/reasonHeadingDelete/<id>")
def reasonHeadingDelete(id):
    reasonheading=ReasonTitle.query.get(id)
    db.session.delete(reasonheading)
    db.session.commit()
    return redirect('/admin/reasonHeadingAdd')
# Reason Heading end

# Reason Item start
@app.route("/admin/reasonItemAdd", methods=['GET', 'POST'])
def reasonItemAdd():
    reasonitems=ReasonItem.query.all()
    if request.method== "POST":
        reasonitem=ReasonItem(
            reasonitem_number=request.form['reasonitem_number'],
            reasonitem_title=request.form['reasonitem_title'],
            reasonitem_text=request.form['reasonitem_text']
        )
        db.session.add(reasonitem)
        db.session.commit()
        return redirect('/admin/reasonItemAdd')
    return render_template('admin/reasonItemAdd.html', reasonitems=reasonitems)

@app.route("/admin/reasonItemUpdate/<id>", methods=['GET','POST'])
def reasonItemUpdate(id):
    reasonitem=ReasonItem.query.get(id)
    if request.method=='POST':
        reasonitem.reasonitem_number=request.form['reasonitem_number']
        reasonitem.reasonitem_title=request.form['reasonitem_title']
        reasonitem.reasonitem_text=request.form['reasonitem_text']
        db.session.commit()
        return redirect('/admin/reasonItemAdd')
    return render_template('admin/reasonItemUpdate.html', reasonitem=reasonitem)

@app.route("/admin/reasonItemDelete/<id>")
def reasonItemDelete(id):
    reasonitem=ReasonItem.query.get(id)
    db.session.delete(reasonitem)
    db.session.commit()
    return redirect('/admin/reasonItemAdd')

# Reason Item end