from news.models import Post 

def news(page=1, qty=20):
	#obtain all the posts from the inbox which are active
	post = Post.objects.all().order_by('-id')[(page-1)*qty : page*qty]

	p_list = []
	count = 0

	for i in post:
		count +=1
		p_list.append({'id': count, 'object': i})

	return p_list