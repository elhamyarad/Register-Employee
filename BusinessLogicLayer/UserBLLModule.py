from DataAccessLayer import UserDALModule


def loginFunction(username, password):
    if username != "" and password != "":
        return UserDALModule.loginFunction(username, password)
