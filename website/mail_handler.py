from website import mail
from flask_mail import Message
from flask import render_template, url_for, flash
import os
from socket import gaierror


def mail_sender(mail_identifier, target, data=None) -> None:
    """
    Will send email, if parameters filled correctly
    """
    if isinstance(target, str):
        target = [target]
    target = list(set(target))
    try:
        if mail_identifier == "tva_rezervace":
            msg = Message("Rezervace termínu u Bytařů",
                        sender=os.environ.get("MAIL_USERNAME"),
                        recipients=target)
            msg.html = render_template("mails/rezervace_terminu.html", url = url_for("views.summary", kod = data, _external = True))
            mail.send(msg)
        
        if mail_identifier == "nova_rezervace":
            msg = Message("Nová rezervace termínu",
                        sender=os.environ.get("MAIL_USERNAME"),
                        recipients=target)
            msg.html = render_template("mails/nova_rezervace.html", jmeno = data)
            mail.send(msg)
        
    except gaierror:
        flash(f"Gaierror, pravděpodobně nejsi online. E-mail se neposlal. Mail identifier: {mail_identifier}, target: {target}", category="info")
        
    
