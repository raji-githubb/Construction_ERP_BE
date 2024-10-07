from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'dob', 'phone_number']
    
@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['location', 'capacity']
    
@admin.register(Subcontractor)
class SubcontractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'certification', 'experience_years', 'financial_stability_rating', 'references', 'status', 'date_prequalified']
    
@admin.register(OpportunityIdentification)
class OpportunityIdentificationAdmin(admin.ModelAdmin):
    list_display = ['tender_title', 'tender_type', 'identification_date', 'source', 'description', 'relevant_to_company']
    
@admin.register(BidProposal)
class BidProposalAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq_title', 'technical_proposal', 'financial_proposal', 'internal_collaboration', 'submission_date', 'status']
    
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'exchange_rate']
    
@admin.register(ClientInteractionType)
class ClientInteractionTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    
@admin.register(CostCategory)
class CostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'account_type', 'balance']
    
@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'phone', 'email', 'address']
    
@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    
@admin.register(RiskOwner)
class RiskOwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    
@admin.register(SalesStage)
class SalesStageAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'phone', 'email', 'address']
    
@admin.register(RiskCategory)
class RiskCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'contact_email', 'contact_phone']
    
@admin.register(DelayCause)
class DelayCauseAdmin(admin.ModelAdmin):
    list_display = ['cause']
    
@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ['name', 'skills']
    
@admin.register(InternalDepartment)
class InternalDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'projected_end_date', 'progress', 'budget', 'location', 'manager']
    
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['resource_type', 'description']
    
@admin.register(RFPRFQ)
class RFPRFQAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'description', 'submission_deadline', 'contact_email', 'procurement_manager']
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
@admin.register(ScoringCriteria)
class ScoringCriteriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight']
    
@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    
@admin.register(TaskDurationEstimation)
class TaskDurationEstimationAdmin(admin.ModelAdmin):
    list_display = ['estimated_duration']
    
@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ['priority_level']
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'phone_number', 'address', 'financial_standing', 'experience_years']
    
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'purchase_date', 'purchase_cost', 'depreciation_rate', 'location', 'assigned_to', 'status']
    
@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['subcontractor', 'area_of_expertise', 'certifications', 'performance_rating']
    
@admin.register(BidNoBidDecision)
class BidNoBidDecisionAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'decision_date', 'is_bid', 'rationale', 'profitability_assessment', 'resource_capacity_assessment']
    
@admin.register(ProposalPreparation)
class ProposalPreparationAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'proposal_title', 'technical_solutions', 'pricing', 'timelines', 'value_propositions', 'compliance_check']
    
@admin.register(BidSubmission)
class BidSubmissionAdmin(admin.ModelAdmin):
    list_display = ['bid_proposal', 'submission_date', 'submission_method', 'documents_included']
    
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'serial_number', 'purchase_date', 'condition', 'location', 'status']
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['message', 'is_read', 'timestamp']
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'supplier', 'stock_quantity', 'reorder_point', 'safety_stock', 'price_per_unit', 'warehouse', 'barcode']
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'email', 'phone', 'project_description', 'source', 'status', 'budget', 'urgency', 'decision_maker', 'assigned_to']
    
@admin.register(ProcurementNeed)
class ProcurementNeedAdmin(admin.ModelAdmin):
    list_display = ['department', 'description', 'quantity', 'date_needed']
    
@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ['project', 'audit_type', 'conducted_by', 'date', 'findings']
    
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['project', 'subcontractor', 'bid_amount', 'bid_submission_date', 'status', 'notes']
    
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['project', 'total_budget', 'allocated_budget', 'remaining_budget', 'currency']
    
@admin.register(BudgetAllocation)
class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = ['project', 'materials_cost', 'labor_cost', 'equipment_cost', 'contingency_cost', 'total_budget']
    
@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ['project', 'feedback_date', 'client_name', 'satisfaction_rating', 'comments']
    
@admin.register(ClientFollowUp)
class ClientFollowUpAdmin(admin.ModelAdmin):
    list_display = ['project', 'follow_up_date', 'message', 'action_taken']
    
@admin.register(ClientSatisfactionSurvey)
class ClientSatisfactionSurveyAdmin(admin.ModelAdmin):
    list_display = ['project', 'sent_date', 'client_feedback', 'score']
    
