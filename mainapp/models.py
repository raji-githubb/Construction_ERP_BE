from django.db import models
from django.contrib.auth.models import User

# MS setup models
class MSRegistration(models.Model):
    mservice_id = models.CharField(max_length=20,primary_key=True)
    mservice_name = models.CharField(max_length=100)
    arguments = models.JSONField(null=True,blank=True)
    arguments_list = models.TextField(null=True,blank=True)
    required_parameter = models.TextField(null=True,blank=True)
    optional_parameter = models.TextField(null=True,blank=True)
    is_authenticate = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
	
    def formatted_mservice_name(self):
        # Replace underscores with spaces in mservice_name
        return self.mservice_name.replace('_', ' ')
    def __str__(self):
        return str(self.mservice_id)
    
class ModuleRegistration(models.Model):
    module_name = models.CharField(max_length=250,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.module_name)

class MsToModuleMapping(models.Model):
    mservice_id = models.OneToOneField(MSRegistration,on_delete=models.CASCADE,related_name='ms_id')
    module_id = models.ForeignKey(ModuleRegistration,on_delete=models.CASCADE,related_name='module_id')

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.module_id)	

class User(models.Model):
	first_name = models.CharField(max_length=30,)
	middle_name = models.CharField(max_length=30,blank=True, null=True ,)
	last_name = models.CharField(max_length=30,)
	dob = models.DateField(blank=True, null=True)
	phone_number = models.PositiveBigIntegerField(blank=True, null=True)
	def __str__(self):
		return self.first_name

class AssetCategory(models.Model):
	name = models.CharField(max_length=255,)
	def __str__(self):
		return self.name

class Warehouse(models.Model):
	location = models.CharField(max_length=255,)
	capacity = models.IntegerField()
	def __str__(self):
		return self.location

class Subcontractor(models.Model):
	name = models.CharField(max_length=255,)
	email = models.EmailField()
	phone = models.CharField(max_length=15,)
	address = models.TextField()
	certification = models.CharField(max_length=255,)
	experience_years = models.IntegerField()
	financial_stability_rating = models.IntegerField()
	references = models.TextField(blank=True, null=True)
	status = models.CharField(max_length=100,)
	date_prequalified = models.DateField(blank=True, null=True)
	def __str__(self):
		return self.name

class OpportunityIdentification(models.Model):
	tender_title = models.CharField(max_length=255,)
	tender_type = models.CharField(max_length=50,)
	identification_date = models.DateField()
	source = models.CharField(max_length=255,blank=True, null=True ,)
	description = models.TextField(blank=True, null=True)
	relevant_to_company = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='OpportunityIdentificationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='OpportunityIdentificationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.tender_title

class BidProposal(models.Model):
	rfp_rfq_title = models.CharField(max_length=255,)
	technical_proposal = models.TextField()
	financial_proposal = models.TextField()
	internal_collaboration = models.TextField()
	submission_date = models.DateField()
	status = models.CharField(max_length=50,choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],default="draft," )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidProposalcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidProposalupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.rfp_rfq_title

class Currency(models.Model):
	name = models.CharField(max_length=255,)
	symbol = models.CharField(max_length=5,)
	exchange_rate = models.DecimalField(max_digits=10, decimal_places=4,)
	def __str__(self):
		return self.name

class ClientInteractionType(models.Model):
	type_name = models.CharField(max_length=100,)
	def __str__(self):
		return self.type_name

class CostCategory(models.Model):
	name = models.CharField(max_length=255,)
	description = models.TextField()
	def __str__(self):
		return self.name

class EquipmentCategory(models.Model):
	name = models.CharField(max_length=255,)
	def __str__(self):
		return self.name

class Account(models.Model):
	name = models.CharField(max_length=255,)
	account_type = models.CharField(max_length=20,)
	balance = models.DecimalField(max_digits=15, decimal_places=2,default="0.0," )
	def __str__(self):
		return self.name

class ItemCategory(models.Model):
	name = models.CharField(max_length=255,)
	def __str__(self):
		return self.name

class Supplier(models.Model):
	name = models.CharField(max_length=255,)
	contact_person = models.CharField(max_length=255,)
	phone = models.CharField(max_length=15,)
	email = models.EmailField()
	address = models.TextField()
	def __str__(self):
		return self.name

class LeadSource(models.Model):
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name

class SalesRepresentative(models.Model):
	name = models.CharField(max_length=255,)
	email = models.EmailField()
	phone = models.CharField(max_length=20,)
	def __str__(self):
		return self.name

class RiskOwner(models.Model):
	name = models.CharField(max_length=255,)
	email = models.EmailField()
	phone = models.CharField(max_length=15,)
	def __str__(self):
		return self.name

class SalesStage(models.Model):
	name = models.CharField(max_length=255,)
	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=255,)
	contact_person = models.CharField(max_length=255,)
	phone = models.CharField(max_length=15,)
	email = models.EmailField()
	address = models.TextField()
	def __str__(self):
		return self.name

class RiskCategory(models.Model):
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name

