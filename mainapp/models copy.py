from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.timezone import now

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(blank=False, null=True)
    phone_number = models.PositiveBigIntegerField(blank=False, null=True)
    

class Project(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    start_date = models.DateField(blank=True, null=True) 
    projected_end_date = models.DateField(blank=True, null=True) 
    progress = models.IntegerField(choices=[(0, 'Not Started'), (1, 'In Progress'), (2, 'Completed')], default=0)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  
    location = models.CharField(max_length=255) 
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='projects_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='projects_updated', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    created_by = models.ForeignKey(User, related_name='roles_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='roles_updated', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name

class Stakeholder(models.Model):
    name = models.CharField(max_length=255)  
    role = models.ForeignKey(Role, on_delete=models.CASCADE) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stakeholders_project') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='stakeholders_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='stakeholders_updated', on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.name} - {self.role.name}" 
    
class BudgetAllocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='budget_allocations')
    materials_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    equipment_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    contingency_cost = models.DecimalField(max_digits=10, decimal_places=2)  
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    created_by = models.ForeignKey(User, related_name='budget_allocations_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='budget_allocations_updated', on_delete=models.CASCADE)  

    def save(self, *args, **kwargs):
       
        self.total_budget = self.materials_cost + self.labor_cost + self.equipment_cost + self.contingency_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Budget for {self.project.name} - Total: {self.total_budget}"


class ResourcePlanning(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='resource_planning') 
    workforce_required = models.IntegerField()
    project_duration = models.IntegerField(help_text="Project duration in days")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_planning_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_planning_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resource planning for {self.project.name}"
    
class Material(models.Model):
    resource_planning = models.ForeignKey(ResourcePlanning, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.quantity})"
    
class Machinery(models.Model):
    resource_planning = models.ForeignKey(ResourcePlanning, on_delete=models.CASCADE, related_name='machinery')
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.quantity})"        
 
class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones') 
    name = models.CharField(max_length=255) 
    target_date = models.DateField()  
    dependency = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='dependent_milestones') 
    client_review_required = models.BooleanField(default=False) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='milestones_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='milestones_updated', on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.name} - Target Date: {self.target_date}"

class ClientReview(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='client_milestones')  
    client_feedback = models.TextField(null=True, blank=True) 
    approved = models.BooleanField(default=False)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='client_reviews_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='client_reviews_updated', on_delete=models.CASCADE)  
    def __str__(self):
        return f"Review for {self.milestone.name} - Approved: {self.approved}"


class Task(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='tasks')  
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    is_completed = models.BooleanField(default=False)  
    duration_estimation = models.ForeignKey('TaskDurationEstimation', on_delete=models.SET_NULL, null=True)  
    priority = models.ForeignKey('TaskPriority', on_delete=models.SET_NULL, null=True) 
    category = models.ForeignKey('TaskCategory', on_delete=models.SET_NULL, null=True) 
    assigned_team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)  
    assigned_individuals = models.ManyToManyField('Individual', blank=True)  
    start_date = models.DateField(null=True, blank=True)  
    end_date = models.DateField(null=True, blank=True) 
    task_owner = models.ForeignKey('Individual', on_delete=models.SET_NULL, null=True, related_name='tasks_owned')  
    
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='tasks_updated', on_delete=models.CASCADE) 
    def __str__(self):
        return f"Task: {self.name} - Milestone: {self.milestone.name}"


class Resource(models.Model):
    resource_type = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True) 
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='resources_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='resources_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.resource_type}: {self.description}"


class TaskResourceAllocation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='resource_allocations')  
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='allocations')
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_resource_allocations_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='task_resource_allocations_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.quantity} x {self.resource.description} for {self.task.name}"



class TaskDependency(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='dependencies')
    dependent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='dependent_on') 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_dependencies_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='task_dependencies_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.task.name} depends on {self.dependent_task.name}"



class TaskDurationEstimation(models.Model):
    estimated_duration = models.PositiveIntegerField(help_text="Estimated duration in hours")  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_duration_estimations_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='task_duration_estimations_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"Estimated Duration: {self.estimated_duration} hours"



class TaskPriority(models.Model):
    priority_level = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_priorities_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='task_priorities_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return self.priority_level




class TaskCategory(models.Model):
    category_name = models.CharField(max_length=30, unique=True)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_categories_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='task_categories_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return self.category_name




class Team(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='teams_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='teams_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return self.name




class Individual(models.Model):
    name = models.CharField(max_length=255) 
    skills = models.TextField(blank=True, null=True)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='individuals_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='individuals_updated', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name

class ProjectSchedule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='schedules') 
    start_date = models.DateField()  
    end_date = models.DateField()  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='project_schedules_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='project_schedules_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"Schedule for {self.project.name} from {self.start_date} to {self.end_date}"



class TaskSchedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_schedules') 
    scheduled_start_date = models.DateField() 
    scheduled_end_date = models.DateField()  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='task_schedules_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='task_schedules_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"Schedule for Task: {self.task.name} - {self.scheduled_start_date} to {self.scheduled_end_date}"


class ResourceAvailability(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='availabilities') 
    available_from = models.DateField() 
    available_until = models.DateField() 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='resource_availabilities_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='resource_availabilities_updated', on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.resource.description} available from {self.available_from} to {self.available_until}"



class ResourceUsage(models.Model):
    task_resource_allocation = models.ForeignKey(TaskResourceAllocation, on_delete=models.CASCADE, related_name='usage_records') 
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)  
    quantity_used = models.PositiveIntegerField()  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='resource_usages_created', on_delete=models.CASCADE)  
    updated_by = models.ForeignKey(User, related_name='resource_usages_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.quantity_used} of {self.task_resource_allocation.resource.description} used for {self.task_resource_allocation.task.name}"



class ResourceAdjustment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='resource_adjustments')  
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='adjustments')  
    adjustment_date = models.DateField()  
    new_schedule = models.DateField()  
    reason = models.TextField(blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, related_name='resource_adjustments_created', on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, related_name='resource_adjustments_updated', on_delete=models.CASCADE)  

    def __str__(self):
        return f"Adjustment for {self.resource.description} on {self.adjustment_date}: new schedule {self.new_schedule} for task {self.task.name}"  
    







class TimeTracking(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_tracks') 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_tracks') 
    date = models.DateField(null=True, blank=True)  
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2) 
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, editable=False) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='time_tracking_created') 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='time_tracking_updated') 
    updated_at = models.DateTimeField(auto_now=True) 

    def save(self, *args, **kwargs):
       
        self.total_cost = self.hours_spent * self.hourly_rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hours_spent} hours tracked for {self.task.name} by {self.user.username} on {self.date} - Cost: {self.total_cost}"   


