from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField
from wtforms.fields.simple import TextAreaField

class HeaderContactForm(FlaskForm):
    hc_content=StringField('hc_content')
    hc_icon_class=StringField('hc_icon_class')
    hc_url=StringField('hc_url')
    submit=SubmitField()

class HeaderSocialIconForm(FlaskForm):
    hsi_name=StringField('hsi_name')
    hsi_css_class=StringField('hsi_css_class')
    hsi_url=StringField('hsi_url')
    submit=SubmitField()

class MeniuLogoForm(FlaskForm):
    logo_title=StringField('logo_title')
    logo_url=StringField('logo_url')
    logo_alt=StringField('logo_alt')
    logo_img=FileField('logo_img')
    submit=SubmitField()
    
class MeniuNameForm(FlaskForm):
    meniu_title=StringField('meniu_title')
    meniu_url=StringField('meniu_url')
    meniu_icon=StringField('meniu_icon')
    submit=SubmitField()

class SliderForm(FlaskForm):
    slider_title=StringField('slider_title')
    slider_text=StringField('slider_text')
    slider_img=FileField('slider_img')
    slider_alt=StringField('slider_alt')
    submit=SubmitField()

class SliderUrlForm(FlaskForm):
    sliderurl_title=StringField('sliderurl_title')
    sliderurl_icon=StringField('sliderurl_icon')
    sliderurl_url=StringField('sliderurl_url')
    submit=SubmitField()

class ServiceTitleForm(FlaskForm):
    service_subheading=StringField('service_subheading')
    service_title=StringField('service_title')
    submit=SubmitField()

class ServiceItemForm(FlaskForm):
    servitem_title=StringField('servitem_title')
    servitem_text=StringField('servitem_text')
    servitem_url=StringField('servitem_url')
    servitem_icon=StringField('servitem_icon')
    submit=SubmitField()

class ServiceButtonForm(FlaskForm):
    servbttn_title=StringField('servbttn_title')
    servbttn_icon=StringField('servbttn_icon')
    servbttn_url=StringField('servbttn_url')
    submit=SubmitField()

class ReasonTitleForm(FlaskForm):
    reason_subheading=StringField('reason_subheading')
    reason_title=StringField('reason_title')
    submit=SubmitField()

class ReasonItemForm(FlaskForm):
    reasonitem_number=StringField('reasonitem_number')
    reasonitem_title=StringField('reasonitem_title')
    reasonitem_text=StringField('reasonitem_text')
    submit=SubmitField()


class ProjectHeaderForm(FlaskForm):
    project_subheading=StringField('project_subheading')
    project_title=StringField('project_title')
    submit=SubmitField()

class ProjectMenuForm(FlaskForm):
    project_menu_name=StringField('project_menu_name')
    submit=SubmitField()

class ProjectBoxForm(FlaskForm):
    project_name=StringField()
    project_info=StringField()
    project_link=StringField()
    project_link_icon=StringField()
    project_img=FileField()
    submit=SubmitField()

class ProjectButtonForm(FlaskForm):
    projectbtn_title=StringField()
    projectbtn_icon=StringField()
    projectbtn_url=StringField()
    submit=SubmitField()


class TeamHeadingForm(FlaskForm):
    team_subheading=StringField()
    team_title=StringField()
    submit=SubmitField()

class TeamBoxForm(FlaskForm):
    teammate_name=StringField()
    teammate_position=StringField()
    teammate_img=FileField()
    submit=SubmitField()

class TeamSocilIconForm(FlaskForm):
    teammate_icon_name=StringField()
    teammate_icon_class=StringField()
    teammate_icon_link=StringField()
    submit=SubmitField()

class TeamButtonForm(FlaskForm):
    teambuuton_title=StringField()
    teambuuton_icon=StringField()
    teambuuton_url=StringField()
    submit=SubmitField()

class ClientHeadingForm(FlaskForm):
    client_subheading=StringField()
    client_title=StringField()
    submit=SubmitField()

class ClientBoxForm(FlaskForm):
    client_name=StringField()
    client_status=StringField()
    client_desc=StringField()
    client_img=FileField()
    submit=SubmitField()

class ClientButtonForm(FlaskForm):
    clientbutton_title=StringField()
    clientbutton_icon=StringField()
    clientbutton_url=StringField()
    submit=SubmitField()

class NewsHeadingForm(FlaskForm):
    news_subheading=StringField()
    news_title=StringField()
    submit=SubmitField()

class NewsBoxForm(FlaskForm):
    newsbox_title=StringField()
    newsbox_desc=StringField()
    newsbox_date=StringField()
    newsbox_link=StringField()
    newsbox_img=FileField()
    submit=SubmitField()

class NewsButtonForm(FlaskForm):
    newsbutton_title=StringField()
    newsbutton_icon=StringField()
    newsbutton_url=StringField()
    submit=SubmitField()
"""class Form(FlaskForm):
    =StringField()
    =FileField()
    submit=SubmitField()"""