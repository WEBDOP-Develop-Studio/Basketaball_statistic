from django.core.mail import send_mail


def Send_email(user_email,user_name):
    send_mail(
        'Привет,' + user_name,
        'Теперь я буду присылать тебе спам',
        'vitok1223@gmail.com',
        [user_email],
        fail_silently=False,
    )
