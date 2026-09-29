from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])
	content = request.POST.get('content')
	if content:
		items.append(content)
		items = items[-10:]
		request.session['items'] = items
	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = request.session.get('items', [])
	request.session['items'] = []
	return render(request, 'pages/index.html', {'items' : request.session['items']})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])
	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
