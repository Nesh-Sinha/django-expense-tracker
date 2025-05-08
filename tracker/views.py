from django.shortcuts import render,redirect
import csv
from django.http import HttpResponse

# Create your views here.

'''--------------  html pages  -------------'''


def layout(request):
    return render(request,'tracker/layout.html')

def about(request):
    return render(request,'tracker/about.html')


def home(request):
    return render(request,'tracker/home.html')

def expense(request):
    return render(request,'tracker/expense.html')

def viewexp(request):
    return render(request,'tracker/viewExpense.html')


'''--------------  functions  -------------'''
def budget(request):
    if request.method == 'POST':
        budget_input = request.POST.get('budget')
        if budget_input and budget_input.isdigit():
            budget = int(budget_input)
            request.session['budget'] = budget
            return redirect('expense')
        return redirect('home')
    return redirect('home')



def addexpense(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        amount_str = request.POST.get('amount', '').strip()

        
        if not title or not amount_str.isdigit():
            return redirect('expense')  # Do nothing if invalid

        amount = int(amount_str)
        new_expense = {'title': title, 'amount': amount}
        expenses = request.session.get('expenses', [])

        for item in expenses:
            if item['title'] == title:
                item['amount'] += amount 
                break
        else:
            expenses.append(new_expense)

        request.session['expenses'] = expenses

        total_expense = sum(item['amount'] for item in expenses)  
        request.session['total_expense'] = total_expense
        request.session.modified = True

        budget = request.session.get('budget', 0)
        request.session['budget_exceeded'] = total_expense > budget

        return redirect('expense')


def viewexpense(request):
    
    return render(request, 'tracker/viewExpense.html') 

def delete_data(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('home')
    

def chart(request):
    from collections import defaultdict
    expenses = request.session.get('expenses', [])
    
    category_totals = defaultdict(int)
    for expense in expenses:
        category_totals[expense['title']] += expense['amount']  # Using 'title' as category

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    context = {
        'categories': categories,
        'amounts': amounts,
    }
    return render(request, 'tracker/chart.html', context)


def export_csv(request):
    expenses = request.session.get('expenses', [])

    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Amount'])

    for item in expenses:
        writer.writerow([item['title'], item['amount']])

    return response