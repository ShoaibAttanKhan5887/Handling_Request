from django.shortcuts import render
from django.shortcuts import render, redirect
from Home.models import Request
from Home.models import DataEntry  # Assuming you have a model for storing data

# Create your views here.
# views.py
def index(request):
    return render(request,'index.html')





from django.shortcuts import render
from .models import Request

# Global variable to track if a request is being processed
is_processing = False

def check_request(request):
    global is_processing

    # Check if there are any requests in the queue that are not completed
    pending_requests = Request.objects.exclude(status='completed').order_by('id')
    
    if not pending_requests and not is_processing:
        # If no pending requests and no request is currently being processed,
        # mark the current request as processing
        current_request = Request(status='processing')
        current_request.save()
        # Set the processing flag to True
        is_processing = True
        # Simulate server-intensive database operation
        insert_large_amount_of_data()
        # Once processing is complete, mark the request as completed
        current_request.status = 'completed'
        current_request.save()
        # Set the processing flag to False
        is_processing = False
        status = 'completed'
    else:
        # Inform the user that their request is waiting
        status = 'waiting'
        # Create a new Request object for the waiting state
        waiting_request = Request(status='waiting')
        waiting_request.save()

    return render(request, 'request_status.html', {'status': status})

def insert_large_amount_of_data():
    # Simulate a server-intensive database operation by inserting a large amount of data
    import random
    import string
    from .models import DataEntry

    # Generate and insert 10,000 records into the DataEntry table
    for _ in range(10000):
        random_data = ''.join(random.choices(string.ascii_letters, k=50))
        DataEntry.objects.create(data=random_data)
