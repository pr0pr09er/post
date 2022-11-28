from django.shortcuts import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse

# Create your views here.
posts = [['Vanya', 'Super heroes', 'The best super hero is Spider-man'],
         ['Ilya', 'Super heroes', 'The worst super hero is Iron man'],
         ['Sashenka', 'Talk', 'My name is Sasha!'],
         ['Samir', 'Games', 'I like OSU!']]


def recent(request):
    recent_post = posts[-1]
    return HttpResponse(f"""Recent:<br><b>Name</b>: {recent_post[0]}<br>
                            <b>Theme of post</b>: {recent_post[1]}<br>
                            <b>Comment</b>: {recent_post[2]}<br>
                        """)


def most_popular(request):
    popular_post = posts[0]
    return HttpResponse(f"""Popular:<br><b>Name</b>: {popular_post[0]}<br>
                            <b>Theme of post</b>: {popular_post[1]}<br>
                            <b>Comment</b>: {popular_post[2]}<br>
                        """)


def all_posts(request):
    return HttpResponse(f"""{index + 1}) <b>Name</b>: {post[0]}<br>
                            <b>Theme of post</b>: {post[1]}<br>
                            <b>Comment</b>: {post[2]}<br>
                        """ for index, post in enumerate(posts))


def post_comments_likes(request):
    id_post = request.GET.get('id')
    if id_post is None:
        curr_post = posts[0]
    elif int(id_post) - 1 > len(posts):
        curr_post = posts[0]
    else:
        curr_post = posts[int(id_post) - 1]
    likes = request.GET.get('likes')
    if likes is None:
        likes = '1'
    comments = request.GET.get('comments')
    if comments is None:
        comments = '1'

    return HttpResponse(f"""Post from {curr_post[0]} have {likes}
                         likes and {comments} comments""")


def login_password(request):
    login = request.GET.get('login')
    if login is None:
        login = 'admin'
    password = request.GET.get('password')
    if password is None:
        password = 'admin'
    return HttpResponse(f"""<b>Your login</b>: {login}<br>
                            <b>Your password</b>: {password}
                        """)


def about(request):
    return HttpResponseRedirect("/")


def contacts(request):
    return HttpResponsePermanentRedirect("/")


def err(request):
    return HttpResponse("Load of the page ends with error.", status=404)

def access(request):
    login = request.GET.get("login")
    password = request.GET.get("password")
    if login == "admin" and password == "admin":
        return HttpResponse("All right!")
    else:
        return HttpResponse("Not allowed!")


def json_return(request):
    return JsonResponse({"Name": "Tom", "Age": "15"})


def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")


def set(request):
    username = request.GET.get("username", "Bob")
    resp = HttpResponse(f"Hello {username}")
    resp.set_cookie("username", username)
    return resp