class Contractor(models.Model):
	name = models.CharField(max_length=255,)
	contact_person = models.CharField(max_length=255,)
	contact_email = models.EmailField()
	contact_phone = models.CharField(max_length=20,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Contractorcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Contractorupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class DelayCause(models.Model):
	cause = models.CharField(max_length=255,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DelayCausecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DelayCauseupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.cause

class Individual(models.Model):
	name = models.CharField(max_length=255,)
	skills = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Individualcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Individualupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class InternalDepartment(models.Model):
	name = models.CharField(max_length=255,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='InternalDepartmentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='InternalDepartmentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	projected_end_date = models.DateField(blank=True, null=True)
	progress = models.IntegerField(default="0.0," )
	budget = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)
	location = models.CharField(max_length=255,)
	manager = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_manager')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Projectcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Projectupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Resource(models.Model):
	resource_type = models.CharField(max_length=100,)
	description = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Resourcecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Resourceupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.resource_type

class RFPRFQ(models.Model):
	title = models.CharField(max_length=255,)
	document_type = models.CharField(max_length=3,choices=[('RFP', 'Rfp'), ('RFQ', 'Rfq')],default="RFP," )
	description = models.TextField()
	submission_deadline = models.DateField()
	contact_email = models.EmailField()
	procurement_manager = models.CharField(max_length=255,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class Role(models.Model):
	name = models.CharField(max_length=100,)
	description = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Rolecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Roleupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class ScoringCriteria(models.Model):
	name = models.CharField(max_length=255,)
	weight = models.DecimalField(max_digits=5, decimal_places=2,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ScoringCriteriacreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ScoringCriteriaupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class TaskCategory(models.Model):
	category_name = models.CharField(max_length=30,unique=True ,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskCategorycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskCategoryupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.category_name

class TaskDurationEstimation(models.Model):
	estimated_duration = models.PositiveIntegerField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskDurationEstimationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskDurationEstimationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pk

class TaskPriority(models.Model):
	priority_level = models.CharField(max_length=10,unique=True ,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskPrioritycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskPriorityupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.priority_level

class Team(models.Model):
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Teamcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Teamupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Vendor(models.Model):
	name = models.CharField(max_length=255,)
	contact_person = models.CharField(max_length=255,)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15,)
	address = models.TextField()
	financial_standing = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)
	experience_years = models.PositiveIntegerField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Vendorcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Vendorupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Asset(models.Model):
	name = models.CharField(max_length=255,)
	category = models.ForeignKey('AssetCategory', on_delete=models.CASCADE, related_name='%(class)s_category')
	purchase_date = models.DateField()
	purchase_cost = models.DecimalField(max_digits=12, decimal_places=2,)
	depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2,)
	location = models.ForeignKey('Warehouse', on_delete=models.CASCADE, related_name='%(class)s_location')
	assigned_to = models.CharField(max_length=255,blank=True, null=True ,)
	status = models.CharField(max_length=255,choices=[('Active', 'Active'), ('Retired', 'Retired')],)
	def __str__(self):
		return self.name

class Expertise(models.Model):
	subcontractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, related_name='%(class)s_subcontractor')
	area_of_expertise = models.CharField(max_length=255,)
	certifications = models.CharField(max_length=255,blank=True, null=True ,)
	performance_rating = models.DecimalField(max_digits=5, decimal_places=2,default="0.0," )
	def __str__(self):
		return self.area_of_expertise

class BidNoBidDecision(models.Model):
	opportunity = models.ForeignKey('OpportunityIdentification', on_delete=models.CASCADE, related_name='%(class)s_opportunity')
	decision_date = models.DateField()
	is_bid = models.BooleanField(default=False, )
	rationale = models.TextField(blank=True, null=True)
	profitability_assessment = models.TextField(blank=True, null=True)
	resource_capacity_assessment = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidNoBidDecisioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidNoBidDecisionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.decision_date

class ProposalPreparation(models.Model):
	opportunity = models.ForeignKey('OpportunityIdentification', on_delete=models.CASCADE, related_name='%(class)s_opportunity')
	proposal_title = models.CharField(max_length=255,)
	technical_solutions = models.TextField()
	pricing = models.DecimalField(max_digits=10, decimal_places=2,)
	timelines = models.TextField()
	value_propositions = models.TextField()
	compliance_check = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalPreparationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalPreparationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.proposal_title

class BidSubmission(models.Model):
	bid_proposal = models.ForeignKey('BidProposal', on_delete=models.CASCADE, related_name='%(class)s_bid_proposal')
	submission_date = models.DateField()
	submission_method = models.CharField(max_length=50,choices=[('portal', 'Portal'), ('email', 'Email'), ('physical', 'Physical')],)
	documents_included = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidSubmissioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidSubmissionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.submission_date

class Equipment(models.Model):
	name = models.CharField(max_length=255,)
	category = models.ForeignKey('EquipmentCategory', on_delete=models.CASCADE, related_name='%(class)s_category')
	serial_number = models.CharField(max_length=255,unique=True ,)
	purchase_date = models.DateField()
	condition = models.CharField(max_length=255,choices=[('New', 'New'), ('Used', 'Used')],)
	location = models.ForeignKey('Warehouse', on_delete=models.CASCADE, related_name='%(class)s_location')
	status = models.CharField(max_length=255,choices=[('Available', 'Available'), ('In Use', 'In use'), ('Under Maintenance', 'Under maintenance')],)
	def __str__(self):
		return self.name

class Notification(models.Model):
	message = models.CharField(max_length=255,)
	is_read = models.BooleanField(default=False, )
	timestamp = models.DateTimeField()
	def __str__(self):
		return self.message

class Item(models.Model):
	name = models.CharField(max_length=255,)
	category = models.ForeignKey('ItemCategory', on_delete=models.CASCADE, related_name='%(class)s_category')
	supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='%(class)s_supplier')
	stock_quantity = models.IntegerField(default="0.0," )
	reorder_point = models.IntegerField(default="10.0," )
	safety_stock = models.IntegerField(default="5.0," )
	price_per_unit = models.DecimalField(max_digits=10, decimal_places=2,)
	warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, related_name='%(class)s_warehouse')
	barcode = models.CharField(max_length=255,unique=True ,)
	def __str__(self):
		return self.name

