from django.shortcuts import render


def Index(request):
    return render(
        request,
        'Base/base.html'
    )


# @permission_required('is_superuser')
def IndexAmdin(request):
    return render(
        request,
        'BaseAdmin/index.html'
    )


def mail(request):
    return render(
        request,
        'Account/email.html'
    )