from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
# from django.forms.formsets.BaseFormSet import forms


class Employee(AbstractUser):
    account_number = models.CharField(max_length=10, unique=True, null=True)
    avatar = models.ImageField(upload_to='avatars' ,
    default='avatars/default.png')


class Project (models.Model):
    description = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2) # amount for this project
    due_date = models.DateField()
    # employees = models.ForeignKey()
    def __str__(self):
        return self.name

class ProjectEmployeeAllocatedBudget(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='allocated_budgets',
                                on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return (f'{self.employee.username} - {self.project.name} -'  
                f' {self.allocated_budget}')


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='uploads/',default='uploads/default.png')
    # should i remove null=True - as uploads should be mandatory to prove
    # expense was justified/real?

    # team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.description} - {self.employee.account_number}'

    # def remaining_budget(self):
    #     return self.initial_amount - spent_amount?
    @property
    def remaining_budget(self):
        # subtract the sum of all associated receipts from  initial amount
        allocated_budget_record = ProjectEmployeeAllocatedBudget.objects.filter(
            employee=self.employee, is_active=True).first()
        total_budget = allocated_budget_record.allocated_budget
        # look at clean_amount to complete this
        # project allocated budget and current user and
        # is active = true
        # filter will return a list of records
        expenses = Expense.objects.filter(created_date__lte=self.created_date, employee=self.employee)
        print(expenses.query)
        total_expenses = expenses.aggregate(total=Sum('initial_amount'))['total'] or 0
       # REMAINING_BUDGET = TOTAL_ALLOCATED - (TOTAL OF EXPENSES before current expense date) - current expense
        return total_budget - total_expenses
        # return self.initial_amount - total_spent

    class Team(models.Model):
        name = models.CharField(max_length=100)
        project = models.ForeignKey(Project, related_name='teams',
                                    on_delete=models.CASCADE)
        members = models.ManyToManyField(Employee, related_name='teams')
        description = models.TextField(blank=True, null=True)

        def __str__(self):
            return self.name

        def total_expenses(self):
            # expenses for all team members for project they are associated
            return Expense.objects.filter(
                employee__in=self.members.all(),
                project=self.project
            ).aggregate(total=Sum('initial_amount'))['total'] or 0


# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['description', 'project', 'initial_amount']

class Receipt(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE) #link to
    # Expense
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) #redundant?

    def __str__(self):
        return f'{self.description} - {self.amount}'



