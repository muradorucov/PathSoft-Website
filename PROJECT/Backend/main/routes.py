from app import app
from app.models import*
from app import db

from flask import Flask,redirect,url_for,render_template,request

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
    return render_template("main/about.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names, reasonheadings=reasonheadings, reasonitems=reasonitems)

@app.route("/services")
def service_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/services.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/team")
def team_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/team.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/testimonials")
def testimonials_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/testimonials.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/news")
def news_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/blog.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/contact")
def contact_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/contact.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)


@app.route("/login")
def login_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/login.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/gallery")
def gallery_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/gallery.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)

@app.route("/news/blogitem")
def blogitem_index():
    header_contacts=HeaderContact.query.all()
    headersocial_icons=HeaderSocialIcon.query.all()
    logos=MeniuLogo.query.all()
    meniu_names=MeniuName.query.all()
    return render_template("main/blogitem.html", header_contacts=header_contacts, headersocial_icons=headersocial_icons, logos=logos, meniu_names=meniu_names)