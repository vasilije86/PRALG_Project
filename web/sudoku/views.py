
from django.shortcuts import render, redirect
from .sudoku_solver import solve_sudoku
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import SudokuBoard

def index(request):
    return render(request, "index.html")

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def sudoku_solver_view(request):
    if request.method == 'POST':
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                input_name = f"puzzle_{i}_{j}"
                cell_value = request.POST.get(input_name, '0')  # Default to '0' if not provided
                row.append(int(cell_value))
            puzzle.append(row)
        original_board = ''.join(str(cell) for row in puzzle for cell in row)
        solution = solve_sudoku(puzzle)
        solved_board = ''.join(str(cell) for row in solution for cell in row)
        if request.user.is_authenticated:
            sudoku_board = SudokuBoard(user=request.user, original_board=original_board, solved_board=solved_board)
            sudoku_board.save()
        return render(request, 'solve.html', {'solution': solution, 'range_9': range(9)})
    else:
        return render(request, 'solve.html', {'range_9': range(9)})

@login_required
def profile_view(request):
    boards = SudokuBoard.objects.filter(user=request.user).order_by('-date_created')
    return render(request, "profile.html", {'boards': boards})

def logout_view(request):
    logout(request)
    return redirect("login")
