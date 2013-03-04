from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#from django.conf import settings


mail_cp = []


def send_response_mail(mail, subject, template, context={}):
    from_email = 'info@garitas.co'
    to = mail + mail_cp
    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


class SendEmail():

    def prepare(self, from_email='', subject=''):
        self.from_email = from_email
        self.subject = subject

    def set_to(self, to=[]):
        self.to = to

    def send_email(self, template='', keys=None):
        html_content = render_to_string(template, keys)
        text_content = strip_tags(html_content)
        self.msg = EmailMultiAlternatives(self.subject, text_content,
            self.from_email, self.to + mail_cp)
        self.msg.attach_alternative(html_content, "text/html")
        self.msg.send()
