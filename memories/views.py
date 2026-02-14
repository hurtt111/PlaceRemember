from django.shortcuts import render, redirect, get_object_or_404
from .models import Memory
from .forms import MemoryForm


def home(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user).order_by('-created_at')
    else:
        memories = Memory.objects.none()

    return render(request, 'pages/home.html', {'memories': memories})


def add_memory(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'pages/add_memory.html', {'form': form})


def memory_detail(request, pk):
    memory = get_object_or_404(Memory, pk=pk, user=request.user)
    return render(request, 'pages/memory_detail.html', {'memory': memory})


def edit_memory(request, pk):
    memory = get_object_or_404(Memory, pk=pk, user=request.user)

    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemoryForm(instance=memory)

    return render(request, 'pages/add_memory.html', {'form': form})


def delete_memory(request, pk):
    memory = get_object_or_404(Memory, pk=pk, user=request.user)

    if request.method == 'POST':
        memory.delete()
        return redirect('home')

    return render(request, 'pages/delete_memory.html', {'memory': memory})
