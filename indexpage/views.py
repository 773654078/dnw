from django.shortcuts import render

# Create your views here.
from indexpage.models import Notice
from users.models import MyUser


def index_page(request):
    admin_user = request.user
    if (request.user.admin_level == 2):
        admin_user = MyUser.objects.get(id=request.user.parent_id)
    message_list = Notice.objects.values_list('message', flat=True)
    context = {
        'admin_user': admin_user,
        'message_list': message_list,
    }

    return render(request, 'indexpage/index.html', context)