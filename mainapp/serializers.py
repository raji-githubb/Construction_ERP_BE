from rest_framework import serializers
from .models import *

#  ms setup serializer
class MSSerializer(serializers.Serializer):
    ms_id = serializers.CharField(max_length=100)
    ms_payload = serializers.JSONField(initial=dict)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AssetCategorySeriali8001zer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = "__all__"

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"

class SubcontractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcontractor
        fields = "__all__"

class OpportunityIdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityIdentification
        fields = "__all__"

class BidProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidProposal
        fields = "__all__"

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class ClientInteractionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInteractionType
        fields = "__all__"

class CostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCategory
        fields = "__all__"

class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class LeadSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = "__all__"

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentative
        fields = "__all__"

class RiskOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOwner
        fields = "__all__"

class SalesStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesStage
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class RiskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskCategory
        fields = "__all__"

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = "__all__"

class DelayCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelayCause
        fields = "__all__"

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = "__all__"

class InternalDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalDepartment
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = "__all__"

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"

class RFPRFQSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFPRFQ
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class ScoringCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringCriteria
        fields = "__all__"

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = "__all__"

class TaskDurationEstimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDurationEstimation
        fields = "__all__"

class TaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPriority
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

class AssetSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    class Meta:
        model = Asset
        fields = "__all__"

class ExpertiseSerializer(serializers.ModelSerializer):
    subcontractor = serializers.StringRelatedField()
    class Meta:
        model = Expertise
        fields = "__all__"

class BidNoBidDecisionSerializer(serializers.ModelSerializer):
    opportunity = serializers.StringRelatedField()
    class Meta:
        model = BidNoBidDecision
        fields = "__all__"

class ProposalPreparationSerializer(serializers.ModelSerializer):
    opportunity = serializers.StringRelatedField()
    class Meta:
        model = ProposalPreparation
        fields = "__all__"

class BidSubmissionSerializer(serializers.ModelSerializer):
    bid_proposal = serializers.StringRelatedField()
    class Meta:
        model = BidSubmission
        fields = "__all__"

class EquipmentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    class Meta:
        model = Equipment
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    supplier = serializers.StringRelatedField()
    warehouse = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = "__all__"

class LeadSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    class Meta:
        model = Lead
        fields = "__all__"

class ProcurementNeedSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model = ProcurementNeed
        fields = "__all__"

class AuditSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    conducted_by = serializers.StringRelatedField()
    class Meta:
        model = Audit
        fields = "__all__"

class BidSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    subcontractor = serializers.StringRelatedField()
    class Meta:
        model = Bid
        fields = "__all__"

class BudgetSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    currency = serializers.StringRelatedField()
    class Meta:
        model = Budget
        fields = "__all__"

class BudgetAllocationSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = BudgetAllocation
        fields = "__all__"

class ClientFeedbackSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ClientFeedback
        fields = "__all__"

class ClientFollowUpSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ClientFollowUp
        fields = "__all__"

class ClientSatisfactionSurveySerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ClientSatisfactionSurvey
        fields = "__all__"

class CloseoutDocumentSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = CloseoutDocument
        fields = "__all__"

class ComplianceMonitorSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ComplianceMonitor
        fields = "__all__"

class ContractSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    contractor = serializers.StringRelatedField()
    class Meta:
        model = Contract
        fields = "__all__"

class ContractAwardExecutionSerializer(serializers.ModelSerializer):
    project_manager = serializers.StringRelatedField()
    class Meta:
        model = ContractAwardExecution
        fields = "__all__"

class CostEstimationSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = CostEstimation
        fields = "__all__"

class FinalClientSignOffSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    class Meta:
        model = FinalClientSignOff
        fields = "__all__"

class FinalInspectionSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    inspector = serializers.StringRelatedField()
    class Meta:
        model = FinalInspection
        fields = "__all__"

class FinalReviewSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    conducted_by = serializers.StringRelatedField()
    class Meta:
        model = FinalReview
        fields = "__all__"

class FinancialTransactionSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    account = serializers.StringRelatedField()
    class Meta:
        model = FinancialTransaction
        fields = "__all__"

class IncidentReportSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    reported_by = serializers.StringRelatedField()
    class Meta:
        model = IncidentReport
        fields = "__all__"

class InspectionSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    inspector = serializers.StringRelatedField()
    class Meta:
        model = Inspection
        fields = "__all__"

class LegalRequirementSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = LegalRequirement
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = Message
        fields = "__all__"

class MilestoneSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = Milestone
        fields = "__all__"

class MilestoneBillingSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = MilestoneBilling
        fields = "__all__"

class PayrollSerializer(serializers.ModelSerializer):
    worker = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = Payroll
        fields = "__all__"

class PostProjectReviewSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = PostProjectReview
        fields = "__all__"

class ProjectCloseoutSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    subcontractor = serializers.StringRelatedField()
    class Meta:
        model = ProjectCloseout
        fields = "__all__"

class ProjectCommunicationSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ProjectCommunication
        fields = "__all__"

class ProjectDocumentationSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ProjectDocumentation
        fields = "__all__"

class ProjectFinancialCloseoutSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ProjectFinancialCloseout
        fields = "__all__"

class ProjectPerformanceReviewSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ProjectPerformanceReview
        fields = "__all__"

class ProjectScheduleSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ProjectSchedule
        fields = "__all__"

class PunchListItemSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    contractor = serializers.StringRelatedField()
    class Meta:
        model = PunchListItem
        fields = "__all__"

class QualityControlPlanSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = QualityControlPlan
        fields = "__all__"

class QualityInspectorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = QualityInspector
        fields = "__all__"

class ResourcePlanningSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ResourcePlanning
        fields = "__all__"

class ResourceUtilizationAnalysisSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = ResourceUtilizationAnalysis
        fields = "__all__"

class RevenueSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    class Meta:
        model = Revenue
        fields = "__all__"

class RiskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    risk_category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()
    class Meta:
        model = Risk
        fields = "__all__"

class SafetyOfficerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = SafetyOfficer
        fields = "__all__"

class SafetyPlanSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    class Meta:
        model = SafetyPlan
        fields = "__all__"

class SubcontractorContractSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    subcontractor = serializers.StringRelatedField()
    class Meta:
        model = SubcontractorContract
        fields = "__all__"

class ResourceAvailabilitySerializer(serializers.ModelSerializer):
    resource = serializers.StringRelatedField()
    class Meta:
        model = ResourceAvailability
        fields = "__all__"

class ClarificationDocumentSerializer(serializers.ModelSerializer):
    rfp_rfq = serializers.StringRelatedField()
    class Meta:
        model = ClarificationDocument
        fields = "__all__"

class StakeholderSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = Stakeholder
        fields = "__all__"

class TeamMemberSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    role = serializers.StringRelatedField()
    class Meta:
        model = TeamMember
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    account = serializers.StringRelatedField()
    vendor = serializers.StringRelatedField()
    class Meta:
        model = Expense
        fields = "__all__"

class PrequalificationQuestionnaireSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    class Meta:
        model = PrequalificationQuestionnaire
        fields = "__all__"

class RFPRFQDistributionSerializer(serializers.ModelSerializer):
    rfp_rfq = serializers.StringRelatedField()
    vendor = serializers.StringRelatedField()
    class Meta:
        model = RFPRFQDistribution
        fields = "__all__"

class SupplierPerformanceEvaluationSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    class Meta:
        model = SupplierPerformanceEvaluation
        fields = "__all__"

class VendorClarificationSerializer(serializers.ModelSerializer):
    rfp_rfq = serializers.StringRelatedField()
    vendor = serializers.StringRelatedField()
    class Meta:
        model = VendorClarification
        fields = "__all__"

class VendorPrequalificationStatusSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    class Meta:
        model = VendorPrequalificationStatus
        fields = "__all__"

class VendorProposalSerializer(serializers.ModelSerializer):
    rfp_rfq = serializers.StringRelatedField()
    vendor = serializers.StringRelatedField()
    class Meta:
        model = VendorProposal
        fields = "__all__"

class AssetAuditSerializer(serializers.ModelSerializer):
    asset = serializers.StringRelatedField()
    class Meta:
        model = AssetAudit
        fields = "__all__"