class Lead(models.Model):
	name = models.CharField(max_length=255,)
	company = models.CharField(max_length=255,)
	email = models.EmailField()
	phone = models.CharField(max_length=20,blank=True, null=True ,)
	project_description = models.TextField()
	source = models.ForeignKey('LeadSource', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_source')
	status = models.CharField(max_length=50,choices=[('new', 'New'), ('qualified', 'Qualified'), ('disqualified', 'Disqualified')],)
	budget = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
	urgency = models.IntegerField()
	decision_maker = models.BooleanField(default=False, )
	assigned_to = models.ForeignKey('SalesRepresentative', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_assigned_to')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class ProcurementNeed(models.Model):
	department = models.ForeignKey('InternalDepartment', on_delete=models.CASCADE, related_name='%(class)s_department')
	description = models.TextField()
	quantity = models.PositiveIntegerField()
	date_needed = models.DateField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProcurementNeedcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProcurementNeedupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.description

class Audit(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	audit_type = models.CharField(max_length=50,choices=[('Safety', 'Safety'), ('Quality', 'Quality')],)
	conducted_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_conducted_by')
	date = models.DateField()
	findings = models.TextField()
	def __str__(self):
		return self.audit_type

class Bid(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	subcontractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, related_name='%(class)s_subcontractor')
	bid_amount = models.DecimalField(max_digits=12, decimal_places=2,)
	bid_submission_date = models.DateField()
	status = models.CharField(max_length=100,)
	notes = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.bid_amount

class Budget(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	total_budget = models.DecimalField(max_digits=15, decimal_places=2,)
	allocated_budget = models.DecimalField(max_digits=15, decimal_places=2,)
	remaining_budget = models.DecimalField(max_digits=15, decimal_places=2,)
	currency = models.ForeignKey('Currency', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_currency')
	def __str__(self):
		return self.total_budget

class BudgetAllocation(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	materials_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	labor_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	equipment_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	contingency_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	total_budget = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BudgetAllocationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BudgetAllocationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.materials_cost

class ClientFeedback(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	feedback_date = models.DateField()
	client_name = models.CharField(max_length=255,)
	satisfaction_rating = models.IntegerField()
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClientFeedbackcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClientFeedbackupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.feedback_date

class ClientFollowUp(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	follow_up_date = models.DateField()
	message = models.TextField()
	action_taken = models.CharField(max_length=255,choices=[('email_sent', 'Email_sent'), ('called', 'Called')],)
	def __str__(self):
		return self.follow_up_date

class ClientSatisfactionSurvey(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	sent_date = models.DateField()
	client_feedback = models.TextField()
	score = models.IntegerField()
	def __str__(self):
		return self.sent_date

class CloseoutDocument(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	document_type = models.CharField(max_length=255,)
	uploaded_at = models.DateTimeField()
	def __str__(self):
		return self.document_type

class ComplianceMonitor(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	compliance_type = models.CharField(max_length=50,)
	description = models.TextField()
	status = models.CharField(max_length=50,choices=[('Compliant', 'Compliant'), ('Non-compliant', 'Non-compliant')],)
	date = models.DateField()
	def __str__(self):
		return self.compliance_type

class Contract(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='%(class)s_contractor')
	scope_of_work = models.TextField()
	pricing = models.DecimalField(max_digits=12, decimal_places=2,)
	payment_terms = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	signed_by_client = models.BooleanField(default=False, )
	signed_by_contractor = models.BooleanField(default=False, )
	approved_by = models.CharField(max_length=255,blank=True, null=True ,)
	status = models.CharField(max_length=50,)
	def __str__(self):
		return self.scope_of_work

class ContractAwardExecution(models.Model):
	contract_title = models.CharField(max_length=255,)
	project_manager = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project_manager')
	execution_status = models.CharField(max_length=100,)
	delivery_commitments = models.TextField()
	execution_notes = models.TextField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractAwardExecutioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractAwardExecutionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.contract_title

class CostEstimation(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	category = models.ForeignKey('CostCategory', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_category')
	estimated_cost = models.DecimalField(max_digits=15, decimal_places=2,)
	actual_cost = models.DecimalField(max_digits=15, decimal_places=2,default="0.0," )
	forecast_cost = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.estimated_cost

class FinalClientSignOff(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	client = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_client')
	sign_off_date = models.DateField()
	is_approved = models.BooleanField(default=False, )
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalClientSignOffcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalClientSignOffupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.sign_off_date

class FinalInspection(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	inspection_date = models.DateField()
	inspector = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_inspector')
	client_present = models.BooleanField(default=False, )
	comments = models.TextField(blank=True, null=True)
	all_punch_items_resolved = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalInspectioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalInspectionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.inspection_date

class FinalReview(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	review_type = models.CharField(max_length=50,choices=[('Safety', 'Safety'), ('Quality', 'Quality')],)
	review_details = models.TextField()
	conducted_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_conducted_by')
	date = models.DateField()
	def __str__(self):
		return self.review_type

class FinancialTransaction(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='%(class)s_account')
	transaction_type = models.CharField(max_length=10,)
	amount = models.DecimalField(max_digits=15, decimal_places=2,)
	description = models.TextField(blank=True, null=True)
	date = models.DateTimeField()
	def __str__(self):
		return self.transaction_type

class IncidentReport(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	reported_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_reported_by')
	incident_type = models.CharField(max_length=50,choices=[('Safety', 'Safety'), ('Quality', 'Quality')],)
	description = models.TextField()
	date_reported = models.DateTimeField()
	immediate_action = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.incident_type

class Inspection(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	inspector = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_inspector')
	inspection_type = models.CharField(max_length=50,choices=[('Safety', 'Safety'), ('Quality', 'Quality')],)
	date = models.DateField()
	checklist = models.TextField()
	findings = models.TextField()
	def __str__(self):
		return self.inspection_type

class LegalRequirement(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	description = models.TextField()
	requirement_type = models.CharField(max_length=255,)
	def __str__(self):
		return self.description

class Message(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	content = models.TextField()
	timestamp = models.DateTimeField()
	def __str__(self):
		return self.content

class Milestone(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	name = models.CharField(max_length=255,)
	target_date = models.DateField()
	client_review_required = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Milestonecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Milestoneupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class MilestoneBilling(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	milestone_name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	due_date = models.DateField()
	amount = models.DecimalField(max_digits=15, decimal_places=2,)
	invoiced = models.BooleanField(default=False, )
	def __str__(self):
		return self.milestone_name

class Payroll(models.Model):
	worker = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_worker')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	pay_period_start = models.DateField()
	pay_period_end = models.DateField()
	total_hours = models.DecimalField(max_digits=5, decimal_places=2,)
	hourly_rate = models.DecimalField(max_digits=10, decimal_places=2,)
	total_pay = models.DecimalField(max_digits=10, decimal_places=2,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Payrollcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Payrollupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pay_period_start

class PostProjectReview(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	review_date = models.DateField()
	evaluation_summary = models.TextField()
	strengths = models.TextField(blank=True, null=True)
	areas_for_improvement = models.TextField(blank=True, null=True)
	lessons_learned = models.TextField(blank=True, null=True)
	recommendations = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PostProjectReviewcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PostProjectReviewupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.review_date

class ProjectCloseout(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	subcontractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, related_name='%(class)s_subcontractor')
	final_inspection_date = models.DateField()
	punch_list_items = models.TextField(blank=True, null=True)
	punch_list_completed = models.BooleanField(default=False, )
	final_payment = models.DecimalField(max_digits=12, decimal_places=2,)
	def __str__(self):
		return self.final_inspection_date

class ProjectCommunication(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	communication_date = models.DateTimeField()
	message = models.TextField()
	def __str__(self):
		return self.communication_date

class ProjectDocumentation(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	document_type = models.CharField(max_length=100,)
	issue_date = models.DateField()
	description = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectDocumentationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectDocumentationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.document_type

class ProjectFinancialCloseout(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	closeout_date = models.DateField()
	total_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	total_revenue = models.DecimalField(max_digits=10, decimal_places=2,)
	total_profit = models.DecimalField(max_digits=10, decimal_places=2,)
	subcontractors_paid = models.BooleanField(default=False, )
	purchase_orders_closed = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectFinancialCloseoutcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectFinancialCloseoutupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.closeout_date

class ProjectPerformanceReview(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	review_date = models.DateField()
	original_budget = models.DecimalField(max_digits=10, decimal_places=2,)
	actual_budget = models.DecimalField(max_digits=10, decimal_places=2,)
	resource_utilization_percentage = models.FloatField()
	notes = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectPerformanceReviewcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectPerformanceReviewupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.review_date

class ProjectSchedule(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	start_date = models.DateField()
	end_date = models.DateField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectSchedulecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectScheduleupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.start_date

class PunchListItem(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	description = models.TextField()
	status = models.CharField(max_length=50,choices=[('Pending', 'Pending'), ('In Progress', 'In progress'), ('Completed', 'Completed')],default="Pending," )
	contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_contractor')
	resolved_at = models.DateField(blank=True, null=True)
	fix_deadline = models.DateField()
	inspected = models.BooleanField(default=False, )
	quality_meets_standards = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PunchListItemcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PunchListItemupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.description

class QualityControlPlan(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	content = models.TextField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='QualityControlPlancreated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.content

class QualityInspector(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s_user")
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	designation = models.CharField(max_length=255,)
	def __str__(self):
		return self.designation

class ResourcePlanning(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	workforce_required = models.IntegerField()
	project_duration = models.IntegerField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourcePlanningcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourcePlanningupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.workforce_required

class ResourceUtilizationAnalysis(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	analysis_date = models.DateField()
	total_labor_hours = models.DecimalField(max_digits=10, decimal_places=2,)
	total_materials_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	total_equipment_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	labor_utilization_percentage = models.FloatField()
	materials_utilization_percentage = models.FloatField()
	equipment_utilization_percentage = models.FloatField()
	recommendations = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceUtilizationAnalysiscreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceUtilizationAnalysisupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.analysis_date

class Revenue(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_customer')
	description = models.TextField()
	amount = models.DecimalField(max_digits=15, decimal_places=2,)
	date = models.DateField()
	received_by = models.CharField(max_length=255,)
	def __str__(self):
		return self.description

class Risk(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	risk_category = models.ForeignKey('RiskCategory', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_risk_category')
	name = models.CharField(max_length=255,)
	description = models.TextField()
	risk_type = models.CharField(max_length=50,)
	date_identified = models.DateField()
	owner = models.ForeignKey('RiskOwner', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_owner')
	status = models.CharField(max_length=50,default="Open," )
	def __str__(self):
		return self.name

class SafetyOfficer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s_user")
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	designation = models.CharField(max_length=255,)
	def __str__(self):
		return self.designation

class SafetyPlan(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	content = models.TextField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SafetyPlancreated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.content

class SubcontractorContract(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	subcontractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, related_name='%(class)s_subcontractor')
	signed_date = models.DateField()
	payment_terms = models.TextField()
	insurance_requirements = models.TextField(blank=True, null=True)
	change_order_provision = models.TextField(blank=True, null=True)
	termination_conditions = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.signed_date

class ResourceAvailability(models.Model):
	resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='%(class)s_resource')
	available_from = models.DateField()
	available_until = models.DateField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAvailabilitycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAvailabilityupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.available_from

class ClarificationDocument(models.Model):
	rfp_rfq = models.ForeignKey('RFPRFQ', on_delete=models.CASCADE, related_name='%(class)s_rfp_rfq')
	issued_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClarificationDocumentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClarificationDocumentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.issued_at

class Stakeholder(models.Model):
	name = models.CharField(max_length=255,)
	role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='%(class)s_role')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Stakeholdercreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Stakeholderupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class TeamMember(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='%(class)s_role')
	permissions = models.TextField()
	def __str__(self):
		return self.permissions

class Expense(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='%(class)s_account')
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_vendor')
	description = models.TextField()
	amount = models.DecimalField(max_digits=15, decimal_places=2,)
	date = models.DateField()
	approved_by = models.CharField(max_length=255,)
	def __str__(self):
		return self.description

class PrequalificationQuestionnaire(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='%(class)s_vendor')
	project_experience = models.TextField()
	financial_status = models.TextField()
	certifications = models.TextField()
	safety_records = models.TextField()
	other_qualifications = models.TextField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PrequalificationQuestionnairecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PrequalificationQuestionnaireupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.project_experience

class RFPRFQDistribution(models.Model):
	rfp_rfq = models.ForeignKey('RFPRFQ', on_delete=models.CASCADE, related_name='%(class)s_rfp_rfq')
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='%(class)s_vendor')
	date_sent = models.DateTimeField()
	response_submitted = models.BooleanField(default=False, )
	submission_date = models.DateField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQDistributioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQDistributionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.date_sent

class SupplierPerformanceEvaluation(models.Model):
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='%(class)s_vendor')
	project = models.CharField(max_length=255,)
	evaluation_date = models.DateField()
	delivery_timeliness = models.IntegerField()
	quality_of_products_services = models.IntegerField()
	overall_execution = models.IntegerField()
	comments = models.TextField(blank=True, null=True)
	average_score = models.FloatField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SupplierPerformanceEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SupplierPerformanceEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.project

class VendorClarification(models.Model):
	rfp_rfq = models.ForeignKey('RFPRFQ', on_delete=models.CASCADE, related_name='%(class)s_rfp_rfq')
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='%(class)s_vendor')
	question = models.TextField()
	submitted_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorClarificationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorClarificationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.question

class VendorPrequalificationStatus(models.Model):
	vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="%(class)s_vendor")
	prequalified = models.BooleanField(default=False, )
	prequalification_date = models.DateField(blank=True, null=True)
	reasons_for_rejection = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorPrequalificationStatuscreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorPrequalificationStatusupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.prequalified

class VendorProposal(models.Model):
	rfp_rfq = models.ForeignKey('RFPRFQ', on_delete=models.CASCADE, related_name='%(class)s_rfp_rfq')
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='%(class)s_vendor')
	submitted_at = models.DateTimeField()
	is_compliant = models.BooleanField(default=False, )
	compliance_remarks = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorProposalcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='VendorProposalupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.submitted_at

class AssetAudit(models.Model):
	asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='%(class)s_asset')
	audit_date = models.DateTimeField(default="now," )
	condition = models.CharField(max_length=255,)
	comments = models.TextField()
	def __str__(self):
		return self.audit_date

class AssetMaintenance(models.Model):
	asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='%(class)s_asset')
	maintenance_date = models.DateTimeField(default="now," )
	maintenance_type = models.CharField(max_length=255,)
	cost = models.DecimalField(max_digits=10, decimal_places=2,)
	notes = models.TextField()
	def __str__(self):
		return self.maintenance_date

class Depreciation(models.Model):
	asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='%(class)s_asset')
	depreciation_date = models.DateTimeField(default="now," )
	amount = models.DecimalField(max_digits=12, decimal_places=2,)
	def __str__(self):
		return self.depreciation_date

class SubmissionFollowUp(models.Model):
	proposal = models.ForeignKey('ProposalPreparation', on_delete=models.CASCADE, related_name='%(class)s_proposal')
	submission_date = models.DateField()
	follow_up_date = models.DateField(blank=True, null=True)
	follow_up_notes = models.TextField()
	negotiation_engaged = models.BooleanField(default=False, )
	revisions_required = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SubmissionFollowUpcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SubmissionFollowUpupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.submission_date

class NegotiationAndAward(models.Model):
	bid_submission = models.ForeignKey('BidSubmission', on_delete=models.CASCADE, related_name='%(class)s_bid_submission')
	negotiation_date = models.DateField()
	negotiation_notes = models.TextField(blank=True, null=True)
	final_terms = models.TextField(blank=True, null=True)
	awarded = models.BooleanField(default=False, )
	internal_preparation_started = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationAndAwardcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationAndAwardupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.negotiation_date

class PostSubmissionFollowUp(models.Model):
	bid_submission = models.ForeignKey('BidSubmission', on_delete=models.CASCADE, related_name='%(class)s_bid_submission')
	follow_up_date = models.DateField()
	communication_method = models.CharField(max_length=50,choices=[('email', 'Email'), ('phone', 'Phone'), ('meeting', 'Meeting')],)
	client_response = models.TextField(blank=True, null=True)
	clarification_requested = models.BooleanField(default=False, )
	additional_info_provided = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PostSubmissionFollowUpcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PostSubmissionFollowUpupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.follow_up_date

class EquipmentAssignment(models.Model):
	equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='%(class)s_equipment')
	assigned_to = models.CharField(max_length=255,)
	assigned_date = models.DateTimeField(default="now," )
	return_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.assigned_to

class EquipmentAudit(models.Model):
	equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='%(class)s_equipment')
	audit_date = models.DateTimeField(default="now," )
	condition = models.CharField(max_length=255,)
	comments = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.audit_date

class EquipmentMaintenance(models.Model):
	equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='%(class)s_equipment')
	maintenance_date = models.DateTimeField(default="now," )
	maintenance_type = models.CharField(max_length=255,choices=[('Preventive', 'Preventive'), ('Corrective', 'Corrective')],)
	cost = models.DecimalField(max_digits=10, decimal_places=2,)
	notes = models.TextField()
	def __str__(self):
		return self.maintenance_date

class InventoryAudit(models.Model):
	item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='%(class)s_item')
	audit_date = models.DateTimeField(default="now," )
	physical_count = models.IntegerField()
	system_count = models.IntegerField()
	discrepancy = models.IntegerField()
	comments = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.audit_date

class Requisition(models.Model):
	item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='%(class)s_item')
	quantity = models.IntegerField()
	requested_by = models.CharField(max_length=255,)
	date_requested = models.DateTimeField(default="now," )
	date_fulfilled = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.quantity

class StockEntry(models.Model):
	item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='%(class)s_item')
	quantity = models.IntegerField()
	movement_type = models.CharField(max_length=10,choices=[('IN', 'In'), ('OUT', 'Out')],)
	date = models.DateTimeField(default="now," )
	def __str__(self):
		return self.quantity

class ClientInteraction(models.Model):
	lead = models.ForeignKey('Lead', on_delete=models.CASCADE, related_name='%(class)s_lead')
	interaction_type = models.ForeignKey('ClientInteractionType', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_interaction_type')
	description = models.TextField()
	date = models.DateTimeField()
	follow_up_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.description

class Opportunity(models.Model):
	lead = models.ForeignKey('Lead', on_delete=models.CASCADE, related_name='%(class)s_lead')
	stage = models.ForeignKey('SalesStage', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_stage')
	amount = models.DecimalField(max_digits=10, decimal_places=2,)
	probability = models.IntegerField()
	expected_close_date = models.DateField()
	assigned_to = models.ForeignKey('SalesRepresentative', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_assigned_to')
	def __str__(self):
		return self.amount

class DocumentedRequirement(models.Model):
	procurement_need = models.ForeignKey('ProcurementNeed', on_delete=models.CASCADE, related_name='%(class)s_procurement_need')
	requirement_description = models.TextField()
	quantity = models.PositiveIntegerField()
	timeline = models.DateField()
	budget_estimate = models.DecimalField(max_digits=10, decimal_places=2,)
	technical_specifications = models.TextField(blank=True, null=True)
	quality_specifications = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DocumentedRequirementcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DocumentedRequirementupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.requirement_description

class CorrectivePreventiveAction(models.Model):
	audit = models.ForeignKey('Audit', on_delete=models.CASCADE, related_name='%(class)s_audit')
	description = models.TextField()
	date_taken = models.DateField()
	status = models.CharField(max_length=50,choices=[('Pending', 'Pending'), ('Completed', 'Completed')],)
	def __str__(self):
		return self.description

class ChangeOrder(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	requestor = models.CharField(max_length=255,)
	description = models.TextField()
	change_reason = models.TextField()
	impact_on_scope = models.TextField()
	cost_impact = models.DecimalField(max_digits=12, decimal_places=2,)
	time_impact = models.IntegerField()
	status = models.CharField(max_length=50,)
	submitted_date = models.DateField()
	approved_date = models.DateField(blank=True, null=True)
	def __str__(self):
		return self.requestor

class ContractCloseout(models.Model):
	contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="%(class)s_contract")
	closeout_date = models.DateField()
	final_review_notes = models.TextField()
	signed_off_by = models.CharField(max_length=255,)
	def __str__(self):
		return self.closeout_date

class ContractExecution(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	execution_date = models.DateField()
	status = models.CharField(max_length=50,choices=[('in_progress', 'In_progress'), ('completed', 'Completed'), ('terminated', 'Terminated')],default="in_progress," )
	notes = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractExecutioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractExecutionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.execution_date

class ContractMilestone(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	name = models.CharField(max_length=255,)
	description = models.TextField()
	due_date = models.DateField()
	completed = models.BooleanField(default=False, )
	def __str__(self):
		return self.name

class LegalReview(models.Model):
	contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="%(class)s_contract")
	review_date = models.DateField()
	reviewed_by = models.CharField(max_length=100,help_text="Name of the legal reviewer,")
	approval_status = models.CharField(max_length=50,choices=[('approved', 'Approved'), ('revised', 'Revised'), ('not_approved', 'Not_approved')],default="approved," )
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='LegalReviewcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='LegalReviewupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.review_date

class PurchaseOrder(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	order_number = models.CharField(max_length=50,unique=True ,)
	order_date = models.DateTimeField()
	product_service_description = models.TextField()
	quantity = models.PositiveIntegerField()
	unit_price = models.DecimalField(max_digits=10, decimal_places=2,)
	total_price = models.DecimalField(max_digits=10, decimal_places=2,)
	status = models.CharField(max_length=20,choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')],default="Pending," )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PurchaseOrdercreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='PurchaseOrderupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.order_number

class CorrectiveAction(models.Model):
	incident = models.ForeignKey('IncidentReport', on_delete=models.CASCADE, related_name='%(class)s_incident')
	description = models.TextField()
	action_taken_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_action_taken_by')
	date_taken = models.DateField()
	status = models.CharField(max_length=50,choices=[('Pending', 'Pending'), ('Completed', 'Completed')],)
	def __str__(self):
		return self.description

class Investigation(models.Model):
	incident = models.OneToOneField(IncidentReport, on_delete=models.CASCADE, related_name="%(class)s_incident")
	investigator = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_investigator')
	findings = models.TextField()
	root_cause = models.TextField()
	investigation_date = models.DateField()
	def __str__(self):
		return self.findings

class ClientReview(models.Model):
	milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE, related_name='%(class)s_milestone')
	client_feedback = models.TextField(blank=True, null=True)
	approved = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClientReviewcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClientReviewupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.client_feedback

class ScheduleAdjustment(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE, related_name='%(class)s_milestone')
	adjustment_date = models.DateField()
	new_date = models.DateField()
	reason = models.TextField(blank=True, null=True)
	adjusted_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_adjusted_by')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ScheduleAdjustmentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ScheduleAdjustmentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.adjustment_date

class Task(models.Model):
	milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE, related_name='%(class)s_milestone')
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True, null=True)
	is_completed = models.BooleanField(default=False, )
	duration_estimation = models.ForeignKey('TaskDurationEstimation', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_duration_estimation')
	priority = models.ForeignKey('TaskPriority', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_priority')
	category = models.ForeignKey('TaskCategory', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_category')
	assigned_team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_assigned_team')
	assigned_individuals = models.ManyToManyField(Individual,related_name="%(class)s_assigned_individuals")
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	task_owner = models.ForeignKey('Individual', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_task_owner')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Taskcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Taskupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class SiteInspection(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	inspection_date = models.DateField()
	inspector = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_inspector')
	observations = models.TextField()
	punch_list_items = models.ManyToManyField(PunchListItem,related_name="%(class)s_punch_list_items")
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SiteInspectioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='SiteInspectionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.inspection_date

class Machinery(models.Model):
	resource_planning = models.ForeignKey('ResourcePlanning', on_delete=models.CASCADE, related_name='%(class)s_resource_planning')
	name = models.CharField(max_length=255,)
	quantity = models.IntegerField()
	def __str__(self):
		return self.name

class Material(models.Model):
	resource_planning = models.ForeignKey('ResourcePlanning', on_delete=models.CASCADE, related_name='%(class)s_resource_planning')
	name = models.CharField(max_length=255,)
	quantity = models.IntegerField()
	def __str__(self):
		return self.name

class MitigationStrategy(models.Model):
	risk = models.ForeignKey('Risk', on_delete=models.CASCADE, related_name='%(class)s_risk')
	strategy = models.TextField()
	mitigation_owner = models.ForeignKey('RiskOwner', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_mitigation_owner')
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.CharField(max_length=50,default="Pending," )
	def __str__(self):
		return self.strategy

class RiskAssessment(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	risk = models.OneToOneField(Risk, on_delete=models.CASCADE, related_name="%(class)s_risk")
	probability = models.IntegerField()
	impact = models.IntegerField()
	overall_risk_score = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
	def __str__(self):
		return self.probability

class RiskReview(models.Model):
	risk = models.ForeignKey('Risk', on_delete=models.CASCADE, related_name='%(class)s_risk')
	review_date = models.DateField()
	status = models.CharField(max_length=50,choices=[('Open', 'Open'), ('Mitigated', 'Mitigated'), ('Closed', 'Closed')],)
	comments = models.TextField(blank=True, null=True)
	reviewed_by = models.ForeignKey('RiskOwner', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_reviewed_by')
	def __str__(self):
		return self.review_date

class DelayNotification(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE, related_name='%(class)s_stakeholder')
	notification_date = models.DateField()
	message = models.TextField()
	updated_timeline = models.DateField()
	plan_to_mitigate = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DelayNotificationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='DelayNotificationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.notification_date

class StakeholderInput(models.Model):
	procurement_need = models.ForeignKey('ProcurementNeed', on_delete=models.CASCADE, related_name='%(class)s_procurement_need')
	stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE, related_name='%(class)s_stakeholder')
	input_description = models.TextField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='StakeholderInputcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='StakeholderInputupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.input_description

class TenderDocument(models.Model):
	tender_type = models.CharField(max_length=3,choices=[('RFP', 'Rfp'), ('RFQ', 'Rfq')],default="RFP," )
	title = models.CharField(max_length=255,)
	description = models.TextField()
	prepared_by = models.ForeignKey('Stakeholder', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_prepared_by')
	issue_date = models.DateField()
	closing_date = models.DateField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderDocumentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderDocumentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.tender_type

class Issue(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	issue_type = models.CharField(max_length=50,)
	description = models.TextField()
	status = models.CharField(max_length=50,)
	assigned_to = models.ForeignKey('TeamMember', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_assigned_to')
	timestamp = models.DateTimeField()
	def __str__(self):
		return self.issue_type

class RFPRFQResponse(models.Model):
	distribution = models.OneToOneField(RFPRFQDistribution, on_delete=models.CASCADE, related_name="%(class)s_distribution")
	response_text = models.TextField()
	submitted_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQResponsecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RFPRFQResponseupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.response_text

class ClarificationResponse(models.Model):
	clarification = models.ForeignKey('VendorClarification', on_delete=models.CASCADE, related_name='%(class)s_clarification')
	response = models.TextField()
	responded_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClarificationResponsecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ClarificationResponseupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.response

class FinalVendorSelection(models.Model):
	vendor_proposal = models.ForeignKey('VendorProposal', on_delete=models.CASCADE, related_name='%(class)s_vendor_proposal')
	selection_date = models.DateField()
	justification = models.TextField()
	approved_by = models.CharField(max_length=100,help_text="Name of the person or committee who approved the selection,")
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalVendorSelectioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinalVendorSelectionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.selection_date

class FinancialEvaluation(models.Model):
	proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name="%(class)s_proposal")
	quoted_price = models.DecimalField(max_digits=12, decimal_places=2,)
	hidden_costs = models.DecimalField(max_digits=12, decimal_places=2,default="0.0," )
	delivery_schedule_assessment = models.TextField(blank=True, null=True)
	warranties_offered = models.TextField(blank=True, null=True)
	after_sales_service = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinancialEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FinancialEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.quoted_price

class NegotiationStakeholder(models.Model):
	team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='%(class)s_team')
	stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE, related_name='%(class)s_stakeholder')
	vendor_proposal = models.ForeignKey('VendorProposal', on_delete=models.CASCADE, related_name='%(class)s_vendor_proposal')
	feedback = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationStakeholdercreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationStakeholderupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.feedback

class NegotiationSummary(models.Model):
	vendor_proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name="%(class)s_vendor_proposal")
	summary = models.TextField()
	final_terms_agreed = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationSummarycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationSummaryupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.summary

class NegotiationTerm(models.Model):
	description = models.CharField(max_length=255,)
	proposed_value = models.CharField(max_length=255,help_text="Vendor's initial proposal for the term,")
	negotiated_value = models.CharField(max_length=255,help_text="Final agreed value after negotiations,")
	vendor_proposal = models.ForeignKey('VendorProposal', on_delete=models.CASCADE, related_name='%(class)s_vendor_proposal')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationTermcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='NegotiationTermupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.description

class ProposalCompliance(models.Model):
	proposal = models.ForeignKey('VendorProposal', on_delete=models.CASCADE, related_name='%(class)s_proposal')
	certification_compliance = models.BooleanField(default=False, )
	technical_spec_compliance = models.BooleanField(default=False, )
	other_compliance = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalCompliancecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalComplianceupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.certification_compliance

class ProposalEvaluation(models.Model):
	proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name="%(class)s_proposal")
	total_score = models.DecimalField(max_digits=6, decimal_places=2,)
	shortlisted = models.BooleanField(default=False, )
	notes = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.total_score

class ProposalScoring(models.Model):
	proposal = models.ForeignKey('VendorProposal', on_delete=models.CASCADE, related_name='%(class)s_proposal')
	criteria = models.ForeignKey('ScoringCriteria', on_delete=models.CASCADE, related_name='%(class)s_criteria')
	score = models.DecimalField(max_digits=5, decimal_places=2,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalScoringcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProposalScoringupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.score

class RiskEvaluation(models.Model):
	proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name="%(class)s_proposal")
	vendor_reliability = models.CharField(max_length=255,blank=True, null=True ,)
	financial_stability = models.CharField(max_length=255,blank=True, null=True ,)
	logistical_issues = models.TextField(blank=True, null=True)
	overall_risk_level = models.CharField(max_length=50,choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],default="Low," )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RiskEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RiskEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.vendor_reliability

class TechnicalEvaluation(models.Model):
	proposal = models.OneToOneField(VendorProposal, on_delete=models.CASCADE, related_name="%(class)s_proposal")
	meets_technical_specs = models.BooleanField(default=False, )
	quality_assessment = models.TextField(blank=True, null=True)
	additional_technical_remarks = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TechnicalEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TechnicalEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.meets_technical_specs

class Proposal(models.Model):
	opportunity = models.ForeignKey('Opportunity', on_delete=models.CASCADE, related_name='%(class)s_opportunity')
	created_date = models.DateTimeField()
	status = models.CharField(max_length=50,choices=[('sent', 'Sent'), ('viewed', 'Viewed'), ('negotiation', 'Negotiation'), ('approved', 'Approved')],)
	negotiation_notes = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.created_date

class AuditLog(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	change_order = models.ForeignKey('ChangeOrder', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_change_order')
	action = models.CharField(max_length=255,)
	action_by = models.CharField(max_length=255,)
	action_date = models.DateTimeField()
	notes = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.action

class ChangeOrderApproval(models.Model):
	change_order = models.OneToOneField(ChangeOrder, on_delete=models.CASCADE, related_name="%(class)s_change_order")
	approved_by = models.CharField(max_length=255,)
	approval_date = models.DateField()
	notes = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.approved_by

class ChangeOrderImplementation(models.Model):
	change_order = models.OneToOneField(ChangeOrder, on_delete=models.CASCADE, related_name="%(class)s_change_order")
	implementation_details = models.TextField()
	implementation_date = models.DateField()
	new_deadline = models.DateField(blank=True, null=True)
	def __str__(self):
		return self.implementation_details

class Document(models.Model):
	contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='%(class)s_contract')
	change_order = models.ForeignKey('ChangeOrder', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_change_order')
	document_name = models.CharField(max_length=255,)
	upload_date = models.DateField()
	def __str__(self):
		return self.document_name

class Invoice(models.Model):
	purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, related_name='%(class)s_purchase_order')
	vendor_name = models.CharField(max_length=255,)
	invoice_number = models.CharField(max_length=50,unique=True ,)
	invoice_date = models.DateField()
	total_amount = models.DecimalField(max_digits=10, decimal_places=2,)
	payment_status = models.CharField(max_length=20,choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Paid', 'Paid'), ('Rejected', 'Rejected')],default="Pending," )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Invoicecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Invoiceupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.vendor_name

class Shipment(models.Model):
	purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, related_name='%(class)s_purchase_order')
	shipment_number = models.CharField(max_length=50,unique=True ,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Shipmentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Shipmentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.shipment_number

class CriticalPath(models.Model):
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	estimated_duration = models.PositiveIntegerField()
	is_on_critical_path = models.BooleanField(default=True, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='CriticalPathcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='CriticalPathupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.is_on_critical_path

class DailyProgressReport(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	report_date = models.DateField()
	description = models.TextField()
	worker_count = models.IntegerField()
	machinery_in_use = models.CharField(max_length=255,)
	materials_used = models.TextField()
	completion_percentage = models.DecimalField(max_digits=5, decimal_places=2,)
	progress_percentage = models.DecimalField(max_digits=5, decimal_places=2,)
	issues_encountered = models.TextField(blank=True, null=True)
	reported_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_reported_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.report_date

class Delay(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	cause = models.ForeignKey('DelayCause', on_delete=models.CASCADE, related_name='%(class)s_cause')
	reported_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_reported_by')
	reported_at = models.DateTimeField()
	notes = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Delaycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Delayupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.reported_at

class PerformanceReport(models.Model):
	subcontractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, related_name='%(class)s_subcontractor')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	report_date = models.DateField()
	tasks_completed = models.IntegerField(default="0," )
	issues_encountered = models.TextField(blank=True, null=True)
	safety_compliance = models.BooleanField(default=True, )
	def __str__(self):
		return self.report_date

class PhotoDocumentation(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	description = models.TextField(blank=True, null=True)
	geo_tag = models.CharField(max_length=255,blank=True, null=True ,)
	timestamp = models.DateTimeField()
	def __str__(self):
		return self.description

class ProjectUpdate(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	date = models.DateField(blank=True, null=True)
	planned_start_date = models.DateField(blank=True, null=True)
	actual_start_date = models.DateField(blank=True, null=True)
	planned_end_date = models.DateField(blank=True, null=True)
	actual_end_date = models.DateField(blank=True, null=True)
	progress_percentage = models.DecimalField(max_digits=5, decimal_places=2,default="0.0," )
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectUpdatecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ProjectUpdateupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.date

class ResourceAdjustment(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='%(class)s_resource')
	adjustment_date = models.DateField()
	new_schedule = models.DateField()
	reason = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAdjustmentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAdjustmentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.adjustment_date

class ResourceAllocation(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	resource_type = models.CharField(max_length=100,)
	allocated_quantity = models.IntegerField()
	allocated_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_allocated_by')
	allocated_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAllocationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceAllocationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.resource_type

class TaskDependency(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	dependent_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_dependent_task')
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskDependencycreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskDependencyupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pk

class TaskResourceAllocation(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='%(class)s_resource')
	quantity = models.PositiveIntegerField(default="1.0," )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskResourceAllocationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskResourceAllocationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.pk

class TaskSchedule(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	scheduled_start_date = models.DateField()
	scheduled_end_date = models.DateField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskSchedulecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskScheduleupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.scheduled_start_date

class TaskStatus(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	status = models.CharField(max_length=20,choices=[('not_started', 'Not_started'), ('in_progress', 'In_progress'), ('completed', 'Completed'), ('on_hold', 'On_hold')],default="not_started," )
	update_date = models.DateField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskStatuscreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TaskStatusupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.status

class Timesheet(models.Model):
	worker = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_worker')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	date = models.DateField()
	hours_worked = models.DecimalField(max_digits=5, decimal_places=2,)
	task = models.ForeignKey('Task', on_delete=models.CASCADE, blank=True, null=True,related_name='%(class)s_task')
	submitted = models.BooleanField(default=False, )
	reviewed = models.BooleanField(default=False, )
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Timesheetcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Timesheetupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.date

class TimeTracking(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_task')
	user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_user')
	date = models.DateField(blank=True, null=True)
	hours_spent = models.DecimalField(max_digits=5, decimal_places=2,)
	hourly_rate = models.DecimalField(max_digits=10, decimal_places=2,)
	total_cost = models.DecimalField(max_digits=10, decimal_places=2,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TimeTrackingcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TimeTrackingupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.date

class StockAdjustment(models.Model):
	material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='%(class)s_material')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	quantity_adjusted = models.DecimalField(max_digits=10, decimal_places=2,)
	reason = models.CharField(max_length=255,)
	adjustment_date = models.DateField()
	def __str__(self):
		return self.quantity_adjusted

class StockReplenishmentRequest(models.Model):
	material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='%(class)s_material')
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	quantity_requested = models.DecimalField(max_digits=10, decimal_places=2,)
	request_date = models.DateField()
	def __str__(self):
		return self.quantity_requested

class MitigationAction(models.Model):
	mitigation_strategy = models.ForeignKey('MitigationStrategy', on_delete=models.CASCADE, related_name='%(class)s_mitigation_strategy')
	action_name = models.CharField(max_length=255,)
	action_description = models.TextField()
	due_date = models.DateField()
	completed = models.BooleanField(default=False, )
	completed_date = models.DateField(blank=True, null=True)
	def __str__(self):
		return self.action_name

class TenderScope(models.Model):
	tender = models.ForeignKey('TenderDocument', on_delete=models.CASCADE, related_name='%(class)s_tender')
	scope_description = models.TextField()
	technical_specifications = models.TextField()
	delivery_timeline = models.DateField()
	quality_standards = models.TextField()
	def __str__(self):
		return self.scope_description

class TenderSubmission(models.Model):
	tender = models.ForeignKey('TenderDocument', on_delete=models.CASCADE, related_name='%(class)s_tender')
	vendor_name = models.CharField(max_length=255,)
	proposal_details = models.TextField()
	submitted_on = models.DateField()
	cost_estimate = models.DecimalField(max_digits=12, decimal_places=2,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderSubmissioncreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderSubmissionupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.vendor_name

class ContractAward(models.Model):
	contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="%(class)s_contract")
	selected_vendor = models.ForeignKey('FinalVendorSelection', on_delete=models.CASCADE, related_name='%(class)s_selected_vendor')
	award_date = models.DateField()
	notification_sent_to_vendor = models.BooleanField(default=False, )
	notification_sent_to_bidders = models.BooleanField(default=False, )
	feedback_to_bidders = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractAwardcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ContractAwardupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.award_date

class StakeholderEvaluation(models.Model):
	evaluation = models.ForeignKey('ProposalEvaluation', on_delete=models.CASCADE, related_name='%(class)s_evaluation')
	stakeholder = models.ForeignKey('Stakeholder', on_delete=models.CASCADE, related_name='%(class)s_stakeholder')
	feedback = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='StakeholderEvaluationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='StakeholderEvaluationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.feedback

class Payment(models.Model):
	invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='%(class)s_invoice')
	payment_date = models.DateField()
	amount_paid = models.DecimalField(max_digits=10, decimal_places=2,)
	payment_method = models.CharField(max_length=50,choices=[('Bank Transfer', 'Bank transfer'), ('Credit Card', 'Credit card'), ('Cash', 'Cash'), ('Check', 'Check')],)
	payment_reference = models.CharField(max_length=100,blank=True, null=True ,)
	project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='%(class)s_project')
	milestone = models.CharField(max_length=255,)
	payment_due = models.DecimalField(max_digits=12, decimal_places=2,)
	status = models.CharField(max_length=100,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Paymentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Paymentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.payment_date

class CriticalPathMonitoring(models.Model):
	critical_path = models.ForeignKey('CriticalPath', on_delete=models.CASCADE, related_name='%(class)s_critical_path')
	actual_start_date = models.DateField(blank=True, null=True)
	actual_end_date = models.DateField(blank=True, null=True)
	delay_days = models.PositiveIntegerField(default="0.0," )
	comments = models.TextField(blank=True, null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='CriticalPathMonitoringcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='CriticalPathMonitoringupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.actual_start_date

class Adjustment(models.Model):
	delay = models.ForeignKey('Delay', on_delete=models.CASCADE, related_name='%(class)s_delay')
	adjusted_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_adjusted_task')
	new_start_date = models.DateField()
	new_end_date = models.DateField()
	adjusted_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_adjusted_by')
	adjustment_reason = models.TextField(blank=True, null=True)
	adjusted_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Adjustmentcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Adjustmentupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.new_start_date

class ResourceReallocation(models.Model):
	original_allocation = models.ForeignKey('ResourceAllocation', on_delete=models.CASCADE, related_name='%(class)s_original_allocation')
	new_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='%(class)s_new_task')
	reallocated_quantity = models.IntegerField()
	reason = models.TextField(blank=True, null=True)
	reallocated_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_reallocated_by')
	reallocated_at = models.DateTimeField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceReallocationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceReallocationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.reallocated_quantity

class ResourceUsage(models.Model):
	task_resource_allocation = models.ForeignKey('TaskResourceAllocation', on_delete=models.CASCADE, related_name='%(class)s_task_resource_allocation')
	start_time = models.DateTimeField(blank=True, null=True)
	end_time = models.DateTimeField(blank=True, null=True)
	quantity_used = models.PositiveIntegerField()
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceUsagecreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ResourceUsageupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.start_time

class Client(models.Model):
	name = models.CharField(max_length=255,)
	address = models.TextField()
	contact_person = models.CharField(max_length=255,)
	email = models.EmailField()
	phone = models.CharField(max_length=15,)
	def __str__(self):
		return self.name

class BidQualification(models.Model):
	rfp_rfq_title = models.CharField(max_length=255,)
	response_due_date = models.DateField()
	alignment_with_strategy = models.TextField()
	capacity_evaluation = models.TextField()
	is_qualified = models.BooleanField(default=False, )
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidQualificationcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BidQualificationupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.rfp_rfq_title

class TenderProposalManagement(models.Model):
	rfp_rfq_title = models.CharField(max_length=255,)
	issued_date = models.DateField()
	response_deadline = models.DateField()
	response_tracking = models.TextField()
	issued_by = models.CharField(max_length=100,)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderProposalManagementcreated_by')
	updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TenderProposalManagementupdated_by')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.rfp_rfq_title
