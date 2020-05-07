from django.shortcuts import render,HttpResponse,redirect
from page.models import Post, PageComment
from django.contrib import messages
from page.templatetags import extras
# Create your views here.
def pagehome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'page/pagehome.html', context)

    

def pagepost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = PageComment.objects.filter(post=post, parent=None)
    replies = PageComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'post': post, 'comments':comments,'user': request.user, 'replyDict': replyDict}
    return render(request,'page/pagepost.html',context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = PageComment(comment=comment, user=user,post=post)
            comment.save() 
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = PageComment.objects.get(sno=parentSno)
            comment = PageComment(comment=comment, user=user,post=post,parent=parent)
            comment.save() 
            messages.success(request, "Your reply has been posted successfully")
    
    return redirect(f"/page/{post.slug}")