@admin.register(CloseoutDocument)
class CloseoutDocumentAdmin(admin.ModelAdmin):
    list_display = ['project', 'document_type', 'uploaded_at']
    
@admin.register(ComplianceMonitor)
class ComplianceMonitorAdmin(admin.ModelAdmin):
    list_display = ['project', 'compliance_type', 'description', 'status', 'date']
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['project', 'contractor', 'scope_of_work', 'pricing', 'payment_terms', 'start_date', 'end_date', 'signed_by_client', 'signed_by_contractor', 'approved_by', 'status']
    
@admin.register(ContractAwardExecution)
class ContractAwardExecutionAdmin(admin.ModelAdmin):
    list_display = ['contract_title', 'project_manager', 'execution_status', 'delivery_commitments', 'execution_notes']
    
@admin.register(CostEstimation)
class CostEstimationAdmin(admin.ModelAdmin):
    list_display = ['project', 'category', 'estimated_cost', 'actual_cost', 'forecast_cost', 'description']
    
@admin.register(FinalClientSignOff)
class FinalClientSignOffAdmin(admin.ModelAdmin):
    list_display = ['project', 'client', 'sign_off_date', 'is_approved', 'comments']
    
@admin.register(FinalInspection)
class FinalInspectionAdmin(admin.ModelAdmin):
    list_display = ['project', 'inspection_date', 'inspector', 'client_present', 'comments', 'all_punch_items_resolved']
    
@admin.register(FinalReview)
class FinalReviewAdmin(admin.ModelAdmin):
    list_display = ['project', 'review_type', 'review_details', 'conducted_by', 'date']
    
@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    list_display = ['project', 'account', 'transaction_type', 'amount', 'description', 'date']
    
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ['project', 'reported_by', 'incident_type', 'description', 'date_reported', 'immediate_action']
    
@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['project', 'inspector', 'inspection_type', 'date', 'checklist', 'findings']
    
@admin.register(LegalRequirement)
class LegalRequirementAdmin(admin.ModelAdmin):
    list_display = ['project', 'description', 'requirement_type']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['project', 'content', 'timestamp']
    
@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'target_date', 'client_review_required']
    
@admin.register(MilestoneBilling)
class MilestoneBillingAdmin(admin.ModelAdmin):
    list_display = ['project', 'milestone_name', 'description', 'due_date', 'amount', 'invoiced']
    
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['worker', 'project', 'pay_period_start', 'pay_period_end', 'total_hours', 'hourly_rate', 'total_pay']
    
@admin.register(PostProjectReview)
class PostProjectReviewAdmin(admin.ModelAdmin):
    list_display = ['project', 'review_date', 'evaluation_summary', 'strengths', 'areas_for_improvement', 'lessons_learned', 'recommendations']
    
@admin.register(ProjectCloseout)
class ProjectCloseoutAdmin(admin.ModelAdmin):
    list_display = ['project', 'subcontractor', 'final_inspection_date', 'punch_list_items', 'punch_list_completed', 'final_payment']
    
@admin.register(ProjectCommunication)
class ProjectCommunicationAdmin(admin.ModelAdmin):
    list_display = ['project', 'communication_date', 'message']
    
@admin.register(ProjectDocumentation)
class ProjectDocumentationAdmin(admin.ModelAdmin):
    list_display = ['project', 'document_type', 'issue_date', 'description']
    
@admin.register(ProjectFinancialCloseout)
class ProjectFinancialCloseoutAdmin(admin.ModelAdmin):
    list_display = ['project', 'closeout_date', 'total_cost', 'total_revenue', 'total_profit', 'subcontractors_paid', 'purchase_orders_closed']
    
@admin.register(ProjectPerformanceReview)
class ProjectPerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ['project', 'review_date', 'original_budget', 'actual_budget', 'resource_utilization_percentage', 'notes']
    
@admin.register(ProjectSchedule)
class ProjectScheduleAdmin(admin.ModelAdmin):
    list_display = ['project', 'start_date', 'end_date']
    
@admin.register(PunchListItem)
class PunchListItemAdmin(admin.ModelAdmin):
    list_display = ['project', 'description', 'status', 'contractor', 'resolved_at', 'fix_deadline', 'inspected', 'quality_meets_standards']
    
@admin.register(QualityControlPlan)
class QualityControlPlanAdmin(admin.ModelAdmin):
    list_display = ['project', 'content']
    
