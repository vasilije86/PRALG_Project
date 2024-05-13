from django.shortcuts import render
from .sudoku_solver import solve_sudoku
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def sudoku_solver_view(request):
    if request.method == 'POST':
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                input_name = f"puzzle_{i}_{j}"
                cell_value = request.POST.get(input_name, '0')
                row.append(int(cell_value))
            puzzle.append(row)
        solution = solve_sudoku(puzzle)
        return render(request, 'solve.html', {'solution': solution, 'range_9': range(9)})
    else:
        return render(request, 'solve.html', {'range_9': range(9)})
    
def index(request):
    return render(request, "index.html")