class AssetMaintenanceSerializer(serializers.ModelSerializer):
    asset = serializers.StringRelatedField()
    class Meta:
        model = AssetMaintenance
        fields = "__all__"

class DepreciationSerializer(serializers.ModelSerializer):
    asset = serializers.StringRelatedField()
    class Meta:
        model = Depreciation
        fields = "__all__"

class SubmissionFollowUpSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = SubmissionFollowUp
        fields = "__all__"

class NegotiationAndAwardSerializer(serializers.ModelSerializer):
    bid_submission = serializers.StringRelatedField()
    class Meta:
        model = NegotiationAndAward
        fields = "__all__"

class PostSubmissionFollowUpSerializer(serializers.ModelSerializer):
    bid_submission = serializers.StringRelatedField()
    class Meta:
        model = PostSubmissionFollowUp
        fields = "__all__"

class EquipmentAssignmentSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField()
    class Meta:
        model = EquipmentAssignment
        fields = "__all__"

class EquipmentAuditSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField()
    class Meta:
        model = EquipmentAudit
        fields = "__all__"

class EquipmentMaintenanceSerializer(serializers.ModelSerializer):
    equipment = serializers.StringRelatedField()
    class Meta:
        model = EquipmentMaintenance
        fields = "__all__"

class InventoryAuditSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    class Meta:
        model = InventoryAudit
        fields = "__all__"

class RequisitionSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    class Meta:
        model = Requisition
        fields = "__all__"

class StockEntrySerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    class Meta:
        model = StockEntry
        fields = "__all__"

class ClientInteractionSerializer(serializers.ModelSerializer):
    lead = serializers.StringRelatedField()
    interaction_type = serializers.StringRelatedField()
    class Meta:
        model = ClientInteraction
        fields = "__all__"

class OpportunitySerializer(serializers.ModelSerializer):
    lead = serializers.StringRelatedField()
    stage = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    class Meta:
        model = Opportunity
        fields = "__all__"

class DocumentedRequirementSerializer(serializers.ModelSerializer):
    procurement_need = serializers.StringRelatedField()
    class Meta:
        model = DocumentedRequirement
        fields = "__all__"

class CorrectivePreventiveActionSerializer(serializers.ModelSerializer):
    audit = serializers.StringRelatedField()
    class Meta:
        model = CorrectivePreventiveAction
        fields = "__all__"

class ChangeOrderSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = ChangeOrder
        fields = "__all__"

class ContractCloseoutSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = ContractCloseout
        fields = "__all__"

class ContractExecutionSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = ContractExecution
        fields = "__all__"

class ContractMilestoneSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = ContractMilestone
        fields = "__all__"

class LegalReviewSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = LegalReview
        fields = "__all__"

class PurchaseOrderSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

class CorrectiveActionSerializer(serializers.ModelSerializer):
    incident = serializers.StringRelatedField()
    action_taken_by = serializers.StringRelatedField()
    class Meta:
        model = CorrectiveAction
        fields = "__all__"

class InvestigationSerializer(serializers.ModelSerializer):
    incident = serializers.StringRelatedField()
    investigator = serializers.StringRelatedField()
    class Meta:
        model = Investigation
        fields = "__all__"

class ClientReviewSerializer(serializers.ModelSerializer):
    milestone = serializers.StringRelatedField()
    class Meta:
        model = ClientReview
        fields = "__all__"

class ScheduleAdjustmentSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    milestone = serializers.StringRelatedField()
    adjusted_by = serializers.StringRelatedField()
    class Meta:
        model = ScheduleAdjustment
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    milestone = serializers.StringRelatedField()
    duration_estimation = serializers.StringRelatedField()
    priority = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    assigned_team = serializers.StringRelatedField()
    assigned_individuals = serializers.StringRelatedField()
    task_owner = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = "__all__"

class SiteInspectionSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    inspector = serializers.StringRelatedField()
    punch_list_items = serializers.StringRelatedField()
    class Meta:
        model = SiteInspection
        fields = "__all__"

class MachinerySerializer(serializers.ModelSerializer):
    resource_planning = serializers.StringRelatedField()
    class Meta:
        model = Machinery
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    resource_planning = serializers.StringRelatedField()
    class Meta:
        model = Material
        fields = "__all__"