class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='status_updates') 
    status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ], default='not_started')  
    update_date = models.DateField(null=True, blank=True) 
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_status_updates')  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_status_created')  
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Status of {self.task.name}: {self.status} on {self.update_date}"
    
 


class ProjectUpdate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='updates') 
    date = models.DateField(null=True, blank=True)  
    planned_start_date = models.DateField(null=True, blank=True) 
    actual_start_date = models.DateField(null=True, blank=True) 
    planned_end_date = models.DateField(null=True, blank=True)  
    actual_end_date = models.DateField(null=True, blank=True) 
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  
    comments = models.TextField(blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_update_created')  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_update_updated') 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Update for {self.task.name} on {self.date} - Progress: {self.progress_percentage}%" 


class CriticalPath(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='critical_paths') 
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='critical_paths') 
    estimated_duration = models.PositiveIntegerField(help_text="Estimated duration in hours")  
    is_on_critical_path = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='critical_path_created')  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='critical_path_updated') 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Critical Path Task: {self.task.name} in {self.project.name}"


class CriticalPathMonitoring(models.Model):
    critical_path = models.ForeignKey(CriticalPath, on_delete=models.CASCADE, related_name='monitors')  
    actual_start_date = models.DateField(null=True, blank=True) 
    actual_end_date = models.DateField(null=True, blank=True)  
    delay_days = models.PositiveIntegerField(default=0)
    comments = models.TextField(blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='critical_path_monitor_created') 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='critical_path_monitor_updated')  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Monitoring {self.critical_path.task.name} - Delayed: {self.delay_days} days"  




class Timesheet(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timesheets')  
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='timesheets')  
    date = models.DateField()  
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)  
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='timesheets', null=True, blank=True) 
    submitted = models.BooleanField(default=False)  
    reviewed = models.BooleanField(default=False)  
    comments = models.TextField(blank=True, null=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='timesheet_created')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='timesheet_updated')  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Timesheet for {self.worker.username} on {self.date} - Hours: {self.hours_worked}"

class Payroll(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payrolls')  
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='payrolls')  
    pay_period_start = models.DateField()  
    pay_period_end = models.DateField()  
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)  
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  
    total_pay = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='payroll_created')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='payroll_updated')  
    updated_at = models.DateTimeField(auto_now=True)  

    def save(self, *args, **kwargs):
        self.total_pay = self.total_hours * self.hourly_rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payroll for {self.worker.username} - Pay Period: {self.pay_period_start} to {self.pay_period_end} - Total Pay: {self.total_pay}"

class DelayCause(models.Model):
    cause = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delaycauses_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delaycauses_updated')  

    def __str__(self):
        return self.cause

class Delay(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='delays') 
    cause = models.ForeignKey(DelayCause, on_delete=models.CASCADE, related_name='delays')  
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_delays')  
    reported_at = models.DateTimeField(auto_now_add=True)  
    duration = models.DurationField()  
    notes = models.TextField(blank=True, null=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delays_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delays_updated')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Delay for {self.task.name} reported by {self.reported_by.username} - Duration: {self.duration}"



class Adjustment(models.Model):
    delay = models.ForeignKey(Delay, on_delete=models.CASCADE, related_name='adjustments')  
    adjusted_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='adjustments')  
    new_start_date = models.DateField()  
    new_end_date = models.DateField()  
    adjusted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adjusted_tasks')  
    adjustment_reason = models.TextField(blank=True, null=True)  
    adjusted_at = models.DateTimeField(auto_now_add=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='adjustments_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='adjustments_updated')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Adjustment for {self.adjusted_task.name} due to {self.delay.cause.cause} - Adjusted by {self.adjusted_by.username}"
    

class ResourceAllocation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='resource_allocations') 
    resource_type = models.CharField(max_length=100)  
    allocated_quantity = models.IntegerField()  
    allocated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allocations')  
    allocated_at = models.DateTimeField(auto_now_add=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_allocations_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_allocations_updated')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.allocated_quantity} {self.resource_type} allocated to {self.task.name} by {self.allocated_by.username}"

class ResourceReallocation(models.Model):
    original_allocation = models.ForeignKey(ResourceAllocation, on_delete=models.CASCADE, related_name='reallocations')  
    new_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reallocated_resources')  
    reallocated_quantity = models.IntegerField()  
    reason = models.TextField(blank=True, null=True)  
    reallocated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reallocation_actions')  
    reallocated_at = models.DateTimeField(auto_now_add=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_reallocations_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_reallocations_updated')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.reallocated_quantity} reallocated from {self.original_allocation.task.name} to {self.new_task.name} by {self.reallocated_by.username}"
    
    
class ScheduleAdjustment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='schedule_adjustments')  
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='schedule_adjustments')  
    adjustment_date = models.DateField()  
    new_date = models.DateField()  
    reason = models.TextField(blank=True, null=True)  
    adjusted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedule_adjustments')  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='schedule_adjustments_created')  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='schedule_adjustments_updated')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Adjustment for {self.milestone.name} on {self.adjustment_date} to {self.new_date}"
    
class DelayNotification(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='delay_notifications')
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE, related_name='notifications')
    notification_date = models.DateField(auto_now_add=True)
    message = models.TextField()
    updated_timeline = models.DateField()
    plan_to_mitigate = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delay_notifications_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='delay_notifications_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notification for {self.stakeholder.name} on {self.notification_date}"

class Contractor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contractors_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contractors_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PunchListItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='punch_list_items')
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True, related_name='punch_list_items')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateField(blank=True, null=True)
    fix_deadline = models.DateField()
    inspected = models.BooleanField(default=False)
    quality_meets_standards = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='punch_list_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='punch_list_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def mark_completed(self):
        if self.inspected and self.quality_meets_standards:
            self.status = 'Completed'
            self.resolved_at = models.DateField.auto_now
            self.save()
        else:
            raise ValueError("Item cannot be marked complete until inspected and meets quality standards.")

    def __str__(self):
        return f"{self.description} - {self.status} (Deadline: {self.fix_deadline})"

class SiteInspection(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='site_inspections')
    inspection_date = models.DateField(auto_now_add=True)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    observations = models.TextField()
    punch_list_items = models.ManyToManyField(PunchListItem, blank=True, related_name='site_inspections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='inspections_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='inspections_updated')

    def __str__(self):
        return f"Inspection on {self.inspection_date} by {self.inspector.username}"
    