@admin.register(QualityInspector)
class QualityInspectorAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'designation']
    
@admin.register(ResourcePlanning)
class ResourcePlanningAdmin(admin.ModelAdmin):
    list_display = ['project', 'workforce_required', 'project_duration']
    
@admin.register(ResourceUtilizationAnalysis)
class ResourceUtilizationAnalysisAdmin(admin.ModelAdmin):
    list_display = ['project', 'analysis_date', 'total_labor_hours', 'total_materials_cost', 'total_equipment_cost', 'labor_utilization_percentage', 'materials_utilization_percentage', 'equipment_utilization_percentage', 'recommendations']
    
@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ['project', 'customer', 'description', 'amount', 'date', 'received_by']
    
@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ['project', 'risk_category', 'name', 'description', 'risk_type', 'date_identified', 'owner', 'status']
    
@admin.register(SafetyOfficer)
class SafetyOfficerAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'designation']
    
@admin.register(SafetyPlan)
class SafetyPlanAdmin(admin.ModelAdmin):
    list_display = ['project', 'content']
    
@admin.register(SubcontractorContract)
class SubcontractorContractAdmin(admin.ModelAdmin):
    list_display = ['project', 'subcontractor', 'signed_date', 'payment_terms', 'insurance_requirements', 'change_order_provision', 'termination_conditions']
    
@admin.register(ResourceAvailability)
class ResourceAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['resource', 'available_from', 'available_until']
    
@admin.register(ClarificationDocument)
class ClarificationDocumentAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq', 'issued_at']
    
@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'project']
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['project', 'role', 'permissions']
    
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['project', 'account', 'vendor', 'description', 'amount', 'date', 'approved_by']
    
@admin.register(PrequalificationQuestionnaire)
class PrequalificationQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'project_experience', 'financial_status', 'certifications', 'safety_records', 'other_qualifications']
    
@admin.register(RFPRFQDistribution)
class RFPRFQDistributionAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq', 'vendor', 'date_sent', 'response_submitted', 'submission_date']
    
@admin.register(SupplierPerformanceEvaluation)
class SupplierPerformanceEvaluationAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'project', 'evaluation_date', 'delivery_timeliness', 'quality_of_products_services', 'overall_execution', 'comments', 'average_score']
    
@admin.register(VendorClarification)
class VendorClarificationAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq', 'vendor', 'question', 'submitted_at']
    
@admin.register(VendorPrequalificationStatus)
class VendorPrequalificationStatusAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'prequalified', 'prequalification_date', 'reasons_for_rejection']
    
@admin.register(VendorProposal)
class VendorProposalAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq', 'vendor', 'submitted_at', 'is_compliant', 'compliance_remarks']
    
@admin.register(AssetAudit)
class AssetAuditAdmin(admin.ModelAdmin):
    list_display = ['asset', 'audit_date', 'condition', 'comments']
    
@admin.register(AssetMaintenance)
class AssetMaintenanceAdmin(admin.ModelAdmin):
    list_display = ['asset', 'maintenance_date', 'maintenance_type', 'cost', 'notes']
    
@admin.register(Depreciation)
class DepreciationAdmin(admin.ModelAdmin):
    list_display = ['asset', 'depreciation_date', 'amount']
    
@admin.register(SubmissionFollowUp)
class SubmissionFollowUpAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'submission_date', 'follow_up_date', 'follow_up_notes', 'negotiation_engaged', 'revisions_required']
    
@admin.register(NegotiationAndAward)
class NegotiationAndAwardAdmin(admin.ModelAdmin):
    list_display = ['bid_submission', 'negotiation_date', 'negotiation_notes', 'final_terms', 'awarded', 'internal_preparation_started']
    
@admin.register(PostSubmissionFollowUp)
class PostSubmissionFollowUpAdmin(admin.ModelAdmin):
    list_display = ['bid_submission', 'follow_up_date', 'communication_method', 'client_response', 'clarification_requested', 'additional_info_provided']
    
@admin.register(EquipmentAssignment)
class EquipmentAssignmentAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'assigned_to', 'assigned_date', 'return_date']
    
@admin.register(EquipmentAudit)
class EquipmentAuditAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'audit_date', 'condition', 'comments']
    
@admin.register(EquipmentMaintenance)
class EquipmentMaintenanceAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'maintenance_date', 'maintenance_type', 'cost', 'notes']
    
