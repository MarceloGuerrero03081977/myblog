from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message
from .forms import MessageForm


@login_required
def inbox_view(request):
    received = Message.objects.filter(receiver=request.user)
    sent = Message.objects.filter(sender=request.user)
    unread_count = received.filter(is_read=False).count()
    return render(request, 'messaging/inbox.html', {
        'received': received,
        'sent': sent,
        'unread_count': unread_count,
    })


@login_required
def send_message_view(request, username=None):
    initial = {}
    if username:
        receiver = get_object_or_404(User, username=username)
        initial['receiver'] = receiver

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('inbox')
    else:
        form = MessageForm(initial=initial)

    return render(request, 'messaging/send.html', {'form': form})


@login_required
def message_detail_view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.receiver == request.user:
        message.is_read = True
        message.save()
    return render(request, 'messaging/detail.html', {'message': message})


@login_required
def delete_message_view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.user == message.sender or request.user == message.receiver:
        message.delete()
        messages.success(request, 'Mensaje eliminado.')
    return redirect('inbox')