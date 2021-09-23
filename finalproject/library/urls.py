from django.urls import path
from library.views import index,login_view,register,admin,student,addbooks,change_password,deleteBook,updateBook,edit_profile,studentFun
urlpatterns = [
    path('',index,name="index"),
     path('login/',login_view,name="login_view"),
    path('register/',register,name="register"),  
    path('adminpage/',admin, name='adminpage'),
    path('student/',studentFun, name='student'),
    path('studentpage/',student, name='student-page'),
    path('addbooks/',addbooks,name='addbooks'),
    path('change-password/',change_password,name='change-password'),
    path('<int:book_id>/delete',deleteBook,name="delete-book"),
    path('<int:book_id>/update',updateBook,name="update-book"),
    path("edit_profile",edit_profile,name="edit_profile"),
    # path("<borrowed_books",borrowed_books,name="borrowed_books"),
    # path('borrow', borrow_book,name= "borrow_book")
]