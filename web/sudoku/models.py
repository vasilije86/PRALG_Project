from django.db import models
from django.contrib.auth.models import User
class SudokuBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_board = models.CharField(max_length=81, help_text="Stores the original board")
    solved_board = models.CharField(max_length=81, help_text="Stores the solved board")
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Sudoku Board {self.id} for {self.user.username}"

