from django.db import models


class Group(models.Model):
    number = models.CharField(max_length=20, unique=True)   # номер групи
    slogan = models.CharField(max_length=200, blank=True)    # гасло
    room = models.CharField(max_length=50, blank=True)       # кабінет зборів

    def __str__(self):
        return f"Group {self.number}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)            # ім'я
    last_name = models.CharField(max_length=50)             # прізвище
    student_card_number = models.CharField(max_length=30, unique=True)  # номер студентської карти
    email = models.EmailField(unique=True)                  # пошта
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LibraryCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="library_card")
    issue_date = models.DateField()          # дата видачі
    expiry_date = models.DateField()         # дата закінчення
    price = models.DecimalField(max_digits=8, decimal_places=2)  # ціна
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"LibraryCard for {self.student}"


class Literature(models.Model):
    title = models.CharField(max_length=200)      # назва
    genre = models.CharField(max_length=100)      # жанр
    published_year = models.IntegerField()        # рік
    published_date = models.DateField(null=True, blank=True)  # дата (можна пусто)
    author = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.title


class BorrowProcess(models.Model):
    card = models.ForeignKey(LibraryCard, on_delete=models.PROTECT, related_name="borrows")
    book = models.ForeignKey(Literature, on_delete=models.PROTECT, related_name="borrows")
    borrowed_at = models.DateTimeField()  # дата взяття
    issued_by_full_name = models.CharField(max_length=120)  # ПІБ працівника, який видав

    def __str__(self):
        return f"{self.card.student} took {self.book}"