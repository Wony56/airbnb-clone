from users import models


def reset_avatar():
    users = models.User.objects.filter(login_method=models.User.LOGIN_EMAIL)

    for user in users:
        user.avatar = None
        user.save()


if __name__ == "__main__":
    reset_avatar()
    