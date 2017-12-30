def is_vendeur(user):
    try:
        user.vendeur
        return True
    except:
        return False


def is_acheteur(user):
    try:
        user.acheteur
        return True
    except:
        return False