from django.shortcuts import render,redirect
# Create your views here.
def home(request):
    return render(request,"home.html")


from first_app.forms import TodoTaskForm
def store_todo(request):
    if request.method =='POST':
        work=TodoTaskForm(request.POST)
        if work.is_valid():
            work.save()
            #print(work.changed_data)
            return redirect('show_todo')
    else:
        work=TodoTaskForm()
    return render(request,'reg_todo.html',{'form':work})



from first_app.models import TodoTaskModel
def show_todo(request):
    work=TodoTaskModel.objects.all()
    #print(work)
    return render(request,'show_todo.html',{'data':work})


def edit_todo(request,id):
    work=TodoTaskModel.objects.get(pk=id)
    form=TodoTaskForm(instance=work)
    if request.method =='POST':
        form=TodoTaskForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('show_todo')
    return render(request,'reg_todo.html',{'form':form})

def delete_todo(request,id):
    book=TodoTaskModel.objects.get(pk=id).delete()
    return redirect('show_todo')

