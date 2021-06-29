from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hi(request):
    return render(request, 'demoapp/index.html')


def mail(request):
    import smtplib as sm
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
# fetching receiver ID and name
    rID = request.POST.get('mail')
    uName = request.POST.get('rName')
# calling certificate generator
    cert(uName)

    sID = "deltashadow16@gmail.com"
    sub = "your certificate"

    msg = MIMEMultipart()
    msg['From'] = sID
    msg['To'] = rID
    msg['Subject'] = sub

    body ='Hi there,\nHere is your certificate for attanding webinar '
    msg.attach(MIMEText(body,'plain'))

    filename= uName+'_certi.pdf'
    attachment =open(filename,'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="{}"'.format(filename))

    msg.attach(part)
    text = msg.as_string()
    server = sm.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("deltashadow16@gmail.com", "12345!@#$%")

    server.sendmail(sID, rID, text)
    server.quit()
    return render(request, 'demoapp/thanks.html')



def cert(name):
    from PIL import Image, ImageDraw, ImageFont
    i = name
    im = Image.open(r'F:\pycharm projects\demoproj\demoapp\static\demoapp\certi.jpg')
    d = ImageDraw.Draw(im)
    location = (250, 340)
    text_color = (0, 0, 0)
    font = ImageFont.truetype("arial.ttf", 80)
    d.text(location, i, fill=text_color, font=font)
    im.save(name+"_certi" + ".pdf")
