from django.contrib import admin
from .models import Group, Student, LibraryCard, Literature, BorrowProcess


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("number", "room", "slogan")
    search_fields = ("number", "room", "slogan")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "student_card_number", "email", "group")
    list_filter = ("group",)
    search_fields = ("first_name", "last_name", "student_card_number", "email")
    autocomplete_fields = ("group",)


@admin.register(LibraryCard)
class LibraryCardAdmin(admin.ModelAdmin):
    list_display = ("student", "issue_date", "expiry_date", "price", "active")
    list_filter = ("active",)
    search_fields = ("student__first_name", "student__last_name", "student__student_card_number")


@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "published_year", "author")
    list_filter = ("genre", "published_year")
    search_fields = ("title", "author")


@admin.register(BorrowProcess)
class BorrowProcessAdmin(admin.ModelAdmin):
    list_display = ("card", "book", "borrowed_at", "issued_by_full_name")
    list_filter = ("borrowed_at",)
    search_fields = ("issued_by_full_name", "book__title", "card__student__last_name")
    autocomplete_fields = ("card", "book")