from django.shortcuts import render

posts =[
    {
        'author': 'Iiris Kissanen',
        'title': 'Cyber Blog Post 1',
        'content': 'First cat post',
        'date_posted': '27 July 2020'
    },
    {
        'author': 'Mosse Kissanen',
        'title': 'Cyber Blog Post 2',
        'content': 'Second cat post',
        'date_posted': '28 July 2020'  
    }
]

def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'cyber_blog/home.html', context)

def about (request):
    return render(request, 'cyber_blog/about.html', {'title': 'About'})

