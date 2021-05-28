from wtforms import form
from app import app
from app.models import*
from app import db
from admin.forms import*
from werkzeug.utils import secure_filename
from flask import Flask,redirect,url_for,render_template,request
from datetime import date
today = date.today()


@app.route("/")
def index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    sliders=Slider.query.all()
    sliderbttns=SliderUrl.query.all()
    serviceheadings=ServiceTitle.query.all()
    serviceitems=ServiceItem.query.all()
    servicebttns=ServiceButton.query.all()
    reasonheadings=ReasonTitle.query.all()
    reasonitems=ReasonItem.query.all()
    projectheadings=ProjectHeader.query.all()
    projectmenus=ProjectMenu.query.all()
    projectboxs=ProjectBox.query.all()
    projectbtns=ProjectButton.query.all()
    teamheadings=TeamHeading.query.all()
    teamboxs=TeamBox.query.all()
    teamsocialicons=TeamSocilIcon.query.all()
    teambuttons=TeamButton.query.all()
    clientheadings=ClientHeading.query.all()
    clientboxs=ClientBox.query.all()
    clientbuttons=ClientButton.query.all()
    newsheadings=NewsHeading.query.all()
    newsboxs=NewsBox.query.all()
    newsbuttons=NewsButton.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/index.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names, sliders=sliders, sliderbttns=sliderbttns, serviceheadings=serviceheadings, serviceitems=serviceitems ,servicebttns=servicebttns, reasonheadings=reasonheadings, reasonitems=reasonitems,projectheadings=projectheadings, projectmenus=projectmenus,projectboxs=projectboxs, projectbtns=projectbtns,teamheadings=teamheadings, teamboxs=teamboxs, teamsocialicons=teamsocialicons, teambuttons=teambuttons, clientboxs=clientboxs,clientheadings=clientheadings, clientbuttons=clientbuttons , newsheadings=newsheadings,newsboxs=newsboxs,newsbuttons=newsbuttons,company_info_footers=company_info_footers , footer_social_icons=footer_social_icons,footer_menus=footer_menus , footer_offers=footer_offers, footer_contacts=footer_contacts)

@app.route("/about")
def about_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    reasonheadings=ReasonTitle.query.all()
    reasonitems=ReasonItem.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/about.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names, reasonheadings=reasonheadings, reasonitems=reasonitems, company_info_footers=company_info_footers,footer_social_icons=footer_social_icons , footer_menus=footer_menus,footer_offers=footer_offers ,footer_contacts=footer_contacts )

@app.route("/services")
def service_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/services.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names , company_info_footers=company_info_footers, footer_social_icons=footer_social_icons, footer_menus=footer_menus, footer_offers=footer_offers, footer_contacts=footer_contacts)

@app.route("/team")
def team_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/team.html",company_info_footers=company_info_footers , footer_social_icons=footer_social_icons, footer_menus=footer_menus, footer_offers=footer_offers, footer_contacts=footer_contacts, header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/testimonials")
def testimonials_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/testimonials.html", company_info_footers=company_info_footers,footer_social_icons=footer_social_icons ,footer_menus=footer_menus , footer_offers=footer_offers, footer_contacts=footer_contacts, header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/news")
def news_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/blog.html",company_info_footers=company_info_footers ,footer_social_icons=footer_social_icons ,footer_menus=footer_menus ,footer_offers=footer_offers ,footer_contacts=footer_contacts , header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/contact")
def contact_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    contactmaps=ContactMap.query.all()
    return render_template("main/contact.html",contactmaps=contactmaps,company_info_footers=company_info_footers ,footer_social_icons=footer_social_icons , footer_menus=footer_menus, footer_offers=footer_offers, footer_contacts=footer_contacts, header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

# Contact Form start
@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   form=ContactFormForm()
   contactforms=ContactForm.query.all()
   if request.method=='POST':
      contactform=ContactForm(
         username=form.username.data,
         userphone=form.userphone.data,
         useremail=form.useremail.data,
         usermessage=form.usermessage.data
      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/contact')
   return render_template('admin/contactform.html',form=form, contactforms=contactforms)

@app.route("/admin/contactformDelete/<id>")
def contactformDelete(id):
   contactform=ContactForm.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect(url_for('contactform'))
# Contact Form end


@app.route("/login")
def login_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    return render_template("main/login.html",company_info_footers=company_info_footers , footer_social_icons=footer_social_icons,footer_menus=footer_menus , footer_offers=footer_offers, footer_contacts=footer_contacts, header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/gallery")
def gallery_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    galleryboxs=GalleryBox.query.all()
    return render_template("main/gallery.html",galleryboxs=galleryboxs, company_info_footers=company_info_footers ,footer_social_icons=footer_social_icons ,footer_menus=footer_menus ,footer_offers=footer_offers ,footer_contacts=footer_contacts , header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/news/blogitem")
def blogitem_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    company_info_footers=FooterCompanyInfo.query.all()
    footer_social_icons=FooterSocialIcon.query.all()
    footer_menus=FooterMenu.query.all()
    footer_offers=FooterOffer.query.all()
    footer_contacts=FooterContact.query.all()
    usercomments=UserComment.query.all()
    return render_template("main/blogitem.html",usercomments=usercomments, company_info_footers=company_info_footers ,footer_social_icons=footer_social_icons ,footer_menus=footer_menus ,footer_offers=footer_offers , footer_contacts=footer_contacts, header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)


# Comment Form start
@app.route('/news/blogitem', methods=['GET','POST']) 
def Usercomment():
   form=UserCommentForm()
   usercomments=UserComment.query.all()
   if request.method=='POST':
      usercomment=UserComment(
        commentusername=form.commentusername.data,
        commentuseremail=form.commentuseremail.data,
        commentdate=today,
        comment=form.comment.data
      )     
      db.session.add(usercomment)
      db.session.commit()
      return redirect('/news/blogitem')
   return render_template('admin/blogitem.html',"admin/usercomment.html", form=form, usercomments=usercomments)

# comment Form end