class FinalInspection(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='final_inspections')
    inspection_date = models.DateField(auto_now_add=True)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    client_present = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    all_punch_items_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='final_inspections_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='final_inspections_updated')

    def verify_resolved_punch_items(self):
        if self.all_punch_items_resolved:
            self.save()
        else:
            raise ValueError("All punch list items must be resolved before conducting the final inspection.")

    def __str__(self):
        return f"Final Inspection for {self.project.name} on {self.inspection_date}"


class FinalClientSignOff(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='final_sign_offs')
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    sign_off_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_sign_offs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_sign_offs_updated')

    def __str__(self):
        return f"Sign-Off for {self.project.name} by {self.client.username} on {self.sign_off_date}"

class ProjectDocumentation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documentation')
    document_type = models.CharField(max_length=100)
    document_file = models.FileField(upload_to='project_documents/')
    issue_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_documentation_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_documentation_updated')

    def __str__(self):
        return f"{self.document_type} for {self.project.name} issued on {self.issue_date}"
 
class PostProjectReview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='post_reviews')
    review_date = models.DateField(auto_now_add=True)
    evaluation_summary = models.TextField()
    strengths = models.TextField(blank=True, null=True)
    areas_for_improvement = models.TextField(blank=True, null=True)
    lessons_learned = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post_project_reviews_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post_project_reviews_updated')

    def __str__(self):
        return f"Review for {self.project.name} on {self.review_date}"
    
class ProjectFinancialCloseout(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='financial_closeouts')
    closeout_date = models.DateField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    subcontractors_paid = models.BooleanField(default=False)
    purchase_orders_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='financial_closeouts_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='financial_closeouts_updated')

    def save(self, *args, **kwargs):
        self.total_profit = self.total_revenue - self.total_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Financial Closeout for {self.project.name} on {self.closeout_date}"   


class ProjectPerformanceReview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='performance_reviews')
    review_date = models.DateField(auto_now_add=True)
    original_budget = models.DecimalField(max_digits=10, decimal_places=2)
    actual_budget = models.DecimalField(max_digits=10, decimal_places=2)
    original_timeline = models.DurationField()
    actual_duration = models.DurationField()
    resource_utilization_percentage = models.FloatField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='performance_reviews_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='performance_reviews_updated')

    def budget_variance(self):
        return self.actual_budget - self.original_budget

    def duration_variance(self):
        return self.actual_duration - self.original_timeline

    def __str__(self):
        return f"Performance Review for {self.project.name} on {self.review_date}"

class ResourceUtilizationAnalysis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='resource_utilization_analyses')
    analysis_date = models.DateField(auto_now_add=True)
    total_labor_hours = models.DecimalField(max_digits=10, decimal_places=2)
    total_materials_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_equipment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    labor_utilization_percentage = models.FloatField()
    materials_utilization_percentage = models.FloatField()
    equipment_utilization_percentage = models.FloatField()
    recommendations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_utilization_analyses_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_utilization_analyses_updated')

    def __str__(self):
        return f"Resource Utilization Analysis for {self.project.name} on {self.analysis_date}"

class ClientFeedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='client_feedbacks')
    feedback_date = models.DateField(auto_now_add=True)
    client_name = models.CharField(max_length=255)
    satisfaction_rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_feedbacks_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_feedbacks_updated')

    def __str__(self):
        return f"Feedback from {self.client_name} for {self.project.name} on {self.feedback_date}" 


class InternalDepartment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='departments_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='departments_updated')

    def __str__(self):
        return self.name

class ProcurementNeed(models.Model):
    department = models.ForeignKey(InternalDepartment, on_delete=models.CASCADE, related_name='procurement_needs')
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    date_needed = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='procurement_needs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='procurement_needs_updated')

    def __str__(self):
        return f"{self.quantity} of {self.description} needed by {self.department.name} on {self.date_needed}"

class DocumentedRequirement(models.Model):
    procurement_need = models.ForeignKey(ProcurementNeed, on_delete=models.CASCADE, related_name='documented_requirements')
    requirement_description = models.TextField()
    quantity = models.PositiveIntegerField()
    timeline = models.DateField()
    budget_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    technical_specifications = models.TextField(blank=True, null=True)
    quality_specifications = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='documented_requirements_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='documented_requirements_updated')

    def __str__(self):
        return f"Requirement for {self.quantity} units of {self.requirement_description} (Budget: {self.budget_estimate})"

class StakeholderInput(models.Model):
    procurement_need = models.ForeignKey(ProcurementNeed, on_delete=models.CASCADE, related_name='stakeholder_inputs')
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE, related_name='inputs')
    input_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='stakeholder_inputs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='stakeholder_inputs_updated')

    def __str__(self):
        return f"Input from {self.stakeholder.role} on {self.procurement_need.description}"
    
    
class TenderDocument(models.Model):
    tender_type = models.CharField(max_length=3, choices=[('RFP', 'Request for Proposal'), ('RFQ', 'Request for Quotation')], default='RFP')
    title = models.CharField(max_length=255)
    description = models.TextField()
    prepared_by = models.ForeignKey(Stakeholder, on_delete=models.SET_NULL, null=True, related_name='tenders')
    issue_date = models.DateField()
    closing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tender_documents_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tender_documents_updated')

    def __str__(self):
        return f"{self.get_tender_type_display()} - {self.title}"

class TenderScope(models.Model):
    tender = models.ForeignKey(TenderDocument, on_delete=models.CASCADE, related_name='scopes')
    scope_description = models.TextField()
    technical_specifications = models.TextField()
    delivery_timeline = models.DateField()
    quality_standards = models.TextField()

    def __str__(self):
        return f"Scope for {self.tender.title}" 

class TenderSubmission(models.Model):
    tender = models.ForeignKey(TenderDocument, on_delete=models.CASCADE, related_name='submissions')
    vendor_name = models.CharField(max_length=255)
    proposal_details = models.TextField()
    submitted_on = models.DateField(auto_now_add=True)
    cost_estimate = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tender_submissions_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tender_submissions_updated')

    def __str__(self):
        return f"Submission by {self.vendor_name} for {self.tender.title}"
    
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    financial_standing = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    experience_years = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendors_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendors_updated')

    def __str__(self):
        return self.name

class PrequalificationQuestionnaire(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='pqqs')
    project_experience = models.TextField()
    financial_status = models.TextField()
    certifications = models.TextField()
    safety_records = models.TextField()
    other_qualifications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pqqs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pqqs_updated')

    def __str__(self):
        return f"Prequalification Questionnaire for {self.vendor.name}"

class VendorPrequalificationStatus(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='prequalification_status')
    prequalified = models.BooleanField(default=False)
    prequalification_date = models.DateField(null=True, blank=True)
    reasons_for_rejection = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_prequalification_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_prequalification_updated')

    def __str__(self):
        return f"Prequalification status for {self.vendor.name}"
    