@admin.register(InventoryAudit)
class InventoryAuditAdmin(admin.ModelAdmin):
    list_display = ['item', 'audit_date', 'physical_count', 'system_count', 'discrepancy', 'comments']
    
@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'requested_by', 'date_requested', 'date_fulfilled']
    
@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'movement_type', 'date']
    
@admin.register(ClientInteraction)
class ClientInteractionAdmin(admin.ModelAdmin):
    list_display = ['lead', 'interaction_type', 'description', 'date', 'follow_up_date']
    
@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['lead', 'stage', 'amount', 'probability', 'expected_close_date', 'assigned_to']
    
@admin.register(DocumentedRequirement)
class DocumentedRequirementAdmin(admin.ModelAdmin):
    list_display = ['procurement_need', 'requirement_description', 'quantity', 'timeline', 'budget_estimate', 'technical_specifications', 'quality_specifications']
    
@admin.register(CorrectivePreventiveAction)
class CorrectivePreventiveActionAdmin(admin.ModelAdmin):
    list_display = ['audit', 'description', 'date_taken', 'status']
    
@admin.register(ChangeOrder)
class ChangeOrderAdmin(admin.ModelAdmin):
    list_display = ['contract', 'requestor', 'description', 'change_reason', 'impact_on_scope', 'cost_impact', 'time_impact', 'status', 'submitted_date', 'approved_date']
    
@admin.register(ContractCloseout)
class ContractCloseoutAdmin(admin.ModelAdmin):
    list_display = ['contract', 'closeout_date', 'final_review_notes', 'signed_off_by']
    
@admin.register(ContractExecution)
class ContractExecutionAdmin(admin.ModelAdmin):
    list_display = ['contract', 'execution_date', 'status', 'notes']
    
@admin.register(ContractMilestone)
class ContractMilestoneAdmin(admin.ModelAdmin):
    list_display = ['contract', 'name', 'description', 'due_date', 'completed']
    
@admin.register(LegalReview)
class LegalReviewAdmin(admin.ModelAdmin):
    list_display = ['contract', 'review_date', 'reviewed_by', 'approval_status', 'comments']
    
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['contract', 'order_number', 'order_date', 'product_service_description', 'quantity', 'unit_price', 'total_price', 'status']
    
@admin.register(CorrectiveAction)
class CorrectiveActionAdmin(admin.ModelAdmin):
    list_display = ['incident', 'description', 'action_taken_by', 'date_taken', 'status']
    
@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
    list_display = ['incident', 'investigator', 'findings', 'root_cause', 'investigation_date']
    
@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ['milestone', 'client_feedback', 'approved']
    
@admin.register(ScheduleAdjustment)
class ScheduleAdjustmentAdmin(admin.ModelAdmin):
    list_display = ['project', 'milestone', 'adjustment_date', 'new_date', 'reason', 'adjusted_by']
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['milestone', 'name', 'description', 'is_completed', 'duration_estimation', 'priority', 'category', 'assigned_team', 'start_date', 'end_date', 'task_owner']
    
@admin.register(SiteInspection)
class SiteInspectionAdmin(admin.ModelAdmin):
    list_display = ['project', 'inspection_date', 'inspector', 'observations']
    
@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = ['resource_planning', 'name', 'quantity']
    
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['resource_planning', 'name', 'quantity']
    
@admin.register(MitigationStrategy)
class MitigationStrategyAdmin(admin.ModelAdmin):
    list_display = ['risk', 'strategy', 'mitigation_owner', 'start_date', 'end_date', 'status']
    
@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ['project', 'risk', 'probability', 'impact', 'overall_risk_score']
    
@admin.register(RiskReview)
class RiskReviewAdmin(admin.ModelAdmin):
    list_display = ['risk', 'review_date', 'status', 'comments', 'reviewed_by']
    
@admin.register(DelayNotification)
class DelayNotificationAdmin(admin.ModelAdmin):
    list_display = ['project', 'stakeholder', 'notification_date', 'message', 'updated_timeline', 'plan_to_mitigate']
    
@admin.register(StakeholderInput)
class StakeholderInputAdmin(admin.ModelAdmin):
    list_display = ['procurement_need', 'stakeholder', 'input_description']
    
@admin.register(TenderDocument)
class TenderDocumentAdmin(admin.ModelAdmin):
    list_display = ['tender_type', 'title', 'description', 'prepared_by', 'issue_date', 'closing_date']
    
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['project', 'issue_type', 'description', 'status', 'assigned_to', 'timestamp']
    
