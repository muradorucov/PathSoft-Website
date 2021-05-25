from app import app
from app.models import*
from admin.forms import*
from app import db
import os
import random
from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import secure_filename

@app.route("/admin/")
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
    projectheadings=ProjectHeader.query.all()
    return render_template("admin/index.html",header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names, sliders=sliders, sliderbttns=sliderbttns,serviceheadings=serviceheadings, serviceitems=serviceitems , servicebttns=servicebttns, reasonheadings=reasonheadings, reasonitems=reasonitems, projectheadings=projectheadings)


# Header Contact Info start
@app.route("/admin/hcContactAdd/", methods=['GET','POST'])
def hcContactAdd():
    form=HeaderContactForm()
    header_contacts=HeaderContact.query.all()
    if request.method=='POST':
        header_contact=HeaderContact(
            hc_content=form.hc_content.data,
            hc_icon_class=form.hc_icon_class.data,
            hc_url=form.hc_url.data
        )
        db.session.add(header_contact)
        db.session.commit()
        return redirect(url_for('hcContactAdd'))
    return render_template("admin/hcContactAdd.html", form=form, header_contacts=header_contacts)

@app.route("/admin/hcContactUpdate/<id>",methods=['GET','POST'])
def hcContactUpdate(id):
    header_contact=HeaderContact.query.get(id)
    form=HeaderContactForm()
    if request.method=='POST':
        header_contact.hc_content=form.hc_content.data
        header_contact.hc_icon_class=form.hc_icon_class.data
        header_contact.hc_url=form.hc_url.data
        db.session.commit()
        return redirect(url_for('hcContactAdd'))
    return render_template('admin/hcContactUpdate.html',form=form, header_contact=header_contact)

@app.route("/admin/hcContactDelete/<id>")
def hcContactDelete(id):
    header_contact=HeaderContact.query.get(id)
    db.session.delete(header_contact)
    db.session.commit()
    return redirect(url_for('hcContactAdd'))
# Header Contact Info end



# Header Social icon start
@app.route("/admin/headerSocialIconAdd/", methods=['GET','POST'])
def headerSocialIconAdd():
    form=HeaderSocialIconForm()
    headersocial_icons=HeaderSocialIcon.query.all()
    if request.method=='POST':
        headersocial_icon=HeaderSocialIcon(
            hsi_name=form.hsi_name.data,
            hsi_css_class=form.hsi_css_class.data,
            hsi_url=form.hsi_url.data
        )
        db.session.add(headersocial_icon)
        db.session.commit()
        return redirect(url_for('headerSocialIconAdd'))
    return render_template("admin/headerSocialIconAdd.html",form=form, headersocial_icons=headersocial_icons)

@app.route("/admin/headerSocialIconUpdate/<id>",methods=['GET','POST'])
def headerSocialIconUpdate(id):
    form=HeaderSocialIconForm()
    headersocial_icon=HeaderSocialIcon.query.get(id)
    if request.method=='POST':
        headersocial_icon.hsi_name=form.hsi_name.data
        headersocial_icon.hsi_css_class=form.hsi_css_class.data
        headersocial_icon.hsi_url=form.hsi_url.data
        db.session.commit()
        return redirect(url_for('headerSocialIconAdd'))
    return render_template('admin/headerSocialIconUpdate.html',form=form, headersocial_icon=headersocial_icon)

@app.route("/admin/headerSocialIconDelete/<id>")
def headerSocialIconDelete(id):
    headersocial_icon=HeaderSocialIcon.query.get(id)
    db.session.delete(headersocial_icon)
    db.session.commit()
    return redirect(url_for('headerSocialIconAdd'))
# Header Socila icon End