class RFP_RFQ(models.Model):
    title = models.CharField(max_length=255)
    document_type = models.CharField(max_length=3, choices=[('RFP', 'Request for Proposal'), ('RFQ', 'Request for Quotation')], default='RFP')
    description = models.TextField()
    submission_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_email = models.EmailField()
    procurement_manager = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfq_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfq_updated')

    def __str__(self):
        return f"{self.title} ({self.document_type})"

class RFP_RFQDistribution(models.Model):
    rfp_rfq = models.ForeignKey(RFP_RFQ, on_delete=models.CASCADE, related_name='distributions')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='rfp_rfq_distributions')
    date_sent = models.DateTimeField()
    response_submitted = models.BooleanField(default=False)
    submission_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfp_rfq_distribution_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfp_rfq_distribution_updated')

    def __str__(self):
        return f"Distribution to {self.vendor.name} for {self.rfp_rfq.title}"

class RFP_RFQResponse(models.Model):
    distribution = models.OneToOneField(RFP_RFQDistribution, on_delete=models.CASCADE, related_name='response')
    response_document = models.FileField(upload_to='rfp_rfq_responses/')
    response_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfp_rfq_response_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rfp_rfq_response_updated')

    def __str__(self):
        return f"Response from {self.distribution.vendor.name} for {self.distribution.rfp_rfq.title}"

class VendorClarification(models.Model):
    rfp_rfq = models.ForeignKey(RFP_RFQ, on_delete=models.CASCADE, related_name='clarifications')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='clarifications')
    question = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_clarification_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_clarification_updated')

    def __str__(self):
        return f"Clarification from {self.vendor.name} for {self.rfp_rfq.title}"

class ClarificationResponse(models.Model):
    clarification = models.ForeignKey(VendorClarification, on_delete=models.CASCADE, related_name='responses')
    response = models.TextField()
    response_document = models.FileField(upload_to='clarification_responses/', null=True, blank=True)
    responded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clarification_response_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clarification_response_updated')

    def __str__(self):
        return f"Response to {self.clarification.vendor.name} for {self.clarification.rfp_rfq.title}"
    
class ClarificationDocument(models.Model):
    rfp_rfq = models.ForeignKey(RFP_RFQ, on_delete=models.CASCADE, related_name='clarification_documents')
    document = models.FileField(upload_to='clarification_documents/')
    issued_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clarification_document_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clarification_document_updated')

    def __str__(self):
        return f"Clarification document for {self.rfp_rfq.title} issued on {self.issued_at}"         

class VendorProposal(models.Model):
    rfp_rfq = models.ForeignKey(RFP_RFQ, on_delete=models.CASCADE, related_name='proposals')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='proposals')
    proposal_document = models.FileField(upload_to='vendor_proposals/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_compliant = models.BooleanField(default=False)
    compliance_remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_proposal_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vendor_proposal_updated')

    def __str__(self):
        return f"Proposal from {self.vendor.name} for {self.rfp_rfq.title}"

class ProposalCompliance(models.Model):
    proposal = models.ForeignKey(VendorProposal, on_delete=models.CASCADE, related_name='compliance_checks')
    certification_compliance = models.BooleanField(default=False)
    technical_spec_compliance = models.BooleanField(default=False)
    other_compliance = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_compliance_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_compliance_updated')

    def __str__(self):
        return f"Compliance check for {self.proposal.vendor.name}'s proposal"

class TechnicalEvaluation(models.Model):
    proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name='technical_evaluation')
    meets_technical_specs = models.BooleanField(default=False)
    quality_assessment = models.TextField(null=True, blank=True)
    additional_technical_remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='technical_evaluation_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='technical_evaluation_updated')

    def __str__(self):
        return f"Technical Evaluation for {self.proposal.vendor.name}'s Proposal"
    
    
class FinancialEvaluation(models.Model):
    proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name='financial_evaluation')
    quoted_price = models.DecimalField(max_digits=12, decimal_places=2)
    hidden_costs = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    delivery_schedule_assessment = models.TextField(null=True, blank=True)
    warranties_offered = models.TextField(null=True, blank=True)
    after_sales_service = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='financial_evaluation_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='financial_evaluation_updated')

    def __str__(self):
        return f"Financial Evaluation for {self.proposal.vendor.name}'s Proposal"

class RiskEvaluation(models.Model):
    proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name='risk_evaluation')
    vendor_reliability = models.CharField(max_length=255, null=True, blank=True)
    financial_stability = models.CharField(max_length=255, null=True, blank=True)
    logistical_issues = models.TextField(null=True, blank=True)
    overall_risk_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='risk_evaluation_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='risk_evaluation_updated')

    def __str__(self):
        return f"Risk Evaluation for {self.proposal.vendor.name}'s Proposal"
    
class ScoringCriteria(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight assigned to the criteria as a percentage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='scoring_criteria_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='scoring_criteria_updated')

    def __str__(self):
        return f"{self.name} (Weight: {self.weight}%)"


class ProposalScoring(models.Model):
    proposal = models.ForeignKey(VendorProposal, on_delete=models.CASCADE, related_name='proposal_scores')
    criteria = models.ForeignKey(ScoringCriteria, on_delete=models.CASCADE, related_name='proposal_scores')
    score = models.DecimalField(max_digits=5, decimal_places=2, help_text="Score given for this criteria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_scores_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_scores_updated')

    def __str__(self):
        return f"Score for {self.proposal.vendor.name} on {self.criteria.name}: {self.score}"
    
class ProposalEvaluation(models.Model):
    proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name='evaluation')
    total_score = models.DecimalField(max_digits=6, decimal_places=2, help_text="Total weighted score for the proposal")
    shortlisted = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_evaluations_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='proposal_evaluations_updated')

    def __str__(self):
        return f"Evaluation for {self.proposal.vendor.name} (Shortlisted: {self.shortlisted})"

class StakeholderEvaluation(models.Model):
    evaluation = models.ForeignKey(ProposalEvaluation, on_delete=models.CASCADE, related_name='stakeholder_feedback')
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE, related_name='evaluations')
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='stakeholder_evaluations_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='stakeholder_evaluations_updated')

    def __str__(self):
        return f"Feedback from {self.stakeholder.name} on {self.evaluation.proposal.vendor.name}'s Proposal"


