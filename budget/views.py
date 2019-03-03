from django.shortcuts import render

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    return render(request, 'budget/project-detail.html')

def account_info(request):
    return render(request, 'budget/account-info.html')