# Header Meniu Logo start
@app.route("/admin/meniuLogoAdd", methods=['GET','POST'])
def meniuLogoAdd():
    form=MeniuLogoForm()
    logos=MeniuLogo.query.all()
    if request.method=='POST':
        file=form.logo_img.data
        logo_name=file.filename
        randomlogo=random.randint(0,599)
        logo_title= secure_filename(form.logo_title.data)
        logo_extention=logo_name.split(".")[-1]
        logoName=logo_title+str(randomlogo)+ '.' + logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], logoName))
        logo=MeniuLogo(
            logo_title=form.logo_title.data,
            logo_url=form.logo_url.data,
            logo_alt=form.logo_alt.data,
            logo_img=logoName
        )
        db.session.add(logo)
        db.session.commit()
        return redirect(url_for('meniuLogoAdd'))
    return render_template("admin/meniuLogoAdd.html", form=form, logos=logos)

@app.route("/admin/meniuLogoUpdate/<id>",methods=['GET','POST'])
def meniuLogoUpdate(id):
    form=MeniuLogoForm()
    logo=MeniuLogo.query.get(id)
    if request.method=='POST':
        file=form.logo_img.data
        logo_name=file.filename
        randomlogo=random.randint(0,599)
        logo_title= secure_filename(form.logo_title.data)
        logo_extention=logo_name.split(".")[-1]
        logoName=logo_title+str(randomlogo)+ '.' + logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], logoName))
        logo.logo_title=form.logo_title.data
        logo.logo_url=form.logo_url.data
        logo.logo_alt=form.logo_alt.data
        logo.logo_img=logoName
        db.session.commit()
        return redirect(url_for('meniuLogoAdd'))
    return render_template('admin/meniuLogoUpdate.html',form=form, logo=logo)

@app.route("/admin/meniuLogoDelete/<id>")
def meniuLogoDelete(id):
    logos=MeniuLogo.query.get(id)
    db.session.delete(logos)
    db.session.commit()
    return redirect(url_for('meniuLogoAdd'))
# Header Meniu Logo end



# Header Meniu Name start
@app.route("/admin/meniuNameAdd", methods=['GET','POST'])
def meniuNameAdd():
    form=MeniuNameForm()
    meniu_names=MeniuName.query.all()
    if request.method=='POST':
        meniu_name=MeniuName(
            meniu_title=form.meniu_title.data,
            meniu_url=form.meniu_url.data,
            meniu_icon=form.meniu_icon.data
        )
        db.session.add(meniu_name)
        db.session.commit()
        return redirect(url_for('meniuNameAdd'))
    return render_template("admin/meniuNameAdd.html",form=form, meniu_names=meniu_names)

@app.route("/admin/meniuNameUpdate/<id>",methods=['GET','POST'])
def meniuNameUpdate(id):
    form=MeniuNameForm()
    meniu_name=MeniuName.query.get(id)
    if request.method=='POST':
        meniu_name.meniu_title=form.meniu_title.data
        meniu_name.meniu_url=form.meniu_url.data
        meniu_name.meniu_icon=form.meniu_icon.data
        db.session.commit()
        return redirect(url_for('meniuNameAdd'))
    return render_template('admin/meniuNameUpdate.html',form=form, meniu_name=meniu_name)

@app.route("/admin/meniuNameDelete/<id>")
def meniuNameDelete(id):
    meniu_name=MeniuName.query.get(id)
    db.session.delete(meniu_name)
    db.session.commit()
    return redirect(url_for('meniuNameAdd'))
# Header Meniu Name end


# Slider Image Start
@app.route("/admin/sliderImageAdd/", methods=['GET','POST'])
def sliderImageAdd():
    form=SliderForm()
    sliders=Slider.query.all()
    if request.method=='POST':
        file=form.slider_img.data
        slider_img_name=file.filename
        randomslider=random.randint(600,1678)
        slider_alt= secure_filename(form.slider_alt.data)
        slider_extention=slider_img_name.split(".")[-1]
        sliderImg=slider_alt+ str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider=Slider(
            slider_title=form.slider_title.data,
            slider_text=form.slider_text.data,
            slider_alt=form.slider_alt.data,
            slider_img=sliderImg
        )
        db.session.add(slider)
        db.session.commit()
        return redirect(url_for('sliderImageAdd'))
    return render_template("admin/sliderImageAdd.html",form=form, sliders=sliders)

