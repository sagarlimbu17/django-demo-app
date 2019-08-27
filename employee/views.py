from django.shortcuts import render

from employee.forms import EmployeeForm


def employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'employee/add_employee.html', {'form': form})