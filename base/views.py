from django.shortcuts import render


rooms = [
    {'id':1,
    'name':'İşletme Giriş Bölümü'
    },
      {'id':2,
    'name':'İşletme Matematiği Bölümü'
    },
      {'id':3,
    'name':'Programlamaya Giriş Bölümü'
    },
      {'id':4,
    'name':'İşletme Bilimine Giriş Bölümü'
    },
      {'id':5,
    'name':'Bilgisayar Kullanımına Giriş Bölümü'
    },
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html') 
