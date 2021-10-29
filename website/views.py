from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		# Process eMail Request
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send eMail
		send_mail(
			'Request from Eljay Website',   #subject
			message, # message
			message_email, # from eMail
			['tbrown@eljaysoftware.com'], # to eMail
			fail_silently=False,
			)
		return render(request, 'contact.html', {'message_name': message_name})

	else:
		# Return the page
		return render(request, 'contact.html', {})

	