class NegotiationTerm(models.Model):
    description = models.CharField(max_length=255)
    proposed_value = models.CharField(max_length=255, help_text="Vendor's initial proposal for the term")
    negotiated_value = models.CharField(max_length=255, help_text="Final agreed value after negotiations")
    vendor_proposal = models.ForeignKey(VendorProposal, on_delete=models.CASCADE, related_name='negotiation_terms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_terms_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_terms_updated')

    def __str__(self):
        return f"{self.description} - Proposed: {self.proposed_value}, Negotiated: {self.negotiated_value}"


class NegotiationStakeholder(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='negotiation_stakeholders')
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE, related_name='negotiation_involvements')
    vendor_proposal = models.ForeignKey(VendorProposal, on_delete=models.CASCADE, related_name='negotiation_stakeholders')
    feedback = models.TextField(null=True, blank=True, help_text="Feedback or concerns raised by the stakeholder during negotiations")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_stakeholders_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_stakeholders_updated')

    def __str__(self):
        return f"{self.team.name} - Stakeholder: {self.stakeholder.name}"
    
class NegotiationSummary(models.Model):
    vendor_proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name='negotiation_summary')
    summary = models.TextField(help_text="Summary of the negotiation process")
    final_terms_agreed = models.BooleanField(default=False, help_text="Indicates if the final terms were agreed upon")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_summaries_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='negotiation_summaries_updated')

    def __str__(self):
        return f"Negotiation Summary for {self.vendor_proposal.vendor.name}"


class FinalVendorSelection(models.Model):
    vendor_proposal = models.ForeignKey(VendorProposal, on_delete=models.CASCADE, related_name='final_selections')
    selection_date = models.DateField(auto_now_add=True)
    justification = models.TextField(help_text="Justification for vendor selection, including considerations like price, quality, etc.")
    approved_by = models.CharField(max_length=100, help_text="Name of the person or committee who approved the selection")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='final_vendor_selections_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='final_vendor_selections_updated')

    def __str__(self):
        return f"Final Vendor Selection: {self.vendor_proposal.vendor.name} on {self.selection_date}"



class Contract(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    scope_of_work = models.TextField()
    pricing = models.DecimalField(max_digits=12, decimal_places=2)
    payment_terms = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    signed_by_client = models.BooleanField(default=False)
    signed_by_contractor = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], default='draft')

    def __str__(self):
        return f"Contract for {self.project.name} with {self.contractor.name}"

class ContractExecution(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='executions')
    execution_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('in_progress', 'In Progress'), ('completed', 'Completed'), ('terminated', 'Terminated')], default='in_progress')
    notes = models.TextField(null=True, blank=True, help_text="Any notes or comments related to the execution process")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contract_executions_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contract_executions_updated')

    def __str__(self):
        return f"Contract Execution for {self.contract.contract_number} - Status: {self.status}"



class LegalReview(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='legal_review')
    review_date = models.DateField(auto_now_add=True)
    reviewed_by = models.CharField(max_length=100, help_text="Name of the legal reviewer")
    approval_status = models.CharField(max_length=50, choices=[('approved', 'Approved'), ('revised', 'Revised'), ('not_approved', 'Not Approved')], default='approved')
    comments = models.TextField(null=True, blank=True, help_text="Comments or notes from the legal review")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='legal_reviews_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='legal_reviews_updated')

    def __str__(self):
        return f"Legal Review for Contract #{self.contract.contract_number} by {self.reviewed_by} on {self.review_date}"
    
class ContractAward(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='contract_award')
    selected_vendor = models.ForeignKey(FinalVendorSelection, on_delete=models.CASCADE, related_name='contract_awards')
    award_date = models.DateField(auto_now_add=True)
    notification_sent_to_vendor = models.BooleanField(default=False)
    notification_sent_to_bidders = models.BooleanField(default=False)
    feedback_to_bidders = models.TextField(null=True, blank=True, help_text="Feedback provided to unsuccessful bidders")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contract_awards_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contract_awards_updated')

    def notify_vendor(self):
        self.notification_sent_to_vendor = True
        self.save()

    def notify_bidders(self):
        self.notification_sent_to_bidders = True
        self.save()

    def __str__(self):
        return f"Contract Award for {self.contract.contract_number} to {self.selected_vendor.vendor_proposal.vendor.name} on {self.award_date}"
    
class PurchaseOrder(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='purchase_orders')
    order_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_service_description = models.TextField(help_text="Description of products or services ordered")
    quantity = models.PositiveIntegerField(help_text="Quantity of items ordered")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total price for the order", editable=False)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='purchase_orders_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='purchase_orders_updated')

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"PO #{self.order_number} - {self.contract.contract_number}"

class Shipment(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='shipments')
    shipment_number = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shipments_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shipments_updated')

    def __str__(self):
        return f"Shipment #{self.shipment_number} for {self.purchase_order.order_number}"
    
class Invoice(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='invoices')
    vendor_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Paid', 'Paid'),
        ('Rejected', 'Rejected'),
    ], default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invoices_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invoices_updated')

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.vendor_name}"
    
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('Bank Transfer', 'Bank Transfer'),
        ('Credit Card', 'Credit Card'),
        ('Cash', 'Cash'),
        ('Check', 'Check'),
    ])
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone = models.CharField(max_length=255)
    payment_due = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'), ('Paid', 'Paid'), ('Delayed', 'Delayed')))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='payments_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='payments_updated')

    def __str__(self):
        return f"Payment of {self.amount_paid} for {self.invoice.invoice_number}"

class SupplierPerformanceEvaluation(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='performance_evaluations')
    project = models.CharField(max_length=255)
    evaluation_date = models.DateField()
    
    delivery_timeliness = models.IntegerField()
    quality_of_products_services = models.IntegerField()
    overall_execution = models.IntegerField()
    
    comments = models.TextField(blank=True, null=True)
    
    average_score = models.FloatField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SupplierPerformanceEvaluation_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SupplierPerformanceEvaluation_updated')

    def save(self, *args, **kwargs):
        self.average_score = (self.delivery_timeliness + 
                              self.quality_of_products_services + 
                              self.overall_execution) / 3
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Performance Evaluation for {self.vendor.name} on {self.project} - {self.evaluation_date}"    
    
    
class BidQualification(models.Model):
    rfp_rfq_title = models.CharField(max_length=255)
    response_due_date = models.DateField()
    alignment_with_strategy = models.TextField()
    capacity_evaluation = models.TextField()
    is_qualified = models.BooleanField(default=False)
    
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rfp_rfq_title
    
class BidProposal(models.Model):
    rfp_rfq_title = models.CharField(max_length=255)
    technical_proposal = models.TextField()
    financial_proposal = models.TextField()
    internal_collaboration = models.TextField()
    submission_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='draft')
    
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Proposal for {self.rfp_rfq_title} - Status: {self.status}" 
    
