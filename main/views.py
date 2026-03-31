from django.shortcuts import render
from .models import Workout
from .forms import WorkoutForm

def home(request):
    workouts = Workout.objects.all()
    return render(request, 'home.html', {'workouts': workouts})

def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WorkoutForm()

    return render(request, 'add.html', {'form': form})