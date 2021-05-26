from app import db

class HeaderContact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hc_content=db.Column(db.String(255))
    hc_icon_class=db.Column(db.String(255))
    hc_url=db.Column(db.String(255))

class HeaderSocialIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hsi_name=db.Column(db.String(255))
    hsi_css_class=db.Column(db.String(255))
    hsi_url=db.Column(db.String(255))

class MeniuLogo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    logo_title=db.Column(db.String(255))
    logo_url=db.Column(db.String(255))
    logo_alt=db.Column(db.String(255))
    logo_img=db.Column(db.String(255))

class MeniuName(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    meniu_title=db.Column(db.String(255))
    meniu_url=db.Column(db.String(255))
    meniu_icon=db.Column(db.String(255))

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    slider_title=db.Column(db.String(255))
    slider_text=db.Column(db.String(255))
    slider_img=db.Column(db.String(255))
    slider_alt=db.Column(db.String(255))

class SliderUrl(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sliderurl_title=db.Column(db.String(255))
    sliderurl_icon=db.Column(db.String(255))
    sliderurl_url=db.Column(db.String(255))

class ServiceTitle(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    service_subheading=db.Column(db.String(255))
    service_title=db.Column(db.String(255))

class ServiceItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servitem_title=db.Column(db.String(255))
    servitem_text=db.Column(db.String(255))
    servitem_url=db.Column(db.String(255))
    servitem_icon=db.Column(db.String(255))

class ServiceButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servbttn_title=db.Column(db.String(255))
    servbttn_icon=db.Column(db.String(255))
    servbttn_url=db.Column(db.String(255))

class ReasonTitle(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reason_subheading=db.Column(db.String(255))
    reason_title=db.Column(db.String(255))

class ReasonItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reasonitem_number=db.Column(db.String(255))
    reasonitem_title=db.Column(db.String(255))
    reasonitem_text=db.Column(db.String(255))

class ProjectHeader(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_subheading=db.Column(db.String(255))
    project_title=db.Column(db.String(255))

class ProjectMenu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_menu_name=db.Column(db.String(255))

class ProjectBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_name=db.Column(db.String(255))
    project_info=db.Column(db.String(255))
    project_link=db.Column(db.String(255))
    project_link_icon=db.Column(db.String(255))
    project_img=db.Column(db.String(255))

class ProjectButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    projectbtn_title=db.Column(db.String(255))
    projectbtn_icon=db.Column(db.String(255))
    projectbtn_url=db.Column(db.String(255))

class TeamHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    team_subheading=db.Column(db.String(255))
    team_title=db.Column(db.String(255))

class TeamBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teammate_img=db.Column(db.String(255))
    teammate_name=db.Column(db.String(255))
    teammate_position=db.Column(db.String(255))

class TeamSocilIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teammate_icon_name=db.Column(db.String(255))
    teammate_icon_class=db.Column(db.String(255))
    teammate_icon_link=db.Column(db.String(255))

class TeamButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teambuuton_title=db.Column(db.String(255))
    teambuuton_icon=db.Column(db.String(255))
    teambuuton_url=db.Column(db.String(255))