class BidSubmission(models.Model):
    bid_proposal = models.ForeignKey(BidProposal, on_delete=models.CASCADE)
    submission_date = models.DateField()
    submission_method = models.CharField(max_length=50, choices=[('portal', 'Online Portal'), ('email', 'Email'), ('physical', 'Physical Delivery')])
    documents_included = models.BooleanField(default=False)
    certificate_documentation = models.FileField(upload_to='certificates/', blank=True, null=True)
    technical_specifications = models.FileField(upload_to='technical_specs/', blank=True, null=True)
    cost_breakdown = models.FileField(upload_to='cost_breakdowns/', blank=True, null=True)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bid Submission for {self.bid_proposal.rfp_rfq_title} on {self.submission_date}"  
    
class PostSubmissionFollowUp(models.Model):
    bid_submission = models.ForeignKey(BidSubmission, on_delete=models.CASCADE)
    follow_up_date = models.DateField()
    communication_method = models.CharField(max_length=50, choices=[('email', 'Email'), ('phone', 'Phone Call'), ('meeting', 'In-Person Meeting')])
    client_response = models.TextField(blank=True, null=True)
    clarification_requested = models.BooleanField(default=False)
    additional_info_provided = models.TextField(blank=True, null=True)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Follow-up for {self.bid_submission.bid_proposal.rfp_rfq_title} on {self.follow_up_date}"     

class NegotiationAndAward(models.Model):
    bid_submission = models.ForeignKey(BidSubmission, on_delete=models.CASCADE)
    negotiation_date = models.DateField()
    negotiation_notes = models.TextField(blank=True, null=True)
    final_terms = models.TextField(blank=True, null=True)
    awarded = models.BooleanField(default=False)
    internal_preparation_started = models.BooleanField(default=False)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Negotiation for {self.bid_submission.bid_proposal.rfp_rfq_title} on {self.negotiation_date}"
    

class OpportunityIdentification(models.Model):
    tender_title = models.CharField(max_length=255)
    tender_type = models.CharField(max_length=50)
    identification_date = models.DateField()
    source = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    relevant_to_company = models.BooleanField(default=False)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tender_title        
    
class BidNoBidDecision(models.Model):
    opportunity = models.ForeignKey(OpportunityIdentification, on_delete=models.CASCADE)
    decision_date = models.DateField()
    is_bid = models.BooleanField(default=False)
    rationale = models.TextField(blank=True, null=True)
    profitability_assessment = models.TextField(blank=True, null=True)
    resource_capacity_assessment = models.TextField(blank=True, null=True)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{'Bid' if self.is_bid else 'No Bid'} Decision for {self.opportunity.tender_title}"  
    
class ProposalPreparation(models.Model):
    opportunity = models.ForeignKey(OpportunityIdentification, on_delete=models.CASCADE)
    proposal_title = models.CharField(max_length=255)
    technical_solutions = models.TextField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    timelines = models.TextField()
    value_propositions = models.TextField()
    compliance_check = models.BooleanField(default=False)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proposal_title   
    
class SubmissionFollowUp(models.Model):
    proposal = models.ForeignKey(ProposalPreparation, on_delete=models.CASCADE)
    submission_date = models.DateField()
    follow_up_date = models.DateField(null=True, blank=True)
    follow_up_notes = models.TextField(blank=True)
    negotiation_engaged = models.BooleanField(default=False)
    revisions_required = models.BooleanField(default=False)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Submission for {self.proposal.proposal_title} on {self.submission_date}"   
    
class ContractAwardExecution(models.Model):
    contract_title = models.CharField(max_length=255)
    project_manager = models.ForeignKey(Project, on_delete=models.CASCADE)
    execution_status = models.CharField(max_length=100)
    delivery_commitments = models.TextField()
    execution_notes = models.TextField(blank=True)

    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Execution for {self.contract_title} by {self.project_manager} - Status: {self.execution_status}"  
    

class TenderProposalManagement(models.Model):
    rfp_rfq_title = models.CharField(max_length=255)
    issued_date = models.DateField()
    response_deadline = models.DateField()
    response_tracking = models.TextField(blank=True)
    documentation = models.FileField(upload_to='tender_documents/', blank=True)
    
    issued_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rfp_rfq_title} - Issued on {self.issued_date}"




