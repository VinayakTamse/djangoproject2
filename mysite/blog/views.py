from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from blog.models import BlogPosts, BlogComments
from blog.templatetags import extraFilters

# Create your views here.

def blog_page(request):

    bp = BlogPosts.objects.all()
    bp_params = {'b_post': bp}

    return render(request, 'blog/blogs.html', bp_params)

def Detailed_Blog(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comments')
        
        user = request.user
        postno = request.POST.get('postno')
        post = BlogPosts.objects.get(sno=postno)
        commentId = request.POST.get('comment_id')
    
        comment_q = None
        if commentId != "":
                comment_q = BlogComments.objects.get(sno=commentId)
             
            

           
        
        comm = BlogComments.objects.create(comments=comment,user=user, post=post, parent=comment_q)
       
        comm.save()
        return redirect("/blogs/blogpost{}/".format(post.sno))
    bp = BlogPosts.objects.get(pk=id)
    com = BlogComments.objects.filter(post=bp, parent=None)
    replies = BlogComments.objects.filter(post=bp).exclude(parent=None)
    commentId = request.POST.get('comment_id')
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    
    return render(request, 'blog/detailedblog.html', {'b_post':bp,'comment_posts':com,'repdict':replyDict})
