from jinja2 import Template


class EmailTemplateService:

    @staticmethod
    def get_login_notification_template(
            username: str, login_time: str, ip: str,
            support_link: str = "http://127.0.0.1:8000/"
    ):

        template = Template("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>User Login Notification</title>
            </head>
            <body>
                <h2>Hello, {{ username }}!</h2>
                <p>We wanted to let you know that your account 
                    was successfully logged in on {{ login_time }} with ip {{ ip }}.</p>
                <p>If you did not make this login, 
                    please <a href="{{ support_link }}">contact support</a> immediately.</p>
                <p>Thank you for using our service!</p>
            </body>
            </html>
        """)

        return template.render(
            username=username,
            login_time=login_time,
            ip=ip,
            support_link=support_link
        )