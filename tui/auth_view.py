import npyscreen


class AuthDisplay(npyscreen.ActionForm):
    def create(self):
        # Добавляем виджет TitleText на форму
        self.title = self.add(npyscreen.TitleText, name="Username")

    def on_ok(self):
        username = self.title.value
        client = self.parentApp.client_controller
        if client.is_registered(username):
            client.login(username)
        else:
            message_to_display = 'Do you want to be admin?'
            is_admin = npyscreen.notify_yes_no(message_to_display, title='popup')
            client.register(username, is_admin)
            client.login(username)

        self.parentApp.username = username
        self.parentApp.setNextForm("MESS")
