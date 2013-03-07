# Create your views here.
from news.forms import PostForm
from news.models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(["GET", "POST"])
def news_create(request):
    if request.method == 'GET':
        post_form = PostForm()
        return render_to_response('news_form.html', {'form': post_form,}, context_instance=RequestContext(request))
    else:
        post_form = PostForm(request.POST)
        if post_form.is_valid(): 
            pf = post_form.save(commit=False)
            #Verifies there's not another file with that name
            if pf.post or pf.url :
                pf.user = request.user
                pf.save()
                return HttpResponseRedirect("/news/"+ str(pf.id))

            else:
                form_errors = {"Empty Fields - You at least need to have filled the URL or Post Field."} 
                return render_to_response('news_form.html',
                    {'form': post_form,'form_errors': form_errors}, 
                    context_instance=RequestContext(request))
        else:
            return render_to_response('news_form.html',
                    {'form': post_form,'form_errors': post_form.errors}, 
                    context_instance=RequestContext(request))
    


@login_required
@require_http_methods(["GET", "POST"])
def news_update(request, id):
    if request.method=="GET":
        post = get_object_or_404(Post, id=id)
        post_form = PostForm(instance=post)
        update = {'edit':True}
        return render_to_response('news_form.html', {'form': post_form, 'update':update}, context_instance=RequestContext(request))
    #Manage POST requests.    
    else:
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            pf = post_form.save(commit=False)
            if pf.post or pf.url :
                post = Post(id=id)
                post.name, post.url, post.post = pf.name, pf.url, pf.post
                post.save()
                return HttpResponseRedirect("/news/"+ str(id)+"/")
            else:
                form_errors = {"Empty Fields - You at least need to have filled the URL or Post Field."} 
                return render_to_response('news_form.html',
                    {'form': post_form,'form_errors': form_errors}, 
                    context_instance=RequestContext(request))
        else:
            return render_to_response('news_form.html',
                    {'form': post_form,'form_errors': post_form.errors}, 
                    context_instance=RequestContext(request))



@login_required
@require_http_methods(["GET"])
def news_delete(request, id):
    #Verify the person has access to the archive or redirect
    post = get_object_or_404(Post,id=id)
    if request.user.is_staff or request.user.is_superuser or request.user == post.user:
        #delete
        post.delete()
        return HttpResponseRedirect("/news/all")
    else:
        return HttpResponseRedirect("news/" + str(post.id)+"/")


@login_required
@require_http_methods(["GET"])
def news_view(request, id):
    post = get_object_or_404(Post, id=id)
     #does the user was the same person that created it?
    if post.user == request.user :
        permission = {'edit':True,}
    else:
        permission = {}
    return render_to_response('news_form.html', {'details': post,'permission':permission}, context_instance=RequestContext(request))