@app.route("/admin/sliderImageUpdate/<id>",methods=['GET','POST'])
def sliderImageUpdate(id):
    form=SliderForm()
    slider=Slider.query.get(id)
    if request.method=='POST':
        file=form.slider_img.data
        slider_img_name=file.filename
        randomslider=random.randint(600,1678)
        slider_alt= secure_filename(form.slider_alt.data)
        slider_extention=slider_img_name.split(".")[-1]
        sliderImg=slider_alt+ str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider.slider_title=form.slider_title.data
        slider.slider_text=form.slider_text.data
        slider.slider_alt=form.slider_alt.data
        slider.slider_img=sliderImg
        db.session.commit()
        return redirect(url_for('sliderImageAdd'))
    return render_template('admin/sliderImageUpdate.html',form=form, slider=slider)

@app.route("/admin/sliderImageDelete/<id>")
def sliderImageDelete(id):
    slider=Slider.query.get(id)
    db.session.delete(slider)
    db.session.commit()
    return redirect(url_for('sliderImageAdd'))
# Slider Image End



# Slider Button Start
@app.route("/admin/sliderBttnAdd", methods=['GET','POST'])
def sliderBttnAdd():
    form=SliderUrlForm()
    sliderbttns=SliderUrl.query.all()
    if request.method=='POST':
        sliderbttn=SliderUrl(
            sliderurl_title=form.sliderurl_title.data,
            sliderurl_icon=form.sliderurl_icon.data,
            sliderurl_url=form.sliderurl_url.data
        )
        db.session.add(sliderbttn)
        db.session.commit()
        return redirect(url_for('sliderBttnAdd'))
    return render_template("admin/sliderBttnAdd.html",form=form, sliderbttns=sliderbttns)

@app.route("/admin/sliderBttnUpdate/<id>",methods=['GET','POST'])
def sliderBttnUpdate(id):
    form=SliderUrlForm()
    sliderbttn=SliderUrl.query.get(id)
    if request.method=='POST':
        sliderbttn.sliderurl_title=form.sliderurl_title.data
        sliderbttn.sliderurl_icon=form.sliderurl_icon.data
        sliderbttn.sliderurl_url=form.sliderurl_url.data
        db.session.commit()
        return redirect(url_for('sliderBttnAdd'))
    return render_template('admin/sliderBttnUpdate.html',form=form, sliderbttn=sliderbttn)

@app.route("/admin/sliderBttnDelete/<id>")
def sliderBttnDelete(id):
    sliderbttn=SliderUrl.query.get(id)
    db.session.delete(sliderbttn)
    db.session.commit()
    return redirect(url_for('sliderBttnAdd'))
# Slider Button End




# Service Heading Start
@app.route("/admin/serviceHeadingAdd", methods=['GET','POST'])
def serviceHeadingAdd():
    form=ServiceTitleForm()
    serviceheadings=ServiceTitle.query.all()
    if request.method=='POST':
        serviceheading=ServiceTitle(
            service_subheading=form.service_subheading.data,
            service_title=form.service_title.data
        )
        db.session.add(serviceheading)
        db.session.commit()
        return redirect(url_for('serviceHeadingAdd'))
    return render_template("admin/serviceHeadingAdd.html",form=form, serviceheadings=serviceheadings)

@app.route("/admin/serviceHeadingUpdate/<id>",methods=['GET','POST'])
def serviceHeadingUpdate(id):
    form=ServiceTitleForm()
    serviceheading=ServiceTitle.query.get(id)
    if request.method=='POST':
        serviceheading.service_subheading=form.service_subheading.data
        serviceheading.service_title=form.service_title.data
        db.session.commit()
        return redirect(url_for('serviceHeadingAdd'))
    return render_template('admin/serviceHeadingUpdate.html',form=form, serviceheading=serviceheading)