@admin.register(RFPRFQResponse)
class RFPRFQResponseAdmin(admin.ModelAdmin):
    list_display = ['distribution', 'response_text', 'submitted_at']
    
@admin.register(ClarificationResponse)
class ClarificationResponseAdmin(admin.ModelAdmin):
    list_display = ['clarification', 'response', 'responded_at']
    
@admin.register(FinalVendorSelection)
class FinalVendorSelectionAdmin(admin.ModelAdmin):
    list_display = ['vendor_proposal', 'selection_date', 'justification', 'approved_by']
    
@admin.register(FinancialEvaluation)
class FinancialEvaluationAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'quoted_price', 'hidden_costs', 'delivery_schedule_assessment', 'warranties_offered', 'after_sales_service']
    
@admin.register(NegotiationStakeholder)
class NegotiationStakeholderAdmin(admin.ModelAdmin):
    list_display = ['team', 'stakeholder', 'vendor_proposal', 'feedback']
    
@admin.register(NegotiationSummary)
class NegotiationSummaryAdmin(admin.ModelAdmin):
    list_display = ['vendor_proposal', 'summary', 'final_terms_agreed']
    
@admin.register(NegotiationTerm)
class NegotiationTermAdmin(admin.ModelAdmin):
    list_display = ['description', 'proposed_value', 'negotiated_value', 'vendor_proposal']
    
@admin.register(ProposalCompliance)
class ProposalComplianceAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'certification_compliance', 'technical_spec_compliance', 'other_compliance']
    
@admin.register(ProposalEvaluation)
class ProposalEvaluationAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'total_score', 'shortlisted', 'notes']
    
@admin.register(ProposalScoring)
class ProposalScoringAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'criteria', 'score']
    
@admin.register(RiskEvaluation)
class RiskEvaluationAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'vendor_reliability', 'financial_stability', 'logistical_issues', 'overall_risk_level']
    
@admin.register(TechnicalEvaluation)
class TechnicalEvaluationAdmin(admin.ModelAdmin):
    list_display = ['proposal', 'meets_technical_specs', 'quality_assessment', 'additional_technical_remarks']
    
@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'created_date', 'status', 'negotiation_notes']
    
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['contract', 'change_order', 'action', 'action_by', 'action_date', 'notes']
    
@admin.register(ChangeOrderApproval)
class ChangeOrderApprovalAdmin(admin.ModelAdmin):
    list_display = ['change_order', 'approved_by', 'approval_date', 'notes']
    
@admin.register(ChangeOrderImplementation)
class ChangeOrderImplementationAdmin(admin.ModelAdmin):
    list_display = ['change_order', 'implementation_details', 'implementation_date', 'new_deadline']
    
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['contract', 'change_order', 'document_name', 'upload_date']
    
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['purchase_order', 'vendor_name', 'invoice_number', 'invoice_date', 'total_amount', 'payment_status']
    
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['purchase_order', 'shipment_number']
    
@admin.register(CriticalPath)
class CriticalPathAdmin(admin.ModelAdmin):
    list_display = ['project', 'task', 'estimated_duration', 'is_on_critical_path']
    
@admin.register(DailyProgressReport)
class DailyProgressReportAdmin(admin.ModelAdmin):
    list_display = ['task', 'report_date', 'description', 'worker_count', 'machinery_in_use', 'materials_used', 'completion_percentage', 'progress_percentage', 'issues_encountered', 'reported_by']
    
@admin.register(Delay)
class DelayAdmin(admin.ModelAdmin):
    list_display = ['task', 'cause', 'reported_by', 'reported_at', 'notes']
    
@admin.register(PerformanceReport)
class PerformanceReportAdmin(admin.ModelAdmin):
    list_display = ['subcontractor', 'project', 'task', 'report_date', 'tasks_completed', 'issues_encountered', 'safety_compliance']
    
@admin.register(PhotoDocumentation)
class PhotoDocumentationAdmin(admin.ModelAdmin):
    list_display = ['task', 'description', 'geo_tag', 'timestamp']
    
@admin.register(ProjectUpdate)
class ProjectUpdateAdmin(admin.ModelAdmin):
    list_display = ['task', 'date', 'planned_start_date', 'actual_start_date', 'planned_end_date', 'actual_end_date', 'progress_percentage', 'comments']
    
