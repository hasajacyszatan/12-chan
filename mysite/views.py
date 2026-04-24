from django.shortcuts import render
posts = [
    {
        "title": "Post 1",
        "content": "treść dupasdfsoiafoiasoieasfoiseiod"
    },
    {
        "title": "Post 2",
        "content": "treść postu 2 dupasdfsoiafoiasoieasfoiseiod"
    }
]
def index(request):
    liste = [1, 2, 3, 'pipa']
    return render(request, 'index.html', {'posts': posts})