@app.route("/admin/serviceHeadingDelete/<id>")
def serviceHeadingDelete(id):
    serviceheading=ServiceTitle.query.get(id)
    db.session.delete(serviceheading)
    db.session.commit()
    return redirect(url_for('serviceHeadingAdd'))
# Service Heading End



# Service Item start
@app.route("/admin/serviceItemAdd", methods=['GET','POST'])
def serviceItemAdd():
    form=ServiceItemForm()
    serviceitems=ServiceItem.query.all()
    if request.method=='POST':
        serviceitem=ServiceItem(
            servitem_title=form.servitem_title.data,
            servitem_text=form.servitem_text.data,
            servitem_url=form.servitem_url.data,
            servitem_icon=form.servitem_icon.data
        )
        db.session.add(serviceitem)
        db.session.commit()
        return redirect(url_for('serviceItemAdd'))
    return render_template("admin/serviceItemAdd.html",form=form, serviceitems=serviceitems)

@app.route("/admin/serviceItemUpdate/<id>",methods=['GET','POST'])
def serviceItemUpdate(id):
    form=ServiceItemForm()
    serviceitem=ServiceItem.query.get(id)
    if request.method=='POST':
        serviceitem.servitem_title=form.servitem_title.data
        serviceitem.servitem_text=form.servitem_text.data
        serviceitem.servitem_url=form.servitem_url.data
        serviceitem.servitem_icon=form.servitem_icon.data
        db.session.commit()
        return redirect(url_for('serviceItemAdd'))
    return render_template('admin/serviceItemUpdate.html',form=form, serviceitem=serviceitem)

@app.route("/admin/serviceItemDelete/<id>")
def serviceItemDelete(id):
    serviceitem=ServiceItem.query.get(id)
    db.session.delete(serviceitem)
    db.session.commit()
    return redirect(url_for('serviceItemAdd'))
# Service Item End



# Service Button start
@app.route("/admin/serviceBttnAdd", methods=['GET', 'POST'])
def serviceBttnAdd():
    form=ServiceButtonForm()
    servicebttns=ServiceButton.query.all()
    if request.method== "POST":
        servicebttn=ServiceButton(
            servbttn_title=form.servbttn_title.data,
            servbttn_icon=form.servbttn_icon.data,
            servbttn_url=form.servbttn_url.data
        )
        db.session.add(servicebttn)
        db.session.commit()
        return redirect(url_for('serviceBttnAdd'))
    return render_template('admin/serviceBttnAdd.html',form=form, servicebttns=servicebttns)

@app.route("/admin/serviceBttnUpdate/<id>", methods=['GET','POST'])
def serviceBttnUpdate(id):
    form=ServiceButtonForm()
    servicebttn=ServiceButton.query.get(id)
    if request.method=='POST':
        servicebttn.servbttn_title=form.servbttn_title.data
        servicebttn.servbttn_icon=form.servbttn_icon.data
        servicebttn.servbttn_url=form.servbttn_url.data
        db.session.commit()
        return redirect(url_for('serviceBttnAdd'))
    return render_template('admin/serviceBttnUpdate.html',form=form, servicebttn=servicebttn)

@app.route("/admin/serviceBttnDelete/<id>")
def serviceBttnDelete(id):
    servicebttn=ServiceButton.query.get(id)
    db.session.delete(servicebttn)
    db.session.commit()
    return redirect(url_for('serviceBttnAdd'))
# Service Button end



# Reason Heading start
@app.route("/admin/reasonHeadingAdd", methods=['GET', 'POST'])
def reasonHeadingAdd():
    form=ReasonTitleForm()
    reasonheadings=ReasonTitle.query.all()
    if request.method== "POST":
        reasonheading=ReasonTitle(
            reason_subheading=form.reason_subheading.data,
            reason_title=form.reason_title.data
        )
        db.session.add(reasonheading)
        db.session.commit()
        return redirect(url_for('reasonHeadingAdd'))
    return render_template('admin/reasonHeadingAdd.html',form=form, reasonheadings=reasonheadings)