class LeadSource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
class Lead(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    project_description = models.TextField()
    source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('qualified', 'Qualified'), ('disqualified', 'Disqualified')])
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    urgency = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    decision_maker = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey('SalesRepresentative', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
class SalesRepresentative(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class ClientInteractionType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name
class ClientInteraction(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    interaction_type = models.ForeignKey(ClientInteractionType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    follow_up_date = models.DateTimeField(null=True, blank=True)
    engagement_metrics = models.JSONField(null=True, blank=True) 

    def __str__(self):
        return f"{self.interaction_type} with {self.lead.name}"
class SalesStage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    stage = models.ForeignKey(SalesStage, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    probability = models.IntegerField() 
    expected_close_date = models.DateField()
    assigned_to = models.ForeignKey(SalesRepresentative, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Opportunity with {self.lead.name} - {self.stage.name}"
class Proposal(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    proposal_file = models.FileField(upload_to='proposals/') 
    status = models.CharField(max_length=50, choices=[('sent', 'Sent'), ('viewed', 'Viewed'), ('negotiation', 'In Negotiation'), ('approved', 'Approved')])
    negotiation_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Proposal for {self.opportunity.lead.name}"

    
class ProjectCommunication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    communication_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    file_attachment = models.FileField(upload_to='communications/', null=True, blank=True) 

    def __str__(self):
        return f"Communication for {self.project.project_name}"
class ClientFollowUp(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    follow_up_date = models.DateField()
    message = models.TextField()
    action_taken = models.CharField(max_length=255, choices=[('email_sent', 'Email Sent'), ('called', 'Called')])

    def __str__(self):
        return f"Follow-up for {self.project.project_name} on {self.follow_up_date}"
class ClientSatisfactionSurvey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sent_date = models.DateField(auto_now_add=True)
    client_feedback = models.TextField()
    score = models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')])

    def __str__(self):
        return f"Survey for {self.project.project_name}"



class Subcontractor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    qualification_documents = models.FileField(upload_to='qualifications/', blank=True, null=True)
    certification = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    financial_stability_rating = models.IntegerField()  
    references = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=(('Prequalified', 'Prequalified'), ('Pending', 'Pending'), ('Rejected', 'Rejected')))
    date_prequalified = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Expertise(models.Model):
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    area_of_expertise = models.CharField(max_length=255)   
    certifications = models.CharField(max_length=255, blank=True, null=True)
    performance_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) 
    
    def __str__(self):
        return f"{self.subcontractor.name} - {self.area_of_expertise}"

    
class Bid(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=12, decimal_places=2)
    bid_submission_date = models.DateField()
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')))
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Bid by {self.subcontractor.name} for {self.project.name}"
    
class SubcontractorContract(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    contract_file = models.FileField(upload_to='contracts/')
    signed_date = models.DateField()
    payment_terms = models.TextField()  
    insurance_requirements = models.TextField(blank=True, null=True)
    change_order_provision = models.TextField(blank=True, null=True)
    termination_conditions = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Contract for {self.subcontractor.name} in {self.project.name}"

class PerformanceReport(models.Model):
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    report_date = models.DateField()
    tasks_completed = models.IntegerField(default=0)
    issues_encountered = models.TextField(blank=True, null=True)
    safety_compliance = models.BooleanField(default=True)
    site_photos = models.ImageField(upload_to='site_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"Performance Report for {self.subcontractor.name} on {self.report_date}"

    
class ChangeOrder(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    requestor = models.CharField(max_length=255) 
    description = models.TextField()
    change_reason = models.TextField()
    impact_on_scope = models.TextField()
    cost_impact = models.DecimalField(max_digits=12, decimal_places=2)
    time_impact = models.IntegerField(help_text="Time impact in days")
    status = models.CharField(max_length=50, choices=[
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('implemented', 'Implemented')
    ], default='submitted')
    submitted_date = models.DateField(auto_now_add=True)
    approved_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Change Order {self.id} for Contract {self.contract.id}"    


class ProjectCloseout(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    final_inspection_date = models.DateField()
    punch_list_items = models.TextField(blank=True, null=True)
    punch_list_completed = models.BooleanField(default=False)
    final_payment = models.DecimalField(max_digits=12, decimal_places=2)
    closeout_documents = models.FileField(upload_to='closeout_documents/', blank=True, null=True)
    
    def __str__(self):
        return f"Closeout for {self.subcontractor.name} in {self.project.name}"



    
class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    mobile_device_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username



class TeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE) 
    permissions = models.TextField()  

    def __str__(self):
        return f"{self.user.username} - {self.role} ({self.project.name})"

class DailyProgressReport(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now_add=True)
    description = models.TextField()  
    worker_count = models.IntegerField()
    machinery_in_use = models.CharField(max_length=255)
    materials_used = models.TextField()  
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Progress percentage of the task")  
    issues_encountered = models.TextField(blank=True, null=True)  
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_reports') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Report for {self.task.name} - {self.report_date}"


    def __str__(self):
        return f"Progress Report for {self.task.name} on {self.report_date} - Progress: {self.progress_percentage}%"
    
class PhotoDocumentation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task_photos/')
    description = models.TextField(blank=True, null=True)
    geo_tag = models.CharField(max_length=255, blank=True, null=True)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.task.name} - {self.timestamp}"
    


class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue_type = models.CharField(
        max_length=50,
        choices=[
            ('Safety', 'Safety'),
            ('Quality', 'Quality'),
            ('Equipment', 'Equipment'),
            ('Other', 'Other')
        ]
    )
    description = models.TextField()
    photo = models.ImageField(upload_to='issue_photos/', blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Open', 'Open'),
            ('In Progress', 'In Progress'),
            ('Resolved', 'Resolved')
        ],
        default='Open'
    )
    assigned_to = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue: {self.issue_type} - Status: {self.status}"    
    
class Message(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(CustomUser, related_name='messages_received')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.project.name}"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}"
    

class StockAdjustment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    adjusted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity_adjusted = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    adjustment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Stock Adjustment for {self.material.name}"

class StockReplenishmentRequest(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity_requested = models.DecimalField(max_digits=10, decimal_places=2)
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Replenishment Request for {self.material.name} - {self.project.name}"





class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Warehouse(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.IntegerField() 
    
    def __str__(self):
        return self.location

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=10)
    safety_stock = models.IntegerField(default=5)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name


class StockEntry(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=10, choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')])
    date = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.item.name} - {self.movement_type} - {self.quantity}"


class Requisition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    requested_by = models.CharField(max_length=255)
    date_requested = models.DateTimeField(default=now)
    date_fulfilled = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Requisition for {self.item.name}"


class InventoryAudit(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    audit_date = models.DateTimeField(default=now)
    physical_count = models.IntegerField()
    system_count = models.IntegerField()
    discrepancy = models.IntegerField()
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Audit for {self.item.name} on {self.audit_date}"
    

class EquipmentCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255, unique=True)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=255, choices=[('New', 'New'), ('Used', 'Used')])
    location = models.ForeignKey(Warehouse, on_delete=models.CASCADE) 
    status = models.CharField(max_length=255, choices=[('Available', 'Available'), ('In Use', 'In Use'), ('Under Maintenance', 'Under Maintenance')])

    def __str__(self):
        return self.name


class EquipmentAssignment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=255)
    assigned_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.equipment.name} assigned to {self.assigned_to}"


class EquipmentMaintenance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField(default=now)
    maintenance_type = models.CharField(max_length=255, choices=[('Preventive', 'Preventive'), ('Corrective', 'Corrective')])
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Maintenance for {self.equipment.name} on {self.maintenance_date}"


class EquipmentAudit(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    audit_date = models.DateTimeField(default=now)
    condition = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Audit for {self.equipment.name} on {self.audit_date}"



class AssetCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits=12, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=[('Active', 'Active'), ('Retired', 'Retired')])

    def __str__(self):
        return self.name



class AssetMaintenance(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField(default=now)
    maintenance_type = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Maintenance for {self.asset.name}"



class Depreciation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    depreciation_date = models.DateTimeField(default=now)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"Depreciation for {self.asset.name}"



class AssetAudit(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    audit_date = models.DateTimeField(default=now)
    condition = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return f"Audit for {self.asset.name}"




class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=255)
    account_type = models.CharField(
        max_length=20,
        choices=[
            ('asset', 'Asset'),
            ('liability', 'Liability'),
            ('equity', 'Equity'),
            ('revenue', 'Revenue'),
            ('expense', 'Expense')
        ]
    )
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} ({self.account_type})"

class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=5)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, help_text="Exchange rate to the base currency")

    def __str__(self):
        return self.name
    



class Budget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    total_budget = models.DecimalField(max_digits=15, decimal_places=2)
    allocated_budget = models.DecimalField(max_digits=15, decimal_places=2)
    remaining_budget = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Budget for {self.project.name}"

class CostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class CostEstimation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(CostCategory, on_delete=models.SET_NULL, null=True)
    estimated_cost = models.DecimalField(max_digits=15, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    forecast_cost = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} for {self.project.name}"



class FinancialTransaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=10,
        choices=[
            ('debit', 'Debit'),
            ('credit', 'Credit')
        ]
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} in {self.project.name} to {self.account.name}"

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="expenses")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    approved_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Expense of {self.amount} for {self.project.name}"

class Revenue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    received_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Revenue of {self.amount} for {self.project.name}"




class MilestoneBilling(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    invoiced = models.BooleanField(default=False)

    def __str__(self):
        return f"Milestone Billing for {self.project.name}: {self.milestone_name}"




class RiskCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class RiskOwner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    


class Risk(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    risk_category = models.ForeignKey(RiskCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    risk_type = models.CharField(
        max_length=50,
        choices=[
            ('financial', 'Financial'),
            ('operational', 'Operational'),
            ('compliance', 'Compliance'),
            ('strategic', 'Strategic'),
            ('safety', 'Safety')
        ]
    )
    date_identified = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(RiskOwner, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='Open')

    def __str__(self):
        return f"{self.name} ({self.project.name})"

class RiskAssessment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    risk = models.OneToOneField(Risk, on_delete=models.CASCADE)
    probability = models.IntegerField(
        choices=[
            (1, 'Very Low'),
            (2, 'Low'),
            (3, 'Medium'),
            (4, 'High'),
            (5, 'Very High'),
        ]
    )
    impact = models.IntegerField(
        choices=[
            (1, 'Very Low'),
            (2, 'Low'),
            (3, 'Medium'),
            (4, 'High'),
            (5, 'Very High'),
        ]
    )
    overall_risk_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def calculate_risk_score(self):
        """Calculates the overall risk score based on probability and impact."""
        self.overall_risk_score = self.probability * self.impact
        self.save()

    def __str__(self):
        return f"Assessment for {self.risk.name}"

    def save(self, *args, **kwargs):
        """Overriding the save method to calculate risk score before saving."""
        self.calculate_risk_score()
        super().save(*args, **kwargs)


class MitigationStrategy(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    strategy = models.TextField()
    mitigation_owner = models.ForeignKey(RiskOwner, on_delete=models.SET_NULL, null=True, related_name="mitigation_owner")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Mitigation for {self.risk.name}"

class MitigationAction(models.Model):
    mitigation_strategy = models.ForeignKey(MitigationStrategy, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=255)
    action_description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Action {self.action_name} for {self.mitigation_strategy.risk.name}"



class RiskReview(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('Mitigated', 'Mitigated'), ('Closed', 'Closed')])
    comments = models.TextField(null=True, blank=True)
    reviewed_by = models.ForeignKey(RiskOwner, on_delete=models.SET_NULL, null=True, related_name="reviewed_by")

    def __str__(self):
        return f"Review of {self.risk.name} on {self.review_date}"





class SafetyOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.project.name}'

class QualityInspector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.project.name}'



class SafetyPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Safety Plan for {self.project.name}"

class QualityControlPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField() 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quality Plan for {self.project.name}"

class LegalRequirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    requirement_type = models.CharField(max_length=255) 

    def __str__(self):
        return f"Legal Requirement for {self.project.name}: {self.requirement_type}"



class Inspection(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    inspection_type = models.CharField(
        max_length=50, 
        choices=[
            ('Safety', 'Safety'),
            ('Quality', 'Quality'),
        ]
    )
    date = models.DateField()
    checklist = models.TextField()  
    findings = models.TextField()  

    def __str__(self):
        return f"{self.inspection_type} Inspection for {self.project.name} on {self.date}"

class ComplianceMonitor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    compliance_type = models.CharField(max_length=50) 
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Compliant', 'Compliant'), ('Non-compliant', 'Non-compliant')])
    date = models.DateField()

    def __str__(self):
        return f"{self.compliance_type} Compliance for {self.project.name} on {self.date}"

class IncidentReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(
        max_length=50,
        choices=[
            ('Safety', 'Safety'),
            ('Quality', 'Quality'),
        ]
    )
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    immediate_action = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f"Incident ({self.incident_type}) for {self.project.name} by {self.reported_by.get_full_name()}"

class Investigation(models.Model):
    incident = models.OneToOneField(IncidentReport, on_delete=models.CASCADE)
    investigator = models.ForeignKey(User, on_delete=models.CASCADE)
    findings = models.TextField()
    root_cause = models.TextField()
    investigation_date = models.DateField()

    def __str__(self):
        return f"Investigation for Incident {self.incident.id} by {self.investigator.get_full_name()}"

class CorrectiveAction(models.Model):
    incident = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    description = models.TextField()
    action_taken_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_taken = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Corrective Action for Incident {self.incident.id}"


class Audit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    audit_type = models.CharField(
        max_length=50,
        choices=[
            ('Safety', 'Safety'),
            ('Quality', 'Quality'),
        ]
    )
    conducted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    findings = models.TextField()

    def __str__(self):
        return f"{self.audit_type} Audit for {self.project.name}"

class CorrectivePreventiveAction(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    description = models.TextField()
    date_taken = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"CAPA for Audit {self.audit.id}"



class FinalReview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review_type = models.CharField(max_length=50, choices=[('Safety', 'Safety'), ('Quality', 'Quality')])
    review_details = models.TextField()
    conducted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Final {self.review_type} Review for {self.project.name}"

class CloseoutDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255) 
    file = models.FileField(upload_to='closeout_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Closeout Document for {self.project.name} - {self.document_type}"



class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name




class ContractMilestone(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Milestone: {self.name} for Contract {self.contract.id}"
    


class ChangeOrderApproval(models.Model):
    change_order = models.OneToOneField(ChangeOrder, on_delete=models.CASCADE)
    approved_by = models.CharField(max_length=255)
    approval_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Approval for Change Order {self.change_order.id}"

class ChangeOrderImplementation(models.Model):
    change_order = models.OneToOneField(ChangeOrder, on_delete=models.CASCADE)
    implementation_details = models.TextField()
    implementation_date = models.DateField()
    new_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Implementation for Change Order {self.change_order.id}"
class ContractCloseout(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    closeout_date = models.DateField()
    final_review_notes = models.TextField()
    completed_documents = models.FileField(upload_to='contract_closeouts/')
    signed_off_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Closeout for Contract {self.contract.id}"
class Document(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    change_order = models.ForeignKey(ChangeOrder, null=True, blank=True, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='documents/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.document_name
class AuditLog(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    change_order = models.ForeignKey(ChangeOrder, null=True, blank=True, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    action_by = models.CharField(max_length=255)
    action_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Audit Log for Contract {self.contract.id} - {self.action}"