@admin.register(ResourceAdjustment)
class ResourceAdjustmentAdmin(admin.ModelAdmin):
    list_display = ['task', 'resource', 'adjustment_date', 'new_schedule', 'reason']
    
@admin.register(ResourceAllocation)
class ResourceAllocationAdmin(admin.ModelAdmin):
    list_display = ['task', 'resource_type', 'allocated_quantity', 'allocated_by', 'allocated_at']
    
@admin.register(TaskDependency)
class TaskDependencyAdmin(admin.ModelAdmin):
    list_display = ['task', 'dependent_task']
    
@admin.register(TaskResourceAllocation)
class TaskResourceAllocationAdmin(admin.ModelAdmin):
    list_display = ['task', 'resource', 'quantity']
    
@admin.register(TaskSchedule)
class TaskScheduleAdmin(admin.ModelAdmin):
    list_display = ['task', 'scheduled_start_date', 'scheduled_end_date']
    
@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['task', 'status', 'update_date']
    
@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['worker', 'project', 'date', 'hours_worked', 'task', 'submitted', 'reviewed', 'comments']
    
@admin.register(TimeTracking)
class TimeTrackingAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'date', 'hours_spent', 'hourly_rate', 'total_cost']
    
@admin.register(StockAdjustment)
class StockAdjustmentAdmin(admin.ModelAdmin):
    list_display = ['material', 'project', 'quantity_adjusted', 'reason', 'adjustment_date']
    
@admin.register(StockReplenishmentRequest)
class StockReplenishmentRequestAdmin(admin.ModelAdmin):
    list_display = ['material', 'project', 'quantity_requested', 'request_date']
    
@admin.register(MitigationAction)
class MitigationActionAdmin(admin.ModelAdmin):
    list_display = ['mitigation_strategy', 'action_name', 'action_description', 'due_date', 'completed', 'completed_date']
    
@admin.register(TenderScope)
class TenderScopeAdmin(admin.ModelAdmin):
    list_display = ['tender', 'scope_description', 'technical_specifications', 'delivery_timeline', 'quality_standards']
    
@admin.register(TenderSubmission)
class TenderSubmissionAdmin(admin.ModelAdmin):
    list_display = ['tender', 'vendor_name', 'proposal_details', 'submitted_on', 'cost_estimate']
    
@admin.register(ContractAward)
class ContractAwardAdmin(admin.ModelAdmin):
    list_display = ['contract', 'selected_vendor', 'award_date', 'notification_sent_to_vendor', 'notification_sent_to_bidders', 'feedback_to_bidders']
    
@admin.register(StakeholderEvaluation)
class StakeholderEvaluationAdmin(admin.ModelAdmin):
    list_display = ['evaluation', 'stakeholder', 'feedback']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'payment_date', 'amount_paid', 'payment_method', 'payment_reference', 'project', 'milestone', 'payment_due', 'status']
    
@admin.register(CriticalPathMonitoring)
class CriticalPathMonitoringAdmin(admin.ModelAdmin):
    list_display = ['critical_path', 'actual_start_date', 'actual_end_date', 'delay_days', 'comments']
    
@admin.register(Adjustment)
class AdjustmentAdmin(admin.ModelAdmin):
    list_display = ['delay', 'adjusted_task', 'new_start_date', 'new_end_date', 'adjusted_by', 'adjustment_reason', 'adjusted_at']
    
@admin.register(ResourceReallocation)
class ResourceReallocationAdmin(admin.ModelAdmin):
    list_display = ['original_allocation', 'new_task', 'reallocated_quantity', 'reason', 'reallocated_by', 'reallocated_at']
    
@admin.register(ResourceUsage)
class ResourceUsageAdmin(admin.ModelAdmin):
    list_display = ['task_resource_allocation', 'start_time', 'end_time', 'quantity_used']
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact_person', 'email', 'phone']
    
@admin.register(BidQualification)
class BidQualificationAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq_title', 'response_due_date', 'alignment_with_strategy', 'capacity_evaluation', 'is_qualified']
    
@admin.register(TenderProposalManagement)
class TenderProposalManagementAdmin(admin.ModelAdmin):
    list_display = ['rfp_rfq_title', 'issued_date', 'response_deadline', 'response_tracking', 'issued_by']
    