@app.route("/admin/reasonHeadingUpdate/<id>", methods=['GET','POST'])
def reasonHeadingUpdate(id):
    form=ReasonTitleForm()
    reasonheading=ReasonTitle.query.get(id)
    if request.method=='POST':
        reasonheading.reason_subheading=form.reason_subheading.data
        reasonheading.reason_title=form.reason_title.data
        db.session.commit()
        return redirect(url_for('reasonHeadingAdd'))
    return render_template('admin/reasonHeadingUpdate.html',form=form, reasonheading=reasonheading)

@app.route("/admin/reasonHeadingDelete/<id>")
def reasonHeadingDelete(id):
    reasonheading=ReasonTitle.query.get(id)
    db.session.delete(reasonheading)
    db.session.commit()
    return redirect(url_for('reasonHeadingAdd'))
# Reason Heading end



# Reason Item start
@app.route("/admin/reasonItemAdd", methods=['GET', 'POST'])
def reasonItemAdd():
    form=ReasonItemForm()
    reasonitems=ReasonItem.query.all()
    if request.method== "POST":
        reasonitem=ReasonItem(
            reasonitem_number=form.reasonitem_number.data,
            reasonitem_title=form.reasonitem_title.data,
            reasonitem_text=form.reasonitem_text.data
        )
        db.session.add(reasonitem)
        db.session.commit()
        return redirect(url_for('reasonItemAdd'))
    return render_template('admin/reasonItemAdd.html',form=form, reasonitems=reasonitems)

@app.route("/admin/reasonItemUpdate/<id>", methods=['GET','POST'])
def reasonItemUpdate(id):
    form=ReasonItemForm()
    reasonitem=ReasonItem.query.get(id)
    if request.method=='POST':
        reasonitem.reasonitem_number=form.reasonitem_number.data
        reasonitem.reasonitem_title=form.reasonitem_title.data
        reasonitem.reasonitem_text=form.reasonitem_text.data
        db.session.commit()
        return redirect(url_for('reasonItemAdd'))
    return render_template('admin/reasonItemUpdate.html',form=form, reasonitem=reasonitem)

@app.route("/admin/reasonItemDelete/<id>")
def reasonItemDelete(id):
    reasonitem=ReasonItem.query.get(id)
    db.session.delete(reasonitem)
    db.session.commit()
    return redirect(url_for('reasonItemAdd'))
# Reason Item end



# Project Heading start
@app.route("/admin/projectHeadingAdd", methods=['GET', 'POST'])
def projectHeadingAdd():
    form=ProjectHeaderForm()
    projectheadings=ProjectHeader.query.all()
    if request.method== "POST":
        projectheading=ProjectHeader(
            project_subheading=form.project_subheading.data,
            project_title=form.project_title.data
        )
        db.session.add(projectheading)
        db.session.commit()
        return redirect(url_for('projectHeadingAdd'))
    return render_template('admin/projectHeadingAdd.html',form=form, projectheadings=projectheadings)

@app.route("/admin/projectHeadingUpdate/<id>", methods=['GET','POST'])
def projectHeadingUpdate(id):
    form=ProjectHeaderForm()
    projectheading=ProjectHeader.query.get(id)
    if request.method=='POST':
        projectheading.project_subheading=form.project_subheading.data
        projectheading.project_title=form.project_title.data
        db.session.commit()
        return redirect(url_for('projectHeadingAdd'))
    return render_template('admin/projectHeadingUpdate.html',form=form, projectheading=projectheading)

@app.route("/admin/projectHeadingDelete/<id>")
def projectHeadingDelete(id):
    projectheading=ProjectHeader.query.get(id)
    db.session.delete(projectheading)
    db.session.commit()
    return redirect(url_for('projectHeadingAdd'))
# Project Heading end