class MitigationStrategySerializer(serializers.ModelSerializer):
    risk = serializers.StringRelatedField()
    mitigation_owner = serializers.StringRelatedField()
    class Meta:
        model = MitigationStrategy
        fields = "__all__"

class RiskAssessmentSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    risk = serializers.StringRelatedField()
    class Meta:
        model = RiskAssessment
        fields = "__all__"

class RiskReviewSerializer(serializers.ModelSerializer):
    risk = serializers.StringRelatedField()
    reviewed_by = serializers.StringRelatedField()
    class Meta:
        model = RiskReview
        fields = "__all__"

class DelayNotificationSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    stakeholder = serializers.StringRelatedField()
    class Meta:
        model = DelayNotification
        fields = "__all__"

class StakeholderInputSerializer(serializers.ModelSerializer):
    procurement_need = serializers.StringRelatedField()
    stakeholder = serializers.StringRelatedField()
    class Meta:
        model = StakeholderInput
        fields = "__all__"

class TenderDocumentSerializer(serializers.ModelSerializer):
    prepared_by = serializers.StringRelatedField()
    class Meta:
        model = TenderDocument
        fields = "__all__"

class IssueSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    class Meta:
        model = Issue
        fields = "__all__"

class RFPRFQResponseSerializer(serializers.ModelSerializer):
    distribution = serializers.StringRelatedField()
    class Meta:
        model = RFPRFQResponse
        fields = "__all__"

class ClarificationResponseSerializer(serializers.ModelSerializer):
    clarification = serializers.StringRelatedField()
    class Meta:
        model = ClarificationResponse
        fields = "__all__"

class FinalVendorSelectionSerializer(serializers.ModelSerializer):
    vendor_proposal = serializers.StringRelatedField()
    class Meta:
        model = FinalVendorSelection
        fields = "__all__"

class FinancialEvaluationSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = FinancialEvaluation
        fields = "__all__"

class NegotiationStakeholderSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    stakeholder = serializers.StringRelatedField()
    vendor_proposal = serializers.StringRelatedField()
    class Meta:
        model = NegotiationStakeholder
        fields = "__all__"

class NegotiationSummarySerializer(serializers.ModelSerializer):
    vendor_proposal = serializers.StringRelatedField()
    class Meta:
        model = NegotiationSummary
        fields = "__all__"

class NegotiationTermSerializer(serializers.ModelSerializer):
    vendor_proposal = serializers.StringRelatedField()
    class Meta:
        model = NegotiationTerm
        fields = "__all__"

class ProposalComplianceSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = ProposalCompliance
        fields = "__all__"

class ProposalEvaluationSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = ProposalEvaluation
        fields = "__all__"

class ProposalScoringSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    criteria = serializers.StringRelatedField()
    class Meta:
        model = ProposalScoring
        fields = "__all__"

class RiskEvaluationSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = RiskEvaluation
        fields = "__all__"

class TechnicalEvaluationSerializer(serializers.ModelSerializer):
    proposal = serializers.StringRelatedField()
    class Meta:
        model = TechnicalEvaluation
        fields = "__all__"

class ProposalSerializer(serializers.ModelSerializer):
    opportunity = serializers.StringRelatedField()
    class Meta:
        model = Proposal
        fields = "__all__"

class AuditLogSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    change_order = serializers.StringRelatedField()
    class Meta:
        model = AuditLog
        fields = "__all__"

class ChangeOrderApprovalSerializer(serializers.ModelSerializer):
    change_order = serializers.StringRelatedField()
    class Meta:
        model = ChangeOrderApproval
        fields = "__all__"

class ChangeOrderImplementationSerializer(serializers.ModelSerializer):
    change_order = serializers.StringRelatedField()
    class Meta:
        model = ChangeOrderImplementation
        fields = "__all__"

class DocumentSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    change_order = serializers.StringRelatedField()
    class Meta:
        model = Document
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    purchase_order = serializers.StringRelatedField()
    class Meta:
        model = Invoice
        fields = "__all__"

class ShipmentSerializer(serializers.ModelSerializer):
    purchase_order = serializers.StringRelatedField()
    class Meta:
        model = Shipment
        fields = "__all__"

class CriticalPathSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    task = serializers.StringRelatedField()
    class Meta:
        model = CriticalPath
        fields = "__all__"

class DailyProgressReportSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    reported_by = serializers.StringRelatedField()
    class Meta:
        model = DailyProgressReport
        fields = "__all__"

class DelaySerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    cause = serializers.StringRelatedField()
    reported_by = serializers.StringRelatedField()
    class Meta:
        model = Delay
        fields = "__all__"

class PerformanceReportSerializer(serializers.ModelSerializer):
    subcontractor = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    task = serializers.StringRelatedField()
    class Meta:
        model = PerformanceReport
        fields = "__all__"

class PhotoDocumentationSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    class Meta:
        model = PhotoDocumentation
        fields = "__all__"

class ProjectUpdateSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    class Meta:
        model = ProjectUpdate
        fields = "__all__"

class ResourceAdjustmentSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    resource = serializers.StringRelatedField()
    class Meta:
        model = ResourceAdjustment
        fields = "__all__"

class ResourceAllocationSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    allocated_by = serializers.StringRelatedField()
    class Meta:
        model = ResourceAllocation
        fields = "__all__"

class TaskDependencySerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    dependent_task = serializers.StringRelatedField()
    class Meta:
        model = TaskDependency
        fields = "__all__"

class TaskResourceAllocationSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    resource = serializers.StringRelatedField()
    class Meta:
        model = TaskResourceAllocation
        fields = "__all__"

class TaskScheduleSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    class Meta:
        model = TaskSchedule
        fields = "__all__"

class TaskStatusSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    class Meta:
        model = TaskStatus
        fields = "__all__"

class TimesheetSerializer(serializers.ModelSerializer):
    worker = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    task = serializers.StringRelatedField()
    class Meta:
        model = Timesheet
        fields = "__all__"

class TimeTrackingSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = TimeTracking
        fields = "__all__"

class StockAdjustmentSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = StockAdjustment
        fields = "__all__"

class StockReplenishmentRequestSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = StockReplenishmentRequest
        fields = "__all__"

class MitigationActionSerializer(serializers.ModelSerializer):
    mitigation_strategy = serializers.StringRelatedField()
    class Meta:
        model = MitigationAction
        fields = "__all__"

class TenderScopeSerializer(serializers.ModelSerializer):
    tender = serializers.StringRelatedField()
    class Meta:
        model = TenderScope
        fields = "__all__"

class TenderSubmissionSerializer(serializers.ModelSerializer):
    tender = serializers.StringRelatedField()
    class Meta:
        model = TenderSubmission
        fields = "__all__"

class ContractAwardSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField()
    selected_vendor = serializers.StringRelatedField()
    class Meta:
        model = ContractAward
        fields = "__all__"

class StakeholderEvaluationSerializer(serializers.ModelSerializer):
    evaluation = serializers.StringRelatedField()
    stakeholder = serializers.StringRelatedField()
    class Meta:
        model = StakeholderEvaluation
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    invoice = serializers.StringRelatedField()
    project = serializers.StringRelatedField()
    class Meta:
        model = Payment
        fields = "__all__"

class CriticalPathMonitoringSerializer(serializers.ModelSerializer):
    critical_path = serializers.StringRelatedField()
    class Meta:
        model = CriticalPathMonitoring
        fields = "__all__"

class AdjustmentSerializer(serializers.ModelSerializer):
    delay = serializers.StringRelatedField()
    adjusted_task = serializers.StringRelatedField()
    adjusted_by = serializers.StringRelatedField()
    class Meta:
        model = Adjustment
        fields = "__all__"

class ResourceReallocationSerializer(serializers.ModelSerializer):
    original_allocation = serializers.StringRelatedField()
    new_task = serializers.StringRelatedField()
    reallocated_by = serializers.StringRelatedField()
    class Meta:
        model = ResourceReallocation
        fields = "__all__"

class ResourceUsageSerializer(serializers.ModelSerializer):
    task_resource_allocation = serializers.StringRelatedField()
    class Meta:
        model = ResourceUsage
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class BidQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidQualification
        fields = "__all__"

class TenderProposalMa8001nagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderProposalManagement
        fields = "__all__"


class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = "__all__"