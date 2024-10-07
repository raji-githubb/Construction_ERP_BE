from django.core.exceptions import ValidationError
from .models import *
from .serializers import *
from .middleware import get_current_request
from .scripts import *

#Create your views here.

def create_user(first_name, middle_name, last_name, dob, phone_number):
    """
    Creates a User instance with the provided data.
        Args:
        first_name, middle_name, last_name, dob, phone_number: Keyword arguments for User fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = User.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            dob=dob,
            phone_number=phone_number,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_user(user_id,first_name=None, middle_name=None, last_name=None, dob=None, phone_number=None):
    """
    Updates a User instance with the provided data.
    
    Args:
        user_id (int): ID of the User to update.
        first_name=None, middle_name=None, last_name=None, dob=None, phone_number=None: Keyword arguments for User fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = User.objects.get(pk=user_id)
        instance.first_name = first_name if first_name is not None else instance.first_name
        instance.middle_name = middle_name if middle_name is not None else instance.middle_name
        instance.last_name = last_name if last_name is not None else instance.last_name
        instance.dob = dob if dob is not None else instance.dob
        instance.phone_number = phone_number if phone_number is not None else instance.phone_number
        instance.save()
        return success('Successfully Updated')
    except  User.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_user(user_id=None):
    """
    Retrieves and serializes a User instance by its ID or all instances if ID is None.
    
    Args:
        User_id (int, optional): ID of the User to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if user_id is not None:
            record = User.objects.get(pk=user_id)
            serializer = UserSerializer(record)
        else:
            records = User.objects.all()
            serializer = UserSerializer(records, many=True)
        return success(serializer.data)
    
    except User.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('User does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_user(user_id):
    """
    Deletes a User instance with the given ID.
    
    Args:
        user_id (int): ID of the User to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = User.objects.get(pk=user_id)
        instance.delete()
        return success("Successfully deleted")
    
    except User.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_assetcategory(name):
    """
    Creates a AssetCategory instance with the provided data.
        Args:
        name: Keyword arguments for AssetCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AssetCategory.objects.create(
            name=name,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_assetcategory(assetcategory_id,name=None):
    """
    Updates a AssetCategory instance with the provided data.
    
    Args:
        assetcategory_id (int): ID of the AssetCategory to update.
        name=None: Keyword arguments for AssetCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AssetCategory.objects.get(pk=assetcategory_id)
        instance.name = name if name is not None else instance.name
        instance.save()
        return success('Successfully Updated')
    except  AssetCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_assetcategory(assetcategory_id=None):
    """
    Retrieves and serializes a AssetCategory instance by its ID or all instances if ID is None.
    
    Args:
        AssetCategory_id (int, optional): ID of the AssetCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if assetcategory_id is not None:
            record = AssetCategory.objects.get(pk=assetcategory_id)
            serializer = AssetCategorySerializer(record)
        else:
            records = AssetCategory.objects.all()
            serializer = AssetCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except AssetCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('AssetCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_assetcategory(assetcategory_id):
    """
    Deletes a AssetCategory instance with the given ID.
    
    Args:
        assetcategory_id (int): ID of the AssetCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AssetCategory.objects.get(pk=assetcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except AssetCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_warehouse(location, capacity):
    """
    Creates a Warehouse instance with the provided data.
        Args:
        location, capacity: Keyword arguments for Warehouse fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Warehouse.objects.create(
            location=location,
            capacity=capacity,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_warehouse(warehouse_id,location=None, capacity=None):
    """
    Updates a Warehouse instance with the provided data.
    
    Args:
        warehouse_id (int): ID of the Warehouse to update.
        location=None, capacity=None: Keyword arguments for Warehouse fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Warehouse.objects.get(pk=warehouse_id)
        instance.location = location if location is not None else instance.location
        instance.capacity = capacity if capacity is not None else instance.capacity
        instance.save()
        return success('Successfully Updated')
    except  Warehouse.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_warehouse(warehouse_id=None):
    """
    Retrieves and serializes a Warehouse instance by its ID or all instances if ID is None.
    
    Args:
        Warehouse_id (int, optional): ID of the Warehouse to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if warehouse_id is not None:
            record = Warehouse.objects.get(pk=warehouse_id)
            serializer = WarehouseSerializer(record)
        else:
            records = Warehouse.objects.all()
            serializer = WarehouseSerializer(records, many=True)
        return success(serializer.data)
    
    except Warehouse.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Warehouse does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_warehouse(warehouse_id):
    """
    Deletes a Warehouse instance with the given ID.
    
    Args:
        warehouse_id (int): ID of the Warehouse to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Warehouse.objects.get(pk=warehouse_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Warehouse.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_subcontractor(name, email, phone, address, certification, experience_years, financial_stability_rating, references, status, date_prequalified):
    """
    Creates a Subcontractor instance with the provided data.
        Args:
        name, email, phone, address, certification, experience_years, financial_stability_rating, references, status, date_prequalified: Keyword arguments for Subcontractor fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Subcontractor.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            certification=certification,
            experience_years=experience_years,
            financial_stability_rating=financial_stability_rating,
            references=references,
            status=status,
            date_prequalified=date_prequalified,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_subcontractor(subcontractor_id,name=None, email=None, phone=None, address=None, certification=None, experience_years=None, financial_stability_rating=None, references=None, status=None, date_prequalified=None):
    """
    Updates a Subcontractor instance with the provided data.
    
    Args:
        subcontractor_id (int): ID of the Subcontractor to update.
        name=None, email=None, phone=None, address=None, certification=None, experience_years=None, financial_stability_rating=None, references=None, status=None, date_prequalified=None: Keyword arguments for Subcontractor fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Subcontractor.objects.get(pk=subcontractor_id)
        instance.name = name if name is not None else instance.name
        instance.email = email if email is not None else instance.email
        instance.phone = phone if phone is not None else instance.phone
        instance.address = address if address is not None else instance.address
        instance.certification = certification if certification is not None else instance.certification
        instance.experience_years = experience_years if experience_years is not None else instance.experience_years
        instance.financial_stability_rating = financial_stability_rating if financial_stability_rating is not None else instance.financial_stability_rating
        instance.references = references if references is not None else instance.references
        instance.status = status if status is not None else instance.status
        instance.date_prequalified = date_prequalified if date_prequalified is not None else instance.date_prequalified
        instance.save()
        return success('Successfully Updated')
    except  Subcontractor.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_subcontractor(subcontractor_id=None):
    """
    Retrieves and serializes a Subcontractor instance by its ID or all instances if ID is None.
    
    Args:
        Subcontractor_id (int, optional): ID of the Subcontractor to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractor_id is not None:
            record = Subcontractor.objects.get(pk=subcontractor_id)
            serializer = SubcontractorSerializer(record)
        else:
            records = Subcontractor.objects.all()
            serializer = SubcontractorSerializer(records, many=True)
        return success(serializer.data)
    
    except Subcontractor.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Subcontractor does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_subcontractor(subcontractor_id):
    """
    Deletes a Subcontractor instance with the given ID.
    
    Args:
        subcontractor_id (int): ID of the Subcontractor to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Subcontractor.objects.get(pk=subcontractor_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Subcontractor.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_opportunityidentification(tender_title, tender_type, identification_date, source, description, relevant_to_company):
    """
    Creates a OpportunityIdentification instance with the provided data.
        Args:
        tender_title, tender_type, identification_date, source, description, relevant_to_company: Keyword arguments for OpportunityIdentification fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = OpportunityIdentification.objects.create(
            tender_title=tender_title,
            tender_type=tender_type,
            identification_date=identification_date,
            source=source,
            description=description,
            relevant_to_company=relevant_to_company,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_opportunityidentification(opportunityidentification_id,tender_title=None, tender_type=None, identification_date=None, source=None, description=None, relevant_to_company=None):
    """
    Updates a OpportunityIdentification instance with the provided data.
    
    Args:
        opportunityidentification_id (int): ID of the OpportunityIdentification to update.
        tender_title=None, tender_type=None, identification_date=None, source=None, description=None, relevant_to_company=None: Keyword arguments for OpportunityIdentification fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = OpportunityIdentification.objects.get(pk=opportunityidentification_id)
        instance.tender_title = tender_title if tender_title is not None else instance.tender_title
        instance.tender_type = tender_type if tender_type is not None else instance.tender_type
        instance.identification_date = identification_date if identification_date is not None else instance.identification_date
        instance.source = source if source is not None else instance.source
        instance.description = description if description is not None else instance.description
        instance.relevant_to_company = relevant_to_company if relevant_to_company is not None else instance.relevant_to_company
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  OpportunityIdentification.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_opportunityidentification(opportunityidentification_id=None):
    """
    Retrieves and serializes a OpportunityIdentification instance by its ID or all instances if ID is None.
    
    Args:
        OpportunityIdentification_id (int, optional): ID of the OpportunityIdentification to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunityidentification_id is not None:
            record = OpportunityIdentification.objects.get(pk=opportunityidentification_id)
            serializer = OpportunityIdentificationSerializer(record)
        else:
            records = OpportunityIdentification.objects.all()
            serializer = OpportunityIdentificationSerializer(records, many=True)
        return success(serializer.data)
    
    except OpportunityIdentification.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('OpportunityIdentification does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_opportunityidentification(opportunityidentification_id):
    """
    Deletes a OpportunityIdentification instance with the given ID.
    
    Args:
        opportunityidentification_id (int): ID of the OpportunityIdentification to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = OpportunityIdentification.objects.get(pk=opportunityidentification_id)
        instance.delete()
        return success("Successfully deleted")
    
    except OpportunityIdentification.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_bidproposal(rfp_rfq_title, technical_proposal, financial_proposal, internal_collaboration, submission_date, status):
    """
    Creates a BidProposal instance with the provided data.
        Args:
        rfp_rfq_title, technical_proposal, financial_proposal, internal_collaboration, submission_date, status: Keyword arguments for BidProposal fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidProposal.objects.create(
            rfp_rfq_title=rfp_rfq_title,
            technical_proposal=technical_proposal,
            financial_proposal=financial_proposal,
            internal_collaboration=internal_collaboration,
            submission_date=submission_date,
            status=status,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_bidproposal(bidproposal_id,rfp_rfq_title=None, technical_proposal=None, financial_proposal=None, internal_collaboration=None, submission_date=None, status=None):
    """
    Updates a BidProposal instance with the provided data.
    
    Args:
        bidproposal_id (int): ID of the BidProposal to update.
        rfp_rfq_title=None, technical_proposal=None, financial_proposal=None, internal_collaboration=None, submission_date=None, status=None: Keyword arguments for BidProposal fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidProposal.objects.get(pk=bidproposal_id)
        instance.rfp_rfq_title = rfp_rfq_title if rfp_rfq_title is not None else instance.rfp_rfq_title
        instance.technical_proposal = technical_proposal if technical_proposal is not None else instance.technical_proposal
        instance.financial_proposal = financial_proposal if financial_proposal is not None else instance.financial_proposal
        instance.internal_collaboration = internal_collaboration if internal_collaboration is not None else instance.internal_collaboration
        instance.submission_date = submission_date if submission_date is not None else instance.submission_date
        instance.status = status if status is not None else instance.status
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  BidProposal.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_bidproposal(bidproposal_id=None):
    """
    Retrieves and serializes a BidProposal instance by its ID or all instances if ID is None.
    
    Args:
        BidProposal_id (int, optional): ID of the BidProposal to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bidproposal_id is not None:
            record = BidProposal.objects.get(pk=bidproposal_id)
            serializer = BidProposalSerializer(record)
        else:
            records = BidProposal.objects.all()
            serializer = BidProposalSerializer(records, many=True)
        return success(serializer.data)
    
    except BidProposal.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('BidProposal does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_bidproposal(bidproposal_id):
    """
    Deletes a BidProposal instance with the given ID.
    
    Args:
        bidproposal_id (int): ID of the BidProposal to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidProposal.objects.get(pk=bidproposal_id)
        instance.delete()
        return success("Successfully deleted")
    
    except BidProposal.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_currency(name, symbol, exchange_rate):
    """
    Creates a Currency instance with the provided data.
        Args:
        name, symbol, exchange_rate: Keyword arguments for Currency fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Currency.objects.create(
            name=name,
            symbol=symbol,
            exchange_rate=exchange_rate,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_currency(currency_id,name=None, symbol=None, exchange_rate=None):
    """
    Updates a Currency instance with the provided data.
    
    Args:
        currency_id (int): ID of the Currency to update.
        name=None, symbol=None, exchange_rate=None: Keyword arguments for Currency fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Currency.objects.get(pk=currency_id)
        instance.name = name if name is not None else instance.name
        instance.symbol = symbol if symbol is not None else instance.symbol
        instance.exchange_rate = exchange_rate if exchange_rate is not None else instance.exchange_rate
        instance.save()
        return success('Successfully Updated')
    except  Currency.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_currency(currency_id=None):
    """
    Retrieves and serializes a Currency instance by its ID or all instances if ID is None.
    
    Args:
        Currency_id (int, optional): ID of the Currency to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if currency_id is not None:
            record = Currency.objects.get(pk=currency_id)
            serializer = CurrencySerializer(record)
        else:
            records = Currency.objects.all()
            serializer = CurrencySerializer(records, many=True)
        return success(serializer.data)
    
    except Currency.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Currency does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_currency(currency_id):
    """
    Deletes a Currency instance with the given ID.
    
    Args:
        currency_id (int): ID of the Currency to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Currency.objects.get(pk=currency_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Currency.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientinteractiontype(type_name):
    """
    Creates a ClientInteractionType instance with the provided data.
        Args:
        type_name: Keyword arguments for ClientInteractionType fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientInteractionType.objects.create(
            type_name=type_name,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientinteractiontype(clientinteractiontype_id,type_name=None):
    """
    Updates a ClientInteractionType instance with the provided data.
    
    Args:
        clientinteractiontype_id (int): ID of the ClientInteractionType to update.
        type_name=None: Keyword arguments for ClientInteractionType fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientInteractionType.objects.get(pk=clientinteractiontype_id)
        instance.type_name = type_name if type_name is not None else instance.type_name
        instance.save()
        return success('Successfully Updated')
    except  ClientInteractionType.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientinteractiontype(clientinteractiontype_id=None):
    """
    Retrieves and serializes a ClientInteractionType instance by its ID or all instances if ID is None.
    
    Args:
        ClientInteractionType_id (int, optional): ID of the ClientInteractionType to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientinteractiontype_id is not None:
            record = ClientInteractionType.objects.get(pk=clientinteractiontype_id)
            serializer = ClientInteractionTypeSerializer(record)
        else:
            records = ClientInteractionType.objects.all()
            serializer = ClientInteractionTypeSerializer(records, many=True)
        return success(serializer.data)
    
    except ClientInteractionType.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientInteractionType does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientinteractiontype(clientinteractiontype_id):
    """
    Deletes a ClientInteractionType instance with the given ID.
    
    Args:
        clientinteractiontype_id (int): ID of the ClientInteractionType to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientInteractionType.objects.get(pk=clientinteractiontype_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientInteractionType.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_costcategory(name, description):
    """
    Creates a CostCategory instance with the provided data.
        Args:
        name, description: Keyword arguments for CostCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CostCategory.objects.create(
            name=name,
            description=description,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_costcategory(costcategory_id,name=None, description=None):
    """
    Updates a CostCategory instance with the provided data.
    
    Args:
        costcategory_id (int): ID of the CostCategory to update.
        name=None, description=None: Keyword arguments for CostCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CostCategory.objects.get(pk=costcategory_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.save()
        return success('Successfully Updated')
    except  CostCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_costcategory(costcategory_id=None):
    """
    Retrieves and serializes a CostCategory instance by its ID or all instances if ID is None.
    
    Args:
        CostCategory_id (int, optional): ID of the CostCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if costcategory_id is not None:
            record = CostCategory.objects.get(pk=costcategory_id)
            serializer = CostCategorySerializer(record)
        else:
            records = CostCategory.objects.all()
            serializer = CostCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except CostCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CostCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_costcategory(costcategory_id):
    """
    Deletes a CostCategory instance with the given ID.
    
    Args:
        costcategory_id (int): ID of the CostCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CostCategory.objects.get(pk=costcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CostCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_equipmentcategory(name):
    """
    Creates a EquipmentCategory instance with the provided data.
        Args:
        name: Keyword arguments for EquipmentCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentCategory.objects.create(
            name=name,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_equipmentcategory(equipmentcategory_id,name=None):
    """
    Updates a EquipmentCategory instance with the provided data.
    
    Args:
        equipmentcategory_id (int): ID of the EquipmentCategory to update.
        name=None: Keyword arguments for EquipmentCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentCategory.objects.get(pk=equipmentcategory_id)
        instance.name = name if name is not None else instance.name
        instance.save()
        return success('Successfully Updated')
    except  EquipmentCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_equipmentcategory(equipmentcategory_id=None):
    """
    Retrieves and serializes a EquipmentCategory instance by its ID or all instances if ID is None.
    
    Args:
        EquipmentCategory_id (int, optional): ID of the EquipmentCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipmentcategory_id is not None:
            record = EquipmentCategory.objects.get(pk=equipmentcategory_id)
            serializer = EquipmentCategorySerializer(record)
        else:
            records = EquipmentCategory.objects.all()
            serializer = EquipmentCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except EquipmentCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('EquipmentCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_equipmentcategory(equipmentcategory_id):
    """
    Deletes a EquipmentCategory instance with the given ID.
    
    Args:
        equipmentcategory_id (int): ID of the EquipmentCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentCategory.objects.get(pk=equipmentcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except EquipmentCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_account(name, account_type, balance):
    """
    Creates a Account instance with the provided data.
        Args:
        name, account_type, balance: Keyword arguments for Account fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Account.objects.create(
            name=name,
            account_type=account_type,
            balance=balance,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_account(account_id,name=None, account_type=None, balance=None):
    """
    Updates a Account instance with the provided data.
    
    Args:
        account_id (int): ID of the Account to update.
        name=None, account_type=None, balance=None: Keyword arguments for Account fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Account.objects.get(pk=account_id)
        instance.name = name if name is not None else instance.name
        instance.account_type = account_type if account_type is not None else instance.account_type
        instance.balance = balance if balance is not None else instance.balance
        instance.save()
        return success('Successfully Updated')
    except  Account.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_account(account_id=None):
    """
    Retrieves and serializes a Account instance by its ID or all instances if ID is None.
    
    Args:
        Account_id (int, optional): ID of the Account to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if account_id is not None:
            record = Account.objects.get(pk=account_id)
            serializer = AccountSerializer(record)
        else:
            records = Account.objects.all()
            serializer = AccountSerializer(records, many=True)
        return success(serializer.data)
    
    except Account.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Account does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_account(account_id):
    """
    Deletes a Account instance with the given ID.
    
    Args:
        account_id (int): ID of the Account to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Account.objects.get(pk=account_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Account.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_itemcategory(name):
    """
    Creates a ItemCategory instance with the provided data.
        Args:
        name: Keyword arguments for ItemCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ItemCategory.objects.create(
            name=name,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_itemcategory(itemcategory_id,name=None):
    """
    Updates a ItemCategory instance with the provided data.
    
    Args:
        itemcategory_id (int): ID of the ItemCategory to update.
        name=None: Keyword arguments for ItemCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ItemCategory.objects.get(pk=itemcategory_id)
        instance.name = name if name is not None else instance.name
        instance.save()
        return success('Successfully Updated')
    except  ItemCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_itemcategory(itemcategory_id=None):
    """
    Retrieves and serializes a ItemCategory instance by its ID or all instances if ID is None.
    
    Args:
        ItemCategory_id (int, optional): ID of the ItemCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if itemcategory_id is not None:
            record = ItemCategory.objects.get(pk=itemcategory_id)
            serializer = ItemCategorySerializer(record)
        else:
            records = ItemCategory.objects.all()
            serializer = ItemCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except ItemCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ItemCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_itemcategory(itemcategory_id):
    """
    Deletes a ItemCategory instance with the given ID.
    
    Args:
        itemcategory_id (int): ID of the ItemCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ItemCategory.objects.get(pk=itemcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ItemCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_supplier(name, contact_person, phone, email, address):
    """
    Creates a Supplier instance with the provided data.
        Args:
        name, contact_person, phone, email, address: Keyword arguments for Supplier fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Supplier.objects.create(
            name=name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_supplier(supplier_id,name=None, contact_person=None, phone=None, email=None, address=None):
    """
    Updates a Supplier instance with the provided data.
    
    Args:
        supplier_id (int): ID of the Supplier to update.
        name=None, contact_person=None, phone=None, email=None, address=None: Keyword arguments for Supplier fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Supplier.objects.get(pk=supplier_id)
        instance.name = name if name is not None else instance.name
        instance.contact_person = contact_person if contact_person is not None else instance.contact_person
        instance.phone = phone if phone is not None else instance.phone
        instance.email = email if email is not None else instance.email
        instance.address = address if address is not None else instance.address
        instance.save()
        return success('Successfully Updated')
    except  Supplier.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_supplier(supplier_id=None):
    """
    Retrieves and serializes a Supplier instance by its ID or all instances if ID is None.
    
    Args:
        Supplier_id (int, optional): ID of the Supplier to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if supplier_id is not None:
            record = Supplier.objects.get(pk=supplier_id)
            serializer = SupplierSerializer(record)
        else:
            records = Supplier.objects.all()
            serializer = SupplierSerializer(records, many=True)
        return success(serializer.data)
    
    except Supplier.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Supplier does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_supplier(supplier_id):
    """
    Deletes a Supplier instance with the given ID.
    
    Args:
        supplier_id (int): ID of the Supplier to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Supplier.objects.get(pk=supplier_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Supplier.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_leadsource(name, description):
    """
    Creates a LeadSource instance with the provided data.
        Args:
        name, description: Keyword arguments for LeadSource fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = LeadSource.objects.create(
            name=name,
            description=description,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_leadsource(leadsource_id,name=None, description=None):
    """
    Updates a LeadSource instance with the provided data.
    
    Args:
        leadsource_id (int): ID of the LeadSource to update.
        name=None, description=None: Keyword arguments for LeadSource fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = LeadSource.objects.get(pk=leadsource_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.save()
        return success('Successfully Updated')
    except  LeadSource.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_leadsource(leadsource_id=None):
    """
    Retrieves and serializes a LeadSource instance by its ID or all instances if ID is None.
    
    Args:
        LeadSource_id (int, optional): ID of the LeadSource to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if leadsource_id is not None:
            record = LeadSource.objects.get(pk=leadsource_id)
            serializer = LeadSourceSerializer(record)
        else:
            records = LeadSource.objects.all()
            serializer = LeadSourceSerializer(records, many=True)
        return success(serializer.data)
    
    except LeadSource.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('LeadSource does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_leadsource(leadsource_id):
    """
    Deletes a LeadSource instance with the given ID.
    
    Args:
        leadsource_id (int): ID of the LeadSource to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = LeadSource.objects.get(pk=leadsource_id)
        instance.delete()
        return success("Successfully deleted")
    
    except LeadSource.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_salesrepresentative(name, email, phone):
    """
    Creates a SalesRepresentative instance with the provided data.
        Args:
        name, email, phone: Keyword arguments for SalesRepresentative fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesRepresentative.objects.create(
            name=name,
            email=email,
            phone=phone,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_salesrepresentative(salesrepresentative_id,name=None, email=None, phone=None):
    """
    Updates a SalesRepresentative instance with the provided data.
    
    Args:
        salesrepresentative_id (int): ID of the SalesRepresentative to update.
        name=None, email=None, phone=None: Keyword arguments for SalesRepresentative fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesRepresentative.objects.get(pk=salesrepresentative_id)
        instance.name = name if name is not None else instance.name
        instance.email = email if email is not None else instance.email
        instance.phone = phone if phone is not None else instance.phone
        instance.save()
        return success('Successfully Updated')
    except  SalesRepresentative.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_salesrepresentative(salesrepresentative_id=None):
    """
    Retrieves and serializes a SalesRepresentative instance by its ID or all instances if ID is None.
    
    Args:
        SalesRepresentative_id (int, optional): ID of the SalesRepresentative to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if salesrepresentative_id is not None:
            record = SalesRepresentative.objects.get(pk=salesrepresentative_id)
            serializer = SalesRepresentativeSerializer(record)
        else:
            records = SalesRepresentative.objects.all()
            serializer = SalesRepresentativeSerializer(records, many=True)
        return success(serializer.data)
    
    except SalesRepresentative.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SalesRepresentative does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_salesrepresentative(salesrepresentative_id):
    """
    Deletes a SalesRepresentative instance with the given ID.
    
    Args:
        salesrepresentative_id (int): ID of the SalesRepresentative to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesRepresentative.objects.get(pk=salesrepresentative_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SalesRepresentative.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_riskowner(name, email, phone):
    """
    Creates a RiskOwner instance with the provided data.
        Args:
        name, email, phone: Keyword arguments for RiskOwner fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskOwner.objects.create(
            name=name,
            email=email,
            phone=phone,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_riskowner(riskowner_id,name=None, email=None, phone=None):
    """
    Updates a RiskOwner instance with the provided data.
    
    Args:
        riskowner_id (int): ID of the RiskOwner to update.
        name=None, email=None, phone=None: Keyword arguments for RiskOwner fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskOwner.objects.get(pk=riskowner_id)
        instance.name = name if name is not None else instance.name
        instance.email = email if email is not None else instance.email
        instance.phone = phone if phone is not None else instance.phone
        instance.save()
        return success('Successfully Updated')
    except  RiskOwner.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_riskowner(riskowner_id=None):
    """
    Retrieves and serializes a RiskOwner instance by its ID or all instances if ID is None.
    
    Args:
        RiskOwner_id (int, optional): ID of the RiskOwner to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if riskowner_id is not None:
            record = RiskOwner.objects.get(pk=riskowner_id)
            serializer = RiskOwnerSerializer(record)
        else:
            records = RiskOwner.objects.all()
            serializer = RiskOwnerSerializer(records, many=True)
        return success(serializer.data)
    
    except RiskOwner.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('RiskOwner does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_riskowner(riskowner_id):
    """
    Deletes a RiskOwner instance with the given ID.
    
    Args:
        riskowner_id (int): ID of the RiskOwner to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskOwner.objects.get(pk=riskowner_id)
        instance.delete()
        return success("Successfully deleted")
    
    except RiskOwner.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_salesstage(name):
    """
    Creates a SalesStage instance with the provided data.
        Args:
        name: Keyword arguments for SalesStage fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesStage.objects.create(
            name=name,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_salesstage(salesstage_id,name=None):
    """
    Updates a SalesStage instance with the provided data.
    
    Args:
        salesstage_id (int): ID of the SalesStage to update.
        name=None: Keyword arguments for SalesStage fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesStage.objects.get(pk=salesstage_id)
        instance.name = name if name is not None else instance.name
        instance.save()
        return success('Successfully Updated')
    except  SalesStage.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_salesstage(salesstage_id=None):
    """
    Retrieves and serializes a SalesStage instance by its ID or all instances if ID is None.
    
    Args:
        SalesStage_id (int, optional): ID of the SalesStage to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if salesstage_id is not None:
            record = SalesStage.objects.get(pk=salesstage_id)
            serializer = SalesStageSerializer(record)
        else:
            records = SalesStage.objects.all()
            serializer = SalesStageSerializer(records, many=True)
        return success(serializer.data)
    
    except SalesStage.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SalesStage does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_salesstage(salesstage_id):
    """
    Deletes a SalesStage instance with the given ID.
    
    Args:
        salesstage_id (int): ID of the SalesStage to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SalesStage.objects.get(pk=salesstage_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SalesStage.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_customer(name, contact_person, phone, email, address):
    """
    Creates a Customer instance with the provided data.
        Args:
        name, contact_person, phone, email, address: Keyword arguments for Customer fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Customer.objects.create(
            name=name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_customer(customer_id,name=None, contact_person=None, phone=None, email=None, address=None):
    """
    Updates a Customer instance with the provided data.
    
    Args:
        customer_id (int): ID of the Customer to update.
        name=None, contact_person=None, phone=None, email=None, address=None: Keyword arguments for Customer fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Customer.objects.get(pk=customer_id)
        instance.name = name if name is not None else instance.name
        instance.contact_person = contact_person if contact_person is not None else instance.contact_person
        instance.phone = phone if phone is not None else instance.phone
        instance.email = email if email is not None else instance.email
        instance.address = address if address is not None else instance.address
        instance.save()
        return success('Successfully Updated')
    except  Customer.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_customer(customer_id=None):
    """
    Retrieves and serializes a Customer instance by its ID or all instances if ID is None.
    
    Args:
        Customer_id (int, optional): ID of the Customer to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if customer_id is not None:
            record = Customer.objects.get(pk=customer_id)
            serializer = CustomerSerializer(record)
        else:
            records = Customer.objects.all()
            serializer = CustomerSerializer(records, many=True)
        return success(serializer.data)
    
    except Customer.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Customer does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_customer(customer_id):
    """
    Deletes a Customer instance with the given ID.
    
    Args:
        customer_id (int): ID of the Customer to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Customer.objects.get(pk=customer_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Customer.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_riskcategory(name, description):
    """
    Creates a RiskCategory instance with the provided data.
        Args:
        name, description: Keyword arguments for RiskCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskCategory.objects.create(
            name=name,
            description=description,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_riskcategory(riskcategory_id,name=None, description=None):
    """
    Updates a RiskCategory instance with the provided data.
    
    Args:
        riskcategory_id (int): ID of the RiskCategory to update.
        name=None, description=None: Keyword arguments for RiskCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskCategory.objects.get(pk=riskcategory_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.save()
        return success('Successfully Updated')
    except  RiskCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_riskcategory(riskcategory_id=None):
    """
    Retrieves and serializes a RiskCategory instance by its ID or all instances if ID is None.
    
    Args:
        RiskCategory_id (int, optional): ID of the RiskCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if riskcategory_id is not None:
            record = RiskCategory.objects.get(pk=riskcategory_id)
            serializer = RiskCategorySerializer(record)
        else:
            records = RiskCategory.objects.all()
            serializer = RiskCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except RiskCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('RiskCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_riskcategory(riskcategory_id):
    """
    Deletes a RiskCategory instance with the given ID.
    
    Args:
        riskcategory_id (int): ID of the RiskCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskCategory.objects.get(pk=riskcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except RiskCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_contractor(name, contact_person, contact_email, contact_phone):
    """
    Creates a Contractor instance with the provided data.
        Args:
        name, contact_person, contact_email, contact_phone: Keyword arguments for Contractor fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Contractor.objects.create(
            name=name,
            contact_person=contact_person,
            contact_email=contact_email,
            contact_phone=contact_phone,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_contractor(contractor_id,name=None, contact_person=None, contact_email=None, contact_phone=None):
    """
    Updates a Contractor instance with the provided data.
    
    Args:
        contractor_id (int): ID of the Contractor to update.
        name=None, contact_person=None, contact_email=None, contact_phone=None: Keyword arguments for Contractor fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Contractor.objects.get(pk=contractor_id)
        instance.name = name if name is not None else instance.name
        instance.contact_person = contact_person if contact_person is not None else instance.contact_person
        instance.contact_email = contact_email if contact_email is not None else instance.contact_email
        instance.contact_phone = contact_phone if contact_phone is not None else instance.contact_phone
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Contractor.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_contractor(contractor_id=None):
    """
    Retrieves and serializes a Contractor instance by its ID or all instances if ID is None.
    
    Args:
        Contractor_id (int, optional): ID of the Contractor to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contractor_id is not None:
            record = Contractor.objects.get(pk=contractor_id)
            serializer = ContractorSerializer(record)
        else:
            records = Contractor.objects.all()
            serializer = ContractorSerializer(records, many=True)
        return success(serializer.data)
    
    except Contractor.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Contractor does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_contractor(contractor_id):
    """
    Deletes a Contractor instance with the given ID.
    
    Args:
        contractor_id (int): ID of the Contractor to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Contractor.objects.get(pk=contractor_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Contractor.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_delaycause(cause):
    """
    Creates a DelayCause instance with the provided data.
        Args:
        cause: Keyword arguments for DelayCause fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DelayCause.objects.create(
            cause=cause,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_delaycause(delaycause_id,cause=None):
    """
    Updates a DelayCause instance with the provided data.
    
    Args:
        delaycause_id (int): ID of the DelayCause to update.
        cause=None: Keyword arguments for DelayCause fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DelayCause.objects.get(pk=delaycause_id)
        instance.cause = cause if cause is not None else instance.cause
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  DelayCause.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_delaycause(delaycause_id=None):
    """
    Retrieves and serializes a DelayCause instance by its ID or all instances if ID is None.
    
    Args:
        DelayCause_id (int, optional): ID of the DelayCause to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if delaycause_id is not None:
            record = DelayCause.objects.get(pk=delaycause_id)
            serializer = DelayCauseSerializer(record)
        else:
            records = DelayCause.objects.all()
            serializer = DelayCauseSerializer(records, many=True)
        return success(serializer.data)
    
    except DelayCause.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('DelayCause does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_delaycause(delaycause_id):
    """
    Deletes a DelayCause instance with the given ID.
    
    Args:
        delaycause_id (int): ID of the DelayCause to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DelayCause.objects.get(pk=delaycause_id)
        instance.delete()
        return success("Successfully deleted")
    
    except DelayCause.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_individual(name, skills):
    """
    Creates a Individual instance with the provided data.
        Args:
        name, skills: Keyword arguments for Individual fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Individual.objects.create(
            name=name,
            skills=skills,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_individual(individual_id,name=None, skills=None):
    """
    Updates a Individual instance with the provided data.
    
    Args:
        individual_id (int): ID of the Individual to update.
        name=None, skills=None: Keyword arguments for Individual fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Individual.objects.get(pk=individual_id)
        instance.name = name if name is not None else instance.name
        instance.skills = skills if skills is not None else instance.skills
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Individual.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_individual(individual_id=None):
    """
    Retrieves and serializes a Individual instance by its ID or all instances if ID is None.
    
    Args:
        Individual_id (int, optional): ID of the Individual to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if individual_id is not None:
            record = Individual.objects.get(pk=individual_id)
            serializer = IndividualSerializer(record)
        else:
            records = Individual.objects.all()
            serializer = IndividualSerializer(records, many=True)
        return success(serializer.data)
    
    except Individual.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Individual does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_individual(individual_id):
    """
    Deletes a Individual instance with the given ID.
    
    Args:
        individual_id (int): ID of the Individual to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Individual.objects.get(pk=individual_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Individual.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_internaldepartment(name):
    """
    Creates a InternalDepartment instance with the provided data.
        Args:
        name: Keyword arguments for InternalDepartment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = InternalDepartment.objects.create(
            name=name,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_internaldepartment(internaldepartment_id,name=None):
    """
    Updates a InternalDepartment instance with the provided data.
    
    Args:
        internaldepartment_id (int): ID of the InternalDepartment to update.
        name=None: Keyword arguments for InternalDepartment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = InternalDepartment.objects.get(pk=internaldepartment_id)
        instance.name = name if name is not None else instance.name
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  InternalDepartment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_internaldepartment(internaldepartment_id=None):
    """
    Retrieves and serializes a InternalDepartment instance by its ID or all instances if ID is None.
    
    Args:
        InternalDepartment_id (int, optional): ID of the InternalDepartment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if internaldepartment_id is not None:
            record = InternalDepartment.objects.get(pk=internaldepartment_id)
            serializer = InternalDepartmentSerializer(record)
        else:
            records = InternalDepartment.objects.all()
            serializer = InternalDepartmentSerializer(records, many=True)
        return success(serializer.data)
    
    except InternalDepartment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('InternalDepartment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_internaldepartment(internaldepartment_id):
    """
    Deletes a InternalDepartment instance with the given ID.
    
    Args:
        internaldepartment_id (int): ID of the InternalDepartment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = InternalDepartment.objects.get(pk=internaldepartment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except InternalDepartment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_project(name, description, start_date, projected_end_date, progress, budget, location, manager_id):
    """
    Creates a Project instance with the provided data.
        Args:
        name, description, start_date, projected_end_date, progress, budget, location, manager_id: Keyword arguments for Project fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if manager_id is not None and manager_id != '': 
             User.objects.get(pk=manager_id)
        instance = Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            projected_end_date=projected_end_date,
            progress=progress,
            budget=budget,
            location=location,
            manager_id=manager_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_project(project_id,name=None, description=None, start_date=None, projected_end_date=None, progress=None, budget=None, location=None, manager_id=None):
    """
    Updates a Project instance with the provided data.
    
    Args:
        project_id (int): ID of the Project to update.
        name=None, description=None, start_date=None, projected_end_date=None, progress=None, budget=None, location=None, manager_id=None: Keyword arguments for Project fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if manager_id is not None and manager_id != '': 
             User.objects.get(pk=manager_id)
        instance = Project.objects.get(pk=project_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.start_date = start_date if start_date is not None else instance.start_date
        instance.projected_end_date = projected_end_date if projected_end_date is not None else instance.projected_end_date
        instance.progress = progress if progress is not None else instance.progress
        instance.budget = budget if budget is not None else instance.budget
        instance.location = location if location is not None else instance.location
        instance.manager_id = manager_id if manager_id is not None else instance.manager_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  Project.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_project(project_id=None):
    """
    Retrieves and serializes a Project instance by its ID or all instances if ID is None.
    
    Args:
        Project_id (int, optional): ID of the Project to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None:
            record = Project.objects.get(pk=project_id)
            serializer = ProjectSerializer(record)
        else:
            records = Project.objects.all()
            serializer = ProjectSerializer(records, many=True)
        return success(serializer.data)
    
    except Project.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Project does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_project(project_id):
    """
    Deletes a Project instance with the given ID.
    
    Args:
        project_id (int): ID of the Project to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Project.objects.get(pk=project_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Project.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resource(resource_type, description):
    """
    Creates a Resource instance with the provided data.
        Args:
        resource_type, description: Keyword arguments for Resource fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Resource.objects.create(
            resource_type=resource_type,
            description=description,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resource(resource_id,resource_type=None, description=None):
    """
    Updates a Resource instance with the provided data.
    
    Args:
        resource_id (int): ID of the Resource to update.
        resource_type=None, description=None: Keyword arguments for Resource fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Resource.objects.get(pk=resource_id)
        instance.resource_type = resource_type if resource_type is not None else instance.resource_type
        instance.description = description if description is not None else instance.description
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Resource.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resource(resource_id=None):
    """
    Retrieves and serializes a Resource instance by its ID or all instances if ID is None.
    
    Args:
        Resource_id (int, optional): ID of the Resource to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_id is not None:
            record = Resource.objects.get(pk=resource_id)
            serializer = ResourceSerializer(record)
        else:
            records = Resource.objects.all()
            serializer = ResourceSerializer(records, many=True)
        return success(serializer.data)
    
    except Resource.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Resource does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resource(resource_id):
    """
    Deletes a Resource instance with the given ID.
    
    Args:
        resource_id (int): ID of the Resource to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Resource.objects.get(pk=resource_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Resource.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_rfprfq(title, document_type, description, submission_deadline, contact_email, procurement_manager):
    """
    Creates a RFPRFQ instance with the provided data.
        Args:
        title, document_type, description, submission_deadline, contact_email, procurement_manager: Keyword arguments for RFPRFQ fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RFPRFQ.objects.create(
            title=title,
            document_type=document_type,
            description=description,
            submission_deadline=submission_deadline,
            contact_email=contact_email,
            procurement_manager=procurement_manager,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_rfprfq(rfprfq_id,title=None, document_type=None, description=None, submission_deadline=None, contact_email=None, procurement_manager=None):
    """
    Updates a RFPRFQ instance with the provided data.
    
    Args:
        rfprfq_id (int): ID of the RFPRFQ to update.
        title=None, document_type=None, description=None, submission_deadline=None, contact_email=None, procurement_manager=None: Keyword arguments for RFPRFQ fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RFPRFQ.objects.get(pk=rfprfq_id)
        instance.title = title if title is not None else instance.title
        instance.document_type = document_type if document_type is not None else instance.document_type
        instance.description = description if description is not None else instance.description
        instance.submission_deadline = submission_deadline if submission_deadline is not None else instance.submission_deadline
        instance.contact_email = contact_email if contact_email is not None else instance.contact_email
        instance.procurement_manager = procurement_manager if procurement_manager is not None else instance.procurement_manager
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  RFPRFQ.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_rfprfq(rfprfq_id=None):
    """
    Retrieves and serializes a RFPRFQ instance by its ID or all instances if ID is None.
    
    Args:
        RFPRFQ_id (int, optional): ID of the RFPRFQ to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfprfq_id is not None:
            record = RFPRFQ.objects.get(pk=rfprfq_id)
            serializer = RFPRFQSerializer(record)
        else:
            records = RFPRFQ.objects.all()
            serializer = RFPRFQSerializer(records, many=True)
        return success(serializer.data)
    
    except RFPRFQ.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('RFPRFQ does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_rfprfq(rfprfq_id):
    """
    Deletes a RFPRFQ instance with the given ID.
    
    Args:
        rfprfq_id (int): ID of the RFPRFQ to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RFPRFQ.objects.get(pk=rfprfq_id)
        instance.delete()
        return success("Successfully deleted")
    
    except RFPRFQ.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_role(name, description):
    """
    Creates a Role instance with the provided data.
        Args:
        name, description: Keyword arguments for Role fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Role.objects.create(
            name=name,
            description=description,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_role(role_id,name=None, description=None):
    """
    Updates a Role instance with the provided data.
    
    Args:
        role_id (int): ID of the Role to update.
        name=None, description=None: Keyword arguments for Role fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Role.objects.get(pk=role_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Role.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_role(role_id=None):
    """
    Retrieves and serializes a Role instance by its ID or all instances if ID is None.
    
    Args:
        Role_id (int, optional): ID of the Role to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if role_id is not None:
            record = Role.objects.get(pk=role_id)
            serializer = RoleSerializer(record)
        else:
            records = Role.objects.all()
            serializer = RoleSerializer(records, many=True)
        return success(serializer.data)
    
    except Role.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Role does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_role(role_id):
    """
    Deletes a Role instance with the given ID.
    
    Args:
        role_id (int): ID of the Role to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Role.objects.get(pk=role_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Role.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_scoringcriteria(name, weight):
    """
    Creates a ScoringCriteria instance with the provided data.
        Args:
        name, weight: Keyword arguments for ScoringCriteria fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ScoringCriteria.objects.create(
            name=name,
            weight=weight,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_scoringcriteria(scoringcriteria_id,name=None, weight=None):
    """
    Updates a ScoringCriteria instance with the provided data.
    
    Args:
        scoringcriteria_id (int): ID of the ScoringCriteria to update.
        name=None, weight=None: Keyword arguments for ScoringCriteria fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ScoringCriteria.objects.get(pk=scoringcriteria_id)
        instance.name = name if name is not None else instance.name
        instance.weight = weight if weight is not None else instance.weight
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  ScoringCriteria.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_scoringcriteria(scoringcriteria_id=None):
    """
    Retrieves and serializes a ScoringCriteria instance by its ID or all instances if ID is None.
    
    Args:
        ScoringCriteria_id (int, optional): ID of the ScoringCriteria to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if scoringcriteria_id is not None:
            record = ScoringCriteria.objects.get(pk=scoringcriteria_id)
            serializer = ScoringCriteriaSerializer(record)
        else:
            records = ScoringCriteria.objects.all()
            serializer = ScoringCriteriaSerializer(records, many=True)
        return success(serializer.data)
    
    except ScoringCriteria.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ScoringCriteria does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_scoringcriteria(scoringcriteria_id):
    """
    Deletes a ScoringCriteria instance with the given ID.
    
    Args:
        scoringcriteria_id (int): ID of the ScoringCriteria to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ScoringCriteria.objects.get(pk=scoringcriteria_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ScoringCriteria.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskcategory(category_name):
    """
    Creates a TaskCategory instance with the provided data.
        Args:
        category_name: Keyword arguments for TaskCategory fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskCategory.objects.create(
            category_name=category_name,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskcategory(taskcategory_id,category_name=None):
    """
    Updates a TaskCategory instance with the provided data.
    
    Args:
        taskcategory_id (int): ID of the TaskCategory to update.
        category_name=None: Keyword arguments for TaskCategory fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskCategory.objects.get(pk=taskcategory_id)
        instance.category_name = category_name if category_name is not None else instance.category_name
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  TaskCategory.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskcategory(taskcategory_id=None):
    """
    Retrieves and serializes a TaskCategory instance by its ID or all instances if ID is None.
    
    Args:
        TaskCategory_id (int, optional): ID of the TaskCategory to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskcategory_id is not None:
            record = TaskCategory.objects.get(pk=taskcategory_id)
            serializer = TaskCategorySerializer(record)
        else:
            records = TaskCategory.objects.all()
            serializer = TaskCategorySerializer(records, many=True)
        return success(serializer.data)
    
    except TaskCategory.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskCategory does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskcategory(taskcategory_id):
    """
    Deletes a TaskCategory instance with the given ID.
    
    Args:
        taskcategory_id (int): ID of the TaskCategory to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskCategory.objects.get(pk=taskcategory_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskCategory.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskdurationestimation(estimated_duration):
    """
    Creates a TaskDurationEstimation instance with the provided data.
        Args:
        estimated_duration: Keyword arguments for TaskDurationEstimation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskDurationEstimation.objects.create(
            estimated_duration=estimated_duration,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskdurationestimation(taskdurationestimation_id,estimated_duration=None):
    """
    Updates a TaskDurationEstimation instance with the provided data.
    
    Args:
        taskdurationestimation_id (int): ID of the TaskDurationEstimation to update.
        estimated_duration=None: Keyword arguments for TaskDurationEstimation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskDurationEstimation.objects.get(pk=taskdurationestimation_id)
        instance.estimated_duration = estimated_duration if estimated_duration is not None else instance.estimated_duration
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  TaskDurationEstimation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskdurationestimation(taskdurationestimation_id=None):
    """
    Retrieves and serializes a TaskDurationEstimation instance by its ID or all instances if ID is None.
    
    Args:
        TaskDurationEstimation_id (int, optional): ID of the TaskDurationEstimation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskdurationestimation_id is not None:
            record = TaskDurationEstimation.objects.get(pk=taskdurationestimation_id)
            serializer = TaskDurationEstimationSerializer(record)
        else:
            records = TaskDurationEstimation.objects.all()
            serializer = TaskDurationEstimationSerializer(records, many=True)
        return success(serializer.data)
    
    except TaskDurationEstimation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskDurationEstimation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskdurationestimation(taskdurationestimation_id):
    """
    Deletes a TaskDurationEstimation instance with the given ID.
    
    Args:
        taskdurationestimation_id (int): ID of the TaskDurationEstimation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskDurationEstimation.objects.get(pk=taskdurationestimation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskDurationEstimation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskpriority(priority_level):
    """
    Creates a TaskPriority instance with the provided data.
        Args:
        priority_level: Keyword arguments for TaskPriority fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskPriority.objects.create(
            priority_level=priority_level,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskpriority(taskpriority_id,priority_level=None):
    """
    Updates a TaskPriority instance with the provided data.
    
    Args:
        taskpriority_id (int): ID of the TaskPriority to update.
        priority_level=None: Keyword arguments for TaskPriority fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskPriority.objects.get(pk=taskpriority_id)
        instance.priority_level = priority_level if priority_level is not None else instance.priority_level
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  TaskPriority.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskpriority(taskpriority_id=None):
    """
    Retrieves and serializes a TaskPriority instance by its ID or all instances if ID is None.
    
    Args:
        TaskPriority_id (int, optional): ID of the TaskPriority to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskpriority_id is not None:
            record = TaskPriority.objects.get(pk=taskpriority_id)
            serializer = TaskPrioritySerializer(record)
        else:
            records = TaskPriority.objects.all()
            serializer = TaskPrioritySerializer(records, many=True)
        return success(serializer.data)
    
    except TaskPriority.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskPriority does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskpriority(taskpriority_id):
    """
    Deletes a TaskPriority instance with the given ID.
    
    Args:
        taskpriority_id (int): ID of the TaskPriority to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskPriority.objects.get(pk=taskpriority_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskPriority.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_team(name, description):
    """
    Creates a Team instance with the provided data.
        Args:
        name, description: Keyword arguments for Team fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Team.objects.create(
            name=name,
            description=description,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_team(team_id,name=None, description=None):
    """
    Updates a Team instance with the provided data.
    
    Args:
        team_id (int): ID of the Team to update.
        name=None, description=None: Keyword arguments for Team fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Team.objects.get(pk=team_id)
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Team.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_team(team_id=None):
    """
    Retrieves and serializes a Team instance by its ID or all instances if ID is None.
    
    Args:
        Team_id (int, optional): ID of the Team to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if team_id is not None:
            record = Team.objects.get(pk=team_id)
            serializer = TeamSerializer(record)
        else:
            records = Team.objects.all()
            serializer = TeamSerializer(records, many=True)
        return success(serializer.data)
    
    except Team.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Team does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_team(team_id):
    """
    Deletes a Team instance with the given ID.
    
    Args:
        team_id (int): ID of the Team to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Team.objects.get(pk=team_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Team.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_vendor(name, contact_person, email, phone_number, address, financial_standing, experience_years):
    """
    Creates a Vendor instance with the provided data.
        Args:
        name, contact_person, email, phone_number, address, financial_standing, experience_years: Keyword arguments for Vendor fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Vendor.objects.create(
            name=name,
            contact_person=contact_person,
            email=email,
            phone_number=phone_number,
            address=address,
            financial_standing=financial_standing,
            experience_years=experience_years,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_vendor(vendor_id,name=None, contact_person=None, email=None, phone_number=None, address=None, financial_standing=None, experience_years=None):
    """
    Updates a Vendor instance with the provided data.
    
    Args:
        vendor_id (int): ID of the Vendor to update.
        name=None, contact_person=None, email=None, phone_number=None, address=None, financial_standing=None, experience_years=None: Keyword arguments for Vendor fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Vendor.objects.get(pk=vendor_id)
        instance.name = name if name is not None else instance.name
        instance.contact_person = contact_person if contact_person is not None else instance.contact_person
        instance.email = email if email is not None else instance.email
        instance.phone_number = phone_number if phone_number is not None else instance.phone_number
        instance.address = address if address is not None else instance.address
        instance.financial_standing = financial_standing if financial_standing is not None else instance.financial_standing
        instance.experience_years = experience_years if experience_years is not None else instance.experience_years
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  Vendor.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_vendor(vendor_id=None):
    """
    Retrieves and serializes a Vendor instance by its ID or all instances if ID is None.
    
    Args:
        Vendor_id (int, optional): ID of the Vendor to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_id is not None:
            record = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(record)
        else:
            records = Vendor.objects.all()
            serializer = VendorSerializer(records, many=True)
        return success(serializer.data)
    
    except Vendor.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Vendor does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_vendor(vendor_id):
    """
    Deletes a Vendor instance with the given ID.
    
    Args:
        vendor_id (int): ID of the Vendor to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Vendor.objects.get(pk=vendor_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Vendor.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_asset(name, category_id, purchase_date, purchase_cost, depreciation_rate, location_id, assigned_to, status):
    """
    Creates a Asset instance with the provided data.
        Args:
        name, category_id, purchase_date, purchase_cost, depreciation_rate, location_id, assigned_to, status: Keyword arguments for Asset fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             AssetCategory.objects.get(pk=category_id)
        if location_id is not None and location_id != '': 
             Warehouse.objects.get(pk=location_id)
        instance = Asset.objects.create(
            name=name,
            category_id=category_id,
            purchase_date=purchase_date,
            purchase_cost=purchase_cost,
            depreciation_rate=depreciation_rate,
            location_id=location_id,
            assigned_to=assigned_to,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except AssetCategory.DoesNotExist:
        return error('Invalid AssetCategory ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_asset(asset_id,name=None, category_id=None, purchase_date=None, purchase_cost=None, depreciation_rate=None, location_id=None, assigned_to=None, status=None):
    """
    Updates a Asset instance with the provided data.
    
    Args:
        asset_id (int): ID of the Asset to update.
        name=None, category_id=None, purchase_date=None, purchase_cost=None, depreciation_rate=None, location_id=None, assigned_to=None, status=None: Keyword arguments for Asset fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             AssetCategory.objects.get(pk=category_id)
        if location_id is not None and location_id != '': 
             Warehouse.objects.get(pk=location_id)
        instance = Asset.objects.get(pk=asset_id)
        instance.name = name if name is not None else instance.name
        instance.category_id = category_id if category_id is not None else instance.category_id
        instance.purchase_date = purchase_date if purchase_date is not None else instance.purchase_date
        instance.purchase_cost = purchase_cost if purchase_cost is not None else instance.purchase_cost
        instance.depreciation_rate = depreciation_rate if depreciation_rate is not None else instance.depreciation_rate
        instance.location_id = location_id if location_id is not None else instance.location_id
        instance.assigned_to = assigned_to if assigned_to is not None else instance.assigned_to
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except AssetCategory.DoesNotExist:
        return error('Invalid AssetCategory ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except  Asset.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_asset(asset_id=None):
    """
    Retrieves and serializes a Asset instance by its ID or all instances if ID is None.
    
    Args:
        Asset_id (int, optional): ID of the Asset to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None:
            record = Asset.objects.get(pk=asset_id)
            serializer = AssetSerializer(record)
        else:
            records = Asset.objects.all()
            serializer = AssetSerializer(records, many=True)
        return success(serializer.data)
    
    except Asset.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Asset does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_asset(asset_id):
    """
    Deletes a Asset instance with the given ID.
    
    Args:
        asset_id (int): ID of the Asset to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Asset.objects.get(pk=asset_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Asset.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_expertise(subcontractor_id, area_of_expertise, certifications, performance_rating):
    """
    Creates a Expertise instance with the provided data.
        Args:
        subcontractor_id, area_of_expertise, certifications, performance_rating: Keyword arguments for Expertise fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = Expertise.objects.create(
            subcontractor_id=subcontractor_id,
            area_of_expertise=area_of_expertise,
            certifications=certifications,
            performance_rating=performance_rating,
        )
        return success(f'Successfully created {instance}')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_expertise(expertise_id,subcontractor_id=None, area_of_expertise=None, certifications=None, performance_rating=None):
    """
    Updates a Expertise instance with the provided data.
    
    Args:
        expertise_id (int): ID of the Expertise to update.
        subcontractor_id=None, area_of_expertise=None, certifications=None, performance_rating=None: Keyword arguments for Expertise fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = Expertise.objects.get(pk=expertise_id)
        instance.subcontractor_id = subcontractor_id if subcontractor_id is not None else instance.subcontractor_id
        instance.area_of_expertise = area_of_expertise if area_of_expertise is not None else instance.area_of_expertise
        instance.certifications = certifications if certifications is not None else instance.certifications
        instance.performance_rating = performance_rating if performance_rating is not None else instance.performance_rating
        instance.save()
        return success('Successfully Updated')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except  Expertise.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_expertise(expertise_id=None):
    """
    Retrieves and serializes a Expertise instance by its ID or all instances if ID is None.
    
    Args:
        Expertise_id (int, optional): ID of the Expertise to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if expertise_id is not None:
            record = Expertise.objects.get(pk=expertise_id)
            serializer = ExpertiseSerializer(record)
        else:
            records = Expertise.objects.all()
            serializer = ExpertiseSerializer(records, many=True)
        return success(serializer.data)
    
    except Expertise.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Expertise does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_expertise(expertise_id):
    """
    Deletes a Expertise instance with the given ID.
    
    Args:
        expertise_id (int): ID of the Expertise to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Expertise.objects.get(pk=expertise_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Expertise.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_bidnobiddecision(opportunity_id, decision_date, is_bid, rationale, profitability_assessment, resource_capacity_assessment):
    """
    Creates a BidNoBidDecision instance with the provided data.
        Args:
        opportunity_id, decision_date, is_bid, rationale, profitability_assessment, resource_capacity_assessment: Keyword arguments for BidNoBidDecision fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             OpportunityIdentification.objects.get(pk=opportunity_id)
        instance = BidNoBidDecision.objects.create(
            opportunity_id=opportunity_id,
            decision_date=decision_date,
            is_bid=is_bid,
            rationale=rationale,
            profitability_assessment=profitability_assessment,
            resource_capacity_assessment=resource_capacity_assessment,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except OpportunityIdentification.DoesNotExist:
        return error('Invalid OpportunityIdentification ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_bidnobiddecision(bidnobiddecision_id,opportunity_id=None, decision_date=None, is_bid=None, rationale=None, profitability_assessment=None, resource_capacity_assessment=None):
    """
    Updates a BidNoBidDecision instance with the provided data.
    
    Args:
        bidnobiddecision_id (int): ID of the BidNoBidDecision to update.
        opportunity_id=None, decision_date=None, is_bid=None, rationale=None, profitability_assessment=None, resource_capacity_assessment=None: Keyword arguments for BidNoBidDecision fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             OpportunityIdentification.objects.get(pk=opportunity_id)
        instance = BidNoBidDecision.objects.get(pk=bidnobiddecision_id)
        instance.opportunity_id = opportunity_id if opportunity_id is not None else instance.opportunity_id
        instance.decision_date = decision_date if decision_date is not None else instance.decision_date
        instance.is_bid = is_bid if is_bid is not None else instance.is_bid
        instance.rationale = rationale if rationale is not None else instance.rationale
        instance.profitability_assessment = profitability_assessment if profitability_assessment is not None else instance.profitability_assessment
        instance.resource_capacity_assessment = resource_capacity_assessment if resource_capacity_assessment is not None else instance.resource_capacity_assessment
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except OpportunityIdentification.DoesNotExist:
        return error('Invalid OpportunityIdentification ID: Destination not found.')
    except  BidNoBidDecision.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_bidnobiddecision(bidnobiddecision_id=None):
    """
    Retrieves and serializes a BidNoBidDecision instance by its ID or all instances if ID is None.
    
    Args:
        BidNoBidDecision_id (int, optional): ID of the BidNoBidDecision to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bidnobiddecision_id is not None:
            record = BidNoBidDecision.objects.get(pk=bidnobiddecision_id)
            serializer = BidNoBidDecisionSerializer(record)
        else:
            records = BidNoBidDecision.objects.all()
            serializer = BidNoBidDecisionSerializer(records, many=True)
        return success(serializer.data)
    
    except BidNoBidDecision.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('BidNoBidDecision does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_bidnobiddecision(bidnobiddecision_id):
    """
    Deletes a BidNoBidDecision instance with the given ID.
    
    Args:
        bidnobiddecision_id (int): ID of the BidNoBidDecision to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidNoBidDecision.objects.get(pk=bidnobiddecision_id)
        instance.delete()
        return success("Successfully deleted")
    
    except BidNoBidDecision.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_proposalpreparation(opportunity_id, proposal_title, technical_solutions, pricing, timelines, value_propositions, compliance_check):
    """
    Creates a ProposalPreparation instance with the provided data.
        Args:
        opportunity_id, proposal_title, technical_solutions, pricing, timelines, value_propositions, compliance_check: Keyword arguments for ProposalPreparation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             OpportunityIdentification.objects.get(pk=opportunity_id)
        instance = ProposalPreparation.objects.create(
            opportunity_id=opportunity_id,
            proposal_title=proposal_title,
            technical_solutions=technical_solutions,
            pricing=pricing,
            timelines=timelines,
            value_propositions=value_propositions,
            compliance_check=compliance_check,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except OpportunityIdentification.DoesNotExist:
        return error('Invalid OpportunityIdentification ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_proposalpreparation(proposalpreparation_id,opportunity_id=None, proposal_title=None, technical_solutions=None, pricing=None, timelines=None, value_propositions=None, compliance_check=None):
    """
    Updates a ProposalPreparation instance with the provided data.
    
    Args:
        proposalpreparation_id (int): ID of the ProposalPreparation to update.
        opportunity_id=None, proposal_title=None, technical_solutions=None, pricing=None, timelines=None, value_propositions=None, compliance_check=None: Keyword arguments for ProposalPreparation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             OpportunityIdentification.objects.get(pk=opportunity_id)
        instance = ProposalPreparation.objects.get(pk=proposalpreparation_id)
        instance.opportunity_id = opportunity_id if opportunity_id is not None else instance.opportunity_id
        instance.proposal_title = proposal_title if proposal_title is not None else instance.proposal_title
        instance.technical_solutions = technical_solutions if technical_solutions is not None else instance.technical_solutions
        instance.pricing = pricing if pricing is not None else instance.pricing
        instance.timelines = timelines if timelines is not None else instance.timelines
        instance.value_propositions = value_propositions if value_propositions is not None else instance.value_propositions
        instance.compliance_check = compliance_check if compliance_check is not None else instance.compliance_check
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except OpportunityIdentification.DoesNotExist:
        return error('Invalid OpportunityIdentification ID: Destination not found.')
    except  ProposalPreparation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_proposalpreparation(proposalpreparation_id=None):
    """
    Retrieves and serializes a ProposalPreparation instance by its ID or all instances if ID is None.
    
    Args:
        ProposalPreparation_id (int, optional): ID of the ProposalPreparation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposalpreparation_id is not None:
            record = ProposalPreparation.objects.get(pk=proposalpreparation_id)
            serializer = ProposalPreparationSerializer(record)
        else:
            records = ProposalPreparation.objects.all()
            serializer = ProposalPreparationSerializer(records, many=True)
        return success(serializer.data)
    
    except ProposalPreparation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProposalPreparation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_proposalpreparation(proposalpreparation_id):
    """
    Deletes a ProposalPreparation instance with the given ID.
    
    Args:
        proposalpreparation_id (int): ID of the ProposalPreparation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProposalPreparation.objects.get(pk=proposalpreparation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProposalPreparation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_bidsubmission(bid_proposal_id, submission_date, submission_method, documents_included):
    """
    Creates a BidSubmission instance with the provided data.
        Args:
        bid_proposal_id, submission_date, submission_method, documents_included: Keyword arguments for BidSubmission fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_proposal_id is not None and bid_proposal_id != '': 
             BidProposal.objects.get(pk=bid_proposal_id)
        instance = BidSubmission.objects.create(
            bid_proposal_id=bid_proposal_id,
            submission_date=submission_date,
            submission_method=submission_method,
            documents_included=documents_included,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except BidProposal.DoesNotExist:
        return error('Invalid BidProposal ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_bidsubmission(bidsubmission_id,bid_proposal_id=None, submission_date=None, submission_method=None, documents_included=None):
    """
    Updates a BidSubmission instance with the provided data.
    
    Args:
        bidsubmission_id (int): ID of the BidSubmission to update.
        bid_proposal_id=None, submission_date=None, submission_method=None, documents_included=None: Keyword arguments for BidSubmission fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_proposal_id is not None and bid_proposal_id != '': 
             BidProposal.objects.get(pk=bid_proposal_id)
        instance = BidSubmission.objects.get(pk=bidsubmission_id)
        instance.bid_proposal_id = bid_proposal_id if bid_proposal_id is not None else instance.bid_proposal_id
        instance.submission_date = submission_date if submission_date is not None else instance.submission_date
        instance.submission_method = submission_method if submission_method is not None else instance.submission_method
        instance.documents_included = documents_included if documents_included is not None else instance.documents_included
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except BidProposal.DoesNotExist:
        return error('Invalid BidProposal ID: Destination not found.')
    except  BidSubmission.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_bidsubmission(bidsubmission_id=None):
    """
    Retrieves and serializes a BidSubmission instance by its ID or all instances if ID is None.
    
    Args:
        BidSubmission_id (int, optional): ID of the BidSubmission to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bidsubmission_id is not None:
            record = BidSubmission.objects.get(pk=bidsubmission_id)
            serializer = BidSubmissionSerializer(record)
        else:
            records = BidSubmission.objects.all()
            serializer = BidSubmissionSerializer(records, many=True)
        return success(serializer.data)
    
    except BidSubmission.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('BidSubmission does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_bidsubmission(bidsubmission_id):
    """
    Deletes a BidSubmission instance with the given ID.
    
    Args:
        bidsubmission_id (int): ID of the BidSubmission to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidSubmission.objects.get(pk=bidsubmission_id)
        instance.delete()
        return success("Successfully deleted")
    
    except BidSubmission.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_equipment(name, category_id, serial_number, purchase_date, condition, location_id, status):
    """
    Creates a Equipment instance with the provided data.
        Args:
        name, category_id, serial_number, purchase_date, condition, location_id, status: Keyword arguments for Equipment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             EquipmentCategory.objects.get(pk=category_id)
        if location_id is not None and location_id != '': 
             Warehouse.objects.get(pk=location_id)
        instance = Equipment.objects.create(
            name=name,
            category_id=category_id,
            serial_number=serial_number,
            purchase_date=purchase_date,
            condition=condition,
            location_id=location_id,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except EquipmentCategory.DoesNotExist:
        return error('Invalid EquipmentCategory ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_equipment(equipment_id,name=None, category_id=None, serial_number=None, purchase_date=None, condition=None, location_id=None, status=None):
    """
    Updates a Equipment instance with the provided data.
    
    Args:
        equipment_id (int): ID of the Equipment to update.
        name=None, category_id=None, serial_number=None, purchase_date=None, condition=None, location_id=None, status=None: Keyword arguments for Equipment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             EquipmentCategory.objects.get(pk=category_id)
        if location_id is not None and location_id != '': 
             Warehouse.objects.get(pk=location_id)
        instance = Equipment.objects.get(pk=equipment_id)
        instance.name = name if name is not None else instance.name
        instance.category_id = category_id if category_id is not None else instance.category_id
        instance.serial_number = serial_number if serial_number is not None else instance.serial_number
        instance.purchase_date = purchase_date if purchase_date is not None else instance.purchase_date
        instance.condition = condition if condition is not None else instance.condition
        instance.location_id = location_id if location_id is not None else instance.location_id
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except EquipmentCategory.DoesNotExist:
        return error('Invalid EquipmentCategory ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except  Equipment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_equipment(equipment_id=None):
    """
    Retrieves and serializes a Equipment instance by its ID or all instances if ID is None.
    
    Args:
        Equipment_id (int, optional): ID of the Equipment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None:
            record = Equipment.objects.get(pk=equipment_id)
            serializer = EquipmentSerializer(record)
        else:
            records = Equipment.objects.all()
            serializer = EquipmentSerializer(records, many=True)
        return success(serializer.data)
    
    except Equipment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Equipment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_equipment(equipment_id):
    """
    Deletes a Equipment instance with the given ID.
    
    Args:
        equipment_id (int): ID of the Equipment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Equipment.objects.get(pk=equipment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Equipment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_notification(message, is_read):
    """
    Creates a Notification instance with the provided data.
        Args:
        message, is_read: Keyword arguments for Notification fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Notification.objects.create(
            message=message,
            is_read=is_read,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_notification(notification_id,message=None, is_read=None):
    """
    Updates a Notification instance with the provided data.
    
    Args:
        notification_id (int): ID of the Notification to update.
        message=None, is_read=None: Keyword arguments for Notification fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Notification.objects.get(pk=notification_id)
        instance.message = message if message is not None else instance.message
        instance.is_read = is_read if is_read is not None else instance.is_read
        instance.save()
        return success('Successfully Updated')
    except  Notification.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_notification(notification_id=None):
    """
    Retrieves and serializes a Notification instance by its ID or all instances if ID is None.
    
    Args:
        Notification_id (int, optional): ID of the Notification to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if notification_id is not None:
            record = Notification.objects.get(pk=notification_id)
            serializer = NotificationSerializer(record)
        else:
            records = Notification.objects.all()
            serializer = NotificationSerializer(records, many=True)
        return success(serializer.data)
    
    except Notification.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Notification does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_notification(notification_id):
    """
    Deletes a Notification instance with the given ID.
    
    Args:
        notification_id (int): ID of the Notification to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Notification.objects.get(pk=notification_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Notification.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_item(name, category_id, supplier_id, stock_quantity, reorder_point, safety_stock, price_per_unit, warehouse_id, barcode):
    """
    Creates a Item instance with the provided data.
        Args:
        name, category_id, supplier_id, stock_quantity, reorder_point, safety_stock, price_per_unit, warehouse_id, barcode: Keyword arguments for Item fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             ItemCategory.objects.get(pk=category_id)
        if supplier_id is not None and supplier_id != '': 
             Supplier.objects.get(pk=supplier_id)
        if warehouse_id is not None and warehouse_id != '': 
             Warehouse.objects.get(pk=warehouse_id)
        instance = Item.objects.create(
            name=name,
            category_id=category_id,
            supplier_id=supplier_id,
            stock_quantity=stock_quantity,
            reorder_point=reorder_point,
            safety_stock=safety_stock,
            price_per_unit=price_per_unit,
            warehouse_id=warehouse_id,
            barcode=barcode,
        )
        return success(f'Successfully created {instance}')
    except ItemCategory.DoesNotExist:
        return error('Invalid ItemCategory ID: Destination not found.')
    except Supplier.DoesNotExist:
        return error('Invalid Supplier ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_item(item_id,name=None, category_id=None, supplier_id=None, stock_quantity=None, reorder_point=None, safety_stock=None, price_per_unit=None, warehouse_id=None, barcode=None):
    """
    Updates a Item instance with the provided data.
    
    Args:
        item_id (int): ID of the Item to update.
        name=None, category_id=None, supplier_id=None, stock_quantity=None, reorder_point=None, safety_stock=None, price_per_unit=None, warehouse_id=None, barcode=None: Keyword arguments for Item fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if category_id is not None and category_id != '': 
             ItemCategory.objects.get(pk=category_id)
        if supplier_id is not None and supplier_id != '': 
             Supplier.objects.get(pk=supplier_id)
        if warehouse_id is not None and warehouse_id != '': 
             Warehouse.objects.get(pk=warehouse_id)
        instance = Item.objects.get(pk=item_id)
        instance.name = name if name is not None else instance.name
        instance.category_id = category_id if category_id is not None else instance.category_id
        instance.supplier_id = supplier_id if supplier_id is not None else instance.supplier_id
        instance.stock_quantity = stock_quantity if stock_quantity is not None else instance.stock_quantity
        instance.reorder_point = reorder_point if reorder_point is not None else instance.reorder_point
        instance.safety_stock = safety_stock if safety_stock is not None else instance.safety_stock
        instance.price_per_unit = price_per_unit if price_per_unit is not None else instance.price_per_unit
        instance.warehouse_id = warehouse_id if warehouse_id is not None else instance.warehouse_id
        instance.barcode = barcode if barcode is not None else instance.barcode
        instance.save()
        return success('Successfully Updated')
    except ItemCategory.DoesNotExist:
        return error('Invalid ItemCategory ID: Destination not found.')
    except Supplier.DoesNotExist:
        return error('Invalid Supplier ID: Destination not found.')
    except Warehouse.DoesNotExist:
        return error('Invalid Warehouse ID: Destination not found.')
    except  Item.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_item(item_id=None):
    """
    Retrieves and serializes a Item instance by its ID or all instances if ID is None.
    
    Args:
        Item_id (int, optional): ID of the Item to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None:
            record = Item.objects.get(pk=item_id)
            serializer = ItemSerializer(record)
        else:
            records = Item.objects.all()
            serializer = ItemSerializer(records, many=True)
        return success(serializer.data)
    
    except Item.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Item does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_item(item_id):
    """
    Deletes a Item instance with the given ID.
    
    Args:
        item_id (int): ID of the Item to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Item.objects.get(pk=item_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Item.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_lead(name, company, email, phone, project_description, source_id, status, budget, urgency, decision_maker, assigned_to_id):
    """
    Creates a Lead instance with the provided data.
        Args:
        name, company, email, phone, project_description, source_id, status, budget, urgency, decision_maker, assigned_to_id: Keyword arguments for Lead fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if source_id is not None and source_id != '': 
             LeadSource.objects.get(pk=source_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             SalesRepresentative.objects.get(pk=assigned_to_id)
        instance = Lead.objects.create(
            name=name,
            company=company,
            email=email,
            phone=phone,
            project_description=project_description,
            source_id=source_id,
            status=status,
            budget=budget,
            urgency=urgency,
            decision_maker=decision_maker,
            assigned_to_id=assigned_to_id,
        )
        return success(f'Successfully created {instance}')
    except LeadSource.DoesNotExist:
        return error('Invalid LeadSource ID: Destination not found.')
    except SalesRepresentative.DoesNotExist:
        return error('Invalid SalesRepresentative ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_lead(lead_id,name=None, company=None, email=None, phone=None, project_description=None, source_id=None, status=None, budget=None, urgency=None, decision_maker=None, assigned_to_id=None):
    """
    Updates a Lead instance with the provided data.
    
    Args:
        lead_id (int): ID of the Lead to update.
        name=None, company=None, email=None, phone=None, project_description=None, source_id=None, status=None, budget=None, urgency=None, decision_maker=None, assigned_to_id=None: Keyword arguments for Lead fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if source_id is not None and source_id != '': 
             LeadSource.objects.get(pk=source_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             SalesRepresentative.objects.get(pk=assigned_to_id)
        instance = Lead.objects.get(pk=lead_id)
        instance.name = name if name is not None else instance.name
        instance.company = company if company is not None else instance.company
        instance.email = email if email is not None else instance.email
        instance.phone = phone if phone is not None else instance.phone
        instance.project_description = project_description if project_description is not None else instance.project_description
        instance.source_id = source_id if source_id is not None else instance.source_id
        instance.status = status if status is not None else instance.status
        instance.budget = budget if budget is not None else instance.budget
        instance.urgency = urgency if urgency is not None else instance.urgency
        instance.decision_maker = decision_maker if decision_maker is not None else instance.decision_maker
        instance.assigned_to_id = assigned_to_id if assigned_to_id is not None else instance.assigned_to_id
        instance.save()
        return success('Successfully Updated')
    except LeadSource.DoesNotExist:
        return error('Invalid LeadSource ID: Destination not found.')
    except SalesRepresentative.DoesNotExist:
        return error('Invalid SalesRepresentative ID: Destination not found.')
    except  Lead.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_lead(lead_id=None):
    """
    Retrieves and serializes a Lead instance by its ID or all instances if ID is None.
    
    Args:
        Lead_id (int, optional): ID of the Lead to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if lead_id is not None:
            record = Lead.objects.get(pk=lead_id)
            serializer = LeadSerializer(record)
        else:
            records = Lead.objects.all()
            serializer = LeadSerializer(records, many=True)
        return success(serializer.data)
    
    except Lead.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Lead does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_lead(lead_id):
    """
    Deletes a Lead instance with the given ID.
    
    Args:
        lead_id (int): ID of the Lead to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Lead.objects.get(pk=lead_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Lead.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_procurementneed(department_id, description, quantity, date_needed):
    """
    Creates a ProcurementNeed instance with the provided data.
        Args:
        department_id, description, quantity, date_needed: Keyword arguments for ProcurementNeed fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if department_id is not None and department_id != '': 
             InternalDepartment.objects.get(pk=department_id)
        instance = ProcurementNeed.objects.create(
            department_id=department_id,
            description=description,
            quantity=quantity,
            date_needed=date_needed,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except InternalDepartment.DoesNotExist:
        return error('Invalid InternalDepartment ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_procurementneed(procurementneed_id,department_id=None, description=None, quantity=None, date_needed=None):
    """
    Updates a ProcurementNeed instance with the provided data.
    
    Args:
        procurementneed_id (int): ID of the ProcurementNeed to update.
        department_id=None, description=None, quantity=None, date_needed=None: Keyword arguments for ProcurementNeed fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if department_id is not None and department_id != '': 
             InternalDepartment.objects.get(pk=department_id)
        instance = ProcurementNeed.objects.get(pk=procurementneed_id)
        instance.department_id = department_id if department_id is not None else instance.department_id
        instance.description = description if description is not None else instance.description
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.date_needed = date_needed if date_needed is not None else instance.date_needed
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except InternalDepartment.DoesNotExist:
        return error('Invalid InternalDepartment ID: Destination not found.')
    except  ProcurementNeed.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_procurementneed(procurementneed_id=None):
    """
    Retrieves and serializes a ProcurementNeed instance by its ID or all instances if ID is None.
    
    Args:
        ProcurementNeed_id (int, optional): ID of the ProcurementNeed to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if procurementneed_id is not None:
            record = ProcurementNeed.objects.get(pk=procurementneed_id)
            serializer = ProcurementNeedSerializer(record)
        else:
            records = ProcurementNeed.objects.all()
            serializer = ProcurementNeedSerializer(records, many=True)
        return success(serializer.data)
    
    except ProcurementNeed.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProcurementNeed does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_procurementneed(procurementneed_id):
    """
    Deletes a ProcurementNeed instance with the given ID.
    
    Args:
        procurementneed_id (int): ID of the ProcurementNeed to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProcurementNeed.objects.get(pk=procurementneed_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProcurementNeed.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_audit(project_id, audit_type, conducted_by_id, date, findings):
    """
    Creates a Audit instance with the provided data.
        Args:
        project_id, audit_type, conducted_by_id, date, findings: Keyword arguments for Audit fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if conducted_by_id is not None and conducted_by_id != '': 
             User.objects.get(pk=conducted_by_id)
        instance = Audit.objects.create(
            project_id=project_id,
            audit_type=audit_type,
            conducted_by_id=conducted_by_id,
            date=date,
            findings=findings,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_audit(audit_id,project_id=None, audit_type=None, conducted_by_id=None, date=None, findings=None):
    """
    Updates a Audit instance with the provided data.
    
    Args:
        audit_id (int): ID of the Audit to update.
        project_id=None, audit_type=None, conducted_by_id=None, date=None, findings=None: Keyword arguments for Audit fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if conducted_by_id is not None and conducted_by_id != '': 
             User.objects.get(pk=conducted_by_id)
        instance = Audit.objects.get(pk=audit_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.audit_type = audit_type if audit_type is not None else instance.audit_type
        instance.conducted_by_id = conducted_by_id if conducted_by_id is not None else instance.conducted_by_id
        instance.date = date if date is not None else instance.date
        instance.findings = findings if findings is not None else instance.findings
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  Audit.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_audit(audit_id=None):
    """
    Retrieves and serializes a Audit instance by its ID or all instances if ID is None.
    
    Args:
        Audit_id (int, optional): ID of the Audit to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if audit_id is not None:
            record = Audit.objects.get(pk=audit_id)
            serializer = AuditSerializer(record)
        else:
            records = Audit.objects.all()
            serializer = AuditSerializer(records, many=True)
        return success(serializer.data)
    
    except Audit.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Audit does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_audit(audit_id):
    """
    Deletes a Audit instance with the given ID.
    
    Args:
        audit_id (int): ID of the Audit to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Audit.objects.get(pk=audit_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Audit.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_bid(project_id, subcontractor_id, bid_amount, bid_submission_date, status, notes):
    """
    Creates a Bid instance with the provided data.
        Args:
        project_id, subcontractor_id, bid_amount, bid_submission_date, status, notes: Keyword arguments for Bid fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = Bid.objects.create(
            project_id=project_id,
            subcontractor_id=subcontractor_id,
            bid_amount=bid_amount,
            bid_submission_date=bid_submission_date,
            status=status,
            notes=notes,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_bid(bid_id,project_id=None, subcontractor_id=None, bid_amount=None, bid_submission_date=None, status=None, notes=None):
    """
    Updates a Bid instance with the provided data.
    
    Args:
        bid_id (int): ID of the Bid to update.
        project_id=None, subcontractor_id=None, bid_amount=None, bid_submission_date=None, status=None, notes=None: Keyword arguments for Bid fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = Bid.objects.get(pk=bid_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.subcontractor_id = subcontractor_id if subcontractor_id is not None else instance.subcontractor_id
        instance.bid_amount = bid_amount if bid_amount is not None else instance.bid_amount
        instance.bid_submission_date = bid_submission_date if bid_submission_date is not None else instance.bid_submission_date
        instance.status = status if status is not None else instance.status
        instance.notes = notes if notes is not None else instance.notes
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except  Bid.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_bid(bid_id=None):
    """
    Retrieves and serializes a Bid instance by its ID or all instances if ID is None.
    
    Args:
        Bid_id (int, optional): ID of the Bid to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_id is not None:
            record = Bid.objects.get(pk=bid_id)
            serializer = BidSerializer(record)
        else:
            records = Bid.objects.all()
            serializer = BidSerializer(records, many=True)
        return success(serializer.data)
    
    except Bid.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Bid does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_bid(bid_id):
    """
    Deletes a Bid instance with the given ID.
    
    Args:
        bid_id (int): ID of the Bid to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Bid.objects.get(pk=bid_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Bid.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_budget(project_id, total_budget, allocated_budget, remaining_budget, currency_id):
    """
    Creates a Budget instance with the provided data.
        Args:
        project_id, total_budget, allocated_budget, remaining_budget, currency_id: Keyword arguments for Budget fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if currency_id is not None and currency_id != '': 
             Currency.objects.get(pk=currency_id)
        instance = Budget.objects.create(
            project_id=project_id,
            total_budget=total_budget,
            allocated_budget=allocated_budget,
            remaining_budget=remaining_budget,
            currency_id=currency_id,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Currency.DoesNotExist:
        return error('Invalid Currency ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_budget(budget_id,project_id=None, total_budget=None, allocated_budget=None, remaining_budget=None, currency_id=None):
    """
    Updates a Budget instance with the provided data.
    
    Args:
        budget_id (int): ID of the Budget to update.
        project_id=None, total_budget=None, allocated_budget=None, remaining_budget=None, currency_id=None: Keyword arguments for Budget fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if currency_id is not None and currency_id != '': 
             Currency.objects.get(pk=currency_id)
        instance = Budget.objects.get(pk=budget_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.total_budget = total_budget if total_budget is not None else instance.total_budget
        instance.allocated_budget = allocated_budget if allocated_budget is not None else instance.allocated_budget
        instance.remaining_budget = remaining_budget if remaining_budget is not None else instance.remaining_budget
        instance.currency_id = currency_id if currency_id is not None else instance.currency_id
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Currency.DoesNotExist:
        return error('Invalid Currency ID: Destination not found.')
    except  Budget.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_budget(budget_id=None):
    """
    Retrieves and serializes a Budget instance by its ID or all instances if ID is None.
    
    Args:
        Budget_id (int, optional): ID of the Budget to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if budget_id is not None:
            record = Budget.objects.get(pk=budget_id)
            serializer = BudgetSerializer(record)
        else:
            records = Budget.objects.all()
            serializer = BudgetSerializer(records, many=True)
        return success(serializer.data)
    
    except Budget.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Budget does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_budget(budget_id):
    """
    Deletes a Budget instance with the given ID.
    
    Args:
        budget_id (int): ID of the Budget to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Budget.objects.get(pk=budget_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Budget.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_budgetallocation(project_id, materials_cost, labor_cost, equipment_cost, contingency_cost, total_budget):
    """
    Creates a BudgetAllocation instance with the provided data.
        Args:
        project_id, materials_cost, labor_cost, equipment_cost, contingency_cost, total_budget: Keyword arguments for BudgetAllocation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = BudgetAllocation.objects.create(
            project_id=project_id,
            materials_cost=materials_cost,
            labor_cost=labor_cost,
            equipment_cost=equipment_cost,
            contingency_cost=contingency_cost,
            total_budget=total_budget,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_budgetallocation(budgetallocation_id,project_id=None, materials_cost=None, labor_cost=None, equipment_cost=None, contingency_cost=None, total_budget=None):
    """
    Updates a BudgetAllocation instance with the provided data.
    
    Args:
        budgetallocation_id (int): ID of the BudgetAllocation to update.
        project_id=None, materials_cost=None, labor_cost=None, equipment_cost=None, contingency_cost=None, total_budget=None: Keyword arguments for BudgetAllocation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = BudgetAllocation.objects.get(pk=budgetallocation_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.materials_cost = materials_cost if materials_cost is not None else instance.materials_cost
        instance.labor_cost = labor_cost if labor_cost is not None else instance.labor_cost
        instance.equipment_cost = equipment_cost if equipment_cost is not None else instance.equipment_cost
        instance.contingency_cost = contingency_cost if contingency_cost is not None else instance.contingency_cost
        instance.total_budget = total_budget if total_budget is not None else instance.total_budget
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  BudgetAllocation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_budgetallocation(budgetallocation_id=None):
    """
    Retrieves and serializes a BudgetAllocation instance by its ID or all instances if ID is None.
    
    Args:
        BudgetAllocation_id (int, optional): ID of the BudgetAllocation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if budgetallocation_id is not None:
            record = BudgetAllocation.objects.get(pk=budgetallocation_id)
            serializer = BudgetAllocationSerializer(record)
        else:
            records = BudgetAllocation.objects.all()
            serializer = BudgetAllocationSerializer(records, many=True)
        return success(serializer.data)
    
    except BudgetAllocation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('BudgetAllocation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_budgetallocation(budgetallocation_id):
    """
    Deletes a BudgetAllocation instance with the given ID.
    
    Args:
        budgetallocation_id (int): ID of the BudgetAllocation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BudgetAllocation.objects.get(pk=budgetallocation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except BudgetAllocation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientfeedback(project_id, feedback_date, client_name, satisfaction_rating, comments):
    """
    Creates a ClientFeedback instance with the provided data.
        Args:
        project_id, feedback_date, client_name, satisfaction_rating, comments: Keyword arguments for ClientFeedback fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientFeedback.objects.create(
            project_id=project_id,
            feedback_date=feedback_date,
            client_name=client_name,
            satisfaction_rating=satisfaction_rating,
            comments=comments,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientfeedback(clientfeedback_id,project_id=None, feedback_date=None, client_name=None, satisfaction_rating=None, comments=None):
    """
    Updates a ClientFeedback instance with the provided data.
    
    Args:
        clientfeedback_id (int): ID of the ClientFeedback to update.
        project_id=None, feedback_date=None, client_name=None, satisfaction_rating=None, comments=None: Keyword arguments for ClientFeedback fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientFeedback.objects.get(pk=clientfeedback_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.feedback_date = feedback_date if feedback_date is not None else instance.feedback_date
        instance.client_name = client_name if client_name is not None else instance.client_name
        instance.satisfaction_rating = satisfaction_rating if satisfaction_rating is not None else instance.satisfaction_rating
        instance.comments = comments if comments is not None else instance.comments
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ClientFeedback.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientfeedback(clientfeedback_id=None):
    """
    Retrieves and serializes a ClientFeedback instance by its ID or all instances if ID is None.
    
    Args:
        ClientFeedback_id (int, optional): ID of the ClientFeedback to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientfeedback_id is not None:
            record = ClientFeedback.objects.get(pk=clientfeedback_id)
            serializer = ClientFeedbackSerializer(record)
        else:
            records = ClientFeedback.objects.all()
            serializer = ClientFeedbackSerializer(records, many=True)
        return success(serializer.data)
    
    except ClientFeedback.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientFeedback does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientfeedback(clientfeedback_id):
    """
    Deletes a ClientFeedback instance with the given ID.
    
    Args:
        clientfeedback_id (int): ID of the ClientFeedback to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientFeedback.objects.get(pk=clientfeedback_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientFeedback.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientfollowup(project_id, follow_up_date, message, action_taken):
    """
    Creates a ClientFollowUp instance with the provided data.
        Args:
        project_id, follow_up_date, message, action_taken: Keyword arguments for ClientFollowUp fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientFollowUp.objects.create(
            project_id=project_id,
            follow_up_date=follow_up_date,
            message=message,
            action_taken=action_taken,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientfollowup(clientfollowup_id,project_id=None, follow_up_date=None, message=None, action_taken=None):
    """
    Updates a ClientFollowUp instance with the provided data.
    
    Args:
        clientfollowup_id (int): ID of the ClientFollowUp to update.
        project_id=None, follow_up_date=None, message=None, action_taken=None: Keyword arguments for ClientFollowUp fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientFollowUp.objects.get(pk=clientfollowup_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.follow_up_date = follow_up_date if follow_up_date is not None else instance.follow_up_date
        instance.message = message if message is not None else instance.message
        instance.action_taken = action_taken if action_taken is not None else instance.action_taken
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ClientFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientfollowup(clientfollowup_id=None):
    """
    Retrieves and serializes a ClientFollowUp instance by its ID or all instances if ID is None.
    
    Args:
        ClientFollowUp_id (int, optional): ID of the ClientFollowUp to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientfollowup_id is not None:
            record = ClientFollowUp.objects.get(pk=clientfollowup_id)
            serializer = ClientFollowUpSerializer(record)
        else:
            records = ClientFollowUp.objects.all()
            serializer = ClientFollowUpSerializer(records, many=True)
        return success(serializer.data)
    
    except ClientFollowUp.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientFollowUp does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientfollowup(clientfollowup_id):
    """
    Deletes a ClientFollowUp instance with the given ID.
    
    Args:
        clientfollowup_id (int): ID of the ClientFollowUp to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientFollowUp.objects.get(pk=clientfollowup_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientsatisfactionsurvey(project_id, sent_date, client_feedback, score):
    """
    Creates a ClientSatisfactionSurvey instance with the provided data.
        Args:
        project_id, sent_date, client_feedback, score: Keyword arguments for ClientSatisfactionSurvey fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientSatisfactionSurvey.objects.create(
            project_id=project_id,
            sent_date=sent_date,
            client_feedback=client_feedback,
            score=score,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientsatisfactionsurvey(clientsatisfactionsurvey_id,project_id=None, sent_date=None, client_feedback=None, score=None):
    """
    Updates a ClientSatisfactionSurvey instance with the provided data.
    
    Args:
        clientsatisfactionsurvey_id (int): ID of the ClientSatisfactionSurvey to update.
        project_id=None, sent_date=None, client_feedback=None, score=None: Keyword arguments for ClientSatisfactionSurvey fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ClientSatisfactionSurvey.objects.get(pk=clientsatisfactionsurvey_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.sent_date = sent_date if sent_date is not None else instance.sent_date
        instance.client_feedback = client_feedback if client_feedback is not None else instance.client_feedback
        instance.score = score if score is not None else instance.score
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ClientSatisfactionSurvey.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientsatisfactionsurvey(clientsatisfactionsurvey_id=None):
    """
    Retrieves and serializes a ClientSatisfactionSurvey instance by its ID or all instances if ID is None.
    
    Args:
        ClientSatisfactionSurvey_id (int, optional): ID of the ClientSatisfactionSurvey to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientsatisfactionsurvey_id is not None:
            record = ClientSatisfactionSurvey.objects.get(pk=clientsatisfactionsurvey_id)
            serializer = ClientSatisfactionSurveySerializer(record)
        else:
            records = ClientSatisfactionSurvey.objects.all()
            serializer = ClientSatisfactionSurveySerializer(records, many=True)
        return success(serializer.data)
    
    except ClientSatisfactionSurvey.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientSatisfactionSurvey does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientsatisfactionsurvey(clientsatisfactionsurvey_id):
    """
    Deletes a ClientSatisfactionSurvey instance with the given ID.
    
    Args:
        clientsatisfactionsurvey_id (int): ID of the ClientSatisfactionSurvey to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientSatisfactionSurvey.objects.get(pk=clientsatisfactionsurvey_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientSatisfactionSurvey.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_closeoutdocument(project_id, document_type):
    """
    Creates a CloseoutDocument instance with the provided data.
        Args:
        project_id, document_type: Keyword arguments for CloseoutDocument fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = CloseoutDocument.objects.create(
            project_id=project_id,
            document_type=document_type,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_closeoutdocument(closeoutdocument_id,project_id=None, document_type=None):
    """
    Updates a CloseoutDocument instance with the provided data.
    
    Args:
        closeoutdocument_id (int): ID of the CloseoutDocument to update.
        project_id=None, document_type=None: Keyword arguments for CloseoutDocument fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = CloseoutDocument.objects.get(pk=closeoutdocument_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.document_type = document_type if document_type is not None else instance.document_type
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  CloseoutDocument.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_closeoutdocument(closeoutdocument_id=None):
    """
    Retrieves and serializes a CloseoutDocument instance by its ID or all instances if ID is None.
    
    Args:
        CloseoutDocument_id (int, optional): ID of the CloseoutDocument to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if closeoutdocument_id is not None:
            record = CloseoutDocument.objects.get(pk=closeoutdocument_id)
            serializer = CloseoutDocumentSerializer(record)
        else:
            records = CloseoutDocument.objects.all()
            serializer = CloseoutDocumentSerializer(records, many=True)
        return success(serializer.data)
    
    except CloseoutDocument.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CloseoutDocument does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_closeoutdocument(closeoutdocument_id):
    """
    Deletes a CloseoutDocument instance with the given ID.
    
    Args:
        closeoutdocument_id (int): ID of the CloseoutDocument to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CloseoutDocument.objects.get(pk=closeoutdocument_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CloseoutDocument.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_compliancemonitor(project_id, compliance_type, description, status, date):
    """
    Creates a ComplianceMonitor instance with the provided data.
        Args:
        project_id, compliance_type, description, status, date: Keyword arguments for ComplianceMonitor fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ComplianceMonitor.objects.create(
            project_id=project_id,
            compliance_type=compliance_type,
            description=description,
            status=status,
            date=date,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_compliancemonitor(compliancemonitor_id,project_id=None, compliance_type=None, description=None, status=None, date=None):
    """
    Updates a ComplianceMonitor instance with the provided data.
    
    Args:
        compliancemonitor_id (int): ID of the ComplianceMonitor to update.
        project_id=None, compliance_type=None, description=None, status=None, date=None: Keyword arguments for ComplianceMonitor fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ComplianceMonitor.objects.get(pk=compliancemonitor_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.compliance_type = compliance_type if compliance_type is not None else instance.compliance_type
        instance.description = description if description is not None else instance.description
        instance.status = status if status is not None else instance.status
        instance.date = date if date is not None else instance.date
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ComplianceMonitor.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_compliancemonitor(compliancemonitor_id=None):
    """
    Retrieves and serializes a ComplianceMonitor instance by its ID or all instances if ID is None.
    
    Args:
        ComplianceMonitor_id (int, optional): ID of the ComplianceMonitor to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if compliancemonitor_id is not None:
            record = ComplianceMonitor.objects.get(pk=compliancemonitor_id)
            serializer = ComplianceMonitorSerializer(record)
        else:
            records = ComplianceMonitor.objects.all()
            serializer = ComplianceMonitorSerializer(records, many=True)
        return success(serializer.data)
    
    except ComplianceMonitor.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ComplianceMonitor does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_compliancemonitor(compliancemonitor_id):
    """
    Deletes a ComplianceMonitor instance with the given ID.
    
    Args:
        compliancemonitor_id (int): ID of the ComplianceMonitor to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ComplianceMonitor.objects.get(pk=compliancemonitor_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ComplianceMonitor.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_contract(project_id, contractor_id, scope_of_work, pricing, payment_terms, start_date, end_date, signed_by_client, signed_by_contractor, approved_by, status):
    """
    Creates a Contract instance with the provided data.
        Args:
        project_id, contractor_id, scope_of_work, pricing, payment_terms, start_date, end_date, signed_by_client, signed_by_contractor, approved_by, status: Keyword arguments for Contract fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if contractor_id is not None and contractor_id != '': 
             Contractor.objects.get(pk=contractor_id)
        instance = Contract.objects.create(
            project_id=project_id,
            contractor_id=contractor_id,
            scope_of_work=scope_of_work,
            pricing=pricing,
            payment_terms=payment_terms,
            start_date=start_date,
            end_date=end_date,
            signed_by_client=signed_by_client,
            signed_by_contractor=signed_by_contractor,
            approved_by=approved_by,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Contractor.DoesNotExist:
        return error('Invalid Contractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_contract(contract_id,project_id=None, contractor_id=None, scope_of_work=None, pricing=None, payment_terms=None, start_date=None, end_date=None, signed_by_client=None, signed_by_contractor=None, approved_by=None, status=None):
    """
    Updates a Contract instance with the provided data.
    
    Args:
        contract_id (int): ID of the Contract to update.
        project_id=None, contractor_id=None, scope_of_work=None, pricing=None, payment_terms=None, start_date=None, end_date=None, signed_by_client=None, signed_by_contractor=None, approved_by=None, status=None: Keyword arguments for Contract fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if contractor_id is not None and contractor_id != '': 
             Contractor.objects.get(pk=contractor_id)
        instance = Contract.objects.get(pk=contract_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.contractor_id = contractor_id if contractor_id is not None else instance.contractor_id
        instance.scope_of_work = scope_of_work if scope_of_work is not None else instance.scope_of_work
        instance.pricing = pricing if pricing is not None else instance.pricing
        instance.payment_terms = payment_terms if payment_terms is not None else instance.payment_terms
        instance.start_date = start_date if start_date is not None else instance.start_date
        instance.end_date = end_date if end_date is not None else instance.end_date
        instance.signed_by_client = signed_by_client if signed_by_client is not None else instance.signed_by_client
        instance.signed_by_contractor = signed_by_contractor if signed_by_contractor is not None else instance.signed_by_contractor
        instance.approved_by = approved_by if approved_by is not None else instance.approved_by
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Contractor.DoesNotExist:
        return error('Invalid Contractor ID: Destination not found.')
    except  Contract.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_contract(contract_id=None):
    """
    Retrieves and serializes a Contract instance by its ID or all instances if ID is None.
    
    Args:
        Contract_id (int, optional): ID of the Contract to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None:
            record = Contract.objects.get(pk=contract_id)
            serializer = ContractSerializer(record)
        else:
            records = Contract.objects.all()
            serializer = ContractSerializer(records, many=True)
        return success(serializer.data)
    
    except Contract.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Contract does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_contract(contract_id):
    """
    Deletes a Contract instance with the given ID.
    
    Args:
        contract_id (int): ID of the Contract to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Contract.objects.get(pk=contract_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Contract.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_contractawardexecution(contract_title, project_manager_id, execution_status, delivery_commitments, execution_notes):
    """
    Creates a ContractAwardExecution instance with the provided data.
        Args:
        contract_title, project_manager_id, execution_status, delivery_commitments, execution_notes: Keyword arguments for ContractAwardExecution fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_manager_id is not None and project_manager_id != '': 
             Project.objects.get(pk=project_manager_id)
        instance = ContractAwardExecution.objects.create(
            contract_title=contract_title,
            project_manager_id=project_manager_id,
            execution_status=execution_status,
            delivery_commitments=delivery_commitments,
            execution_notes=execution_notes,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_contractawardexecution(contractawardexecution_id,contract_title=None, project_manager_id=None, execution_status=None, delivery_commitments=None, execution_notes=None):
    """
    Updates a ContractAwardExecution instance with the provided data.
    
    Args:
        contractawardexecution_id (int): ID of the ContractAwardExecution to update.
        contract_title=None, project_manager_id=None, execution_status=None, delivery_commitments=None, execution_notes=None: Keyword arguments for ContractAwardExecution fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_manager_id is not None and project_manager_id != '': 
             Project.objects.get(pk=project_manager_id)
        instance = ContractAwardExecution.objects.get(pk=contractawardexecution_id)
        instance.contract_title = contract_title if contract_title is not None else instance.contract_title
        instance.project_manager_id = project_manager_id if project_manager_id is not None else instance.project_manager_id
        instance.execution_status = execution_status if execution_status is not None else instance.execution_status
        instance.delivery_commitments = delivery_commitments if delivery_commitments is not None else instance.delivery_commitments
        instance.execution_notes = execution_notes if execution_notes is not None else instance.execution_notes
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ContractAwardExecution.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_contractawardexecution(contractawardexecution_id=None):
    """
    Retrieves and serializes a ContractAwardExecution instance by its ID or all instances if ID is None.
    
    Args:
        ContractAwardExecution_id (int, optional): ID of the ContractAwardExecution to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contractawardexecution_id is not None:
            record = ContractAwardExecution.objects.get(pk=contractawardexecution_id)
            serializer = ContractAwardExecutionSerializer(record)
        else:
            records = ContractAwardExecution.objects.all()
            serializer = ContractAwardExecutionSerializer(records, many=True)
        return success(serializer.data)
    
    except ContractAwardExecution.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ContractAwardExecution does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_contractawardexecution(contractawardexecution_id):
    """
    Deletes a ContractAwardExecution instance with the given ID.
    
    Args:
        contractawardexecution_id (int): ID of the ContractAwardExecution to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ContractAwardExecution.objects.get(pk=contractawardexecution_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ContractAwardExecution.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_costestimation(project_id, category_id, estimated_cost, actual_cost, forecast_cost, description):
    """
    Creates a CostEstimation instance with the provided data.
        Args:
        project_id, category_id, estimated_cost, actual_cost, forecast_cost, description: Keyword arguments for CostEstimation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if category_id is not None and category_id != '': 
             CostCategory.objects.get(pk=category_id)
        instance = CostEstimation.objects.create(
            project_id=project_id,
            category_id=category_id,
            estimated_cost=estimated_cost,
            actual_cost=actual_cost,
            forecast_cost=forecast_cost,
            description=description,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except CostCategory.DoesNotExist:
        return error('Invalid CostCategory ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_costestimation(costestimation_id,project_id=None, category_id=None, estimated_cost=None, actual_cost=None, forecast_cost=None, description=None):
    """
    Updates a CostEstimation instance with the provided data.
    
    Args:
        costestimation_id (int): ID of the CostEstimation to update.
        project_id=None, category_id=None, estimated_cost=None, actual_cost=None, forecast_cost=None, description=None: Keyword arguments for CostEstimation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if category_id is not None and category_id != '': 
             CostCategory.objects.get(pk=category_id)
        instance = CostEstimation.objects.get(pk=costestimation_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.category_id = category_id if category_id is not None else instance.category_id
        instance.estimated_cost = estimated_cost if estimated_cost is not None else instance.estimated_cost
        instance.actual_cost = actual_cost if actual_cost is not None else instance.actual_cost
        instance.forecast_cost = forecast_cost if forecast_cost is not None else instance.forecast_cost
        instance.description = description if description is not None else instance.description
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except CostCategory.DoesNotExist:
        return error('Invalid CostCategory ID: Destination not found.')
    except  CostEstimation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_costestimation(costestimation_id=None):
    """
    Retrieves and serializes a CostEstimation instance by its ID or all instances if ID is None.
    
    Args:
        CostEstimation_id (int, optional): ID of the CostEstimation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if costestimation_id is not None:
            record = CostEstimation.objects.get(pk=costestimation_id)
            serializer = CostEstimationSerializer(record)
        else:
            records = CostEstimation.objects.all()
            serializer = CostEstimationSerializer(records, many=True)
        return success(serializer.data)
    
    except CostEstimation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CostEstimation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_costestimation(costestimation_id):
    """
    Deletes a CostEstimation instance with the given ID.
    
    Args:
        costestimation_id (int): ID of the CostEstimation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CostEstimation.objects.get(pk=costestimation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CostEstimation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_finalclientsignoff(project_id, client_id, sign_off_date, is_approved, comments):
    """
    Creates a FinalClientSignOff instance with the provided data.
        Args:
        project_id, client_id, sign_off_date, is_approved, comments: Keyword arguments for FinalClientSignOff fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if client_id is not None and client_id != '': 
             User.objects.get(pk=client_id)
        instance = FinalClientSignOff.objects.create(
            project_id=project_id,
            client_id=client_id,
            sign_off_date=sign_off_date,
            is_approved=is_approved,
            comments=comments,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_finalclientsignoff(finalclientsignoff_id,project_id=None, client_id=None, sign_off_date=None, is_approved=None, comments=None):
    """
    Updates a FinalClientSignOff instance with the provided data.
    
    Args:
        finalclientsignoff_id (int): ID of the FinalClientSignOff to update.
        project_id=None, client_id=None, sign_off_date=None, is_approved=None, comments=None: Keyword arguments for FinalClientSignOff fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if client_id is not None and client_id != '': 
             User.objects.get(pk=client_id)
        instance = FinalClientSignOff.objects.get(pk=finalclientsignoff_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.client_id = client_id if client_id is not None else instance.client_id
        instance.sign_off_date = sign_off_date if sign_off_date is not None else instance.sign_off_date
        instance.is_approved = is_approved if is_approved is not None else instance.is_approved
        instance.comments = comments if comments is not None else instance.comments
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  FinalClientSignOff.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_finalclientsignoff(finalclientsignoff_id=None):
    """
    Retrieves and serializes a FinalClientSignOff instance by its ID or all instances if ID is None.
    
    Args:
        FinalClientSignOff_id (int, optional): ID of the FinalClientSignOff to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if finalclientsignoff_id is not None:
            record = FinalClientSignOff.objects.get(pk=finalclientsignoff_id)
            serializer = FinalClientSignOffSerializer(record)
        else:
            records = FinalClientSignOff.objects.all()
            serializer = FinalClientSignOffSerializer(records, many=True)
        return success(serializer.data)
    
    except FinalClientSignOff.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('FinalClientSignOff does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_finalclientsignoff(finalclientsignoff_id):
    """
    Deletes a FinalClientSignOff instance with the given ID.
    
    Args:
        finalclientsignoff_id (int): ID of the FinalClientSignOff to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = FinalClientSignOff.objects.get(pk=finalclientsignoff_id)
        instance.delete()
        return success("Successfully deleted")
    
    except FinalClientSignOff.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_finalinspection(project_id, inspection_date, inspector_id, client_present, comments, all_punch_items_resolved):
    """
    Creates a FinalInspection instance with the provided data.
        Args:
        project_id, inspection_date, inspector_id, client_present, comments, all_punch_items_resolved: Keyword arguments for FinalInspection fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if inspector_id is not None and inspector_id != '': 
             User.objects.get(pk=inspector_id)
        instance = FinalInspection.objects.create(
            project_id=project_id,
            inspection_date=inspection_date,
            inspector_id=inspector_id,
            client_present=client_present,
            comments=comments,
            all_punch_items_resolved=all_punch_items_resolved,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_finalinspection(finalinspection_id,project_id=None, inspection_date=None, inspector_id=None, client_present=None, comments=None, all_punch_items_resolved=None):
    """
    Updates a FinalInspection instance with the provided data.
    
    Args:
        finalinspection_id (int): ID of the FinalInspection to update.
        project_id=None, inspection_date=None, inspector_id=None, client_present=None, comments=None, all_punch_items_resolved=None: Keyword arguments for FinalInspection fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if inspector_id is not None and inspector_id != '': 
             User.objects.get(pk=inspector_id)
        instance = FinalInspection.objects.get(pk=finalinspection_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.inspection_date = inspection_date if inspection_date is not None else instance.inspection_date
        instance.inspector_id = inspector_id if inspector_id is not None else instance.inspector_id
        instance.client_present = client_present if client_present is not None else instance.client_present
        instance.comments = comments if comments is not None else instance.comments
        instance.all_punch_items_resolved = all_punch_items_resolved if all_punch_items_resolved is not None else instance.all_punch_items_resolved
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  FinalInspection.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_finalinspection(finalinspection_id=None):
    """
    Retrieves and serializes a FinalInspection instance by its ID or all instances if ID is None.
    
    Args:
        FinalInspection_id (int, optional): ID of the FinalInspection to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if finalinspection_id is not None:
            record = FinalInspection.objects.get(pk=finalinspection_id)
            serializer = FinalInspectionSerializer(record)
        else:
            records = FinalInspection.objects.all()
            serializer = FinalInspectionSerializer(records, many=True)
        return success(serializer.data)
    
    except FinalInspection.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('FinalInspection does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_finalinspection(finalinspection_id):
    """
    Deletes a FinalInspection instance with the given ID.
    
    Args:
        finalinspection_id (int): ID of the FinalInspection to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = FinalInspection.objects.get(pk=finalinspection_id)
        instance.delete()
        return success("Successfully deleted")
    
    except FinalInspection.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_finalreview(project_id, review_type, review_details, conducted_by_id, date):
    """
    Creates a FinalReview instance with the provided data.
        Args:
        project_id, review_type, review_details, conducted_by_id, date: Keyword arguments for FinalReview fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if conducted_by_id is not None and conducted_by_id != '': 
             User.objects.get(pk=conducted_by_id)
        instance = FinalReview.objects.create(
            project_id=project_id,
            review_type=review_type,
            review_details=review_details,
            conducted_by_id=conducted_by_id,
            date=date,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_finalreview(finalreview_id,project_id=None, review_type=None, review_details=None, conducted_by_id=None, date=None):
    """
    Updates a FinalReview instance with the provided data.
    
    Args:
        finalreview_id (int): ID of the FinalReview to update.
        project_id=None, review_type=None, review_details=None, conducted_by_id=None, date=None: Keyword arguments for FinalReview fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if conducted_by_id is not None and conducted_by_id != '': 
             User.objects.get(pk=conducted_by_id)
        instance = FinalReview.objects.get(pk=finalreview_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.review_type = review_type if review_type is not None else instance.review_type
        instance.review_details = review_details if review_details is not None else instance.review_details
        instance.conducted_by_id = conducted_by_id if conducted_by_id is not None else instance.conducted_by_id
        instance.date = date if date is not None else instance.date
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  FinalReview.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_finalreview(finalreview_id=None):
    """
    Retrieves and serializes a FinalReview instance by its ID or all instances if ID is None.
    
    Args:
        FinalReview_id (int, optional): ID of the FinalReview to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if finalreview_id is not None:
            record = FinalReview.objects.get(pk=finalreview_id)
            serializer = FinalReviewSerializer(record)
        else:
            records = FinalReview.objects.all()
            serializer = FinalReviewSerializer(records, many=True)
        return success(serializer.data)
    
    except FinalReview.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('FinalReview does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_finalreview(finalreview_id):
    """
    Deletes a FinalReview instance with the given ID.
    
    Args:
        finalreview_id (int): ID of the FinalReview to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = FinalReview.objects.get(pk=finalreview_id)
        instance.delete()
        return success("Successfully deleted")
    
    except FinalReview.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_financialtransaction(project_id, account_id, transaction_type, amount, description):
    """
    Creates a FinancialTransaction instance with the provided data.
        Args:
        project_id, account_id, transaction_type, amount, description: Keyword arguments for FinancialTransaction fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if account_id is not None and account_id != '': 
             Account.objects.get(pk=account_id)
        instance = FinancialTransaction.objects.create(
            project_id=project_id,
            account_id=account_id,
            transaction_type=transaction_type,
            amount=amount,
            description=description,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Account.DoesNotExist:
        return error('Invalid Account ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_financialtransaction(financialtransaction_id,project_id=None, account_id=None, transaction_type=None, amount=None, description=None):
    """
    Updates a FinancialTransaction instance with the provided data.
    
    Args:
        financialtransaction_id (int): ID of the FinancialTransaction to update.
        project_id=None, account_id=None, transaction_type=None, amount=None, description=None: Keyword arguments for FinancialTransaction fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if account_id is not None and account_id != '': 
             Account.objects.get(pk=account_id)
        instance = FinancialTransaction.objects.get(pk=financialtransaction_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.account_id = account_id if account_id is not None else instance.account_id
        instance.transaction_type = transaction_type if transaction_type is not None else instance.transaction_type
        instance.amount = amount if amount is not None else instance.amount
        instance.description = description if description is not None else instance.description
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Account.DoesNotExist:
        return error('Invalid Account ID: Destination not found.')
    except  FinancialTransaction.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_financialtransaction(financialtransaction_id=None):
    """
    Retrieves and serializes a FinancialTransaction instance by its ID or all instances if ID is None.
    
    Args:
        FinancialTransaction_id (int, optional): ID of the FinancialTransaction to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if financialtransaction_id is not None:
            record = FinancialTransaction.objects.get(pk=financialtransaction_id)
            serializer = FinancialTransactionSerializer(record)
        else:
            records = FinancialTransaction.objects.all()
            serializer = FinancialTransactionSerializer(records, many=True)
        return success(serializer.data)
    
    except FinancialTransaction.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('FinancialTransaction does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_financialtransaction(financialtransaction_id):
    """
    Deletes a FinancialTransaction instance with the given ID.
    
    Args:
        financialtransaction_id (int): ID of the FinancialTransaction to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = FinancialTransaction.objects.get(pk=financialtransaction_id)
        instance.delete()
        return success("Successfully deleted")
    
    except FinancialTransaction.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_incidentreport(project_id, reported_by_id, incident_type, description, immediate_action):
    """
    Creates a IncidentReport instance with the provided data.
        Args:
        project_id, reported_by_id, incident_type, description, immediate_action: Keyword arguments for IncidentReport fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = IncidentReport.objects.create(
            project_id=project_id,
            reported_by_id=reported_by_id,
            incident_type=incident_type,
            description=description,
            immediate_action=immediate_action,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_incidentreport(incidentreport_id,project_id=None, reported_by_id=None, incident_type=None, description=None, immediate_action=None):
    """
    Updates a IncidentReport instance with the provided data.
    
    Args:
        incidentreport_id (int): ID of the IncidentReport to update.
        project_id=None, reported_by_id=None, incident_type=None, description=None, immediate_action=None: Keyword arguments for IncidentReport fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = IncidentReport.objects.get(pk=incidentreport_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.reported_by_id = reported_by_id if reported_by_id is not None else instance.reported_by_id
        instance.incident_type = incident_type if incident_type is not None else instance.incident_type
        instance.description = description if description is not None else instance.description
        instance.immediate_action = immediate_action if immediate_action is not None else instance.immediate_action
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  IncidentReport.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_incidentreport(incidentreport_id=None):
    """
    Retrieves and serializes a IncidentReport instance by its ID or all instances if ID is None.
    
    Args:
        IncidentReport_id (int, optional): ID of the IncidentReport to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if incidentreport_id is not None:
            record = IncidentReport.objects.get(pk=incidentreport_id)
            serializer = IncidentReportSerializer(record)
        else:
            records = IncidentReport.objects.all()
            serializer = IncidentReportSerializer(records, many=True)
        return success(serializer.data)
    
    except IncidentReport.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('IncidentReport does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_incidentreport(incidentreport_id):
    """
    Deletes a IncidentReport instance with the given ID.
    
    Args:
        incidentreport_id (int): ID of the IncidentReport to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = IncidentReport.objects.get(pk=incidentreport_id)
        instance.delete()
        return success("Successfully deleted")
    
    except IncidentReport.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_inspection(project_id, inspector_id, inspection_type, date, checklist, findings):
    """
    Creates a Inspection instance with the provided data.
        Args:
        project_id, inspector_id, inspection_type, date, checklist, findings: Keyword arguments for Inspection fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if inspector_id is not None and inspector_id != '': 
             User.objects.get(pk=inspector_id)
        instance = Inspection.objects.create(
            project_id=project_id,
            inspector_id=inspector_id,
            inspection_type=inspection_type,
            date=date,
            checklist=checklist,
            findings=findings,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_inspection(inspection_id,project_id=None, inspector_id=None, inspection_type=None, date=None, checklist=None, findings=None):
    """
    Updates a Inspection instance with the provided data.
    
    Args:
        inspection_id (int): ID of the Inspection to update.
        project_id=None, inspector_id=None, inspection_type=None, date=None, checklist=None, findings=None: Keyword arguments for Inspection fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if inspector_id is not None and inspector_id != '': 
             User.objects.get(pk=inspector_id)
        instance = Inspection.objects.get(pk=inspection_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.inspector_id = inspector_id if inspector_id is not None else instance.inspector_id
        instance.inspection_type = inspection_type if inspection_type is not None else instance.inspection_type
        instance.date = date if date is not None else instance.date
        instance.checklist = checklist if checklist is not None else instance.checklist
        instance.findings = findings if findings is not None else instance.findings
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  Inspection.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_inspection(inspection_id=None):
    """
    Retrieves and serializes a Inspection instance by its ID or all instances if ID is None.
    
    Args:
        Inspection_id (int, optional): ID of the Inspection to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if inspection_id is not None:
            record = Inspection.objects.get(pk=inspection_id)
            serializer = InspectionSerializer(record)
        else:
            records = Inspection.objects.all()
            serializer = InspectionSerializer(records, many=True)
        return success(serializer.data)
    
    except Inspection.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Inspection does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_inspection(inspection_id):
    """
    Deletes a Inspection instance with the given ID.
    
    Args:
        inspection_id (int): ID of the Inspection to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Inspection.objects.get(pk=inspection_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Inspection.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_legalrequirement(project_id, description, requirement_type):
    """
    Creates a LegalRequirement instance with the provided data.
        Args:
        project_id, description, requirement_type: Keyword arguments for LegalRequirement fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = LegalRequirement.objects.create(
            project_id=project_id,
            description=description,
            requirement_type=requirement_type,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_legalrequirement(legalrequirement_id,project_id=None, description=None, requirement_type=None):
    """
    Updates a LegalRequirement instance with the provided data.
    
    Args:
        legalrequirement_id (int): ID of the LegalRequirement to update.
        project_id=None, description=None, requirement_type=None: Keyword arguments for LegalRequirement fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = LegalRequirement.objects.get(pk=legalrequirement_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.description = description if description is not None else instance.description
        instance.requirement_type = requirement_type if requirement_type is not None else instance.requirement_type
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  LegalRequirement.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_legalrequirement(legalrequirement_id=None):
    """
    Retrieves and serializes a LegalRequirement instance by its ID or all instances if ID is None.
    
    Args:
        LegalRequirement_id (int, optional): ID of the LegalRequirement to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if legalrequirement_id is not None:
            record = LegalRequirement.objects.get(pk=legalrequirement_id)
            serializer = LegalRequirementSerializer(record)
        else:
            records = LegalRequirement.objects.all()
            serializer = LegalRequirementSerializer(records, many=True)
        return success(serializer.data)
    
    except LegalRequirement.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('LegalRequirement does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_legalrequirement(legalrequirement_id):
    """
    Deletes a LegalRequirement instance with the given ID.
    
    Args:
        legalrequirement_id (int): ID of the LegalRequirement to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = LegalRequirement.objects.get(pk=legalrequirement_id)
        instance.delete()
        return success("Successfully deleted")
    
    except LegalRequirement.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_message(project_id, content):
    """
    Creates a Message instance with the provided data.
        Args:
        project_id, content: Keyword arguments for Message fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Message.objects.create(
            project_id=project_id,
            content=content,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_message(message_id,project_id=None, content=None):
    """
    Updates a Message instance with the provided data.
    
    Args:
        message_id (int): ID of the Message to update.
        project_id=None, content=None: Keyword arguments for Message fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Message.objects.get(pk=message_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.content = content if content is not None else instance.content
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  Message.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_message(message_id=None):
    """
    Retrieves and serializes a Message instance by its ID or all instances if ID is None.
    
    Args:
        Message_id (int, optional): ID of the Message to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if message_id is not None:
            record = Message.objects.get(pk=message_id)
            serializer = MessageSerializer(record)
        else:
            records = Message.objects.all()
            serializer = MessageSerializer(records, many=True)
        return success(serializer.data)
    
    except Message.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Message does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_message(message_id):
    """
    Deletes a Message instance with the given ID.
    
    Args:
        message_id (int): ID of the Message to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Message.objects.get(pk=message_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Message.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_milestone(project_id, name, target_date, client_review_required):
    """
    Creates a Milestone instance with the provided data.
        Args:
        project_id, name, target_date, client_review_required: Keyword arguments for Milestone fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Milestone.objects.create(
            project_id=project_id,
            name=name,
            target_date=target_date,
            client_review_required=client_review_required,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_milestone(milestone_id,project_id=None, name=None, target_date=None, client_review_required=None):
    """
    Updates a Milestone instance with the provided data.
    
    Args:
        milestone_id (int): ID of the Milestone to update.
        project_id=None, name=None, target_date=None, client_review_required=None: Keyword arguments for Milestone fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Milestone.objects.get(pk=milestone_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.name = name if name is not None else instance.name
        instance.target_date = target_date if target_date is not None else instance.target_date
        instance.client_review_required = client_review_required if client_review_required is not None else instance.client_review_required
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  Milestone.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_milestone(milestone_id=None):
    """
    Retrieves and serializes a Milestone instance by its ID or all instances if ID is None.
    
    Args:
        Milestone_id (int, optional): ID of the Milestone to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if milestone_id is not None:
            record = Milestone.objects.get(pk=milestone_id)
            serializer = MilestoneSerializer(record)
        else:
            records = Milestone.objects.all()
            serializer = MilestoneSerializer(records, many=True)
        return success(serializer.data)
    
    except Milestone.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Milestone does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_milestone(milestone_id):
    """
    Deletes a Milestone instance with the given ID.
    
    Args:
        milestone_id (int): ID of the Milestone to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Milestone.objects.get(pk=milestone_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Milestone.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_milestonebilling(project_id, milestone_name, description, due_date, amount, invoiced):
    """
    Creates a MilestoneBilling instance with the provided data.
        Args:
        project_id, milestone_name, description, due_date, amount, invoiced: Keyword arguments for MilestoneBilling fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = MilestoneBilling.objects.create(
            project_id=project_id,
            milestone_name=milestone_name,
            description=description,
            due_date=due_date,
            amount=amount,
            invoiced=invoiced,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_milestonebilling(milestonebilling_id,project_id=None, milestone_name=None, description=None, due_date=None, amount=None, invoiced=None):
    """
    Updates a MilestoneBilling instance with the provided data.
    
    Args:
        milestonebilling_id (int): ID of the MilestoneBilling to update.
        project_id=None, milestone_name=None, description=None, due_date=None, amount=None, invoiced=None: Keyword arguments for MilestoneBilling fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = MilestoneBilling.objects.get(pk=milestonebilling_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.milestone_name = milestone_name if milestone_name is not None else instance.milestone_name
        instance.description = description if description is not None else instance.description
        instance.due_date = due_date if due_date is not None else instance.due_date
        instance.amount = amount if amount is not None else instance.amount
        instance.invoiced = invoiced if invoiced is not None else instance.invoiced
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  MilestoneBilling.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_milestonebilling(milestonebilling_id=None):
    """
    Retrieves and serializes a MilestoneBilling instance by its ID or all instances if ID is None.
    
    Args:
        MilestoneBilling_id (int, optional): ID of the MilestoneBilling to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if milestonebilling_id is not None:
            record = MilestoneBilling.objects.get(pk=milestonebilling_id)
            serializer = MilestoneBillingSerializer(record)
        else:
            records = MilestoneBilling.objects.all()
            serializer = MilestoneBillingSerializer(records, many=True)
        return success(serializer.data)
    
    except MilestoneBilling.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('MilestoneBilling does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_milestonebilling(milestonebilling_id):
    """
    Deletes a MilestoneBilling instance with the given ID.
    
    Args:
        milestonebilling_id (int): ID of the MilestoneBilling to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = MilestoneBilling.objects.get(pk=milestonebilling_id)
        instance.delete()
        return success("Successfully deleted")
    
    except MilestoneBilling.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_payroll(worker_id, project_id, pay_period_start, pay_period_end, total_hours, hourly_rate, total_pay):
    """
    Creates a Payroll instance with the provided data.
        Args:
        worker_id, project_id, pay_period_start, pay_period_end, total_hours, hourly_rate, total_pay: Keyword arguments for Payroll fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if worker_id is not None and worker_id != '': 
             User.objects.get(pk=worker_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Payroll.objects.create(
            worker_id=worker_id,
            project_id=project_id,
            pay_period_start=pay_period_start,
            pay_period_end=pay_period_end,
            total_hours=total_hours,
            hourly_rate=hourly_rate,
            total_pay=total_pay,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_payroll(payroll_id,worker_id=None, project_id=None, pay_period_start=None, pay_period_end=None, total_hours=None, hourly_rate=None, total_pay=None):
    """
    Updates a Payroll instance with the provided data.
    
    Args:
        payroll_id (int): ID of the Payroll to update.
        worker_id=None, project_id=None, pay_period_start=None, pay_period_end=None, total_hours=None, hourly_rate=None, total_pay=None: Keyword arguments for Payroll fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if worker_id is not None and worker_id != '': 
             User.objects.get(pk=worker_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Payroll.objects.get(pk=payroll_id)
        instance.worker_id = worker_id if worker_id is not None else instance.worker_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.pay_period_start = pay_period_start if pay_period_start is not None else instance.pay_period_start
        instance.pay_period_end = pay_period_end if pay_period_end is not None else instance.pay_period_end
        instance.total_hours = total_hours if total_hours is not None else instance.total_hours
        instance.hourly_rate = hourly_rate if hourly_rate is not None else instance.hourly_rate
        instance.total_pay = total_pay if total_pay is not None else instance.total_pay
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  Payroll.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_payroll(payroll_id=None):
    """
    Retrieves and serializes a Payroll instance by its ID or all instances if ID is None.
    
    Args:
        Payroll_id (int, optional): ID of the Payroll to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if payroll_id is not None:
            record = Payroll.objects.get(pk=payroll_id)
            serializer = PayrollSerializer(record)
        else:
            records = Payroll.objects.all()
            serializer = PayrollSerializer(records, many=True)
        return success(serializer.data)
    
    except Payroll.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Payroll does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_payroll(payroll_id):
    """
    Deletes a Payroll instance with the given ID.
    
    Args:
        payroll_id (int): ID of the Payroll to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Payroll.objects.get(pk=payroll_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Payroll.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_postprojectreview(project_id, review_date, evaluation_summary, strengths, areas_for_improvement, lessons_learned, recommendations):
    """
    Creates a PostProjectReview instance with the provided data.
        Args:
        project_id, review_date, evaluation_summary, strengths, areas_for_improvement, lessons_learned, recommendations: Keyword arguments for PostProjectReview fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = PostProjectReview.objects.create(
            project_id=project_id,
            review_date=review_date,
            evaluation_summary=evaluation_summary,
            strengths=strengths,
            areas_for_improvement=areas_for_improvement,
            lessons_learned=lessons_learned,
            recommendations=recommendations,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_postprojectreview(postprojectreview_id,project_id=None, review_date=None, evaluation_summary=None, strengths=None, areas_for_improvement=None, lessons_learned=None, recommendations=None):
    """
    Updates a PostProjectReview instance with the provided data.
    
    Args:
        postprojectreview_id (int): ID of the PostProjectReview to update.
        project_id=None, review_date=None, evaluation_summary=None, strengths=None, areas_for_improvement=None, lessons_learned=None, recommendations=None: Keyword arguments for PostProjectReview fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = PostProjectReview.objects.get(pk=postprojectreview_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.review_date = review_date if review_date is not None else instance.review_date
        instance.evaluation_summary = evaluation_summary if evaluation_summary is not None else instance.evaluation_summary
        instance.strengths = strengths if strengths is not None else instance.strengths
        instance.areas_for_improvement = areas_for_improvement if areas_for_improvement is not None else instance.areas_for_improvement
        instance.lessons_learned = lessons_learned if lessons_learned is not None else instance.lessons_learned
        instance.recommendations = recommendations if recommendations is not None else instance.recommendations
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  PostProjectReview.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_postprojectreview(postprojectreview_id=None):
    """
    Retrieves and serializes a PostProjectReview instance by its ID or all instances if ID is None.
    
    Args:
        PostProjectReview_id (int, optional): ID of the PostProjectReview to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if postprojectreview_id is not None:
            record = PostProjectReview.objects.get(pk=postprojectreview_id)
            serializer = PostProjectReviewSerializer(record)
        else:
            records = PostProjectReview.objects.all()
            serializer = PostProjectReviewSerializer(records, many=True)
        return success(serializer.data)
    
    except PostProjectReview.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PostProjectReview does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_postprojectreview(postprojectreview_id):
    """
    Deletes a PostProjectReview instance with the given ID.
    
    Args:
        postprojectreview_id (int): ID of the PostProjectReview to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PostProjectReview.objects.get(pk=postprojectreview_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PostProjectReview.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectcloseout(project_id, subcontractor_id, final_inspection_date, punch_list_items, punch_list_completed, final_payment):
    """
    Creates a ProjectCloseout instance with the provided data.
        Args:
        project_id, subcontractor_id, final_inspection_date, punch_list_items, punch_list_completed, final_payment: Keyword arguments for ProjectCloseout fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = ProjectCloseout.objects.create(
            project_id=project_id,
            subcontractor_id=subcontractor_id,
            final_inspection_date=final_inspection_date,
            punch_list_items=punch_list_items,
            punch_list_completed=punch_list_completed,
            final_payment=final_payment,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectcloseout(projectcloseout_id,project_id=None, subcontractor_id=None, final_inspection_date=None, punch_list_items=None, punch_list_completed=None, final_payment=None):
    """
    Updates a ProjectCloseout instance with the provided data.
    
    Args:
        projectcloseout_id (int): ID of the ProjectCloseout to update.
        project_id=None, subcontractor_id=None, final_inspection_date=None, punch_list_items=None, punch_list_completed=None, final_payment=None: Keyword arguments for ProjectCloseout fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = ProjectCloseout.objects.get(pk=projectcloseout_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.subcontractor_id = subcontractor_id if subcontractor_id is not None else instance.subcontractor_id
        instance.final_inspection_date = final_inspection_date if final_inspection_date is not None else instance.final_inspection_date
        instance.punch_list_items = punch_list_items if punch_list_items is not None else instance.punch_list_items
        instance.punch_list_completed = punch_list_completed if punch_list_completed is not None else instance.punch_list_completed
        instance.final_payment = final_payment if final_payment is not None else instance.final_payment
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except  ProjectCloseout.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectcloseout(projectcloseout_id=None):
    """
    Retrieves and serializes a ProjectCloseout instance by its ID or all instances if ID is None.
    
    Args:
        ProjectCloseout_id (int, optional): ID of the ProjectCloseout to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectcloseout_id is not None:
            record = ProjectCloseout.objects.get(pk=projectcloseout_id)
            serializer = ProjectCloseoutSerializer(record)
        else:
            records = ProjectCloseout.objects.all()
            serializer = ProjectCloseoutSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectCloseout.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectCloseout does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectcloseout(projectcloseout_id):
    """
    Deletes a ProjectCloseout instance with the given ID.
    
    Args:
        projectcloseout_id (int): ID of the ProjectCloseout to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectCloseout.objects.get(pk=projectcloseout_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectCloseout.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectcommunication(project_id, message):
    """
    Creates a ProjectCommunication instance with the provided data.
        Args:
        project_id, message: Keyword arguments for ProjectCommunication fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectCommunication.objects.create(
            project_id=project_id,
            message=message,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectcommunication(projectcommunication_id,project_id=None, message=None):
    """
    Updates a ProjectCommunication instance with the provided data.
    
    Args:
        projectcommunication_id (int): ID of the ProjectCommunication to update.
        project_id=None, message=None: Keyword arguments for ProjectCommunication fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectCommunication.objects.get(pk=projectcommunication_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.message = message if message is not None else instance.message
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ProjectCommunication.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectcommunication(projectcommunication_id=None):
    """
    Retrieves and serializes a ProjectCommunication instance by its ID or all instances if ID is None.
    
    Args:
        ProjectCommunication_id (int, optional): ID of the ProjectCommunication to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectcommunication_id is not None:
            record = ProjectCommunication.objects.get(pk=projectcommunication_id)
            serializer = ProjectCommunicationSerializer(record)
        else:
            records = ProjectCommunication.objects.all()
            serializer = ProjectCommunicationSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectCommunication.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectCommunication does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectcommunication(projectcommunication_id):
    """
    Deletes a ProjectCommunication instance with the given ID.
    
    Args:
        projectcommunication_id (int): ID of the ProjectCommunication to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectCommunication.objects.get(pk=projectcommunication_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectCommunication.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectdocumentation(project_id, document_type, issue_date, description):
    """
    Creates a ProjectDocumentation instance with the provided data.
        Args:
        project_id, document_type, issue_date, description: Keyword arguments for ProjectDocumentation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectDocumentation.objects.create(
            project_id=project_id,
            document_type=document_type,
            issue_date=issue_date,
            description=description,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectdocumentation(projectdocumentation_id,project_id=None, document_type=None, issue_date=None, description=None):
    """
    Updates a ProjectDocumentation instance with the provided data.
    
    Args:
        projectdocumentation_id (int): ID of the ProjectDocumentation to update.
        project_id=None, document_type=None, issue_date=None, description=None: Keyword arguments for ProjectDocumentation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectDocumentation.objects.get(pk=projectdocumentation_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.document_type = document_type if document_type is not None else instance.document_type
        instance.issue_date = issue_date if issue_date is not None else instance.issue_date
        instance.description = description if description is not None else instance.description
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ProjectDocumentation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectdocumentation(projectdocumentation_id=None):
    """
    Retrieves and serializes a ProjectDocumentation instance by its ID or all instances if ID is None.
    
    Args:
        ProjectDocumentation_id (int, optional): ID of the ProjectDocumentation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectdocumentation_id is not None:
            record = ProjectDocumentation.objects.get(pk=projectdocumentation_id)
            serializer = ProjectDocumentationSerializer(record)
        else:
            records = ProjectDocumentation.objects.all()
            serializer = ProjectDocumentationSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectDocumentation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectDocumentation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectdocumentation(projectdocumentation_id):
    """
    Deletes a ProjectDocumentation instance with the given ID.
    
    Args:
        projectdocumentation_id (int): ID of the ProjectDocumentation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectDocumentation.objects.get(pk=projectdocumentation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectDocumentation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectfinancialcloseout(project_id, closeout_date, total_cost, total_revenue, total_profit, subcontractors_paid, purchase_orders_closed):
    """
    Creates a ProjectFinancialCloseout instance with the provided data.
        Args:
        project_id, closeout_date, total_cost, total_revenue, total_profit, subcontractors_paid, purchase_orders_closed: Keyword arguments for ProjectFinancialCloseout fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectFinancialCloseout.objects.create(
            project_id=project_id,
            closeout_date=closeout_date,
            total_cost=total_cost,
            total_revenue=total_revenue,
            total_profit=total_profit,
            subcontractors_paid=subcontractors_paid,
            purchase_orders_closed=purchase_orders_closed,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectfinancialcloseout(projectfinancialcloseout_id,project_id=None, closeout_date=None, total_cost=None, total_revenue=None, total_profit=None, subcontractors_paid=None, purchase_orders_closed=None):
    """
    Updates a ProjectFinancialCloseout instance with the provided data.
    
    Args:
        projectfinancialcloseout_id (int): ID of the ProjectFinancialCloseout to update.
        project_id=None, closeout_date=None, total_cost=None, total_revenue=None, total_profit=None, subcontractors_paid=None, purchase_orders_closed=None: Keyword arguments for ProjectFinancialCloseout fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectFinancialCloseout.objects.get(pk=projectfinancialcloseout_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.closeout_date = closeout_date if closeout_date is not None else instance.closeout_date
        instance.total_cost = total_cost if total_cost is not None else instance.total_cost
        instance.total_revenue = total_revenue if total_revenue is not None else instance.total_revenue
        instance.total_profit = total_profit if total_profit is not None else instance.total_profit
        instance.subcontractors_paid = subcontractors_paid if subcontractors_paid is not None else instance.subcontractors_paid
        instance.purchase_orders_closed = purchase_orders_closed if purchase_orders_closed is not None else instance.purchase_orders_closed
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ProjectFinancialCloseout.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectfinancialcloseout(projectfinancialcloseout_id=None):
    """
    Retrieves and serializes a ProjectFinancialCloseout instance by its ID or all instances if ID is None.
    
    Args:
        ProjectFinancialCloseout_id (int, optional): ID of the ProjectFinancialCloseout to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectfinancialcloseout_id is not None:
            record = ProjectFinancialCloseout.objects.get(pk=projectfinancialcloseout_id)
            serializer = ProjectFinancialCloseoutSerializer(record)
        else:
            records = ProjectFinancialCloseout.objects.all()
            serializer = ProjectFinancialCloseoutSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectFinancialCloseout.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectFinancialCloseout does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectfinancialcloseout(projectfinancialcloseout_id):
    """
    Deletes a ProjectFinancialCloseout instance with the given ID.
    
    Args:
        projectfinancialcloseout_id (int): ID of the ProjectFinancialCloseout to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectFinancialCloseout.objects.get(pk=projectfinancialcloseout_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectFinancialCloseout.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectperformancereview(project_id, review_date, original_budget, actual_budget, resource_utilization_percentage, notes):
    """
    Creates a ProjectPerformanceReview instance with the provided data.
        Args:
        project_id, review_date, original_budget, actual_budget, resource_utilization_percentage, notes: Keyword arguments for ProjectPerformanceReview fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectPerformanceReview.objects.create(
            project_id=project_id,
            review_date=review_date,
            original_budget=original_budget,
            actual_budget=actual_budget,
            resource_utilization_percentage=resource_utilization_percentage,
            notes=notes,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectperformancereview(projectperformancereview_id,project_id=None, review_date=None, original_budget=None, actual_budget=None, resource_utilization_percentage=None, notes=None):
    """
    Updates a ProjectPerformanceReview instance with the provided data.
    
    Args:
        projectperformancereview_id (int): ID of the ProjectPerformanceReview to update.
        project_id=None, review_date=None, original_budget=None, actual_budget=None, resource_utilization_percentage=None, notes=None: Keyword arguments for ProjectPerformanceReview fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectPerformanceReview.objects.get(pk=projectperformancereview_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.review_date = review_date if review_date is not None else instance.review_date
        instance.original_budget = original_budget if original_budget is not None else instance.original_budget
        instance.actual_budget = actual_budget if actual_budget is not None else instance.actual_budget
        instance.resource_utilization_percentage = resource_utilization_percentage if resource_utilization_percentage is not None else instance.resource_utilization_percentage
        instance.notes = notes if notes is not None else instance.notes
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ProjectPerformanceReview.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectperformancereview(projectperformancereview_id=None):
    """
    Retrieves and serializes a ProjectPerformanceReview instance by its ID or all instances if ID is None.
    
    Args:
        ProjectPerformanceReview_id (int, optional): ID of the ProjectPerformanceReview to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectperformancereview_id is not None:
            record = ProjectPerformanceReview.objects.get(pk=projectperformancereview_id)
            serializer = ProjectPerformanceReviewSerializer(record)
        else:
            records = ProjectPerformanceReview.objects.all()
            serializer = ProjectPerformanceReviewSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectPerformanceReview.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectPerformanceReview does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectperformancereview(projectperformancereview_id):
    """
    Deletes a ProjectPerformanceReview instance with the given ID.
    
    Args:
        projectperformancereview_id (int): ID of the ProjectPerformanceReview to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectPerformanceReview.objects.get(pk=projectperformancereview_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectPerformanceReview.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectschedule(project_id, start_date, end_date):
    """
    Creates a ProjectSchedule instance with the provided data.
        Args:
        project_id, start_date, end_date: Keyword arguments for ProjectSchedule fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectSchedule.objects.create(
            project_id=project_id,
            start_date=start_date,
            end_date=end_date,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectschedule(projectschedule_id,project_id=None, start_date=None, end_date=None):
    """
    Updates a ProjectSchedule instance with the provided data.
    
    Args:
        projectschedule_id (int): ID of the ProjectSchedule to update.
        project_id=None, start_date=None, end_date=None: Keyword arguments for ProjectSchedule fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ProjectSchedule.objects.get(pk=projectschedule_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.start_date = start_date if start_date is not None else instance.start_date
        instance.end_date = end_date if end_date is not None else instance.end_date
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ProjectSchedule.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectschedule(projectschedule_id=None):
    """
    Retrieves and serializes a ProjectSchedule instance by its ID or all instances if ID is None.
    
    Args:
        ProjectSchedule_id (int, optional): ID of the ProjectSchedule to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectschedule_id is not None:
            record = ProjectSchedule.objects.get(pk=projectschedule_id)
            serializer = ProjectScheduleSerializer(record)
        else:
            records = ProjectSchedule.objects.all()
            serializer = ProjectScheduleSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectSchedule.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectSchedule does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectschedule(projectschedule_id):
    """
    Deletes a ProjectSchedule instance with the given ID.
    
    Args:
        projectschedule_id (int): ID of the ProjectSchedule to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectSchedule.objects.get(pk=projectschedule_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectSchedule.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_punchlistitem(project_id, description, status, contractor_id, resolved_at, fix_deadline, inspected, quality_meets_standards):
    """
    Creates a PunchListItem instance with the provided data.
        Args:
        project_id, description, status, contractor_id, resolved_at, fix_deadline, inspected, quality_meets_standards: Keyword arguments for PunchListItem fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if contractor_id is not None and contractor_id != '': 
             Contractor.objects.get(pk=contractor_id)
        instance = PunchListItem.objects.create(
            project_id=project_id,
            description=description,
            status=status,
            contractor_id=contractor_id,
            resolved_at=resolved_at,
            fix_deadline=fix_deadline,
            inspected=inspected,
            quality_meets_standards=quality_meets_standards,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Contractor.DoesNotExist:
        return error('Invalid Contractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_punchlistitem(punchlistitem_id,project_id=None, description=None, status=None, contractor_id=None, resolved_at=None, fix_deadline=None, inspected=None, quality_meets_standards=None):
    """
    Updates a PunchListItem instance with the provided data.
    
    Args:
        punchlistitem_id (int): ID of the PunchListItem to update.
        project_id=None, description=None, status=None, contractor_id=None, resolved_at=None, fix_deadline=None, inspected=None, quality_meets_standards=None: Keyword arguments for PunchListItem fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if contractor_id is not None and contractor_id != '': 
             Contractor.objects.get(pk=contractor_id)
        instance = PunchListItem.objects.get(pk=punchlistitem_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.description = description if description is not None else instance.description
        instance.status = status if status is not None else instance.status
        instance.contractor_id = contractor_id if contractor_id is not None else instance.contractor_id
        instance.resolved_at = resolved_at if resolved_at is not None else instance.resolved_at
        instance.fix_deadline = fix_deadline if fix_deadline is not None else instance.fix_deadline
        instance.inspected = inspected if inspected is not None else instance.inspected
        instance.quality_meets_standards = quality_meets_standards if quality_meets_standards is not None else instance.quality_meets_standards
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Contractor.DoesNotExist:
        return error('Invalid Contractor ID: Destination not found.')
    except  PunchListItem.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_punchlistitem(punchlistitem_id=None):
    """
    Retrieves and serializes a PunchListItem instance by its ID or all instances if ID is None.
    
    Args:
        PunchListItem_id (int, optional): ID of the PunchListItem to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if punchlistitem_id is not None:
            record = PunchListItem.objects.get(pk=punchlistitem_id)
            serializer = PunchListItemSerializer(record)
        else:
            records = PunchListItem.objects.all()
            serializer = PunchListItemSerializer(records, many=True)
        return success(serializer.data)
    
    except PunchListItem.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PunchListItem does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_punchlistitem(punchlistitem_id):
    """
    Deletes a PunchListItem instance with the given ID.
    
    Args:
        punchlistitem_id (int): ID of the PunchListItem to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PunchListItem.objects.get(pk=punchlistitem_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PunchListItem.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_qualitycontrolplan(project_id, content):
    """
    Creates a QualityControlPlan instance with the provided data.
        Args:
        project_id, content: Keyword arguments for QualityControlPlan fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = QualityControlPlan.objects.create(
            project_id=project_id,
            content=content,
            created_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_qualitycontrolplan(qualitycontrolplan_id,project_id=None, content=None):
    """
    Updates a QualityControlPlan instance with the provided data.
    
    Args:
        qualitycontrolplan_id (int): ID of the QualityControlPlan to update.
        project_id=None, content=None: Keyword arguments for QualityControlPlan fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = QualityControlPlan.objects.get(pk=qualitycontrolplan_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.content = content if content is not None else instance.content
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  QualityControlPlan.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_qualitycontrolplan(qualitycontrolplan_id=None):
    """
    Retrieves and serializes a QualityControlPlan instance by its ID or all instances if ID is None.
    
    Args:
        QualityControlPlan_id (int, optional): ID of the QualityControlPlan to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if qualitycontrolplan_id is not None:
            record = QualityControlPlan.objects.get(pk=qualitycontrolplan_id)
            serializer = QualityControlPlanSerializer(record)
        else:
            records = QualityControlPlan.objects.all()
            serializer = QualityControlPlanSerializer(records, many=True)
        return success(serializer.data)
    
    except QualityControlPlan.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('QualityControlPlan does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_qualitycontrolplan(qualitycontrolplan_id):
    """
    Deletes a QualityControlPlan instance with the given ID.
    
    Args:
        qualitycontrolplan_id (int): ID of the QualityControlPlan to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = QualityControlPlan.objects.get(pk=qualitycontrolplan_id)
        instance.delete()
        return success("Successfully deleted")
    
    except QualityControlPlan.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceplanning(project_id, workforce_required, project_duration):
    """
    Creates a ResourcePlanning instance with the provided data.
        Args:
        project_id, workforce_required, project_duration: Keyword arguments for ResourcePlanning fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ResourcePlanning.objects.create(
            project_id=project_id,
            workforce_required=workforce_required,
            project_duration=project_duration,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceplanning(resourceplanning_id,project_id=None, workforce_required=None, project_duration=None):
    """
    Updates a ResourcePlanning instance with the provided data.
    
    Args:
        resourceplanning_id (int): ID of the ResourcePlanning to update.
        project_id=None, workforce_required=None, project_duration=None: Keyword arguments for ResourcePlanning fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ResourcePlanning.objects.get(pk=resourceplanning_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.workforce_required = workforce_required if workforce_required is not None else instance.workforce_required
        instance.project_duration = project_duration if project_duration is not None else instance.project_duration
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ResourcePlanning.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceplanning(resourceplanning_id=None):
    """
    Retrieves and serializes a ResourcePlanning instance by its ID or all instances if ID is None.
    
    Args:
        ResourcePlanning_id (int, optional): ID of the ResourcePlanning to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceplanning_id is not None:
            record = ResourcePlanning.objects.get(pk=resourceplanning_id)
            serializer = ResourcePlanningSerializer(record)
        else:
            records = ResourcePlanning.objects.all()
            serializer = ResourcePlanningSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourcePlanning.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourcePlanning does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceplanning(resourceplanning_id):
    """
    Deletes a ResourcePlanning instance with the given ID.
    
    Args:
        resourceplanning_id (int): ID of the ResourcePlanning to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourcePlanning.objects.get(pk=resourceplanning_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourcePlanning.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceutilizationanalysis(project_id, analysis_date, total_labor_hours, total_materials_cost, total_equipment_cost, labor_utilization_percentage, materials_utilization_percentage, equipment_utilization_percentage, recommendations):
    """
    Creates a ResourceUtilizationAnalysis instance with the provided data.
        Args:
        project_id, analysis_date, total_labor_hours, total_materials_cost, total_equipment_cost, labor_utilization_percentage, materials_utilization_percentage, equipment_utilization_percentage, recommendations: Keyword arguments for ResourceUtilizationAnalysis fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ResourceUtilizationAnalysis.objects.create(
            project_id=project_id,
            analysis_date=analysis_date,
            total_labor_hours=total_labor_hours,
            total_materials_cost=total_materials_cost,
            total_equipment_cost=total_equipment_cost,
            labor_utilization_percentage=labor_utilization_percentage,
            materials_utilization_percentage=materials_utilization_percentage,
            equipment_utilization_percentage=equipment_utilization_percentage,
            recommendations=recommendations,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceutilizationanalysis(resourceutilizationanalysis_id,project_id=None, analysis_date=None, total_labor_hours=None, total_materials_cost=None, total_equipment_cost=None, labor_utilization_percentage=None, materials_utilization_percentage=None, equipment_utilization_percentage=None, recommendations=None):
    """
    Updates a ResourceUtilizationAnalysis instance with the provided data.
    
    Args:
        resourceutilizationanalysis_id (int): ID of the ResourceUtilizationAnalysis to update.
        project_id=None, analysis_date=None, total_labor_hours=None, total_materials_cost=None, total_equipment_cost=None, labor_utilization_percentage=None, materials_utilization_percentage=None, equipment_utilization_percentage=None, recommendations=None: Keyword arguments for ResourceUtilizationAnalysis fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = ResourceUtilizationAnalysis.objects.get(pk=resourceutilizationanalysis_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.analysis_date = analysis_date if analysis_date is not None else instance.analysis_date
        instance.total_labor_hours = total_labor_hours if total_labor_hours is not None else instance.total_labor_hours
        instance.total_materials_cost = total_materials_cost if total_materials_cost is not None else instance.total_materials_cost
        instance.total_equipment_cost = total_equipment_cost if total_equipment_cost is not None else instance.total_equipment_cost
        instance.labor_utilization_percentage = labor_utilization_percentage if labor_utilization_percentage is not None else instance.labor_utilization_percentage
        instance.materials_utilization_percentage = materials_utilization_percentage if materials_utilization_percentage is not None else instance.materials_utilization_percentage
        instance.equipment_utilization_percentage = equipment_utilization_percentage if equipment_utilization_percentage is not None else instance.equipment_utilization_percentage
        instance.recommendations = recommendations if recommendations is not None else instance.recommendations
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  ResourceUtilizationAnalysis.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceutilizationanalysis(resourceutilizationanalysis_id=None):
    """
    Retrieves and serializes a ResourceUtilizationAnalysis instance by its ID or all instances if ID is None.
    
    Args:
        ResourceUtilizationAnalysis_id (int, optional): ID of the ResourceUtilizationAnalysis to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceutilizationanalysis_id is not None:
            record = ResourceUtilizationAnalysis.objects.get(pk=resourceutilizationanalysis_id)
            serializer = ResourceUtilizationAnalysisSerializer(record)
        else:
            records = ResourceUtilizationAnalysis.objects.all()
            serializer = ResourceUtilizationAnalysisSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceUtilizationAnalysis.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceUtilizationAnalysis does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceutilizationanalysis(resourceutilizationanalysis_id):
    """
    Deletes a ResourceUtilizationAnalysis instance with the given ID.
    
    Args:
        resourceutilizationanalysis_id (int): ID of the ResourceUtilizationAnalysis to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceUtilizationAnalysis.objects.get(pk=resourceutilizationanalysis_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceUtilizationAnalysis.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_revenue(project_id, customer_id, description, amount, date, received_by):
    """
    Creates a Revenue instance with the provided data.
        Args:
        project_id, customer_id, description, amount, date, received_by: Keyword arguments for Revenue fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if customer_id is not None and customer_id != '': 
             Customer.objects.get(pk=customer_id)
        instance = Revenue.objects.create(
            project_id=project_id,
            customer_id=customer_id,
            description=description,
            amount=amount,
            date=date,
            received_by=received_by,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Customer.DoesNotExist:
        return error('Invalid Customer ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_revenue(revenue_id,project_id=None, customer_id=None, description=None, amount=None, date=None, received_by=None):
    """
    Updates a Revenue instance with the provided data.
    
    Args:
        revenue_id (int): ID of the Revenue to update.
        project_id=None, customer_id=None, description=None, amount=None, date=None, received_by=None: Keyword arguments for Revenue fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if customer_id is not None and customer_id != '': 
             Customer.objects.get(pk=customer_id)
        instance = Revenue.objects.get(pk=revenue_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.customer_id = customer_id if customer_id is not None else instance.customer_id
        instance.description = description if description is not None else instance.description
        instance.amount = amount if amount is not None else instance.amount
        instance.date = date if date is not None else instance.date
        instance.received_by = received_by if received_by is not None else instance.received_by
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Customer.DoesNotExist:
        return error('Invalid Customer ID: Destination not found.')
    except  Revenue.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_revenue(revenue_id=None):
    """
    Retrieves and serializes a Revenue instance by its ID or all instances if ID is None.
    
    Args:
        Revenue_id (int, optional): ID of the Revenue to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if revenue_id is not None:
            record = Revenue.objects.get(pk=revenue_id)
            serializer = RevenueSerializer(record)
        else:
            records = Revenue.objects.all()
            serializer = RevenueSerializer(records, many=True)
        return success(serializer.data)
    
    except Revenue.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Revenue does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_revenue(revenue_id):
    """
    Deletes a Revenue instance with the given ID.
    
    Args:
        revenue_id (int): ID of the Revenue to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Revenue.objects.get(pk=revenue_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Revenue.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_risk(project_id, risk_category_id, name, description, risk_type, date_identified, owner_id, status):
    """
    Creates a Risk instance with the provided data.
        Args:
        project_id, risk_category_id, name, description, risk_type, date_identified, owner_id, status: Keyword arguments for Risk fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if risk_category_id is not None and risk_category_id != '': 
             RiskCategory.objects.get(pk=risk_category_id)
        if owner_id is not None and owner_id != '': 
             RiskOwner.objects.get(pk=owner_id)
        instance = Risk.objects.create(
            project_id=project_id,
            risk_category_id=risk_category_id,
            name=name,
            description=description,
            risk_type=risk_type,
            date_identified=date_identified,
            owner_id=owner_id,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except RiskCategory.DoesNotExist:
        return error('Invalid RiskCategory ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_risk(risk_id,project_id=None, risk_category_id=None, name=None, description=None, risk_type=None, date_identified=None, owner_id=None, status=None):
    """
    Updates a Risk instance with the provided data.
    
    Args:
        risk_id (int): ID of the Risk to update.
        project_id=None, risk_category_id=None, name=None, description=None, risk_type=None, date_identified=None, owner_id=None, status=None: Keyword arguments for Risk fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if risk_category_id is not None and risk_category_id != '': 
             RiskCategory.objects.get(pk=risk_category_id)
        if owner_id is not None and owner_id != '': 
             RiskOwner.objects.get(pk=owner_id)
        instance = Risk.objects.get(pk=risk_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.risk_category_id = risk_category_id if risk_category_id is not None else instance.risk_category_id
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.risk_type = risk_type if risk_type is not None else instance.risk_type
        instance.date_identified = date_identified if date_identified is not None else instance.date_identified
        instance.owner_id = owner_id if owner_id is not None else instance.owner_id
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except RiskCategory.DoesNotExist:
        return error('Invalid RiskCategory ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except  Risk.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_risk(risk_id=None):
    """
    Retrieves and serializes a Risk instance by its ID or all instances if ID is None.
    
    Args:
        Risk_id (int, optional): ID of the Risk to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if risk_id is not None:
            record = Risk.objects.get(pk=risk_id)
            serializer = RiskSerializer(record)
        else:
            records = Risk.objects.all()
            serializer = RiskSerializer(records, many=True)
        return success(serializer.data)
    
    except Risk.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Risk does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_risk(risk_id):
    """
    Deletes a Risk instance with the given ID.
    
    Args:
        risk_id (int): ID of the Risk to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Risk.objects.get(pk=risk_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Risk.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_safetyplan(project_id, content):
    """
    Creates a SafetyPlan instance with the provided data.
        Args:
        project_id, content: Keyword arguments for SafetyPlan fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = SafetyPlan.objects.create(
            project_id=project_id,
            content=content,
            created_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_safetyplan(safetyplan_id,project_id=None, content=None):
    """
    Updates a SafetyPlan instance with the provided data.
    
    Args:
        safetyplan_id (int): ID of the SafetyPlan to update.
        project_id=None, content=None: Keyword arguments for SafetyPlan fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = SafetyPlan.objects.get(pk=safetyplan_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.content = content if content is not None else instance.content
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  SafetyPlan.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_safetyplan(safetyplan_id=None):
    """
    Retrieves and serializes a SafetyPlan instance by its ID or all instances if ID is None.
    
    Args:
        SafetyPlan_id (int, optional): ID of the SafetyPlan to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if safetyplan_id is not None:
            record = SafetyPlan.objects.get(pk=safetyplan_id)
            serializer = SafetyPlanSerializer(record)
        else:
            records = SafetyPlan.objects.all()
            serializer = SafetyPlanSerializer(records, many=True)
        return success(serializer.data)
    
    except SafetyPlan.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SafetyPlan does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_safetyplan(safetyplan_id):
    """
    Deletes a SafetyPlan instance with the given ID.
    
    Args:
        safetyplan_id (int): ID of the SafetyPlan to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SafetyPlan.objects.get(pk=safetyplan_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SafetyPlan.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_subcontractorcontract(project_id, subcontractor_id, signed_date, payment_terms, insurance_requirements, change_order_provision, termination_conditions):
    """
    Creates a SubcontractorContract instance with the provided data.
        Args:
        project_id, subcontractor_id, signed_date, payment_terms, insurance_requirements, change_order_provision, termination_conditions: Keyword arguments for SubcontractorContract fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = SubcontractorContract.objects.create(
            project_id=project_id,
            subcontractor_id=subcontractor_id,
            signed_date=signed_date,
            payment_terms=payment_terms,
            insurance_requirements=insurance_requirements,
            change_order_provision=change_order_provision,
            termination_conditions=termination_conditions,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_subcontractorcontract(subcontractorcontract_id,project_id=None, subcontractor_id=None, signed_date=None, payment_terms=None, insurance_requirements=None, change_order_provision=None, termination_conditions=None):
    """
    Updates a SubcontractorContract instance with the provided data.
    
    Args:
        subcontractorcontract_id (int): ID of the SubcontractorContract to update.
        project_id=None, subcontractor_id=None, signed_date=None, payment_terms=None, insurance_requirements=None, change_order_provision=None, termination_conditions=None: Keyword arguments for SubcontractorContract fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        instance = SubcontractorContract.objects.get(pk=subcontractorcontract_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.subcontractor_id = subcontractor_id if subcontractor_id is not None else instance.subcontractor_id
        instance.signed_date = signed_date if signed_date is not None else instance.signed_date
        instance.payment_terms = payment_terms if payment_terms is not None else instance.payment_terms
        instance.insurance_requirements = insurance_requirements if insurance_requirements is not None else instance.insurance_requirements
        instance.change_order_provision = change_order_provision if change_order_provision is not None else instance.change_order_provision
        instance.termination_conditions = termination_conditions if termination_conditions is not None else instance.termination_conditions
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except  SubcontractorContract.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_subcontractorcontract(subcontractorcontract_id=None):
    """
    Retrieves and serializes a SubcontractorContract instance by its ID or all instances if ID is None.
    
    Args:
        SubcontractorContract_id (int, optional): ID of the SubcontractorContract to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractorcontract_id is not None:
            record = SubcontractorContract.objects.get(pk=subcontractorcontract_id)
            serializer = SubcontractorContractSerializer(record)
        else:
            records = SubcontractorContract.objects.all()
            serializer = SubcontractorContractSerializer(records, many=True)
        return success(serializer.data)
    
    except SubcontractorContract.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SubcontractorContract does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_subcontractorcontract(subcontractorcontract_id):
    """
    Deletes a SubcontractorContract instance with the given ID.
    
    Args:
        subcontractorcontract_id (int): ID of the SubcontractorContract to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SubcontractorContract.objects.get(pk=subcontractorcontract_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SubcontractorContract.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceavailability(resource_id, available_from, available_until):
    """
    Creates a ResourceAvailability instance with the provided data.
        Args:
        resource_id, available_from, available_until: Keyword arguments for ResourceAvailability fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = ResourceAvailability.objects.create(
            resource_id=resource_id,
            available_from=available_from,
            available_until=available_until,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceavailability(resourceavailability_id,resource_id=None, available_from=None, available_until=None):
    """
    Updates a ResourceAvailability instance with the provided data.
    
    Args:
        resourceavailability_id (int): ID of the ResourceAvailability to update.
        resource_id=None, available_from=None, available_until=None: Keyword arguments for ResourceAvailability fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = ResourceAvailability.objects.get(pk=resourceavailability_id)
        instance.resource_id = resource_id if resource_id is not None else instance.resource_id
        instance.available_from = available_from if available_from is not None else instance.available_from
        instance.available_until = available_until if available_until is not None else instance.available_until
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except  ResourceAvailability.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceavailability(resourceavailability_id=None):
    """
    Retrieves and serializes a ResourceAvailability instance by its ID or all instances if ID is None.
    
    Args:
        ResourceAvailability_id (int, optional): ID of the ResourceAvailability to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceavailability_id is not None:
            record = ResourceAvailability.objects.get(pk=resourceavailability_id)
            serializer = ResourceAvailabilitySerializer(record)
        else:
            records = ResourceAvailability.objects.all()
            serializer = ResourceAvailabilitySerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceAvailability.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceAvailability does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceavailability(resourceavailability_id):
    """
    Deletes a ResourceAvailability instance with the given ID.
    
    Args:
        resourceavailability_id (int): ID of the ResourceAvailability to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceAvailability.objects.get(pk=resourceavailability_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceAvailability.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clarificationdocument(rfp_rfq_id):
    """
    Creates a ClarificationDocument instance with the provided data.
        Args:
        rfp_rfq_id: Keyword arguments for ClarificationDocument fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        instance = ClarificationDocument.objects.create(
            rfp_rfq_id=rfp_rfq_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clarificationdocument(clarificationdocument_id,rfp_rfq_id=None):
    """
    Updates a ClarificationDocument instance with the provided data.
    
    Args:
        clarificationdocument_id (int): ID of the ClarificationDocument to update.
        rfp_rfq_id=None: Keyword arguments for ClarificationDocument fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        instance = ClarificationDocument.objects.get(pk=clarificationdocument_id)
        instance.rfp_rfq_id = rfp_rfq_id if rfp_rfq_id is not None else instance.rfp_rfq_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except  ClarificationDocument.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clarificationdocument(clarificationdocument_id=None):
    """
    Retrieves and serializes a ClarificationDocument instance by its ID or all instances if ID is None.
    
    Args:
        ClarificationDocument_id (int, optional): ID of the ClarificationDocument to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clarificationdocument_id is not None:
            record = ClarificationDocument.objects.get(pk=clarificationdocument_id)
            serializer = ClarificationDocumentSerializer(record)
        else:
            records = ClarificationDocument.objects.all()
            serializer = ClarificationDocumentSerializer(records, many=True)
        return success(serializer.data)
    
    except ClarificationDocument.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClarificationDocument does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clarificationdocument(clarificationdocument_id):
    """
    Deletes a ClarificationDocument instance with the given ID.
    
    Args:
        clarificationdocument_id (int): ID of the ClarificationDocument to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClarificationDocument.objects.get(pk=clarificationdocument_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClarificationDocument.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stakeholder(name, role_id, project_id):
    """
    Creates a Stakeholder instance with the provided data.
        Args:
        name, role_id, project_id: Keyword arguments for Stakeholder fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if role_id is not None and role_id != '': 
             Role.objects.get(pk=role_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Stakeholder.objects.create(
            name=name,
            role_id=role_id,
            project_id=project_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Role.DoesNotExist:
        return error('Invalid Role ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stakeholder(stakeholder_id,name=None, role_id=None, project_id=None):
    """
    Updates a Stakeholder instance with the provided data.
    
    Args:
        stakeholder_id (int): ID of the Stakeholder to update.
        name=None, role_id=None, project_id=None: Keyword arguments for Stakeholder fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if role_id is not None and role_id != '': 
             Role.objects.get(pk=role_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Stakeholder.objects.get(pk=stakeholder_id)
        instance.name = name if name is not None else instance.name
        instance.role_id = role_id if role_id is not None else instance.role_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Role.DoesNotExist:
        return error('Invalid Role ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  Stakeholder.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stakeholder(stakeholder_id=None):
    """
    Retrieves and serializes a Stakeholder instance by its ID or all instances if ID is None.
    
    Args:
        Stakeholder_id (int, optional): ID of the Stakeholder to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stakeholder_id is not None:
            record = Stakeholder.objects.get(pk=stakeholder_id)
            serializer = StakeholderSerializer(record)
        else:
            records = Stakeholder.objects.all()
            serializer = StakeholderSerializer(records, many=True)
        return success(serializer.data)
    
    except Stakeholder.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Stakeholder does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stakeholder(stakeholder_id):
    """
    Deletes a Stakeholder instance with the given ID.
    
    Args:
        stakeholder_id (int): ID of the Stakeholder to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Stakeholder.objects.get(pk=stakeholder_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Stakeholder.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_teammember(project_id, role_id, permissions):
    """
    Creates a TeamMember instance with the provided data.
        Args:
        project_id, role_id, permissions: Keyword arguments for TeamMember fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if role_id is not None and role_id != '': 
             Role.objects.get(pk=role_id)
        instance = TeamMember.objects.create(
            project_id=project_id,
            role_id=role_id,
            permissions=permissions,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Role.DoesNotExist:
        return error('Invalid Role ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_teammember(teammember_id,project_id=None, role_id=None, permissions=None):
    """
    Updates a TeamMember instance with the provided data.
    
    Args:
        teammember_id (int): ID of the TeamMember to update.
        project_id=None, role_id=None, permissions=None: Keyword arguments for TeamMember fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if role_id is not None and role_id != '': 
             Role.objects.get(pk=role_id)
        instance = TeamMember.objects.get(pk=teammember_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.role_id = role_id if role_id is not None else instance.role_id
        instance.permissions = permissions if permissions is not None else instance.permissions
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Role.DoesNotExist:
        return error('Invalid Role ID: Destination not found.')
    except  TeamMember.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_teammember(teammember_id=None):
    """
    Retrieves and serializes a TeamMember instance by its ID or all instances if ID is None.
    
    Args:
        TeamMember_id (int, optional): ID of the TeamMember to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if teammember_id is not None:
            record = TeamMember.objects.get(pk=teammember_id)
            serializer = TeamMemberSerializer(record)
        else:
            records = TeamMember.objects.all()
            serializer = TeamMemberSerializer(records, many=True)
        return success(serializer.data)
    
    except TeamMember.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TeamMember does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_teammember(teammember_id):
    """
    Deletes a TeamMember instance with the given ID.
    
    Args:
        teammember_id (int): ID of the TeamMember to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TeamMember.objects.get(pk=teammember_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TeamMember.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_expense(project_id, account_id, vendor_id, description, amount, date, approved_by):
    """
    Creates a Expense instance with the provided data.
        Args:
        project_id, account_id, vendor_id, description, amount, date, approved_by: Keyword arguments for Expense fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if account_id is not None and account_id != '': 
             Account.objects.get(pk=account_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = Expense.objects.create(
            project_id=project_id,
            account_id=account_id,
            vendor_id=vendor_id,
            description=description,
            amount=amount,
            date=date,
            approved_by=approved_by,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Account.DoesNotExist:
        return error('Invalid Account ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_expense(expense_id,project_id=None, account_id=None, vendor_id=None, description=None, amount=None, date=None, approved_by=None):
    """
    Updates a Expense instance with the provided data.
    
    Args:
        expense_id (int): ID of the Expense to update.
        project_id=None, account_id=None, vendor_id=None, description=None, amount=None, date=None, approved_by=None: Keyword arguments for Expense fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if account_id is not None and account_id != '': 
             Account.objects.get(pk=account_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = Expense.objects.get(pk=expense_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.account_id = account_id if account_id is not None else instance.account_id
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.description = description if description is not None else instance.description
        instance.amount = amount if amount is not None else instance.amount
        instance.date = date if date is not None else instance.date
        instance.approved_by = approved_by if approved_by is not None else instance.approved_by
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Account.DoesNotExist:
        return error('Invalid Account ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  Expense.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_expense(expense_id=None):
    """
    Retrieves and serializes a Expense instance by its ID or all instances if ID is None.
    
    Args:
        Expense_id (int, optional): ID of the Expense to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if expense_id is not None:
            record = Expense.objects.get(pk=expense_id)
            serializer = ExpenseSerializer(record)
        else:
            records = Expense.objects.all()
            serializer = ExpenseSerializer(records, many=True)
        return success(serializer.data)
    
    except Expense.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Expense does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_expense(expense_id):
    """
    Deletes a Expense instance with the given ID.
    
    Args:
        expense_id (int): ID of the Expense to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Expense.objects.get(pk=expense_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Expense.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_prequalificationquestionnaire(vendor_id, project_experience, financial_status, certifications, safety_records, other_qualifications):
    """
    Creates a PrequalificationQuestionnaire instance with the provided data.
        Args:
        vendor_id, project_experience, financial_status, certifications, safety_records, other_qualifications: Keyword arguments for PrequalificationQuestionnaire fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = PrequalificationQuestionnaire.objects.create(
            vendor_id=vendor_id,
            project_experience=project_experience,
            financial_status=financial_status,
            certifications=certifications,
            safety_records=safety_records,
            other_qualifications=other_qualifications,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_prequalificationquestionnaire(prequalificationquestionnaire_id,vendor_id=None, project_experience=None, financial_status=None, certifications=None, safety_records=None, other_qualifications=None):
    """
    Updates a PrequalificationQuestionnaire instance with the provided data.
    
    Args:
        prequalificationquestionnaire_id (int): ID of the PrequalificationQuestionnaire to update.
        vendor_id=None, project_experience=None, financial_status=None, certifications=None, safety_records=None, other_qualifications=None: Keyword arguments for PrequalificationQuestionnaire fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = PrequalificationQuestionnaire.objects.get(pk=prequalificationquestionnaire_id)
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.project_experience = project_experience if project_experience is not None else instance.project_experience
        instance.financial_status = financial_status if financial_status is not None else instance.financial_status
        instance.certifications = certifications if certifications is not None else instance.certifications
        instance.safety_records = safety_records if safety_records is not None else instance.safety_records
        instance.other_qualifications = other_qualifications if other_qualifications is not None else instance.other_qualifications
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  PrequalificationQuestionnaire.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_prequalificationquestionnaire(prequalificationquestionnaire_id=None):
    """
    Retrieves and serializes a PrequalificationQuestionnaire instance by its ID or all instances if ID is None.
    
    Args:
        PrequalificationQuestionnaire_id (int, optional): ID of the PrequalificationQuestionnaire to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if prequalificationquestionnaire_id is not None:
            record = PrequalificationQuestionnaire.objects.get(pk=prequalificationquestionnaire_id)
            serializer = PrequalificationQuestionnaireSerializer(record)
        else:
            records = PrequalificationQuestionnaire.objects.all()
            serializer = PrequalificationQuestionnaireSerializer(records, many=True)
        return success(serializer.data)
    
    except PrequalificationQuestionnaire.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PrequalificationQuestionnaire does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_prequalificationquestionnaire(prequalificationquestionnaire_id):
    """
    Deletes a PrequalificationQuestionnaire instance with the given ID.
    
    Args:
        prequalificationquestionnaire_id (int): ID of the PrequalificationQuestionnaire to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PrequalificationQuestionnaire.objects.get(pk=prequalificationquestionnaire_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PrequalificationQuestionnaire.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_rfprfqdistribution(rfp_rfq_id, vendor_id, date_sent, response_submitted, submission_date):
    """
    Creates a RFPRFQDistribution instance with the provided data.
        Args:
        rfp_rfq_id, vendor_id, date_sent, response_submitted, submission_date: Keyword arguments for RFPRFQDistribution fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = RFPRFQDistribution.objects.create(
            rfp_rfq_id=rfp_rfq_id,
            vendor_id=vendor_id,
            date_sent=date_sent,
            response_submitted=response_submitted,
            submission_date=submission_date,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_rfprfqdistribution(rfprfqdistribution_id,rfp_rfq_id=None, vendor_id=None, date_sent=None, response_submitted=None, submission_date=None):
    """
    Updates a RFPRFQDistribution instance with the provided data.
    
    Args:
        rfprfqdistribution_id (int): ID of the RFPRFQDistribution to update.
        rfp_rfq_id=None, vendor_id=None, date_sent=None, response_submitted=None, submission_date=None: Keyword arguments for RFPRFQDistribution fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = RFPRFQDistribution.objects.get(pk=rfprfqdistribution_id)
        instance.rfp_rfq_id = rfp_rfq_id if rfp_rfq_id is not None else instance.rfp_rfq_id
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.date_sent = date_sent if date_sent is not None else instance.date_sent
        instance.response_submitted = response_submitted if response_submitted is not None else instance.response_submitted
        instance.submission_date = submission_date if submission_date is not None else instance.submission_date
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  RFPRFQDistribution.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_rfprfqdistribution(rfprfqdistribution_id=None):
    """
    Retrieves and serializes a RFPRFQDistribution instance by its ID or all instances if ID is None.
    
    Args:
        RFPRFQDistribution_id (int, optional): ID of the RFPRFQDistribution to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfprfqdistribution_id is not None:
            record = RFPRFQDistribution.objects.get(pk=rfprfqdistribution_id)
            serializer = RFPRFQDistributionSerializer(record)
        else:
            records = RFPRFQDistribution.objects.all()
            serializer = RFPRFQDistributionSerializer(records, many=True)
        return success(serializer.data)
    
    except RFPRFQDistribution.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('RFPRFQDistribution does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_rfprfqdistribution(rfprfqdistribution_id):
    """
    Deletes a RFPRFQDistribution instance with the given ID.
    
    Args:
        rfprfqdistribution_id (int): ID of the RFPRFQDistribution to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RFPRFQDistribution.objects.get(pk=rfprfqdistribution_id)
        instance.delete()
        return success("Successfully deleted")
    
    except RFPRFQDistribution.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_supplierperformanceevaluation(vendor_id, project, evaluation_date, delivery_timeliness, quality_of_products_services, overall_execution, comments, average_score):
    """
    Creates a SupplierPerformanceEvaluation instance with the provided data.
        Args:
        vendor_id, project, evaluation_date, delivery_timeliness, quality_of_products_services, overall_execution, comments, average_score: Keyword arguments for SupplierPerformanceEvaluation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = SupplierPerformanceEvaluation.objects.create(
            vendor_id=vendor_id,
            project=project,
            evaluation_date=evaluation_date,
            delivery_timeliness=delivery_timeliness,
            quality_of_products_services=quality_of_products_services,
            overall_execution=overall_execution,
            comments=comments,
            average_score=average_score,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_supplierperformanceevaluation(supplierperformanceevaluation_id,vendor_id=None, project=None, evaluation_date=None, delivery_timeliness=None, quality_of_products_services=None, overall_execution=None, comments=None, average_score=None):
    """
    Updates a SupplierPerformanceEvaluation instance with the provided data.
    
    Args:
        supplierperformanceevaluation_id (int): ID of the SupplierPerformanceEvaluation to update.
        vendor_id=None, project=None, evaluation_date=None, delivery_timeliness=None, quality_of_products_services=None, overall_execution=None, comments=None, average_score=None: Keyword arguments for SupplierPerformanceEvaluation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = SupplierPerformanceEvaluation.objects.get(pk=supplierperformanceevaluation_id)
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.project = project if project is not None else instance.project
        instance.evaluation_date = evaluation_date if evaluation_date is not None else instance.evaluation_date
        instance.delivery_timeliness = delivery_timeliness if delivery_timeliness is not None else instance.delivery_timeliness
        instance.quality_of_products_services = quality_of_products_services if quality_of_products_services is not None else instance.quality_of_products_services
        instance.overall_execution = overall_execution if overall_execution is not None else instance.overall_execution
        instance.comments = comments if comments is not None else instance.comments
        instance.average_score = average_score if average_score is not None else instance.average_score
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  SupplierPerformanceEvaluation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_supplierperformanceevaluation(supplierperformanceevaluation_id=None):
    """
    Retrieves and serializes a SupplierPerformanceEvaluation instance by its ID or all instances if ID is None.
    
    Args:
        SupplierPerformanceEvaluation_id (int, optional): ID of the SupplierPerformanceEvaluation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if supplierperformanceevaluation_id is not None:
            record = SupplierPerformanceEvaluation.objects.get(pk=supplierperformanceevaluation_id)
            serializer = SupplierPerformanceEvaluationSerializer(record)
        else:
            records = SupplierPerformanceEvaluation.objects.all()
            serializer = SupplierPerformanceEvaluationSerializer(records, many=True)
        return success(serializer.data)
    
    except SupplierPerformanceEvaluation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SupplierPerformanceEvaluation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_supplierperformanceevaluation(supplierperformanceevaluation_id):
    """
    Deletes a SupplierPerformanceEvaluation instance with the given ID.
    
    Args:
        supplierperformanceevaluation_id (int): ID of the SupplierPerformanceEvaluation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SupplierPerformanceEvaluation.objects.get(pk=supplierperformanceevaluation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SupplierPerformanceEvaluation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_vendorclarification(rfp_rfq_id, vendor_id, question):
    """
    Creates a VendorClarification instance with the provided data.
        Args:
        rfp_rfq_id, vendor_id, question: Keyword arguments for VendorClarification fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = VendorClarification.objects.create(
            rfp_rfq_id=rfp_rfq_id,
            vendor_id=vendor_id,
            question=question,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_vendorclarification(vendorclarification_id,rfp_rfq_id=None, vendor_id=None, question=None):
    """
    Updates a VendorClarification instance with the provided data.
    
    Args:
        vendorclarification_id (int): ID of the VendorClarification to update.
        rfp_rfq_id=None, vendor_id=None, question=None: Keyword arguments for VendorClarification fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = VendorClarification.objects.get(pk=vendorclarification_id)
        instance.rfp_rfq_id = rfp_rfq_id if rfp_rfq_id is not None else instance.rfp_rfq_id
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.question = question if question is not None else instance.question
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  VendorClarification.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_vendorclarification(vendorclarification_id=None):
    """
    Retrieves and serializes a VendorClarification instance by its ID or all instances if ID is None.
    
    Args:
        VendorClarification_id (int, optional): ID of the VendorClarification to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendorclarification_id is not None:
            record = VendorClarification.objects.get(pk=vendorclarification_id)
            serializer = VendorClarificationSerializer(record)
        else:
            records = VendorClarification.objects.all()
            serializer = VendorClarificationSerializer(records, many=True)
        return success(serializer.data)
    
    except VendorClarification.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('VendorClarification does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_vendorclarification(vendorclarification_id):
    """
    Deletes a VendorClarification instance with the given ID.
    
    Args:
        vendorclarification_id (int): ID of the VendorClarification to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = VendorClarification.objects.get(pk=vendorclarification_id)
        instance.delete()
        return success("Successfully deleted")
    
    except VendorClarification.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_vendorproposal(rfp_rfq_id, vendor_id, is_compliant, compliance_remarks):
    """
    Creates a VendorProposal instance with the provided data.
        Args:
        rfp_rfq_id, vendor_id, is_compliant, compliance_remarks: Keyword arguments for VendorProposal fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = VendorProposal.objects.create(
            rfp_rfq_id=rfp_rfq_id,
            vendor_id=vendor_id,
            is_compliant=is_compliant,
            compliance_remarks=compliance_remarks,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_vendorproposal(vendorproposal_id,rfp_rfq_id=None, vendor_id=None, is_compliant=None, compliance_remarks=None):
    """
    Updates a VendorProposal instance with the provided data.
    
    Args:
        vendorproposal_id (int): ID of the VendorProposal to update.
        rfp_rfq_id=None, vendor_id=None, is_compliant=None, compliance_remarks=None: Keyword arguments for VendorProposal fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if rfp_rfq_id is not None and rfp_rfq_id != '': 
             RFPRFQ.objects.get(pk=rfp_rfq_id)
        if vendor_id is not None and vendor_id != '': 
             Vendor.objects.get(pk=vendor_id)
        instance = VendorProposal.objects.get(pk=vendorproposal_id)
        instance.rfp_rfq_id = rfp_rfq_id if rfp_rfq_id is not None else instance.rfp_rfq_id
        instance.vendor_id = vendor_id if vendor_id is not None else instance.vendor_id
        instance.is_compliant = is_compliant if is_compliant is not None else instance.is_compliant
        instance.compliance_remarks = compliance_remarks if compliance_remarks is not None else instance.compliance_remarks
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except RFPRFQ.DoesNotExist:
        return error('Invalid RFPRFQ ID: Destination not found.')
    except Vendor.DoesNotExist:
        return error('Invalid Vendor ID: Destination not found.')
    except  VendorProposal.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_vendorproposal(vendorproposal_id=None):
    """
    Retrieves and serializes a VendorProposal instance by its ID or all instances if ID is None.
    
    Args:
        VendorProposal_id (int, optional): ID of the VendorProposal to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendorproposal_id is not None:
            record = VendorProposal.objects.get(pk=vendorproposal_id)
            serializer = VendorProposalSerializer(record)
        else:
            records = VendorProposal.objects.all()
            serializer = VendorProposalSerializer(records, many=True)
        return success(serializer.data)
    
    except VendorProposal.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('VendorProposal does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_vendorproposal(vendorproposal_id):
    """
    Deletes a VendorProposal instance with the given ID.
    
    Args:
        vendorproposal_id (int): ID of the VendorProposal to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = VendorProposal.objects.get(pk=vendorproposal_id)
        instance.delete()
        return success("Successfully deleted")
    
    except VendorProposal.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_assetaudit(asset_id, audit_date, condition, comments):
    """
    Creates a AssetAudit instance with the provided data.
        Args:
        asset_id, audit_date, condition, comments: Keyword arguments for AssetAudit fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = AssetAudit.objects.create(
            asset_id=asset_id,
            audit_date=audit_date,
            condition=condition,
            comments=comments,
        )
        return success(f'Successfully created {instance}')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_assetaudit(assetaudit_id,asset_id=None, audit_date=None, condition=None, comments=None):
    """
    Updates a AssetAudit instance with the provided data.
    
    Args:
        assetaudit_id (int): ID of the AssetAudit to update.
        asset_id=None, audit_date=None, condition=None, comments=None: Keyword arguments for AssetAudit fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = AssetAudit.objects.get(pk=assetaudit_id)
        instance.asset_id = asset_id if asset_id is not None else instance.asset_id
        instance.audit_date = audit_date if audit_date is not None else instance.audit_date
        instance.condition = condition if condition is not None else instance.condition
        instance.comments = comments if comments is not None else instance.comments
        instance.save()
        return success('Successfully Updated')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except  AssetAudit.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_assetaudit(assetaudit_id=None):
    """
    Retrieves and serializes a AssetAudit instance by its ID or all instances if ID is None.
    
    Args:
        AssetAudit_id (int, optional): ID of the AssetAudit to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if assetaudit_id is not None:
            record = AssetAudit.objects.get(pk=assetaudit_id)
            serializer = AssetAuditSerializer(record)
        else:
            records = AssetAudit.objects.all()
            serializer = AssetAuditSerializer(records, many=True)
        return success(serializer.data)
    
    except AssetAudit.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('AssetAudit does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_assetaudit(assetaudit_id):
    """
    Deletes a AssetAudit instance with the given ID.
    
    Args:
        assetaudit_id (int): ID of the AssetAudit to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AssetAudit.objects.get(pk=assetaudit_id)
        instance.delete()
        return success("Successfully deleted")
    
    except AssetAudit.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_assetmaintenance(asset_id, maintenance_date, maintenance_type, cost, notes):
    """
    Creates a AssetMaintenance instance with the provided data.
        Args:
        asset_id, maintenance_date, maintenance_type, cost, notes: Keyword arguments for AssetMaintenance fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = AssetMaintenance.objects.create(
            asset_id=asset_id,
            maintenance_date=maintenance_date,
            maintenance_type=maintenance_type,
            cost=cost,
            notes=notes,
        )
        return success(f'Successfully created {instance}')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_assetmaintenance(assetmaintenance_id,asset_id=None, maintenance_date=None, maintenance_type=None, cost=None, notes=None):
    """
    Updates a AssetMaintenance instance with the provided data.
    
    Args:
        assetmaintenance_id (int): ID of the AssetMaintenance to update.
        asset_id=None, maintenance_date=None, maintenance_type=None, cost=None, notes=None: Keyword arguments for AssetMaintenance fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = AssetMaintenance.objects.get(pk=assetmaintenance_id)
        instance.asset_id = asset_id if asset_id is not None else instance.asset_id
        instance.maintenance_date = maintenance_date if maintenance_date is not None else instance.maintenance_date
        instance.maintenance_type = maintenance_type if maintenance_type is not None else instance.maintenance_type
        instance.cost = cost if cost is not None else instance.cost
        instance.notes = notes if notes is not None else instance.notes
        instance.save()
        return success('Successfully Updated')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except  AssetMaintenance.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_assetmaintenance(assetmaintenance_id=None):
    """
    Retrieves and serializes a AssetMaintenance instance by its ID or all instances if ID is None.
    
    Args:
        AssetMaintenance_id (int, optional): ID of the AssetMaintenance to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if assetmaintenance_id is not None:
            record = AssetMaintenance.objects.get(pk=assetmaintenance_id)
            serializer = AssetMaintenanceSerializer(record)
        else:
            records = AssetMaintenance.objects.all()
            serializer = AssetMaintenanceSerializer(records, many=True)
        return success(serializer.data)
    
    except AssetMaintenance.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('AssetMaintenance does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_assetmaintenance(assetmaintenance_id):
    """
    Deletes a AssetMaintenance instance with the given ID.
    
    Args:
        assetmaintenance_id (int): ID of the AssetMaintenance to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AssetMaintenance.objects.get(pk=assetmaintenance_id)
        instance.delete()
        return success("Successfully deleted")
    
    except AssetMaintenance.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_depreciation(asset_id, depreciation_date, amount):
    """
    Creates a Depreciation instance with the provided data.
        Args:
        asset_id, depreciation_date, amount: Keyword arguments for Depreciation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = Depreciation.objects.create(
            asset_id=asset_id,
            depreciation_date=depreciation_date,
            amount=amount,
        )
        return success(f'Successfully created {instance}')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_depreciation(depreciation_id,asset_id=None, depreciation_date=None, amount=None):
    """
    Updates a Depreciation instance with the provided data.
    
    Args:
        depreciation_id (int): ID of the Depreciation to update.
        asset_id=None, depreciation_date=None, amount=None: Keyword arguments for Depreciation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if asset_id is not None and asset_id != '': 
             Asset.objects.get(pk=asset_id)
        instance = Depreciation.objects.get(pk=depreciation_id)
        instance.asset_id = asset_id if asset_id is not None else instance.asset_id
        instance.depreciation_date = depreciation_date if depreciation_date is not None else instance.depreciation_date
        instance.amount = amount if amount is not None else instance.amount
        instance.save()
        return success('Successfully Updated')
    except Asset.DoesNotExist:
        return error('Invalid Asset ID: Destination not found.')
    except  Depreciation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_depreciation(depreciation_id=None):
    """
    Retrieves and serializes a Depreciation instance by its ID or all instances if ID is None.
    
    Args:
        Depreciation_id (int, optional): ID of the Depreciation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if depreciation_id is not None:
            record = Depreciation.objects.get(pk=depreciation_id)
            serializer = DepreciationSerializer(record)
        else:
            records = Depreciation.objects.all()
            serializer = DepreciationSerializer(records, many=True)
        return success(serializer.data)
    
    except Depreciation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Depreciation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_depreciation(depreciation_id):
    """
    Deletes a Depreciation instance with the given ID.
    
    Args:
        depreciation_id (int): ID of the Depreciation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Depreciation.objects.get(pk=depreciation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Depreciation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_submissionfollowup(proposal_id, submission_date, follow_up_date, follow_up_notes, negotiation_engaged, revisions_required):
    """
    Creates a SubmissionFollowUp instance with the provided data.
        Args:
        proposal_id, submission_date, follow_up_date, follow_up_notes, negotiation_engaged, revisions_required: Keyword arguments for SubmissionFollowUp fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             ProposalPreparation.objects.get(pk=proposal_id)
        instance = SubmissionFollowUp.objects.create(
            proposal_id=proposal_id,
            submission_date=submission_date,
            follow_up_date=follow_up_date,
            follow_up_notes=follow_up_notes,
            negotiation_engaged=negotiation_engaged,
            revisions_required=revisions_required,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ProposalPreparation.DoesNotExist:
        return error('Invalid ProposalPreparation ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_submissionfollowup(submissionfollowup_id,proposal_id=None, submission_date=None, follow_up_date=None, follow_up_notes=None, negotiation_engaged=None, revisions_required=None):
    """
    Updates a SubmissionFollowUp instance with the provided data.
    
    Args:
        submissionfollowup_id (int): ID of the SubmissionFollowUp to update.
        proposal_id=None, submission_date=None, follow_up_date=None, follow_up_notes=None, negotiation_engaged=None, revisions_required=None: Keyword arguments for SubmissionFollowUp fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             ProposalPreparation.objects.get(pk=proposal_id)
        instance = SubmissionFollowUp.objects.get(pk=submissionfollowup_id)
        instance.proposal_id = proposal_id if proposal_id is not None else instance.proposal_id
        instance.submission_date = submission_date if submission_date is not None else instance.submission_date
        instance.follow_up_date = follow_up_date if follow_up_date is not None else instance.follow_up_date
        instance.follow_up_notes = follow_up_notes if follow_up_notes is not None else instance.follow_up_notes
        instance.negotiation_engaged = negotiation_engaged if negotiation_engaged is not None else instance.negotiation_engaged
        instance.revisions_required = revisions_required if revisions_required is not None else instance.revisions_required
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except ProposalPreparation.DoesNotExist:
        return error('Invalid ProposalPreparation ID: Destination not found.')
    except  SubmissionFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_submissionfollowup(submissionfollowup_id=None):
    """
    Retrieves and serializes a SubmissionFollowUp instance by its ID or all instances if ID is None.
    
    Args:
        SubmissionFollowUp_id (int, optional): ID of the SubmissionFollowUp to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if submissionfollowup_id is not None:
            record = SubmissionFollowUp.objects.get(pk=submissionfollowup_id)
            serializer = SubmissionFollowUpSerializer(record)
        else:
            records = SubmissionFollowUp.objects.all()
            serializer = SubmissionFollowUpSerializer(records, many=True)
        return success(serializer.data)
    
    except SubmissionFollowUp.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('SubmissionFollowUp does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_submissionfollowup(submissionfollowup_id):
    """
    Deletes a SubmissionFollowUp instance with the given ID.
    
    Args:
        submissionfollowup_id (int): ID of the SubmissionFollowUp to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = SubmissionFollowUp.objects.get(pk=submissionfollowup_id)
        instance.delete()
        return success("Successfully deleted")
    
    except SubmissionFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_negotiationandaward(bid_submission_id, negotiation_date, negotiation_notes, final_terms, awarded, internal_preparation_started):
    """
    Creates a NegotiationAndAward instance with the provided data.
        Args:
        bid_submission_id, negotiation_date, negotiation_notes, final_terms, awarded, internal_preparation_started: Keyword arguments for NegotiationAndAward fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_submission_id is not None and bid_submission_id != '': 
             BidSubmission.objects.get(pk=bid_submission_id)
        instance = NegotiationAndAward.objects.create(
            bid_submission_id=bid_submission_id,
            negotiation_date=negotiation_date,
            negotiation_notes=negotiation_notes,
            final_terms=final_terms,
            awarded=awarded,
            internal_preparation_started=internal_preparation_started,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except BidSubmission.DoesNotExist:
        return error('Invalid BidSubmission ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_negotiationandaward(negotiationandaward_id,bid_submission_id=None, negotiation_date=None, negotiation_notes=None, final_terms=None, awarded=None, internal_preparation_started=None):
    """
    Updates a NegotiationAndAward instance with the provided data.
    
    Args:
        negotiationandaward_id (int): ID of the NegotiationAndAward to update.
        bid_submission_id=None, negotiation_date=None, negotiation_notes=None, final_terms=None, awarded=None, internal_preparation_started=None: Keyword arguments for NegotiationAndAward fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_submission_id is not None and bid_submission_id != '': 
             BidSubmission.objects.get(pk=bid_submission_id)
        instance = NegotiationAndAward.objects.get(pk=negotiationandaward_id)
        instance.bid_submission_id = bid_submission_id if bid_submission_id is not None else instance.bid_submission_id
        instance.negotiation_date = negotiation_date if negotiation_date is not None else instance.negotiation_date
        instance.negotiation_notes = negotiation_notes if negotiation_notes is not None else instance.negotiation_notes
        instance.final_terms = final_terms if final_terms is not None else instance.final_terms
        instance.awarded = awarded if awarded is not None else instance.awarded
        instance.internal_preparation_started = internal_preparation_started if internal_preparation_started is not None else instance.internal_preparation_started
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except BidSubmission.DoesNotExist:
        return error('Invalid BidSubmission ID: Destination not found.')
    except  NegotiationAndAward.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_negotiationandaward(negotiationandaward_id=None):
    """
    Retrieves and serializes a NegotiationAndAward instance by its ID or all instances if ID is None.
    
    Args:
        NegotiationAndAward_id (int, optional): ID of the NegotiationAndAward to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if negotiationandaward_id is not None:
            record = NegotiationAndAward.objects.get(pk=negotiationandaward_id)
            serializer = NegotiationAndAwardSerializer(record)
        else:
            records = NegotiationAndAward.objects.all()
            serializer = NegotiationAndAwardSerializer(records, many=True)
        return success(serializer.data)
    
    except NegotiationAndAward.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('NegotiationAndAward does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_negotiationandaward(negotiationandaward_id):
    """
    Deletes a NegotiationAndAward instance with the given ID.
    
    Args:
        negotiationandaward_id (int): ID of the NegotiationAndAward to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = NegotiationAndAward.objects.get(pk=negotiationandaward_id)
        instance.delete()
        return success("Successfully deleted")
    
    except NegotiationAndAward.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_postsubmissionfollowup(bid_submission_id, follow_up_date, communication_method, client_response, clarification_requested, additional_info_provided):
    """
    Creates a PostSubmissionFollowUp instance with the provided data.
        Args:
        bid_submission_id, follow_up_date, communication_method, client_response, clarification_requested, additional_info_provided: Keyword arguments for PostSubmissionFollowUp fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_submission_id is not None and bid_submission_id != '': 
             BidSubmission.objects.get(pk=bid_submission_id)
        instance = PostSubmissionFollowUp.objects.create(
            bid_submission_id=bid_submission_id,
            follow_up_date=follow_up_date,
            communication_method=communication_method,
            client_response=client_response,
            clarification_requested=clarification_requested,
            additional_info_provided=additional_info_provided,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except BidSubmission.DoesNotExist:
        return error('Invalid BidSubmission ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_postsubmissionfollowup(postsubmissionfollowup_id,bid_submission_id=None, follow_up_date=None, communication_method=None, client_response=None, clarification_requested=None, additional_info_provided=None):
    """
    Updates a PostSubmissionFollowUp instance with the provided data.
    
    Args:
        postsubmissionfollowup_id (int): ID of the PostSubmissionFollowUp to update.
        bid_submission_id=None, follow_up_date=None, communication_method=None, client_response=None, clarification_requested=None, additional_info_provided=None: Keyword arguments for PostSubmissionFollowUp fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bid_submission_id is not None and bid_submission_id != '': 
             BidSubmission.objects.get(pk=bid_submission_id)
        instance = PostSubmissionFollowUp.objects.get(pk=postsubmissionfollowup_id)
        instance.bid_submission_id = bid_submission_id if bid_submission_id is not None else instance.bid_submission_id
        instance.follow_up_date = follow_up_date if follow_up_date is not None else instance.follow_up_date
        instance.communication_method = communication_method if communication_method is not None else instance.communication_method
        instance.client_response = client_response if client_response is not None else instance.client_response
        instance.clarification_requested = clarification_requested if clarification_requested is not None else instance.clarification_requested
        instance.additional_info_provided = additional_info_provided if additional_info_provided is not None else instance.additional_info_provided
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except BidSubmission.DoesNotExist:
        return error('Invalid BidSubmission ID: Destination not found.')
    except  PostSubmissionFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_postsubmissionfollowup(postsubmissionfollowup_id=None):
    """
    Retrieves and serializes a PostSubmissionFollowUp instance by its ID or all instances if ID is None.
    
    Args:
        PostSubmissionFollowUp_id (int, optional): ID of the PostSubmissionFollowUp to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if postsubmissionfollowup_id is not None:
            record = PostSubmissionFollowUp.objects.get(pk=postsubmissionfollowup_id)
            serializer = PostSubmissionFollowUpSerializer(record)
        else:
            records = PostSubmissionFollowUp.objects.all()
            serializer = PostSubmissionFollowUpSerializer(records, many=True)
        return success(serializer.data)
    
    except PostSubmissionFollowUp.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PostSubmissionFollowUp does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_postsubmissionfollowup(postsubmissionfollowup_id):
    """
    Deletes a PostSubmissionFollowUp instance with the given ID.
    
    Args:
        postsubmissionfollowup_id (int): ID of the PostSubmissionFollowUp to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PostSubmissionFollowUp.objects.get(pk=postsubmissionfollowup_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PostSubmissionFollowUp.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_equipmentassignment(equipment_id, assigned_to, assigned_date, return_date):
    """
    Creates a EquipmentAssignment instance with the provided data.
        Args:
        equipment_id, assigned_to, assigned_date, return_date: Keyword arguments for EquipmentAssignment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentAssignment.objects.create(
            equipment_id=equipment_id,
            assigned_to=assigned_to,
            assigned_date=assigned_date,
            return_date=return_date,
        )
        return success(f'Successfully created {instance}')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_equipmentassignment(equipmentassignment_id,equipment_id=None, assigned_to=None, assigned_date=None, return_date=None):
    """
    Updates a EquipmentAssignment instance with the provided data.
    
    Args:
        equipmentassignment_id (int): ID of the EquipmentAssignment to update.
        equipment_id=None, assigned_to=None, assigned_date=None, return_date=None: Keyword arguments for EquipmentAssignment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentAssignment.objects.get(pk=equipmentassignment_id)
        instance.equipment_id = equipment_id if equipment_id is not None else instance.equipment_id
        instance.assigned_to = assigned_to if assigned_to is not None else instance.assigned_to
        instance.assigned_date = assigned_date if assigned_date is not None else instance.assigned_date
        instance.return_date = return_date if return_date is not None else instance.return_date
        instance.save()
        return success('Successfully Updated')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except  EquipmentAssignment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_equipmentassignment(equipmentassignment_id=None):
    """
    Retrieves and serializes a EquipmentAssignment instance by its ID or all instances if ID is None.
    
    Args:
        EquipmentAssignment_id (int, optional): ID of the EquipmentAssignment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipmentassignment_id is not None:
            record = EquipmentAssignment.objects.get(pk=equipmentassignment_id)
            serializer = EquipmentAssignmentSerializer(record)
        else:
            records = EquipmentAssignment.objects.all()
            serializer = EquipmentAssignmentSerializer(records, many=True)
        return success(serializer.data)
    
    except EquipmentAssignment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('EquipmentAssignment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_equipmentassignment(equipmentassignment_id):
    """
    Deletes a EquipmentAssignment instance with the given ID.
    
    Args:
        equipmentassignment_id (int): ID of the EquipmentAssignment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentAssignment.objects.get(pk=equipmentassignment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except EquipmentAssignment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_equipmentaudit(equipment_id, audit_date, condition, comments):
    """
    Creates a EquipmentAudit instance with the provided data.
        Args:
        equipment_id, audit_date, condition, comments: Keyword arguments for EquipmentAudit fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentAudit.objects.create(
            equipment_id=equipment_id,
            audit_date=audit_date,
            condition=condition,
            comments=comments,
        )
        return success(f'Successfully created {instance}')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_equipmentaudit(equipmentaudit_id,equipment_id=None, audit_date=None, condition=None, comments=None):
    """
    Updates a EquipmentAudit instance with the provided data.
    
    Args:
        equipmentaudit_id (int): ID of the EquipmentAudit to update.
        equipment_id=None, audit_date=None, condition=None, comments=None: Keyword arguments for EquipmentAudit fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentAudit.objects.get(pk=equipmentaudit_id)
        instance.equipment_id = equipment_id if equipment_id is not None else instance.equipment_id
        instance.audit_date = audit_date if audit_date is not None else instance.audit_date
        instance.condition = condition if condition is not None else instance.condition
        instance.comments = comments if comments is not None else instance.comments
        instance.save()
        return success('Successfully Updated')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except  EquipmentAudit.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_equipmentaudit(equipmentaudit_id=None):
    """
    Retrieves and serializes a EquipmentAudit instance by its ID or all instances if ID is None.
    
    Args:
        EquipmentAudit_id (int, optional): ID of the EquipmentAudit to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipmentaudit_id is not None:
            record = EquipmentAudit.objects.get(pk=equipmentaudit_id)
            serializer = EquipmentAuditSerializer(record)
        else:
            records = EquipmentAudit.objects.all()
            serializer = EquipmentAuditSerializer(records, many=True)
        return success(serializer.data)
    
    except EquipmentAudit.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('EquipmentAudit does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_equipmentaudit(equipmentaudit_id):
    """
    Deletes a EquipmentAudit instance with the given ID.
    
    Args:
        equipmentaudit_id (int): ID of the EquipmentAudit to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentAudit.objects.get(pk=equipmentaudit_id)
        instance.delete()
        return success("Successfully deleted")
    
    except EquipmentAudit.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_equipmentmaintenance(equipment_id, maintenance_date, maintenance_type, cost, notes):
    """
    Creates a EquipmentMaintenance instance with the provided data.
        Args:
        equipment_id, maintenance_date, maintenance_type, cost, notes: Keyword arguments for EquipmentMaintenance fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentMaintenance.objects.create(
            equipment_id=equipment_id,
            maintenance_date=maintenance_date,
            maintenance_type=maintenance_type,
            cost=cost,
            notes=notes,
        )
        return success(f'Successfully created {instance}')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_equipmentmaintenance(equipmentmaintenance_id,equipment_id=None, maintenance_date=None, maintenance_type=None, cost=None, notes=None):
    """
    Updates a EquipmentMaintenance instance with the provided data.
    
    Args:
        equipmentmaintenance_id (int): ID of the EquipmentMaintenance to update.
        equipment_id=None, maintenance_date=None, maintenance_type=None, cost=None, notes=None: Keyword arguments for EquipmentMaintenance fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipment_id is not None and equipment_id != '': 
             Equipment.objects.get(pk=equipment_id)
        instance = EquipmentMaintenance.objects.get(pk=equipmentmaintenance_id)
        instance.equipment_id = equipment_id if equipment_id is not None else instance.equipment_id
        instance.maintenance_date = maintenance_date if maintenance_date is not None else instance.maintenance_date
        instance.maintenance_type = maintenance_type if maintenance_type is not None else instance.maintenance_type
        instance.cost = cost if cost is not None else instance.cost
        instance.notes = notes if notes is not None else instance.notes
        instance.save()
        return success('Successfully Updated')
    except Equipment.DoesNotExist:
        return error('Invalid Equipment ID: Destination not found.')
    except  EquipmentMaintenance.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_equipmentmaintenance(equipmentmaintenance_id=None):
    """
    Retrieves and serializes a EquipmentMaintenance instance by its ID or all instances if ID is None.
    
    Args:
        EquipmentMaintenance_id (int, optional): ID of the EquipmentMaintenance to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if equipmentmaintenance_id is not None:
            record = EquipmentMaintenance.objects.get(pk=equipmentmaintenance_id)
            serializer = EquipmentMaintenanceSerializer(record)
        else:
            records = EquipmentMaintenance.objects.all()
            serializer = EquipmentMaintenanceSerializer(records, many=True)
        return success(serializer.data)
    
    except EquipmentMaintenance.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('EquipmentMaintenance does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_equipmentmaintenance(equipmentmaintenance_id):
    """
    Deletes a EquipmentMaintenance instance with the given ID.
    
    Args:
        equipmentmaintenance_id (int): ID of the EquipmentMaintenance to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = EquipmentMaintenance.objects.get(pk=equipmentmaintenance_id)
        instance.delete()
        return success("Successfully deleted")
    
    except EquipmentMaintenance.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_inventoryaudit(item_id, audit_date, physical_count, system_count, discrepancy, comments):
    """
    Creates a InventoryAudit instance with the provided data.
        Args:
        item_id, audit_date, physical_count, system_count, discrepancy, comments: Keyword arguments for InventoryAudit fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = InventoryAudit.objects.create(
            item_id=item_id,
            audit_date=audit_date,
            physical_count=physical_count,
            system_count=system_count,
            discrepancy=discrepancy,
            comments=comments,
        )
        return success(f'Successfully created {instance}')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_inventoryaudit(inventoryaudit_id,item_id=None, audit_date=None, physical_count=None, system_count=None, discrepancy=None, comments=None):
    """
    Updates a InventoryAudit instance with the provided data.
    
    Args:
        inventoryaudit_id (int): ID of the InventoryAudit to update.
        item_id=None, audit_date=None, physical_count=None, system_count=None, discrepancy=None, comments=None: Keyword arguments for InventoryAudit fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = InventoryAudit.objects.get(pk=inventoryaudit_id)
        instance.item_id = item_id if item_id is not None else instance.item_id
        instance.audit_date = audit_date if audit_date is not None else instance.audit_date
        instance.physical_count = physical_count if physical_count is not None else instance.physical_count
        instance.system_count = system_count if system_count is not None else instance.system_count
        instance.discrepancy = discrepancy if discrepancy is not None else instance.discrepancy
        instance.comments = comments if comments is not None else instance.comments
        instance.save()
        return success('Successfully Updated')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except  InventoryAudit.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_inventoryaudit(inventoryaudit_id=None):
    """
    Retrieves and serializes a InventoryAudit instance by its ID or all instances if ID is None.
    
    Args:
        InventoryAudit_id (int, optional): ID of the InventoryAudit to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if inventoryaudit_id is not None:
            record = InventoryAudit.objects.get(pk=inventoryaudit_id)
            serializer = InventoryAuditSerializer(record)
        else:
            records = InventoryAudit.objects.all()
            serializer = InventoryAuditSerializer(records, many=True)
        return success(serializer.data)
    
    except InventoryAudit.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('InventoryAudit does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_inventoryaudit(inventoryaudit_id):
    """
    Deletes a InventoryAudit instance with the given ID.
    
    Args:
        inventoryaudit_id (int): ID of the InventoryAudit to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = InventoryAudit.objects.get(pk=inventoryaudit_id)
        instance.delete()
        return success("Successfully deleted")
    
    except InventoryAudit.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_requisition(item_id, quantity, requested_by, date_requested, date_fulfilled):
    """
    Creates a Requisition instance with the provided data.
        Args:
        item_id, quantity, requested_by, date_requested, date_fulfilled: Keyword arguments for Requisition fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = Requisition.objects.create(
            item_id=item_id,
            quantity=quantity,
            requested_by=requested_by,
            date_requested=date_requested,
            date_fulfilled=date_fulfilled,
        )
        return success(f'Successfully created {instance}')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_requisition(requisition_id,item_id=None, quantity=None, requested_by=None, date_requested=None, date_fulfilled=None):
    """
    Updates a Requisition instance with the provided data.
    
    Args:
        requisition_id (int): ID of the Requisition to update.
        item_id=None, quantity=None, requested_by=None, date_requested=None, date_fulfilled=None: Keyword arguments for Requisition fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = Requisition.objects.get(pk=requisition_id)
        instance.item_id = item_id if item_id is not None else instance.item_id
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.requested_by = requested_by if requested_by is not None else instance.requested_by
        instance.date_requested = date_requested if date_requested is not None else instance.date_requested
        instance.date_fulfilled = date_fulfilled if date_fulfilled is not None else instance.date_fulfilled
        instance.save()
        return success('Successfully Updated')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except  Requisition.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_requisition(requisition_id=None):
    """
    Retrieves and serializes a Requisition instance by its ID or all instances if ID is None.
    
    Args:
        Requisition_id (int, optional): ID of the Requisition to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if requisition_id is not None:
            record = Requisition.objects.get(pk=requisition_id)
            serializer = RequisitionSerializer(record)
        else:
            records = Requisition.objects.all()
            serializer = RequisitionSerializer(records, many=True)
        return success(serializer.data)
    
    except Requisition.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Requisition does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_requisition(requisition_id):
    """
    Deletes a Requisition instance with the given ID.
    
    Args:
        requisition_id (int): ID of the Requisition to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Requisition.objects.get(pk=requisition_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Requisition.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stockentry(item_id, quantity, movement_type, date):
    """
    Creates a StockEntry instance with the provided data.
        Args:
        item_id, quantity, movement_type, date: Keyword arguments for StockEntry fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = StockEntry.objects.create(
            item_id=item_id,
            quantity=quantity,
            movement_type=movement_type,
            date=date,
        )
        return success(f'Successfully created {instance}')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stockentry(stockentry_id,item_id=None, quantity=None, movement_type=None, date=None):
    """
    Updates a StockEntry instance with the provided data.
    
    Args:
        stockentry_id (int): ID of the StockEntry to update.
        item_id=None, quantity=None, movement_type=None, date=None: Keyword arguments for StockEntry fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if item_id is not None and item_id != '': 
             Item.objects.get(pk=item_id)
        instance = StockEntry.objects.get(pk=stockentry_id)
        instance.item_id = item_id if item_id is not None else instance.item_id
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.movement_type = movement_type if movement_type is not None else instance.movement_type
        instance.date = date if date is not None else instance.date
        instance.save()
        return success('Successfully Updated')
    except Item.DoesNotExist:
        return error('Invalid Item ID: Destination not found.')
    except  StockEntry.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stockentry(stockentry_id=None):
    """
    Retrieves and serializes a StockEntry instance by its ID or all instances if ID is None.
    
    Args:
        StockEntry_id (int, optional): ID of the StockEntry to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stockentry_id is not None:
            record = StockEntry.objects.get(pk=stockentry_id)
            serializer = StockEntrySerializer(record)
        else:
            records = StockEntry.objects.all()
            serializer = StockEntrySerializer(records, many=True)
        return success(serializer.data)
    
    except StockEntry.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('StockEntry does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stockentry(stockentry_id):
    """
    Deletes a StockEntry instance with the given ID.
    
    Args:
        stockentry_id (int): ID of the StockEntry to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = StockEntry.objects.get(pk=stockentry_id)
        instance.delete()
        return success("Successfully deleted")
    
    except StockEntry.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientinteraction(lead_id, interaction_type_id, description, follow_up_date):
    """
    Creates a ClientInteraction instance with the provided data.
        Args:
        lead_id, interaction_type_id, description, follow_up_date: Keyword arguments for ClientInteraction fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if lead_id is not None and lead_id != '': 
             Lead.objects.get(pk=lead_id)
        if interaction_type_id is not None and interaction_type_id != '': 
             ClientInteractionType.objects.get(pk=interaction_type_id)
        instance = ClientInteraction.objects.create(
            lead_id=lead_id,
            interaction_type_id=interaction_type_id,
            description=description,
            follow_up_date=follow_up_date,
        )
        return success(f'Successfully created {instance}')
    except Lead.DoesNotExist:
        return error('Invalid Lead ID: Destination not found.')
    except ClientInteractionType.DoesNotExist:
        return error('Invalid ClientInteractionType ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientinteraction(clientinteraction_id,lead_id=None, interaction_type_id=None, description=None, follow_up_date=None):
    """
    Updates a ClientInteraction instance with the provided data.
    
    Args:
        clientinteraction_id (int): ID of the ClientInteraction to update.
        lead_id=None, interaction_type_id=None, description=None, follow_up_date=None: Keyword arguments for ClientInteraction fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if lead_id is not None and lead_id != '': 
             Lead.objects.get(pk=lead_id)
        if interaction_type_id is not None and interaction_type_id != '': 
             ClientInteractionType.objects.get(pk=interaction_type_id)
        instance = ClientInteraction.objects.get(pk=clientinteraction_id)
        instance.lead_id = lead_id if lead_id is not None else instance.lead_id
        instance.interaction_type_id = interaction_type_id if interaction_type_id is not None else instance.interaction_type_id
        instance.description = description if description is not None else instance.description
        instance.follow_up_date = follow_up_date if follow_up_date is not None else instance.follow_up_date
        instance.save()
        return success('Successfully Updated')
    except Lead.DoesNotExist:
        return error('Invalid Lead ID: Destination not found.')
    except ClientInteractionType.DoesNotExist:
        return error('Invalid ClientInteractionType ID: Destination not found.')
    except  ClientInteraction.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientinteraction(clientinteraction_id=None):
    """
    Retrieves and serializes a ClientInteraction instance by its ID or all instances if ID is None.
    
    Args:
        ClientInteraction_id (int, optional): ID of the ClientInteraction to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientinteraction_id is not None:
            record = ClientInteraction.objects.get(pk=clientinteraction_id)
            serializer = ClientInteractionSerializer(record)
        else:
            records = ClientInteraction.objects.all()
            serializer = ClientInteractionSerializer(records, many=True)
        return success(serializer.data)
    
    except ClientInteraction.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientInteraction does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientinteraction(clientinteraction_id):
    """
    Deletes a ClientInteraction instance with the given ID.
    
    Args:
        clientinteraction_id (int): ID of the ClientInteraction to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientInteraction.objects.get(pk=clientinteraction_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientInteraction.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_opportunity(lead_id, stage_id, amount, probability, expected_close_date, assigned_to_id):
    """
    Creates a Opportunity instance with the provided data.
        Args:
        lead_id, stage_id, amount, probability, expected_close_date, assigned_to_id: Keyword arguments for Opportunity fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if lead_id is not None and lead_id != '': 
             Lead.objects.get(pk=lead_id)
        if stage_id is not None and stage_id != '': 
             SalesStage.objects.get(pk=stage_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             SalesRepresentative.objects.get(pk=assigned_to_id)
        instance = Opportunity.objects.create(
            lead_id=lead_id,
            stage_id=stage_id,
            amount=amount,
            probability=probability,
            expected_close_date=expected_close_date,
            assigned_to_id=assigned_to_id,
        )
        return success(f'Successfully created {instance}')
    except Lead.DoesNotExist:
        return error('Invalid Lead ID: Destination not found.')
    except SalesStage.DoesNotExist:
        return error('Invalid SalesStage ID: Destination not found.')
    except SalesRepresentative.DoesNotExist:
        return error('Invalid SalesRepresentative ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_opportunity(opportunity_id,lead_id=None, stage_id=None, amount=None, probability=None, expected_close_date=None, assigned_to_id=None):
    """
    Updates a Opportunity instance with the provided data.
    
    Args:
        opportunity_id (int): ID of the Opportunity to update.
        lead_id=None, stage_id=None, amount=None, probability=None, expected_close_date=None, assigned_to_id=None: Keyword arguments for Opportunity fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if lead_id is not None and lead_id != '': 
             Lead.objects.get(pk=lead_id)
        if stage_id is not None and stage_id != '': 
             SalesStage.objects.get(pk=stage_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             SalesRepresentative.objects.get(pk=assigned_to_id)
        instance = Opportunity.objects.get(pk=opportunity_id)
        instance.lead_id = lead_id if lead_id is not None else instance.lead_id
        instance.stage_id = stage_id if stage_id is not None else instance.stage_id
        instance.amount = amount if amount is not None else instance.amount
        instance.probability = probability if probability is not None else instance.probability
        instance.expected_close_date = expected_close_date if expected_close_date is not None else instance.expected_close_date
        instance.assigned_to_id = assigned_to_id if assigned_to_id is not None else instance.assigned_to_id
        instance.save()
        return success('Successfully Updated')
    except Lead.DoesNotExist:
        return error('Invalid Lead ID: Destination not found.')
    except SalesStage.DoesNotExist:
        return error('Invalid SalesStage ID: Destination not found.')
    except SalesRepresentative.DoesNotExist:
        return error('Invalid SalesRepresentative ID: Destination not found.')
    except  Opportunity.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_opportunity(opportunity_id=None):
    """
    Retrieves and serializes a Opportunity instance by its ID or all instances if ID is None.
    
    Args:
        Opportunity_id (int, optional): ID of the Opportunity to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None:
            record = Opportunity.objects.get(pk=opportunity_id)
            serializer = OpportunitySerializer(record)
        else:
            records = Opportunity.objects.all()
            serializer = OpportunitySerializer(records, many=True)
        return success(serializer.data)
    
    except Opportunity.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Opportunity does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_opportunity(opportunity_id):
    """
    Deletes a Opportunity instance with the given ID.
    
    Args:
        opportunity_id (int): ID of the Opportunity to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Opportunity.objects.get(pk=opportunity_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Opportunity.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_documentedrequirement(procurement_need_id, requirement_description, quantity, timeline, budget_estimate, technical_specifications, quality_specifications):
    """
    Creates a DocumentedRequirement instance with the provided data.
        Args:
        procurement_need_id, requirement_description, quantity, timeline, budget_estimate, technical_specifications, quality_specifications: Keyword arguments for DocumentedRequirement fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if procurement_need_id is not None and procurement_need_id != '': 
             ProcurementNeed.objects.get(pk=procurement_need_id)
        instance = DocumentedRequirement.objects.create(
            procurement_need_id=procurement_need_id,
            requirement_description=requirement_description,
            quantity=quantity,
            timeline=timeline,
            budget_estimate=budget_estimate,
            technical_specifications=technical_specifications,
            quality_specifications=quality_specifications,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ProcurementNeed.DoesNotExist:
        return error('Invalid ProcurementNeed ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_documentedrequirement(documentedrequirement_id,procurement_need_id=None, requirement_description=None, quantity=None, timeline=None, budget_estimate=None, technical_specifications=None, quality_specifications=None):
    """
    Updates a DocumentedRequirement instance with the provided data.
    
    Args:
        documentedrequirement_id (int): ID of the DocumentedRequirement to update.
        procurement_need_id=None, requirement_description=None, quantity=None, timeline=None, budget_estimate=None, technical_specifications=None, quality_specifications=None: Keyword arguments for DocumentedRequirement fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if procurement_need_id is not None and procurement_need_id != '': 
             ProcurementNeed.objects.get(pk=procurement_need_id)
        instance = DocumentedRequirement.objects.get(pk=documentedrequirement_id)
        instance.procurement_need_id = procurement_need_id if procurement_need_id is not None else instance.procurement_need_id
        instance.requirement_description = requirement_description if requirement_description is not None else instance.requirement_description
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.timeline = timeline if timeline is not None else instance.timeline
        instance.budget_estimate = budget_estimate if budget_estimate is not None else instance.budget_estimate
        instance.technical_specifications = technical_specifications if technical_specifications is not None else instance.technical_specifications
        instance.quality_specifications = quality_specifications if quality_specifications is not None else instance.quality_specifications
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except ProcurementNeed.DoesNotExist:
        return error('Invalid ProcurementNeed ID: Destination not found.')
    except  DocumentedRequirement.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_documentedrequirement(documentedrequirement_id=None):
    """
    Retrieves and serializes a DocumentedRequirement instance by its ID or all instances if ID is None.
    
    Args:
        DocumentedRequirement_id (int, optional): ID of the DocumentedRequirement to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if documentedrequirement_id is not None:
            record = DocumentedRequirement.objects.get(pk=documentedrequirement_id)
            serializer = DocumentedRequirementSerializer(record)
        else:
            records = DocumentedRequirement.objects.all()
            serializer = DocumentedRequirementSerializer(records, many=True)
        return success(serializer.data)
    
    except DocumentedRequirement.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('DocumentedRequirement does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_documentedrequirement(documentedrequirement_id):
    """
    Deletes a DocumentedRequirement instance with the given ID.
    
    Args:
        documentedrequirement_id (int): ID of the DocumentedRequirement to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DocumentedRequirement.objects.get(pk=documentedrequirement_id)
        instance.delete()
        return success("Successfully deleted")
    
    except DocumentedRequirement.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_correctivepreventiveaction(audit_id, description, date_taken, status):
    """
    Creates a CorrectivePreventiveAction instance with the provided data.
        Args:
        audit_id, description, date_taken, status: Keyword arguments for CorrectivePreventiveAction fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if audit_id is not None and audit_id != '': 
             Audit.objects.get(pk=audit_id)
        instance = CorrectivePreventiveAction.objects.create(
            audit_id=audit_id,
            description=description,
            date_taken=date_taken,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except Audit.DoesNotExist:
        return error('Invalid Audit ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_correctivepreventiveaction(correctivepreventiveaction_id,audit_id=None, description=None, date_taken=None, status=None):
    """
    Updates a CorrectivePreventiveAction instance with the provided data.
    
    Args:
        correctivepreventiveaction_id (int): ID of the CorrectivePreventiveAction to update.
        audit_id=None, description=None, date_taken=None, status=None: Keyword arguments for CorrectivePreventiveAction fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if audit_id is not None and audit_id != '': 
             Audit.objects.get(pk=audit_id)
        instance = CorrectivePreventiveAction.objects.get(pk=correctivepreventiveaction_id)
        instance.audit_id = audit_id if audit_id is not None else instance.audit_id
        instance.description = description if description is not None else instance.description
        instance.date_taken = date_taken if date_taken is not None else instance.date_taken
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except Audit.DoesNotExist:
        return error('Invalid Audit ID: Destination not found.')
    except  CorrectivePreventiveAction.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_correctivepreventiveaction(correctivepreventiveaction_id=None):
    """
    Retrieves and serializes a CorrectivePreventiveAction instance by its ID or all instances if ID is None.
    
    Args:
        CorrectivePreventiveAction_id (int, optional): ID of the CorrectivePreventiveAction to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if correctivepreventiveaction_id is not None:
            record = CorrectivePreventiveAction.objects.get(pk=correctivepreventiveaction_id)
            serializer = CorrectivePreventiveActionSerializer(record)
        else:
            records = CorrectivePreventiveAction.objects.all()
            serializer = CorrectivePreventiveActionSerializer(records, many=True)
        return success(serializer.data)
    
    except CorrectivePreventiveAction.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CorrectivePreventiveAction does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_correctivepreventiveaction(correctivepreventiveaction_id):
    """
    Deletes a CorrectivePreventiveAction instance with the given ID.
    
    Args:
        correctivepreventiveaction_id (int): ID of the CorrectivePreventiveAction to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CorrectivePreventiveAction.objects.get(pk=correctivepreventiveaction_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CorrectivePreventiveAction.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_changeorder(contract_id, requestor, description, change_reason, impact_on_scope, cost_impact, time_impact, status, submitted_date, approved_date):
    """
    Creates a ChangeOrder instance with the provided data.
        Args:
        contract_id, requestor, description, change_reason, impact_on_scope, cost_impact, time_impact, status, submitted_date, approved_date: Keyword arguments for ChangeOrder fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ChangeOrder.objects.create(
            contract_id=contract_id,
            requestor=requestor,
            description=description,
            change_reason=change_reason,
            impact_on_scope=impact_on_scope,
            cost_impact=cost_impact,
            time_impact=time_impact,
            status=status,
            submitted_date=submitted_date,
            approved_date=approved_date,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_changeorder(changeorder_id,contract_id=None, requestor=None, description=None, change_reason=None, impact_on_scope=None, cost_impact=None, time_impact=None, status=None, submitted_date=None, approved_date=None):
    """
    Updates a ChangeOrder instance with the provided data.
    
    Args:
        changeorder_id (int): ID of the ChangeOrder to update.
        contract_id=None, requestor=None, description=None, change_reason=None, impact_on_scope=None, cost_impact=None, time_impact=None, status=None, submitted_date=None, approved_date=None: Keyword arguments for ChangeOrder fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ChangeOrder.objects.get(pk=changeorder_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.requestor = requestor if requestor is not None else instance.requestor
        instance.description = description if description is not None else instance.description
        instance.change_reason = change_reason if change_reason is not None else instance.change_reason
        instance.impact_on_scope = impact_on_scope if impact_on_scope is not None else instance.impact_on_scope
        instance.cost_impact = cost_impact if cost_impact is not None else instance.cost_impact
        instance.time_impact = time_impact if time_impact is not None else instance.time_impact
        instance.status = status if status is not None else instance.status
        instance.submitted_date = submitted_date if submitted_date is not None else instance.submitted_date
        instance.approved_date = approved_date if approved_date is not None else instance.approved_date
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except  ChangeOrder.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_changeorder(changeorder_id=None):
    """
    Retrieves and serializes a ChangeOrder instance by its ID or all instances if ID is None.
    
    Args:
        ChangeOrder_id (int, optional): ID of the ChangeOrder to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if changeorder_id is not None:
            record = ChangeOrder.objects.get(pk=changeorder_id)
            serializer = ChangeOrderSerializer(record)
        else:
            records = ChangeOrder.objects.all()
            serializer = ChangeOrderSerializer(records, many=True)
        return success(serializer.data)
    
    except ChangeOrder.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ChangeOrder does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_changeorder(changeorder_id):
    """
    Deletes a ChangeOrder instance with the given ID.
    
    Args:
        changeorder_id (int): ID of the ChangeOrder to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ChangeOrder.objects.get(pk=changeorder_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ChangeOrder.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_contractexecution(contract_id, execution_date, status, notes):
    """
    Creates a ContractExecution instance with the provided data.
        Args:
        contract_id, execution_date, status, notes: Keyword arguments for ContractExecution fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ContractExecution.objects.create(
            contract_id=contract_id,
            execution_date=execution_date,
            status=status,
            notes=notes,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_contractexecution(contractexecution_id,contract_id=None, execution_date=None, status=None, notes=None):
    """
    Updates a ContractExecution instance with the provided data.
    
    Args:
        contractexecution_id (int): ID of the ContractExecution to update.
        contract_id=None, execution_date=None, status=None, notes=None: Keyword arguments for ContractExecution fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ContractExecution.objects.get(pk=contractexecution_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.execution_date = execution_date if execution_date is not None else instance.execution_date
        instance.status = status if status is not None else instance.status
        instance.notes = notes if notes is not None else instance.notes
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except  ContractExecution.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_contractexecution(contractexecution_id=None):
    """
    Retrieves and serializes a ContractExecution instance by its ID or all instances if ID is None.
    
    Args:
        ContractExecution_id (int, optional): ID of the ContractExecution to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contractexecution_id is not None:
            record = ContractExecution.objects.get(pk=contractexecution_id)
            serializer = ContractExecutionSerializer(record)
        else:
            records = ContractExecution.objects.all()
            serializer = ContractExecutionSerializer(records, many=True)
        return success(serializer.data)
    
    except ContractExecution.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ContractExecution does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_contractexecution(contractexecution_id):
    """
    Deletes a ContractExecution instance with the given ID.
    
    Args:
        contractexecution_id (int): ID of the ContractExecution to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ContractExecution.objects.get(pk=contractexecution_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ContractExecution.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_contractmilestone(contract_id, name, description, due_date, completed):
    """
    Creates a ContractMilestone instance with the provided data.
        Args:
        contract_id, name, description, due_date, completed: Keyword arguments for ContractMilestone fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ContractMilestone.objects.create(
            contract_id=contract_id,
            name=name,
            description=description,
            due_date=due_date,
            completed=completed,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_contractmilestone(contractmilestone_id,contract_id=None, name=None, description=None, due_date=None, completed=None):
    """
    Updates a ContractMilestone instance with the provided data.
    
    Args:
        contractmilestone_id (int): ID of the ContractMilestone to update.
        contract_id=None, name=None, description=None, due_date=None, completed=None: Keyword arguments for ContractMilestone fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = ContractMilestone.objects.get(pk=contractmilestone_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.name = name if name is not None else instance.name
        instance.description = description if description is not None else instance.description
        instance.due_date = due_date if due_date is not None else instance.due_date
        instance.completed = completed if completed is not None else instance.completed
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except  ContractMilestone.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_contractmilestone(contractmilestone_id=None):
    """
    Retrieves and serializes a ContractMilestone instance by its ID or all instances if ID is None.
    
    Args:
        ContractMilestone_id (int, optional): ID of the ContractMilestone to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contractmilestone_id is not None:
            record = ContractMilestone.objects.get(pk=contractmilestone_id)
            serializer = ContractMilestoneSerializer(record)
        else:
            records = ContractMilestone.objects.all()
            serializer = ContractMilestoneSerializer(records, many=True)
        return success(serializer.data)
    
    except ContractMilestone.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ContractMilestone does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_contractmilestone(contractmilestone_id):
    """
    Deletes a ContractMilestone instance with the given ID.
    
    Args:
        contractmilestone_id (int): ID of the ContractMilestone to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ContractMilestone.objects.get(pk=contractmilestone_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ContractMilestone.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_purchaseorder(contract_id, order_number, product_service_description, quantity, unit_price, total_price, status):
    """
    Creates a PurchaseOrder instance with the provided data.
        Args:
        contract_id, order_number, product_service_description, quantity, unit_price, total_price, status: Keyword arguments for PurchaseOrder fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = PurchaseOrder.objects.create(
            contract_id=contract_id,
            order_number=order_number,
            product_service_description=product_service_description,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
            status=status,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_purchaseorder(purchaseorder_id,contract_id=None, order_number=None, product_service_description=None, quantity=None, unit_price=None, total_price=None, status=None):
    """
    Updates a PurchaseOrder instance with the provided data.
    
    Args:
        purchaseorder_id (int): ID of the PurchaseOrder to update.
        contract_id=None, order_number=None, product_service_description=None, quantity=None, unit_price=None, total_price=None, status=None: Keyword arguments for PurchaseOrder fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        instance = PurchaseOrder.objects.get(pk=purchaseorder_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.order_number = order_number if order_number is not None else instance.order_number
        instance.product_service_description = product_service_description if product_service_description is not None else instance.product_service_description
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.unit_price = unit_price if unit_price is not None else instance.unit_price
        instance.total_price = total_price if total_price is not None else instance.total_price
        instance.status = status if status is not None else instance.status
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except  PurchaseOrder.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_purchaseorder(purchaseorder_id=None):
    """
    Retrieves and serializes a PurchaseOrder instance by its ID or all instances if ID is None.
    
    Args:
        PurchaseOrder_id (int, optional): ID of the PurchaseOrder to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if purchaseorder_id is not None:
            record = PurchaseOrder.objects.get(pk=purchaseorder_id)
            serializer = PurchaseOrderSerializer(record)
        else:
            records = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(records, many=True)
        return success(serializer.data)
    
    except PurchaseOrder.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PurchaseOrder does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_purchaseorder(purchaseorder_id):
    """
    Deletes a PurchaseOrder instance with the given ID.
    
    Args:
        purchaseorder_id (int): ID of the PurchaseOrder to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PurchaseOrder.objects.get(pk=purchaseorder_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PurchaseOrder.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_correctiveaction(incident_id, description, action_taken_by_id, date_taken, status):
    """
    Creates a CorrectiveAction instance with the provided data.
        Args:
        incident_id, description, action_taken_by_id, date_taken, status: Keyword arguments for CorrectiveAction fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if incident_id is not None and incident_id != '': 
             IncidentReport.objects.get(pk=incident_id)
        if action_taken_by_id is not None and action_taken_by_id != '': 
             User.objects.get(pk=action_taken_by_id)
        instance = CorrectiveAction.objects.create(
            incident_id=incident_id,
            description=description,
            action_taken_by_id=action_taken_by_id,
            date_taken=date_taken,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except IncidentReport.DoesNotExist:
        return error('Invalid IncidentReport ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_correctiveaction(correctiveaction_id,incident_id=None, description=None, action_taken_by_id=None, date_taken=None, status=None):
    """
    Updates a CorrectiveAction instance with the provided data.
    
    Args:
        correctiveaction_id (int): ID of the CorrectiveAction to update.
        incident_id=None, description=None, action_taken_by_id=None, date_taken=None, status=None: Keyword arguments for CorrectiveAction fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if incident_id is not None and incident_id != '': 
             IncidentReport.objects.get(pk=incident_id)
        if action_taken_by_id is not None and action_taken_by_id != '': 
             User.objects.get(pk=action_taken_by_id)
        instance = CorrectiveAction.objects.get(pk=correctiveaction_id)
        instance.incident_id = incident_id if incident_id is not None else instance.incident_id
        instance.description = description if description is not None else instance.description
        instance.action_taken_by_id = action_taken_by_id if action_taken_by_id is not None else instance.action_taken_by_id
        instance.date_taken = date_taken if date_taken is not None else instance.date_taken
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except IncidentReport.DoesNotExist:
        return error('Invalid IncidentReport ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  CorrectiveAction.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_correctiveaction(correctiveaction_id=None):
    """
    Retrieves and serializes a CorrectiveAction instance by its ID or all instances if ID is None.
    
    Args:
        CorrectiveAction_id (int, optional): ID of the CorrectiveAction to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if correctiveaction_id is not None:
            record = CorrectiveAction.objects.get(pk=correctiveaction_id)
            serializer = CorrectiveActionSerializer(record)
        else:
            records = CorrectiveAction.objects.all()
            serializer = CorrectiveActionSerializer(records, many=True)
        return success(serializer.data)
    
    except CorrectiveAction.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CorrectiveAction does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_correctiveaction(correctiveaction_id):
    """
    Deletes a CorrectiveAction instance with the given ID.
    
    Args:
        correctiveaction_id (int): ID of the CorrectiveAction to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CorrectiveAction.objects.get(pk=correctiveaction_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CorrectiveAction.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clientreview(milestone_id, client_feedback, approved):
    """
    Creates a ClientReview instance with the provided data.
        Args:
        milestone_id, client_feedback, approved: Keyword arguments for ClientReview fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if milestone_id is not None and milestone_id != '': 
             Milestone.objects.get(pk=milestone_id)
        instance = ClientReview.objects.create(
            milestone_id=milestone_id,
            client_feedback=client_feedback,
            approved=approved,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Milestone.DoesNotExist:
        return error('Invalid Milestone ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clientreview(clientreview_id,milestone_id=None, client_feedback=None, approved=None):
    """
    Updates a ClientReview instance with the provided data.
    
    Args:
        clientreview_id (int): ID of the ClientReview to update.
        milestone_id=None, client_feedback=None, approved=None: Keyword arguments for ClientReview fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if milestone_id is not None and milestone_id != '': 
             Milestone.objects.get(pk=milestone_id)
        instance = ClientReview.objects.get(pk=clientreview_id)
        instance.milestone_id = milestone_id if milestone_id is not None else instance.milestone_id
        instance.client_feedback = client_feedback if client_feedback is not None else instance.client_feedback
        instance.approved = approved if approved is not None else instance.approved
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Milestone.DoesNotExist:
        return error('Invalid Milestone ID: Destination not found.')
    except  ClientReview.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clientreview(clientreview_id=None):
    """
    Retrieves and serializes a ClientReview instance by its ID or all instances if ID is None.
    
    Args:
        ClientReview_id (int, optional): ID of the ClientReview to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clientreview_id is not None:
            record = ClientReview.objects.get(pk=clientreview_id)
            serializer = ClientReviewSerializer(record)
        else:
            records = ClientReview.objects.all()
            serializer = ClientReviewSerializer(records, many=True)
        return success(serializer.data)
    
    except ClientReview.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClientReview does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clientreview(clientreview_id):
    """
    Deletes a ClientReview instance with the given ID.
    
    Args:
        clientreview_id (int): ID of the ClientReview to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClientReview.objects.get(pk=clientreview_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClientReview.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_scheduleadjustment(project_id, milestone_id, adjustment_date, new_date, reason, adjusted_by_id):
    """
    Creates a ScheduleAdjustment instance with the provided data.
        Args:
        project_id, milestone_id, adjustment_date, new_date, reason, adjusted_by_id: Keyword arguments for ScheduleAdjustment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if milestone_id is not None and milestone_id != '': 
             Milestone.objects.get(pk=milestone_id)
        if adjusted_by_id is not None and adjusted_by_id != '': 
             User.objects.get(pk=adjusted_by_id)
        instance = ScheduleAdjustment.objects.create(
            project_id=project_id,
            milestone_id=milestone_id,
            adjustment_date=adjustment_date,
            new_date=new_date,
            reason=reason,
            adjusted_by_id=adjusted_by_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Milestone.DoesNotExist:
        return error('Invalid Milestone ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_scheduleadjustment(scheduleadjustment_id,project_id=None, milestone_id=None, adjustment_date=None, new_date=None, reason=None, adjusted_by_id=None):
    """
    Updates a ScheduleAdjustment instance with the provided data.
    
    Args:
        scheduleadjustment_id (int): ID of the ScheduleAdjustment to update.
        project_id=None, milestone_id=None, adjustment_date=None, new_date=None, reason=None, adjusted_by_id=None: Keyword arguments for ScheduleAdjustment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if milestone_id is not None and milestone_id != '': 
             Milestone.objects.get(pk=milestone_id)
        if adjusted_by_id is not None and adjusted_by_id != '': 
             User.objects.get(pk=adjusted_by_id)
        instance = ScheduleAdjustment.objects.get(pk=scheduleadjustment_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.milestone_id = milestone_id if milestone_id is not None else instance.milestone_id
        instance.adjustment_date = adjustment_date if adjustment_date is not None else instance.adjustment_date
        instance.new_date = new_date if new_date is not None else instance.new_date
        instance.reason = reason if reason is not None else instance.reason
        instance.adjusted_by_id = adjusted_by_id if adjusted_by_id is not None else instance.adjusted_by_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Milestone.DoesNotExist:
        return error('Invalid Milestone ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  ScheduleAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_scheduleadjustment(scheduleadjustment_id=None):
    """
    Retrieves and serializes a ScheduleAdjustment instance by its ID or all instances if ID is None.
    
    Args:
        ScheduleAdjustment_id (int, optional): ID of the ScheduleAdjustment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if scheduleadjustment_id is not None:
            record = ScheduleAdjustment.objects.get(pk=scheduleadjustment_id)
            serializer = ScheduleAdjustmentSerializer(record)
        else:
            records = ScheduleAdjustment.objects.all()
            serializer = ScheduleAdjustmentSerializer(records, many=True)
        return success(serializer.data)
    
    except ScheduleAdjustment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ScheduleAdjustment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_scheduleadjustment(scheduleadjustment_id):
    """
    Deletes a ScheduleAdjustment instance with the given ID.
    
    Args:
        scheduleadjustment_id (int): ID of the ScheduleAdjustment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ScheduleAdjustment.objects.get(pk=scheduleadjustment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ScheduleAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_machinery(resource_planning_id, name, quantity):
    """
    Creates a Machinery instance with the provided data.
        Args:
        resource_planning_id, name, quantity: Keyword arguments for Machinery fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_planning_id is not None and resource_planning_id != '': 
             ResourcePlanning.objects.get(pk=resource_planning_id)
        instance = Machinery.objects.create(
            resource_planning_id=resource_planning_id,
            name=name,
            quantity=quantity,
        )
        return success(f'Successfully created {instance}')
    except ResourcePlanning.DoesNotExist:
        return error('Invalid ResourcePlanning ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_machinery(machinery_id,resource_planning_id=None, name=None, quantity=None):
    """
    Updates a Machinery instance with the provided data.
    
    Args:
        machinery_id (int): ID of the Machinery to update.
        resource_planning_id=None, name=None, quantity=None: Keyword arguments for Machinery fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_planning_id is not None and resource_planning_id != '': 
             ResourcePlanning.objects.get(pk=resource_planning_id)
        instance = Machinery.objects.get(pk=machinery_id)
        instance.resource_planning_id = resource_planning_id if resource_planning_id is not None else instance.resource_planning_id
        instance.name = name if name is not None else instance.name
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.save()
        return success('Successfully Updated')
    except ResourcePlanning.DoesNotExist:
        return error('Invalid ResourcePlanning ID: Destination not found.')
    except  Machinery.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_machinery(machinery_id=None):
    """
    Retrieves and serializes a Machinery instance by its ID or all instances if ID is None.
    
    Args:
        Machinery_id (int, optional): ID of the Machinery to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if machinery_id is not None:
            record = Machinery.objects.get(pk=machinery_id)
            serializer = MachinerySerializer(record)
        else:
            records = Machinery.objects.all()
            serializer = MachinerySerializer(records, many=True)
        return success(serializer.data)
    
    except Machinery.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Machinery does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_machinery(machinery_id):
    """
    Deletes a Machinery instance with the given ID.
    
    Args:
        machinery_id (int): ID of the Machinery to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Machinery.objects.get(pk=machinery_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Machinery.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_material(resource_planning_id, name, quantity):
    """
    Creates a Material instance with the provided data.
        Args:
        resource_planning_id, name, quantity: Keyword arguments for Material fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_planning_id is not None and resource_planning_id != '': 
             ResourcePlanning.objects.get(pk=resource_planning_id)
        instance = Material.objects.create(
            resource_planning_id=resource_planning_id,
            name=name,
            quantity=quantity,
        )
        return success(f'Successfully created {instance}')
    except ResourcePlanning.DoesNotExist:
        return error('Invalid ResourcePlanning ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_material(material_id,resource_planning_id=None, name=None, quantity=None):
    """
    Updates a Material instance with the provided data.
    
    Args:
        material_id (int): ID of the Material to update.
        resource_planning_id=None, name=None, quantity=None: Keyword arguments for Material fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resource_planning_id is not None and resource_planning_id != '': 
             ResourcePlanning.objects.get(pk=resource_planning_id)
        instance = Material.objects.get(pk=material_id)
        instance.resource_planning_id = resource_planning_id if resource_planning_id is not None else instance.resource_planning_id
        instance.name = name if name is not None else instance.name
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.save()
        return success('Successfully Updated')
    except ResourcePlanning.DoesNotExist:
        return error('Invalid ResourcePlanning ID: Destination not found.')
    except  Material.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_material(material_id=None):
    """
    Retrieves and serializes a Material instance by its ID or all instances if ID is None.
    
    Args:
        Material_id (int, optional): ID of the Material to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if material_id is not None:
            record = Material.objects.get(pk=material_id)
            serializer = MaterialSerializer(record)
        else:
            records = Material.objects.all()
            serializer = MaterialSerializer(records, many=True)
        return success(serializer.data)
    
    except Material.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Material does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_material(material_id):
    """
    Deletes a Material instance with the given ID.
    
    Args:
        material_id (int): ID of the Material to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Material.objects.get(pk=material_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Material.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_mitigationstrategy(risk_id, strategy, mitigation_owner_id, start_date, end_date, status):
    """
    Creates a MitigationStrategy instance with the provided data.
        Args:
        risk_id, strategy, mitigation_owner_id, start_date, end_date, status: Keyword arguments for MitigationStrategy fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if risk_id is not None and risk_id != '': 
             Risk.objects.get(pk=risk_id)
        if mitigation_owner_id is not None and mitigation_owner_id != '': 
             RiskOwner.objects.get(pk=mitigation_owner_id)
        instance = MitigationStrategy.objects.create(
            risk_id=risk_id,
            strategy=strategy,
            mitigation_owner_id=mitigation_owner_id,
            start_date=start_date,
            end_date=end_date,
            status=status,
        )
        return success(f'Successfully created {instance}')
    except Risk.DoesNotExist:
        return error('Invalid Risk ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_mitigationstrategy(mitigationstrategy_id,risk_id=None, strategy=None, mitigation_owner_id=None, start_date=None, end_date=None, status=None):
    """
    Updates a MitigationStrategy instance with the provided data.
    
    Args:
        mitigationstrategy_id (int): ID of the MitigationStrategy to update.
        risk_id=None, strategy=None, mitigation_owner_id=None, start_date=None, end_date=None, status=None: Keyword arguments for MitigationStrategy fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if risk_id is not None and risk_id != '': 
             Risk.objects.get(pk=risk_id)
        if mitigation_owner_id is not None and mitigation_owner_id != '': 
             RiskOwner.objects.get(pk=mitigation_owner_id)
        instance = MitigationStrategy.objects.get(pk=mitigationstrategy_id)
        instance.risk_id = risk_id if risk_id is not None else instance.risk_id
        instance.strategy = strategy if strategy is not None else instance.strategy
        instance.mitigation_owner_id = mitigation_owner_id if mitigation_owner_id is not None else instance.mitigation_owner_id
        instance.start_date = start_date if start_date is not None else instance.start_date
        instance.end_date = end_date if end_date is not None else instance.end_date
        instance.status = status if status is not None else instance.status
        instance.save()
        return success('Successfully Updated')
    except Risk.DoesNotExist:
        return error('Invalid Risk ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except  MitigationStrategy.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_mitigationstrategy(mitigationstrategy_id=None):
    """
    Retrieves and serializes a MitigationStrategy instance by its ID or all instances if ID is None.
    
    Args:
        MitigationStrategy_id (int, optional): ID of the MitigationStrategy to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if mitigationstrategy_id is not None:
            record = MitigationStrategy.objects.get(pk=mitigationstrategy_id)
            serializer = MitigationStrategySerializer(record)
        else:
            records = MitigationStrategy.objects.all()
            serializer = MitigationStrategySerializer(records, many=True)
        return success(serializer.data)
    
    except MitigationStrategy.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('MitigationStrategy does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_mitigationstrategy(mitigationstrategy_id):
    """
    Deletes a MitigationStrategy instance with the given ID.
    
    Args:
        mitigationstrategy_id (int): ID of the MitigationStrategy to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = MitigationStrategy.objects.get(pk=mitigationstrategy_id)
        instance.delete()
        return success("Successfully deleted")
    
    except MitigationStrategy.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_riskreview(risk_id, review_date, status, comments, reviewed_by_id):
    """
    Creates a RiskReview instance with the provided data.
        Args:
        risk_id, review_date, status, comments, reviewed_by_id: Keyword arguments for RiskReview fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if risk_id is not None and risk_id != '': 
             Risk.objects.get(pk=risk_id)
        if reviewed_by_id is not None and reviewed_by_id != '': 
             RiskOwner.objects.get(pk=reviewed_by_id)
        instance = RiskReview.objects.create(
            risk_id=risk_id,
            review_date=review_date,
            status=status,
            comments=comments,
            reviewed_by_id=reviewed_by_id,
        )
        return success(f'Successfully created {instance}')
    except Risk.DoesNotExist:
        return error('Invalid Risk ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_riskreview(riskreview_id,risk_id=None, review_date=None, status=None, comments=None, reviewed_by_id=None):
    """
    Updates a RiskReview instance with the provided data.
    
    Args:
        riskreview_id (int): ID of the RiskReview to update.
        risk_id=None, review_date=None, status=None, comments=None, reviewed_by_id=None: Keyword arguments for RiskReview fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if risk_id is not None and risk_id != '': 
             Risk.objects.get(pk=risk_id)
        if reviewed_by_id is not None and reviewed_by_id != '': 
             RiskOwner.objects.get(pk=reviewed_by_id)
        instance = RiskReview.objects.get(pk=riskreview_id)
        instance.risk_id = risk_id if risk_id is not None else instance.risk_id
        instance.review_date = review_date if review_date is not None else instance.review_date
        instance.status = status if status is not None else instance.status
        instance.comments = comments if comments is not None else instance.comments
        instance.reviewed_by_id = reviewed_by_id if reviewed_by_id is not None else instance.reviewed_by_id
        instance.save()
        return success('Successfully Updated')
    except Risk.DoesNotExist:
        return error('Invalid Risk ID: Destination not found.')
    except RiskOwner.DoesNotExist:
        return error('Invalid RiskOwner ID: Destination not found.')
    except  RiskReview.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_riskreview(riskreview_id=None):
    """
    Retrieves and serializes a RiskReview instance by its ID or all instances if ID is None.
    
    Args:
        RiskReview_id (int, optional): ID of the RiskReview to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if riskreview_id is not None:
            record = RiskReview.objects.get(pk=riskreview_id)
            serializer = RiskReviewSerializer(record)
        else:
            records = RiskReview.objects.all()
            serializer = RiskReviewSerializer(records, many=True)
        return success(serializer.data)
    
    except RiskReview.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('RiskReview does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_riskreview(riskreview_id):
    """
    Deletes a RiskReview instance with the given ID.
    
    Args:
        riskreview_id (int): ID of the RiskReview to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = RiskReview.objects.get(pk=riskreview_id)
        instance.delete()
        return success("Successfully deleted")
    
    except RiskReview.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_delaynotification(project_id, stakeholder_id, notification_date, message, updated_timeline, plan_to_mitigate):
    """
    Creates a DelayNotification instance with the provided data.
        Args:
        project_id, stakeholder_id, notification_date, message, updated_timeline, plan_to_mitigate: Keyword arguments for DelayNotification fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = DelayNotification.objects.create(
            project_id=project_id,
            stakeholder_id=stakeholder_id,
            notification_date=notification_date,
            message=message,
            updated_timeline=updated_timeline,
            plan_to_mitigate=plan_to_mitigate,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_delaynotification(delaynotification_id,project_id=None, stakeholder_id=None, notification_date=None, message=None, updated_timeline=None, plan_to_mitigate=None):
    """
    Updates a DelayNotification instance with the provided data.
    
    Args:
        delaynotification_id (int): ID of the DelayNotification to update.
        project_id=None, stakeholder_id=None, notification_date=None, message=None, updated_timeline=None, plan_to_mitigate=None: Keyword arguments for DelayNotification fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = DelayNotification.objects.get(pk=delaynotification_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.stakeholder_id = stakeholder_id if stakeholder_id is not None else instance.stakeholder_id
        instance.notification_date = notification_date if notification_date is not None else instance.notification_date
        instance.message = message if message is not None else instance.message
        instance.updated_timeline = updated_timeline if updated_timeline is not None else instance.updated_timeline
        instance.plan_to_mitigate = plan_to_mitigate if plan_to_mitigate is not None else instance.plan_to_mitigate
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except  DelayNotification.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_delaynotification(delaynotification_id=None):
    """
    Retrieves and serializes a DelayNotification instance by its ID or all instances if ID is None.
    
    Args:
        DelayNotification_id (int, optional): ID of the DelayNotification to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if delaynotification_id is not None:
            record = DelayNotification.objects.get(pk=delaynotification_id)
            serializer = DelayNotificationSerializer(record)
        else:
            records = DelayNotification.objects.all()
            serializer = DelayNotificationSerializer(records, many=True)
        return success(serializer.data)
    
    except DelayNotification.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('DelayNotification does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_delaynotification(delaynotification_id):
    """
    Deletes a DelayNotification instance with the given ID.
    
    Args:
        delaynotification_id (int): ID of the DelayNotification to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DelayNotification.objects.get(pk=delaynotification_id)
        instance.delete()
        return success("Successfully deleted")
    
    except DelayNotification.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stakeholderinput(procurement_need_id, stakeholder_id, input_description):
    """
    Creates a StakeholderInput instance with the provided data.
        Args:
        procurement_need_id, stakeholder_id, input_description: Keyword arguments for StakeholderInput fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if procurement_need_id is not None and procurement_need_id != '': 
             ProcurementNeed.objects.get(pk=procurement_need_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = StakeholderInput.objects.create(
            procurement_need_id=procurement_need_id,
            stakeholder_id=stakeholder_id,
            input_description=input_description,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ProcurementNeed.DoesNotExist:
        return error('Invalid ProcurementNeed ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stakeholderinput(stakeholderinput_id,procurement_need_id=None, stakeholder_id=None, input_description=None):
    """
    Updates a StakeholderInput instance with the provided data.
    
    Args:
        stakeholderinput_id (int): ID of the StakeholderInput to update.
        procurement_need_id=None, stakeholder_id=None, input_description=None: Keyword arguments for StakeholderInput fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if procurement_need_id is not None and procurement_need_id != '': 
             ProcurementNeed.objects.get(pk=procurement_need_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = StakeholderInput.objects.get(pk=stakeholderinput_id)
        instance.procurement_need_id = procurement_need_id if procurement_need_id is not None else instance.procurement_need_id
        instance.stakeholder_id = stakeholder_id if stakeholder_id is not None else instance.stakeholder_id
        instance.input_description = input_description if input_description is not None else instance.input_description
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except ProcurementNeed.DoesNotExist:
        return error('Invalid ProcurementNeed ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except  StakeholderInput.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stakeholderinput(stakeholderinput_id=None):
    """
    Retrieves and serializes a StakeholderInput instance by its ID or all instances if ID is None.
    
    Args:
        StakeholderInput_id (int, optional): ID of the StakeholderInput to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stakeholderinput_id is not None:
            record = StakeholderInput.objects.get(pk=stakeholderinput_id)
            serializer = StakeholderInputSerializer(record)
        else:
            records = StakeholderInput.objects.all()
            serializer = StakeholderInputSerializer(records, many=True)
        return success(serializer.data)
    
    except StakeholderInput.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('StakeholderInput does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stakeholderinput(stakeholderinput_id):
    """
    Deletes a StakeholderInput instance with the given ID.
    
    Args:
        stakeholderinput_id (int): ID of the StakeholderInput to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = StakeholderInput.objects.get(pk=stakeholderinput_id)
        instance.delete()
        return success("Successfully deleted")
    
    except StakeholderInput.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_tenderdocument(tender_type, title, description, prepared_by_id, issue_date, closing_date):
    """
    Creates a TenderDocument instance with the provided data.
        Args:
        tender_type, title, description, prepared_by_id, issue_date, closing_date: Keyword arguments for TenderDocument fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if prepared_by_id is not None and prepared_by_id != '': 
             Stakeholder.objects.get(pk=prepared_by_id)
        instance = TenderDocument.objects.create(
            tender_type=tender_type,
            title=title,
            description=description,
            prepared_by_id=prepared_by_id,
            issue_date=issue_date,
            closing_date=closing_date,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_tenderdocument(tenderdocument_id,tender_type=None, title=None, description=None, prepared_by_id=None, issue_date=None, closing_date=None):
    """
    Updates a TenderDocument instance with the provided data.
    
    Args:
        tenderdocument_id (int): ID of the TenderDocument to update.
        tender_type=None, title=None, description=None, prepared_by_id=None, issue_date=None, closing_date=None: Keyword arguments for TenderDocument fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if prepared_by_id is not None and prepared_by_id != '': 
             Stakeholder.objects.get(pk=prepared_by_id)
        instance = TenderDocument.objects.get(pk=tenderdocument_id)
        instance.tender_type = tender_type if tender_type is not None else instance.tender_type
        instance.title = title if title is not None else instance.title
        instance.description = description if description is not None else instance.description
        instance.prepared_by_id = prepared_by_id if prepared_by_id is not None else instance.prepared_by_id
        instance.issue_date = issue_date if issue_date is not None else instance.issue_date
        instance.closing_date = closing_date if closing_date is not None else instance.closing_date
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except  TenderDocument.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_tenderdocument(tenderdocument_id=None):
    """
    Retrieves and serializes a TenderDocument instance by its ID or all instances if ID is None.
    
    Args:
        TenderDocument_id (int, optional): ID of the TenderDocument to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tenderdocument_id is not None:
            record = TenderDocument.objects.get(pk=tenderdocument_id)
            serializer = TenderDocumentSerializer(record)
        else:
            records = TenderDocument.objects.all()
            serializer = TenderDocumentSerializer(records, many=True)
        return success(serializer.data)
    
    except TenderDocument.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TenderDocument does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_tenderdocument(tenderdocument_id):
    """
    Deletes a TenderDocument instance with the given ID.
    
    Args:
        tenderdocument_id (int): ID of the TenderDocument to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderDocument.objects.get(pk=tenderdocument_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TenderDocument.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_issue(project_id, issue_type, description, status, assigned_to_id):
    """
    Creates a Issue instance with the provided data.
        Args:
        project_id, issue_type, description, status, assigned_to_id: Keyword arguments for Issue fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             TeamMember.objects.get(pk=assigned_to_id)
        instance = Issue.objects.create(
            project_id=project_id,
            issue_type=issue_type,
            description=description,
            status=status,
            assigned_to_id=assigned_to_id,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except TeamMember.DoesNotExist:
        return error('Invalid TeamMember ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_issue(issue_id,project_id=None, issue_type=None, description=None, status=None, assigned_to_id=None):
    """
    Updates a Issue instance with the provided data.
    
    Args:
        issue_id (int): ID of the Issue to update.
        project_id=None, issue_type=None, description=None, status=None, assigned_to_id=None: Keyword arguments for Issue fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if assigned_to_id is not None and assigned_to_id != '': 
             TeamMember.objects.get(pk=assigned_to_id)
        instance = Issue.objects.get(pk=issue_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.issue_type = issue_type if issue_type is not None else instance.issue_type
        instance.description = description if description is not None else instance.description
        instance.status = status if status is not None else instance.status
        instance.assigned_to_id = assigned_to_id if assigned_to_id is not None else instance.assigned_to_id
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except TeamMember.DoesNotExist:
        return error('Invalid TeamMember ID: Destination not found.')
    except  Issue.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_issue(issue_id=None):
    """
    Retrieves and serializes a Issue instance by its ID or all instances if ID is None.
    
    Args:
        Issue_id (int, optional): ID of the Issue to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if issue_id is not None:
            record = Issue.objects.get(pk=issue_id)
            serializer = IssueSerializer(record)
        else:
            records = Issue.objects.all()
            serializer = IssueSerializer(records, many=True)
        return success(serializer.data)
    
    except Issue.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Issue does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_issue(issue_id):
    """
    Deletes a Issue instance with the given ID.
    
    Args:
        issue_id (int): ID of the Issue to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Issue.objects.get(pk=issue_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Issue.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_clarificationresponse(clarification_id, response):
    """
    Creates a ClarificationResponse instance with the provided data.
        Args:
        clarification_id, response: Keyword arguments for ClarificationResponse fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clarification_id is not None and clarification_id != '': 
             VendorClarification.objects.get(pk=clarification_id)
        instance = ClarificationResponse.objects.create(
            clarification_id=clarification_id,
            response=response,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except VendorClarification.DoesNotExist:
        return error('Invalid VendorClarification ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_clarificationresponse(clarificationresponse_id,clarification_id=None, response=None):
    """
    Updates a ClarificationResponse instance with the provided data.
    
    Args:
        clarificationresponse_id (int): ID of the ClarificationResponse to update.
        clarification_id=None, response=None: Keyword arguments for ClarificationResponse fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clarification_id is not None and clarification_id != '': 
             VendorClarification.objects.get(pk=clarification_id)
        instance = ClarificationResponse.objects.get(pk=clarificationresponse_id)
        instance.clarification_id = clarification_id if clarification_id is not None else instance.clarification_id
        instance.response = response if response is not None else instance.response
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except VendorClarification.DoesNotExist:
        return error('Invalid VendorClarification ID: Destination not found.')
    except  ClarificationResponse.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_clarificationresponse(clarificationresponse_id=None):
    """
    Retrieves and serializes a ClarificationResponse instance by its ID or all instances if ID is None.
    
    Args:
        ClarificationResponse_id (int, optional): ID of the ClarificationResponse to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if clarificationresponse_id is not None:
            record = ClarificationResponse.objects.get(pk=clarificationresponse_id)
            serializer = ClarificationResponseSerializer(record)
        else:
            records = ClarificationResponse.objects.all()
            serializer = ClarificationResponseSerializer(records, many=True)
        return success(serializer.data)
    
    except ClarificationResponse.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ClarificationResponse does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_clarificationresponse(clarificationresponse_id):
    """
    Deletes a ClarificationResponse instance with the given ID.
    
    Args:
        clarificationresponse_id (int): ID of the ClarificationResponse to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ClarificationResponse.objects.get(pk=clarificationresponse_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ClarificationResponse.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_finalvendorselection(vendor_proposal_id, selection_date, justification, approved_by):
    """
    Creates a FinalVendorSelection instance with the provided data.
        Args:
        vendor_proposal_id, selection_date, justification, approved_by: Keyword arguments for FinalVendorSelection fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = FinalVendorSelection.objects.create(
            vendor_proposal_id=vendor_proposal_id,
            selection_date=selection_date,
            justification=justification,
            approved_by=approved_by,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_finalvendorselection(finalvendorselection_id,vendor_proposal_id=None, selection_date=None, justification=None, approved_by=None):
    """
    Updates a FinalVendorSelection instance with the provided data.
    
    Args:
        finalvendorselection_id (int): ID of the FinalVendorSelection to update.
        vendor_proposal_id=None, selection_date=None, justification=None, approved_by=None: Keyword arguments for FinalVendorSelection fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = FinalVendorSelection.objects.get(pk=finalvendorselection_id)
        instance.vendor_proposal_id = vendor_proposal_id if vendor_proposal_id is not None else instance.vendor_proposal_id
        instance.selection_date = selection_date if selection_date is not None else instance.selection_date
        instance.justification = justification if justification is not None else instance.justification
        instance.approved_by = approved_by if approved_by is not None else instance.approved_by
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except  FinalVendorSelection.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_finalvendorselection(finalvendorselection_id=None):
    """
    Retrieves and serializes a FinalVendorSelection instance by its ID or all instances if ID is None.
    
    Args:
        FinalVendorSelection_id (int, optional): ID of the FinalVendorSelection to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if finalvendorselection_id is not None:
            record = FinalVendorSelection.objects.get(pk=finalvendorselection_id)
            serializer = FinalVendorSelectionSerializer(record)
        else:
            records = FinalVendorSelection.objects.all()
            serializer = FinalVendorSelectionSerializer(records, many=True)
        return success(serializer.data)
    
    except FinalVendorSelection.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('FinalVendorSelection does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_finalvendorselection(finalvendorselection_id):
    """
    Deletes a FinalVendorSelection instance with the given ID.
    
    Args:
        finalvendorselection_id (int): ID of the FinalVendorSelection to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = FinalVendorSelection.objects.get(pk=finalvendorselection_id)
        instance.delete()
        return success("Successfully deleted")
    
    except FinalVendorSelection.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_negotiationstakeholder(team_id, stakeholder_id, vendor_proposal_id, feedback):
    """
    Creates a NegotiationStakeholder instance with the provided data.
        Args:
        team_id, stakeholder_id, vendor_proposal_id, feedback: Keyword arguments for NegotiationStakeholder fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if team_id is not None and team_id != '': 
             Team.objects.get(pk=team_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = NegotiationStakeholder.objects.create(
            team_id=team_id,
            stakeholder_id=stakeholder_id,
            vendor_proposal_id=vendor_proposal_id,
            feedback=feedback,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Team.DoesNotExist:
        return error('Invalid Team ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_negotiationstakeholder(negotiationstakeholder_id,team_id=None, stakeholder_id=None, vendor_proposal_id=None, feedback=None):
    """
    Updates a NegotiationStakeholder instance with the provided data.
    
    Args:
        negotiationstakeholder_id (int): ID of the NegotiationStakeholder to update.
        team_id=None, stakeholder_id=None, vendor_proposal_id=None, feedback=None: Keyword arguments for NegotiationStakeholder fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if team_id is not None and team_id != '': 
             Team.objects.get(pk=team_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = NegotiationStakeholder.objects.get(pk=negotiationstakeholder_id)
        instance.team_id = team_id if team_id is not None else instance.team_id
        instance.stakeholder_id = stakeholder_id if stakeholder_id is not None else instance.stakeholder_id
        instance.vendor_proposal_id = vendor_proposal_id if vendor_proposal_id is not None else instance.vendor_proposal_id
        instance.feedback = feedback if feedback is not None else instance.feedback
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Team.DoesNotExist:
        return error('Invalid Team ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except  NegotiationStakeholder.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_negotiationstakeholder(negotiationstakeholder_id=None):
    """
    Retrieves and serializes a NegotiationStakeholder instance by its ID or all instances if ID is None.
    
    Args:
        NegotiationStakeholder_id (int, optional): ID of the NegotiationStakeholder to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if negotiationstakeholder_id is not None:
            record = NegotiationStakeholder.objects.get(pk=negotiationstakeholder_id)
            serializer = NegotiationStakeholderSerializer(record)
        else:
            records = NegotiationStakeholder.objects.all()
            serializer = NegotiationStakeholderSerializer(records, many=True)
        return success(serializer.data)
    
    except NegotiationStakeholder.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('NegotiationStakeholder does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_negotiationstakeholder(negotiationstakeholder_id):
    """
    Deletes a NegotiationStakeholder instance with the given ID.
    
    Args:
        negotiationstakeholder_id (int): ID of the NegotiationStakeholder to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = NegotiationStakeholder.objects.get(pk=negotiationstakeholder_id)
        instance.delete()
        return success("Successfully deleted")
    
    except NegotiationStakeholder.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_negotiationterm(description, proposed_value, negotiated_value, vendor_proposal_id):
    """
    Creates a NegotiationTerm instance with the provided data.
        Args:
        description, proposed_value, negotiated_value, vendor_proposal_id: Keyword arguments for NegotiationTerm fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = NegotiationTerm.objects.create(
            description=description,
            proposed_value=proposed_value,
            negotiated_value=negotiated_value,
            vendor_proposal_id=vendor_proposal_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_negotiationterm(negotiationterm_id,description=None, proposed_value=None, negotiated_value=None, vendor_proposal_id=None):
    """
    Updates a NegotiationTerm instance with the provided data.
    
    Args:
        negotiationterm_id (int): ID of the NegotiationTerm to update.
        description=None, proposed_value=None, negotiated_value=None, vendor_proposal_id=None: Keyword arguments for NegotiationTerm fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if vendor_proposal_id is not None and vendor_proposal_id != '': 
             VendorProposal.objects.get(pk=vendor_proposal_id)
        instance = NegotiationTerm.objects.get(pk=negotiationterm_id)
        instance.description = description if description is not None else instance.description
        instance.proposed_value = proposed_value if proposed_value is not None else instance.proposed_value
        instance.negotiated_value = negotiated_value if negotiated_value is not None else instance.negotiated_value
        instance.vendor_proposal_id = vendor_proposal_id if vendor_proposal_id is not None else instance.vendor_proposal_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except  NegotiationTerm.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_negotiationterm(negotiationterm_id=None):
    """
    Retrieves and serializes a NegotiationTerm instance by its ID or all instances if ID is None.
    
    Args:
        NegotiationTerm_id (int, optional): ID of the NegotiationTerm to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if negotiationterm_id is not None:
            record = NegotiationTerm.objects.get(pk=negotiationterm_id)
            serializer = NegotiationTermSerializer(record)
        else:
            records = NegotiationTerm.objects.all()
            serializer = NegotiationTermSerializer(records, many=True)
        return success(serializer.data)
    
    except NegotiationTerm.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('NegotiationTerm does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_negotiationterm(negotiationterm_id):
    """
    Deletes a NegotiationTerm instance with the given ID.
    
    Args:
        negotiationterm_id (int): ID of the NegotiationTerm to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = NegotiationTerm.objects.get(pk=negotiationterm_id)
        instance.delete()
        return success("Successfully deleted")
    
    except NegotiationTerm.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_proposalcompliance(proposal_id, certification_compliance, technical_spec_compliance, other_compliance):
    """
    Creates a ProposalCompliance instance with the provided data.
        Args:
        proposal_id, certification_compliance, technical_spec_compliance, other_compliance: Keyword arguments for ProposalCompliance fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             VendorProposal.objects.get(pk=proposal_id)
        instance = ProposalCompliance.objects.create(
            proposal_id=proposal_id,
            certification_compliance=certification_compliance,
            technical_spec_compliance=technical_spec_compliance,
            other_compliance=other_compliance,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_proposalcompliance(proposalcompliance_id,proposal_id=None, certification_compliance=None, technical_spec_compliance=None, other_compliance=None):
    """
    Updates a ProposalCompliance instance with the provided data.
    
    Args:
        proposalcompliance_id (int): ID of the ProposalCompliance to update.
        proposal_id=None, certification_compliance=None, technical_spec_compliance=None, other_compliance=None: Keyword arguments for ProposalCompliance fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             VendorProposal.objects.get(pk=proposal_id)
        instance = ProposalCompliance.objects.get(pk=proposalcompliance_id)
        instance.proposal_id = proposal_id if proposal_id is not None else instance.proposal_id
        instance.certification_compliance = certification_compliance if certification_compliance is not None else instance.certification_compliance
        instance.technical_spec_compliance = technical_spec_compliance if technical_spec_compliance is not None else instance.technical_spec_compliance
        instance.other_compliance = other_compliance if other_compliance is not None else instance.other_compliance
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except  ProposalCompliance.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_proposalcompliance(proposalcompliance_id=None):
    """
    Retrieves and serializes a ProposalCompliance instance by its ID or all instances if ID is None.
    
    Args:
        ProposalCompliance_id (int, optional): ID of the ProposalCompliance to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposalcompliance_id is not None:
            record = ProposalCompliance.objects.get(pk=proposalcompliance_id)
            serializer = ProposalComplianceSerializer(record)
        else:
            records = ProposalCompliance.objects.all()
            serializer = ProposalComplianceSerializer(records, many=True)
        return success(serializer.data)
    
    except ProposalCompliance.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProposalCompliance does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_proposalcompliance(proposalcompliance_id):
    """
    Deletes a ProposalCompliance instance with the given ID.
    
    Args:
        proposalcompliance_id (int): ID of the ProposalCompliance to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProposalCompliance.objects.get(pk=proposalcompliance_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProposalCompliance.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_proposalscoring(proposal_id, criteria_id, score):
    """
    Creates a ProposalScoring instance with the provided data.
        Args:
        proposal_id, criteria_id, score: Keyword arguments for ProposalScoring fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             VendorProposal.objects.get(pk=proposal_id)
        if criteria_id is not None and criteria_id != '': 
             ScoringCriteria.objects.get(pk=criteria_id)
        instance = ProposalScoring.objects.create(
            proposal_id=proposal_id,
            criteria_id=criteria_id,
            score=score,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ScoringCriteria.DoesNotExist:
        return error('Invalid ScoringCriteria ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_proposalscoring(proposalscoring_id,proposal_id=None, criteria_id=None, score=None):
    """
    Updates a ProposalScoring instance with the provided data.
    
    Args:
        proposalscoring_id (int): ID of the ProposalScoring to update.
        proposal_id=None, criteria_id=None, score=None: Keyword arguments for ProposalScoring fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None and proposal_id != '': 
             VendorProposal.objects.get(pk=proposal_id)
        if criteria_id is not None and criteria_id != '': 
             ScoringCriteria.objects.get(pk=criteria_id)
        instance = ProposalScoring.objects.get(pk=proposalscoring_id)
        instance.proposal_id = proposal_id if proposal_id is not None else instance.proposal_id
        instance.criteria_id = criteria_id if criteria_id is not None else instance.criteria_id
        instance.score = score if score is not None else instance.score
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except VendorProposal.DoesNotExist:
        return error('Invalid VendorProposal ID: Destination not found.')
    except ScoringCriteria.DoesNotExist:
        return error('Invalid ScoringCriteria ID: Destination not found.')
    except  ProposalScoring.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_proposalscoring(proposalscoring_id=None):
    """
    Retrieves and serializes a ProposalScoring instance by its ID or all instances if ID is None.
    
    Args:
        ProposalScoring_id (int, optional): ID of the ProposalScoring to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposalscoring_id is not None:
            record = ProposalScoring.objects.get(pk=proposalscoring_id)
            serializer = ProposalScoringSerializer(record)
        else:
            records = ProposalScoring.objects.all()
            serializer = ProposalScoringSerializer(records, many=True)
        return success(serializer.data)
    
    except ProposalScoring.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProposalScoring does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_proposalscoring(proposalscoring_id):
    """
    Deletes a ProposalScoring instance with the given ID.
    
    Args:
        proposalscoring_id (int): ID of the ProposalScoring to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProposalScoring.objects.get(pk=proposalscoring_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProposalScoring.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_proposal(opportunity_id, status, negotiation_notes):
    """
    Creates a Proposal instance with the provided data.
        Args:
        opportunity_id, status, negotiation_notes: Keyword arguments for Proposal fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             Opportunity.objects.get(pk=opportunity_id)
        instance = Proposal.objects.create(
            opportunity_id=opportunity_id,
            status=status,
            negotiation_notes=negotiation_notes,
        )
        return success(f'Successfully created {instance}')
    except Opportunity.DoesNotExist:
        return error('Invalid Opportunity ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_proposal(proposal_id,opportunity_id=None, status=None, negotiation_notes=None):
    """
    Updates a Proposal instance with the provided data.
    
    Args:
        proposal_id (int): ID of the Proposal to update.
        opportunity_id=None, status=None, negotiation_notes=None: Keyword arguments for Proposal fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if opportunity_id is not None and opportunity_id != '': 
             Opportunity.objects.get(pk=opportunity_id)
        instance = Proposal.objects.get(pk=proposal_id)
        instance.opportunity_id = opportunity_id if opportunity_id is not None else instance.opportunity_id
        instance.status = status if status is not None else instance.status
        instance.negotiation_notes = negotiation_notes if negotiation_notes is not None else instance.negotiation_notes
        instance.save()
        return success('Successfully Updated')
    except Opportunity.DoesNotExist:
        return error('Invalid Opportunity ID: Destination not found.')
    except  Proposal.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_proposal(proposal_id=None):
    """
    Retrieves and serializes a Proposal instance by its ID or all instances if ID is None.
    
    Args:
        Proposal_id (int, optional): ID of the Proposal to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if proposal_id is not None:
            record = Proposal.objects.get(pk=proposal_id)
            serializer = ProposalSerializer(record)
        else:
            records = Proposal.objects.all()
            serializer = ProposalSerializer(records, many=True)
        return success(serializer.data)
    
    except Proposal.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Proposal does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_proposal(proposal_id):
    """
    Deletes a Proposal instance with the given ID.
    
    Args:
        proposal_id (int): ID of the Proposal to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Proposal.objects.get(pk=proposal_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Proposal.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_auditlog(contract_id, change_order_id, action, action_by, notes):
    """
    Creates a AuditLog instance with the provided data.
        Args:
        contract_id, change_order_id, action, action_by, notes: Keyword arguments for AuditLog fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        if change_order_id is not None and change_order_id != '': 
             ChangeOrder.objects.get(pk=change_order_id)
        instance = AuditLog.objects.create(
            contract_id=contract_id,
            change_order_id=change_order_id,
            action=action,
            action_by=action_by,
            notes=notes,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ChangeOrder.DoesNotExist:
        return error('Invalid ChangeOrder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_auditlog(auditlog_id,contract_id=None, change_order_id=None, action=None, action_by=None, notes=None):
    """
    Updates a AuditLog instance with the provided data.
    
    Args:
        auditlog_id (int): ID of the AuditLog to update.
        contract_id=None, change_order_id=None, action=None, action_by=None, notes=None: Keyword arguments for AuditLog fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        if change_order_id is not None and change_order_id != '': 
             ChangeOrder.objects.get(pk=change_order_id)
        instance = AuditLog.objects.get(pk=auditlog_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.change_order_id = change_order_id if change_order_id is not None else instance.change_order_id
        instance.action = action if action is not None else instance.action
        instance.action_by = action_by if action_by is not None else instance.action_by
        instance.notes = notes if notes is not None else instance.notes
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ChangeOrder.DoesNotExist:
        return error('Invalid ChangeOrder ID: Destination not found.')
    except  AuditLog.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_auditlog(auditlog_id=None):
    """
    Retrieves and serializes a AuditLog instance by its ID or all instances if ID is None.
    
    Args:
        AuditLog_id (int, optional): ID of the AuditLog to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if auditlog_id is not None:
            record = AuditLog.objects.get(pk=auditlog_id)
            serializer = AuditLogSerializer(record)
        else:
            records = AuditLog.objects.all()
            serializer = AuditLogSerializer(records, many=True)
        return success(serializer.data)
    
    except AuditLog.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('AuditLog does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_auditlog(auditlog_id):
    """
    Deletes a AuditLog instance with the given ID.
    
    Args:
        auditlog_id (int): ID of the AuditLog to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = AuditLog.objects.get(pk=auditlog_id)
        instance.delete()
        return success("Successfully deleted")
    
    except AuditLog.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_document(contract_id, change_order_id, document_name, upload_date):
    """
    Creates a Document instance with the provided data.
        Args:
        contract_id, change_order_id, document_name, upload_date: Keyword arguments for Document fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        if change_order_id is not None and change_order_id != '': 
             ChangeOrder.objects.get(pk=change_order_id)
        instance = Document.objects.create(
            contract_id=contract_id,
            change_order_id=change_order_id,
            document_name=document_name,
            upload_date=upload_date,
        )
        return success(f'Successfully created {instance}')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ChangeOrder.DoesNotExist:
        return error('Invalid ChangeOrder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_document(document_id,contract_id=None, change_order_id=None, document_name=None, upload_date=None):
    """
    Updates a Document instance with the provided data.
    
    Args:
        document_id (int): ID of the Document to update.
        contract_id=None, change_order_id=None, document_name=None, upload_date=None: Keyword arguments for Document fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if contract_id is not None and contract_id != '': 
             Contract.objects.get(pk=contract_id)
        if change_order_id is not None and change_order_id != '': 
             ChangeOrder.objects.get(pk=change_order_id)
        instance = Document.objects.get(pk=document_id)
        instance.contract_id = contract_id if contract_id is not None else instance.contract_id
        instance.change_order_id = change_order_id if change_order_id is not None else instance.change_order_id
        instance.document_name = document_name if document_name is not None else instance.document_name
        instance.upload_date = upload_date if upload_date is not None else instance.upload_date
        instance.save()
        return success('Successfully Updated')
    except Contract.DoesNotExist:
        return error('Invalid Contract ID: Destination not found.')
    except ChangeOrder.DoesNotExist:
        return error('Invalid ChangeOrder ID: Destination not found.')
    except  Document.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_document(document_id=None):
    """
    Retrieves and serializes a Document instance by its ID or all instances if ID is None.
    
    Args:
        Document_id (int, optional): ID of the Document to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if document_id is not None:
            record = Document.objects.get(pk=document_id)
            serializer = DocumentSerializer(record)
        else:
            records = Document.objects.all()
            serializer = DocumentSerializer(records, many=True)
        return success(serializer.data)
    
    except Document.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Document does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_document(document_id):
    """
    Deletes a Document instance with the given ID.
    
    Args:
        document_id (int): ID of the Document to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Document.objects.get(pk=document_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Document.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_invoice(purchase_order_id, vendor_name, invoice_number, invoice_date, total_amount, payment_status):
    """
    Creates a Invoice instance with the provided data.
        Args:
        purchase_order_id, vendor_name, invoice_number, invoice_date, total_amount, payment_status: Keyword arguments for Invoice fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if purchase_order_id is not None and purchase_order_id != '': 
             PurchaseOrder.objects.get(pk=purchase_order_id)
        instance = Invoice.objects.create(
            purchase_order_id=purchase_order_id,
            vendor_name=vendor_name,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            total_amount=total_amount,
            payment_status=payment_status,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except PurchaseOrder.DoesNotExist:
        return error('Invalid PurchaseOrder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_invoice(invoice_id,purchase_order_id=None, vendor_name=None, invoice_number=None, invoice_date=None, total_amount=None, payment_status=None):
    """
    Updates a Invoice instance with the provided data.
    
    Args:
        invoice_id (int): ID of the Invoice to update.
        purchase_order_id=None, vendor_name=None, invoice_number=None, invoice_date=None, total_amount=None, payment_status=None: Keyword arguments for Invoice fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if purchase_order_id is not None and purchase_order_id != '': 
             PurchaseOrder.objects.get(pk=purchase_order_id)
        instance = Invoice.objects.get(pk=invoice_id)
        instance.purchase_order_id = purchase_order_id if purchase_order_id is not None else instance.purchase_order_id
        instance.vendor_name = vendor_name if vendor_name is not None else instance.vendor_name
        instance.invoice_number = invoice_number if invoice_number is not None else instance.invoice_number
        instance.invoice_date = invoice_date if invoice_date is not None else instance.invoice_date
        instance.total_amount = total_amount if total_amount is not None else instance.total_amount
        instance.payment_status = payment_status if payment_status is not None else instance.payment_status
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except PurchaseOrder.DoesNotExist:
        return error('Invalid PurchaseOrder ID: Destination not found.')
    except  Invoice.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_invoice(invoice_id=None):
    """
    Retrieves and serializes a Invoice instance by its ID or all instances if ID is None.
    
    Args:
        Invoice_id (int, optional): ID of the Invoice to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if invoice_id is not None:
            record = Invoice.objects.get(pk=invoice_id)
            serializer = InvoiceSerializer(record)
        else:
            records = Invoice.objects.all()
            serializer = InvoiceSerializer(records, many=True)
        return success(serializer.data)
    
    except Invoice.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Invoice does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_invoice(invoice_id):
    """
    Deletes a Invoice instance with the given ID.
    
    Args:
        invoice_id (int): ID of the Invoice to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Invoice.objects.get(pk=invoice_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Invoice.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_shipment(purchase_order_id, shipment_number):
    """
    Creates a Shipment instance with the provided data.
        Args:
        purchase_order_id, shipment_number: Keyword arguments for Shipment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if purchase_order_id is not None and purchase_order_id != '': 
             PurchaseOrder.objects.get(pk=purchase_order_id)
        instance = Shipment.objects.create(
            purchase_order_id=purchase_order_id,
            shipment_number=shipment_number,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except PurchaseOrder.DoesNotExist:
        return error('Invalid PurchaseOrder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_shipment(shipment_id,purchase_order_id=None, shipment_number=None):
    """
    Updates a Shipment instance with the provided data.
    
    Args:
        shipment_id (int): ID of the Shipment to update.
        purchase_order_id=None, shipment_number=None: Keyword arguments for Shipment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if purchase_order_id is not None and purchase_order_id != '': 
             PurchaseOrder.objects.get(pk=purchase_order_id)
        instance = Shipment.objects.get(pk=shipment_id)
        instance.purchase_order_id = purchase_order_id if purchase_order_id is not None else instance.purchase_order_id
        instance.shipment_number = shipment_number if shipment_number is not None else instance.shipment_number
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except PurchaseOrder.DoesNotExist:
        return error('Invalid PurchaseOrder ID: Destination not found.')
    except  Shipment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_shipment(shipment_id=None):
    """
    Retrieves and serializes a Shipment instance by its ID or all instances if ID is None.
    
    Args:
        Shipment_id (int, optional): ID of the Shipment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if shipment_id is not None:
            record = Shipment.objects.get(pk=shipment_id)
            serializer = ShipmentSerializer(record)
        else:
            records = Shipment.objects.all()
            serializer = ShipmentSerializer(records, many=True)
        return success(serializer.data)
    
    except Shipment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Shipment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_shipment(shipment_id):
    """
    Deletes a Shipment instance with the given ID.
    
    Args:
        shipment_id (int): ID of the Shipment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Shipment.objects.get(pk=shipment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Shipment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_criticalpath(project_id, task_id, estimated_duration, is_on_critical_path):
    """
    Creates a CriticalPath instance with the provided data.
        Args:
        project_id, task_id, estimated_duration, is_on_critical_path: Keyword arguments for CriticalPath fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = CriticalPath.objects.create(
            project_id=project_id,
            task_id=task_id,
            estimated_duration=estimated_duration,
            is_on_critical_path=is_on_critical_path,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_criticalpath(criticalpath_id,project_id=None, task_id=None, estimated_duration=None, is_on_critical_path=None):
    """
    Updates a CriticalPath instance with the provided data.
    
    Args:
        criticalpath_id (int): ID of the CriticalPath to update.
        project_id=None, task_id=None, estimated_duration=None, is_on_critical_path=None: Keyword arguments for CriticalPath fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = CriticalPath.objects.get(pk=criticalpath_id)
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.estimated_duration = estimated_duration if estimated_duration is not None else instance.estimated_duration
        instance.is_on_critical_path = is_on_critical_path if is_on_critical_path is not None else instance.is_on_critical_path
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  CriticalPath.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_criticalpath(criticalpath_id=None):
    """
    Retrieves and serializes a CriticalPath instance by its ID or all instances if ID is None.
    
    Args:
        CriticalPath_id (int, optional): ID of the CriticalPath to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if criticalpath_id is not None:
            record = CriticalPath.objects.get(pk=criticalpath_id)
            serializer = CriticalPathSerializer(record)
        else:
            records = CriticalPath.objects.all()
            serializer = CriticalPathSerializer(records, many=True)
        return success(serializer.data)
    
    except CriticalPath.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CriticalPath does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_criticalpath(criticalpath_id):
    """
    Deletes a CriticalPath instance with the given ID.
    
    Args:
        criticalpath_id (int): ID of the CriticalPath to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CriticalPath.objects.get(pk=criticalpath_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CriticalPath.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_dailyprogressreport(task_id, report_date, description, worker_count, machinery_in_use, materials_used, completion_percentage, progress_percentage, issues_encountered, reported_by_id):
    """
    Creates a DailyProgressReport instance with the provided data.
        Args:
        task_id, report_date, description, worker_count, machinery_in_use, materials_used, completion_percentage, progress_percentage, issues_encountered, reported_by_id: Keyword arguments for DailyProgressReport fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = DailyProgressReport.objects.create(
            task_id=task_id,
            report_date=report_date,
            description=description,
            worker_count=worker_count,
            machinery_in_use=machinery_in_use,
            materials_used=materials_used,
            completion_percentage=completion_percentage,
            progress_percentage=progress_percentage,
            issues_encountered=issues_encountered,
            reported_by_id=reported_by_id,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_dailyprogressreport(dailyprogressreport_id,task_id=None, report_date=None, description=None, worker_count=None, machinery_in_use=None, materials_used=None, completion_percentage=None, progress_percentage=None, issues_encountered=None, reported_by_id=None):
    """
    Updates a DailyProgressReport instance with the provided data.
    
    Args:
        dailyprogressreport_id (int): ID of the DailyProgressReport to update.
        task_id=None, report_date=None, description=None, worker_count=None, machinery_in_use=None, materials_used=None, completion_percentage=None, progress_percentage=None, issues_encountered=None, reported_by_id=None: Keyword arguments for DailyProgressReport fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = DailyProgressReport.objects.get(pk=dailyprogressreport_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.report_date = report_date if report_date is not None else instance.report_date
        instance.description = description if description is not None else instance.description
        instance.worker_count = worker_count if worker_count is not None else instance.worker_count
        instance.machinery_in_use = machinery_in_use if machinery_in_use is not None else instance.machinery_in_use
        instance.materials_used = materials_used if materials_used is not None else instance.materials_used
        instance.completion_percentage = completion_percentage if completion_percentage is not None else instance.completion_percentage
        instance.progress_percentage = progress_percentage if progress_percentage is not None else instance.progress_percentage
        instance.issues_encountered = issues_encountered if issues_encountered is not None else instance.issues_encountered
        instance.reported_by_id = reported_by_id if reported_by_id is not None else instance.reported_by_id
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  DailyProgressReport.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_dailyprogressreport(dailyprogressreport_id=None):
    """
    Retrieves and serializes a DailyProgressReport instance by its ID or all instances if ID is None.
    
    Args:
        DailyProgressReport_id (int, optional): ID of the DailyProgressReport to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if dailyprogressreport_id is not None:
            record = DailyProgressReport.objects.get(pk=dailyprogressreport_id)
            serializer = DailyProgressReportSerializer(record)
        else:
            records = DailyProgressReport.objects.all()
            serializer = DailyProgressReportSerializer(records, many=True)
        return success(serializer.data)
    
    except DailyProgressReport.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('DailyProgressReport does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_dailyprogressreport(dailyprogressreport_id):
    """
    Deletes a DailyProgressReport instance with the given ID.
    
    Args:
        dailyprogressreport_id (int): ID of the DailyProgressReport to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = DailyProgressReport.objects.get(pk=dailyprogressreport_id)
        instance.delete()
        return success("Successfully deleted")
    
    except DailyProgressReport.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_delay(task_id, cause_id, reported_by_id, notes):
    """
    Creates a Delay instance with the provided data.
        Args:
        task_id, cause_id, reported_by_id, notes: Keyword arguments for Delay fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if cause_id is not None and cause_id != '': 
             DelayCause.objects.get(pk=cause_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = Delay.objects.create(
            task_id=task_id,
            cause_id=cause_id,
            reported_by_id=reported_by_id,
            notes=notes,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except DelayCause.DoesNotExist:
        return error('Invalid DelayCause ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_delay(delay_id,task_id=None, cause_id=None, reported_by_id=None, notes=None):
    """
    Updates a Delay instance with the provided data.
    
    Args:
        delay_id (int): ID of the Delay to update.
        task_id=None, cause_id=None, reported_by_id=None, notes=None: Keyword arguments for Delay fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if cause_id is not None and cause_id != '': 
             DelayCause.objects.get(pk=cause_id)
        if reported_by_id is not None and reported_by_id != '': 
             User.objects.get(pk=reported_by_id)
        instance = Delay.objects.get(pk=delay_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.cause_id = cause_id if cause_id is not None else instance.cause_id
        instance.reported_by_id = reported_by_id if reported_by_id is not None else instance.reported_by_id
        instance.notes = notes if notes is not None else instance.notes
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except DelayCause.DoesNotExist:
        return error('Invalid DelayCause ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  Delay.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_delay(delay_id=None):
    """
    Retrieves and serializes a Delay instance by its ID or all instances if ID is None.
    
    Args:
        Delay_id (int, optional): ID of the Delay to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if delay_id is not None:
            record = Delay.objects.get(pk=delay_id)
            serializer = DelaySerializer(record)
        else:
            records = Delay.objects.all()
            serializer = DelaySerializer(records, many=True)
        return success(serializer.data)
    
    except Delay.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Delay does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_delay(delay_id):
    """
    Deletes a Delay instance with the given ID.
    
    Args:
        delay_id (int): ID of the Delay to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Delay.objects.get(pk=delay_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Delay.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_performancereport(subcontractor_id, project_id, task_id, report_date, tasks_completed, issues_encountered, safety_compliance):
    """
    Creates a PerformanceReport instance with the provided data.
        Args:
        subcontractor_id, project_id, task_id, report_date, tasks_completed, issues_encountered, safety_compliance: Keyword arguments for PerformanceReport fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = PerformanceReport.objects.create(
            subcontractor_id=subcontractor_id,
            project_id=project_id,
            task_id=task_id,
            report_date=report_date,
            tasks_completed=tasks_completed,
            issues_encountered=issues_encountered,
            safety_compliance=safety_compliance,
        )
        return success(f'Successfully created {instance}')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_performancereport(performancereport_id,subcontractor_id=None, project_id=None, task_id=None, report_date=None, tasks_completed=None, issues_encountered=None, safety_compliance=None):
    """
    Updates a PerformanceReport instance with the provided data.
    
    Args:
        performancereport_id (int): ID of the PerformanceReport to update.
        subcontractor_id=None, project_id=None, task_id=None, report_date=None, tasks_completed=None, issues_encountered=None, safety_compliance=None: Keyword arguments for PerformanceReport fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if subcontractor_id is not None and subcontractor_id != '': 
             Subcontractor.objects.get(pk=subcontractor_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = PerformanceReport.objects.get(pk=performancereport_id)
        instance.subcontractor_id = subcontractor_id if subcontractor_id is not None else instance.subcontractor_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.report_date = report_date if report_date is not None else instance.report_date
        instance.tasks_completed = tasks_completed if tasks_completed is not None else instance.tasks_completed
        instance.issues_encountered = issues_encountered if issues_encountered is not None else instance.issues_encountered
        instance.safety_compliance = safety_compliance if safety_compliance is not None else instance.safety_compliance
        instance.save()
        return success('Successfully Updated')
    except Subcontractor.DoesNotExist:
        return error('Invalid Subcontractor ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  PerformanceReport.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_performancereport(performancereport_id=None):
    """
    Retrieves and serializes a PerformanceReport instance by its ID or all instances if ID is None.
    
    Args:
        PerformanceReport_id (int, optional): ID of the PerformanceReport to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if performancereport_id is not None:
            record = PerformanceReport.objects.get(pk=performancereport_id)
            serializer = PerformanceReportSerializer(record)
        else:
            records = PerformanceReport.objects.all()
            serializer = PerformanceReportSerializer(records, many=True)
        return success(serializer.data)
    
    except PerformanceReport.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PerformanceReport does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_performancereport(performancereport_id):
    """
    Deletes a PerformanceReport instance with the given ID.
    
    Args:
        performancereport_id (int): ID of the PerformanceReport to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PerformanceReport.objects.get(pk=performancereport_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PerformanceReport.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_photodocumentation(task_id, description, geo_tag):
    """
    Creates a PhotoDocumentation instance with the provided data.
        Args:
        task_id, description, geo_tag: Keyword arguments for PhotoDocumentation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = PhotoDocumentation.objects.create(
            task_id=task_id,
            description=description,
            geo_tag=geo_tag,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_photodocumentation(photodocumentation_id,task_id=None, description=None, geo_tag=None):
    """
    Updates a PhotoDocumentation instance with the provided data.
    
    Args:
        photodocumentation_id (int): ID of the PhotoDocumentation to update.
        task_id=None, description=None, geo_tag=None: Keyword arguments for PhotoDocumentation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = PhotoDocumentation.objects.get(pk=photodocumentation_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.description = description if description is not None else instance.description
        instance.geo_tag = geo_tag if geo_tag is not None else instance.geo_tag
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  PhotoDocumentation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_photodocumentation(photodocumentation_id=None):
    """
    Retrieves and serializes a PhotoDocumentation instance by its ID or all instances if ID is None.
    
    Args:
        PhotoDocumentation_id (int, optional): ID of the PhotoDocumentation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if photodocumentation_id is not None:
            record = PhotoDocumentation.objects.get(pk=photodocumentation_id)
            serializer = PhotoDocumentationSerializer(record)
        else:
            records = PhotoDocumentation.objects.all()
            serializer = PhotoDocumentationSerializer(records, many=True)
        return success(serializer.data)
    
    except PhotoDocumentation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('PhotoDocumentation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_photodocumentation(photodocumentation_id):
    """
    Deletes a PhotoDocumentation instance with the given ID.
    
    Args:
        photodocumentation_id (int): ID of the PhotoDocumentation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = PhotoDocumentation.objects.get(pk=photodocumentation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except PhotoDocumentation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_projectupdate(task_id, date, planned_start_date, actual_start_date, planned_end_date, actual_end_date, progress_percentage, comments):
    """
    Creates a ProjectUpdate instance with the provided data.
        Args:
        task_id, date, planned_start_date, actual_start_date, planned_end_date, actual_end_date, progress_percentage, comments: Keyword arguments for ProjectUpdate fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = ProjectUpdate.objects.create(
            task_id=task_id,
            date=date,
            planned_start_date=planned_start_date,
            actual_start_date=actual_start_date,
            planned_end_date=planned_end_date,
            actual_end_date=actual_end_date,
            progress_percentage=progress_percentage,
            comments=comments,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_projectupdate(projectupdate_id,task_id=None, date=None, planned_start_date=None, actual_start_date=None, planned_end_date=None, actual_end_date=None, progress_percentage=None, comments=None):
    """
    Updates a ProjectUpdate instance with the provided data.
    
    Args:
        projectupdate_id (int): ID of the ProjectUpdate to update.
        task_id=None, date=None, planned_start_date=None, actual_start_date=None, planned_end_date=None, actual_end_date=None, progress_percentage=None, comments=None: Keyword arguments for ProjectUpdate fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = ProjectUpdate.objects.get(pk=projectupdate_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.date = date if date is not None else instance.date
        instance.planned_start_date = planned_start_date if planned_start_date is not None else instance.planned_start_date
        instance.actual_start_date = actual_start_date if actual_start_date is not None else instance.actual_start_date
        instance.planned_end_date = planned_end_date if planned_end_date is not None else instance.planned_end_date
        instance.actual_end_date = actual_end_date if actual_end_date is not None else instance.actual_end_date
        instance.progress_percentage = progress_percentage if progress_percentage is not None else instance.progress_percentage
        instance.comments = comments if comments is not None else instance.comments
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  ProjectUpdate.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_projectupdate(projectupdate_id=None):
    """
    Retrieves and serializes a ProjectUpdate instance by its ID or all instances if ID is None.
    
    Args:
        ProjectUpdate_id (int, optional): ID of the ProjectUpdate to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if projectupdate_id is not None:
            record = ProjectUpdate.objects.get(pk=projectupdate_id)
            serializer = ProjectUpdateSerializer(record)
        else:
            records = ProjectUpdate.objects.all()
            serializer = ProjectUpdateSerializer(records, many=True)
        return success(serializer.data)
    
    except ProjectUpdate.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ProjectUpdate does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_projectupdate(projectupdate_id):
    """
    Deletes a ProjectUpdate instance with the given ID.
    
    Args:
        projectupdate_id (int): ID of the ProjectUpdate to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ProjectUpdate.objects.get(pk=projectupdate_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ProjectUpdate.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceadjustment(task_id, resource_id, adjustment_date, new_schedule, reason):
    """
    Creates a ResourceAdjustment instance with the provided data.
        Args:
        task_id, resource_id, adjustment_date, new_schedule, reason: Keyword arguments for ResourceAdjustment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = ResourceAdjustment.objects.create(
            task_id=task_id,
            resource_id=resource_id,
            adjustment_date=adjustment_date,
            new_schedule=new_schedule,
            reason=reason,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceadjustment(resourceadjustment_id,task_id=None, resource_id=None, adjustment_date=None, new_schedule=None, reason=None):
    """
    Updates a ResourceAdjustment instance with the provided data.
    
    Args:
        resourceadjustment_id (int): ID of the ResourceAdjustment to update.
        task_id=None, resource_id=None, adjustment_date=None, new_schedule=None, reason=None: Keyword arguments for ResourceAdjustment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = ResourceAdjustment.objects.get(pk=resourceadjustment_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.resource_id = resource_id if resource_id is not None else instance.resource_id
        instance.adjustment_date = adjustment_date if adjustment_date is not None else instance.adjustment_date
        instance.new_schedule = new_schedule if new_schedule is not None else instance.new_schedule
        instance.reason = reason if reason is not None else instance.reason
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except  ResourceAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceadjustment(resourceadjustment_id=None):
    """
    Retrieves and serializes a ResourceAdjustment instance by its ID or all instances if ID is None.
    
    Args:
        ResourceAdjustment_id (int, optional): ID of the ResourceAdjustment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceadjustment_id is not None:
            record = ResourceAdjustment.objects.get(pk=resourceadjustment_id)
            serializer = ResourceAdjustmentSerializer(record)
        else:
            records = ResourceAdjustment.objects.all()
            serializer = ResourceAdjustmentSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceAdjustment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceAdjustment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceadjustment(resourceadjustment_id):
    """
    Deletes a ResourceAdjustment instance with the given ID.
    
    Args:
        resourceadjustment_id (int): ID of the ResourceAdjustment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceAdjustment.objects.get(pk=resourceadjustment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceallocation(task_id, resource_type, allocated_quantity, allocated_by_id):
    """
    Creates a ResourceAllocation instance with the provided data.
        Args:
        task_id, resource_type, allocated_quantity, allocated_by_id: Keyword arguments for ResourceAllocation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if allocated_by_id is not None and allocated_by_id != '': 
             User.objects.get(pk=allocated_by_id)
        instance = ResourceAllocation.objects.create(
            task_id=task_id,
            resource_type=resource_type,
            allocated_quantity=allocated_quantity,
            allocated_by_id=allocated_by_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceallocation(resourceallocation_id,task_id=None, resource_type=None, allocated_quantity=None, allocated_by_id=None):
    """
    Updates a ResourceAllocation instance with the provided data.
    
    Args:
        resourceallocation_id (int): ID of the ResourceAllocation to update.
        task_id=None, resource_type=None, allocated_quantity=None, allocated_by_id=None: Keyword arguments for ResourceAllocation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if allocated_by_id is not None and allocated_by_id != '': 
             User.objects.get(pk=allocated_by_id)
        instance = ResourceAllocation.objects.get(pk=resourceallocation_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.resource_type = resource_type if resource_type is not None else instance.resource_type
        instance.allocated_quantity = allocated_quantity if allocated_quantity is not None else instance.allocated_quantity
        instance.allocated_by_id = allocated_by_id if allocated_by_id is not None else instance.allocated_by_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  ResourceAllocation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceallocation(resourceallocation_id=None):
    """
    Retrieves and serializes a ResourceAllocation instance by its ID or all instances if ID is None.
    
    Args:
        ResourceAllocation_id (int, optional): ID of the ResourceAllocation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceallocation_id is not None:
            record = ResourceAllocation.objects.get(pk=resourceallocation_id)
            serializer = ResourceAllocationSerializer(record)
        else:
            records = ResourceAllocation.objects.all()
            serializer = ResourceAllocationSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceAllocation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceAllocation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceallocation(resourceallocation_id):
    """
    Deletes a ResourceAllocation instance with the given ID.
    
    Args:
        resourceallocation_id (int): ID of the ResourceAllocation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceAllocation.objects.get(pk=resourceallocation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceAllocation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskdependency(task_id, dependent_task_id):
    """
    Creates a TaskDependency instance with the provided data.
        Args:
        task_id, dependent_task_id: Keyword arguments for TaskDependency fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if dependent_task_id is not None and dependent_task_id != '': 
             Task.objects.get(pk=dependent_task_id)
        instance = TaskDependency.objects.create(
            task_id=task_id,
            dependent_task_id=dependent_task_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskdependency(taskdependency_id,task_id=None, dependent_task_id=None):
    """
    Updates a TaskDependency instance with the provided data.
    
    Args:
        taskdependency_id (int): ID of the TaskDependency to update.
        task_id=None, dependent_task_id=None: Keyword arguments for TaskDependency fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if dependent_task_id is not None and dependent_task_id != '': 
             Task.objects.get(pk=dependent_task_id)
        instance = TaskDependency.objects.get(pk=taskdependency_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.dependent_task_id = dependent_task_id if dependent_task_id is not None else instance.dependent_task_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  TaskDependency.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskdependency(taskdependency_id=None):
    """
    Retrieves and serializes a TaskDependency instance by its ID or all instances if ID is None.
    
    Args:
        TaskDependency_id (int, optional): ID of the TaskDependency to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskdependency_id is not None:
            record = TaskDependency.objects.get(pk=taskdependency_id)
            serializer = TaskDependencySerializer(record)
        else:
            records = TaskDependency.objects.all()
            serializer = TaskDependencySerializer(records, many=True)
        return success(serializer.data)
    
    except TaskDependency.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskDependency does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskdependency(taskdependency_id):
    """
    Deletes a TaskDependency instance with the given ID.
    
    Args:
        taskdependency_id (int): ID of the TaskDependency to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskDependency.objects.get(pk=taskdependency_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskDependency.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskresourceallocation(task_id, resource_id, quantity):
    """
    Creates a TaskResourceAllocation instance with the provided data.
        Args:
        task_id, resource_id, quantity: Keyword arguments for TaskResourceAllocation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = TaskResourceAllocation.objects.create(
            task_id=task_id,
            resource_id=resource_id,
            quantity=quantity,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskresourceallocation(taskresourceallocation_id,task_id=None, resource_id=None, quantity=None):
    """
    Updates a TaskResourceAllocation instance with the provided data.
    
    Args:
        taskresourceallocation_id (int): ID of the TaskResourceAllocation to update.
        task_id=None, resource_id=None, quantity=None: Keyword arguments for TaskResourceAllocation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if resource_id is not None and resource_id != '': 
             Resource.objects.get(pk=resource_id)
        instance = TaskResourceAllocation.objects.get(pk=taskresourceallocation_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.resource_id = resource_id if resource_id is not None else instance.resource_id
        instance.quantity = quantity if quantity is not None else instance.quantity
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except Resource.DoesNotExist:
        return error('Invalid Resource ID: Destination not found.')
    except  TaskResourceAllocation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskresourceallocation(taskresourceallocation_id=None):
    """
    Retrieves and serializes a TaskResourceAllocation instance by its ID or all instances if ID is None.
    
    Args:
        TaskResourceAllocation_id (int, optional): ID of the TaskResourceAllocation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskresourceallocation_id is not None:
            record = TaskResourceAllocation.objects.get(pk=taskresourceallocation_id)
            serializer = TaskResourceAllocationSerializer(record)
        else:
            records = TaskResourceAllocation.objects.all()
            serializer = TaskResourceAllocationSerializer(records, many=True)
        return success(serializer.data)
    
    except TaskResourceAllocation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskResourceAllocation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskresourceallocation(taskresourceallocation_id):
    """
    Deletes a TaskResourceAllocation instance with the given ID.
    
    Args:
        taskresourceallocation_id (int): ID of the TaskResourceAllocation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskResourceAllocation.objects.get(pk=taskresourceallocation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskResourceAllocation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskschedule(task_id, scheduled_start_date, scheduled_end_date):
    """
    Creates a TaskSchedule instance with the provided data.
        Args:
        task_id, scheduled_start_date, scheduled_end_date: Keyword arguments for TaskSchedule fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = TaskSchedule.objects.create(
            task_id=task_id,
            scheduled_start_date=scheduled_start_date,
            scheduled_end_date=scheduled_end_date,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskschedule(taskschedule_id,task_id=None, scheduled_start_date=None, scheduled_end_date=None):
    """
    Updates a TaskSchedule instance with the provided data.
    
    Args:
        taskschedule_id (int): ID of the TaskSchedule to update.
        task_id=None, scheduled_start_date=None, scheduled_end_date=None: Keyword arguments for TaskSchedule fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = TaskSchedule.objects.get(pk=taskschedule_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.scheduled_start_date = scheduled_start_date if scheduled_start_date is not None else instance.scheduled_start_date
        instance.scheduled_end_date = scheduled_end_date if scheduled_end_date is not None else instance.scheduled_end_date
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  TaskSchedule.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskschedule(taskschedule_id=None):
    """
    Retrieves and serializes a TaskSchedule instance by its ID or all instances if ID is None.
    
    Args:
        TaskSchedule_id (int, optional): ID of the TaskSchedule to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskschedule_id is not None:
            record = TaskSchedule.objects.get(pk=taskschedule_id)
            serializer = TaskScheduleSerializer(record)
        else:
            records = TaskSchedule.objects.all()
            serializer = TaskScheduleSerializer(records, many=True)
        return success(serializer.data)
    
    except TaskSchedule.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskSchedule does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskschedule(taskschedule_id):
    """
    Deletes a TaskSchedule instance with the given ID.
    
    Args:
        taskschedule_id (int): ID of the TaskSchedule to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskSchedule.objects.get(pk=taskschedule_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskSchedule.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_taskstatus(task_id, status, update_date):
    """
    Creates a TaskStatus instance with the provided data.
        Args:
        task_id, status, update_date: Keyword arguments for TaskStatus fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = TaskStatus.objects.create(
            task_id=task_id,
            status=status,
            update_date=update_date,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_taskstatus(taskstatus_id,task_id=None, status=None, update_date=None):
    """
    Updates a TaskStatus instance with the provided data.
    
    Args:
        taskstatus_id (int): ID of the TaskStatus to update.
        task_id=None, status=None, update_date=None: Keyword arguments for TaskStatus fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = TaskStatus.objects.get(pk=taskstatus_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.status = status if status is not None else instance.status
        instance.update_date = update_date if update_date is not None else instance.update_date
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  TaskStatus.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_taskstatus(taskstatus_id=None):
    """
    Retrieves and serializes a TaskStatus instance by its ID or all instances if ID is None.
    
    Args:
        TaskStatus_id (int, optional): ID of the TaskStatus to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if taskstatus_id is not None:
            record = TaskStatus.objects.get(pk=taskstatus_id)
            serializer = TaskStatusSerializer(record)
        else:
            records = TaskStatus.objects.all()
            serializer = TaskStatusSerializer(records, many=True)
        return success(serializer.data)
    
    except TaskStatus.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TaskStatus does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_taskstatus(taskstatus_id):
    """
    Deletes a TaskStatus instance with the given ID.
    
    Args:
        taskstatus_id (int): ID of the TaskStatus to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TaskStatus.objects.get(pk=taskstatus_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TaskStatus.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_timesheet(worker_id, project_id, date, hours_worked, task_id, submitted, reviewed, comments):
    """
    Creates a Timesheet instance with the provided data.
        Args:
        worker_id, project_id, date, hours_worked, task_id, submitted, reviewed, comments: Keyword arguments for Timesheet fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if worker_id is not None and worker_id != '': 
             User.objects.get(pk=worker_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = Timesheet.objects.create(
            worker_id=worker_id,
            project_id=project_id,
            date=date,
            hours_worked=hours_worked,
            task_id=task_id,
            submitted=submitted,
            reviewed=reviewed,
            comments=comments,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_timesheet(timesheet_id,worker_id=None, project_id=None, date=None, hours_worked=None, task_id=None, submitted=None, reviewed=None, comments=None):
    """
    Updates a Timesheet instance with the provided data.
    
    Args:
        timesheet_id (int): ID of the Timesheet to update.
        worker_id=None, project_id=None, date=None, hours_worked=None, task_id=None, submitted=None, reviewed=None, comments=None: Keyword arguments for Timesheet fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if worker_id is not None and worker_id != '': 
             User.objects.get(pk=worker_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        instance = Timesheet.objects.get(pk=timesheet_id)
        instance.worker_id = worker_id if worker_id is not None else instance.worker_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.date = date if date is not None else instance.date
        instance.hours_worked = hours_worked if hours_worked is not None else instance.hours_worked
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.submitted = submitted if submitted is not None else instance.submitted
        instance.reviewed = reviewed if reviewed is not None else instance.reviewed
        instance.comments = comments if comments is not None else instance.comments
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except  Timesheet.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_timesheet(timesheet_id=None):
    """
    Retrieves and serializes a Timesheet instance by its ID or all instances if ID is None.
    
    Args:
        Timesheet_id (int, optional): ID of the Timesheet to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if timesheet_id is not None:
            record = Timesheet.objects.get(pk=timesheet_id)
            serializer = TimesheetSerializer(record)
        else:
            records = Timesheet.objects.all()
            serializer = TimesheetSerializer(records, many=True)
        return success(serializer.data)
    
    except Timesheet.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Timesheet does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_timesheet(timesheet_id):
    """
    Deletes a Timesheet instance with the given ID.
    
    Args:
        timesheet_id (int): ID of the Timesheet to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Timesheet.objects.get(pk=timesheet_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Timesheet.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_timetracking(task_id, user_id, date, hours_spent, hourly_rate, total_cost):
    """
    Creates a TimeTracking instance with the provided data.
        Args:
        task_id, user_id, date, hours_spent, hourly_rate, total_cost: Keyword arguments for TimeTracking fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if user_id is not None and user_id != '': 
             User.objects.get(pk=user_id)
        instance = TimeTracking.objects.create(
            task_id=task_id,
            user_id=user_id,
            date=date,
            hours_spent=hours_spent,
            hourly_rate=hourly_rate,
            total_cost=total_cost,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_timetracking(timetracking_id,task_id=None, user_id=None, date=None, hours_spent=None, hourly_rate=None, total_cost=None):
    """
    Updates a TimeTracking instance with the provided data.
    
    Args:
        timetracking_id (int): ID of the TimeTracking to update.
        task_id=None, user_id=None, date=None, hours_spent=None, hourly_rate=None, total_cost=None: Keyword arguments for TimeTracking fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_id is not None and task_id != '': 
             Task.objects.get(pk=task_id)
        if user_id is not None and user_id != '': 
             User.objects.get(pk=user_id)
        instance = TimeTracking.objects.get(pk=timetracking_id)
        instance.task_id = task_id if task_id is not None else instance.task_id
        instance.user_id = user_id if user_id is not None else instance.user_id
        instance.date = date if date is not None else instance.date
        instance.hours_spent = hours_spent if hours_spent is not None else instance.hours_spent
        instance.hourly_rate = hourly_rate if hourly_rate is not None else instance.hourly_rate
        instance.total_cost = total_cost if total_cost is not None else instance.total_cost
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  TimeTracking.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_timetracking(timetracking_id=None):
    """
    Retrieves and serializes a TimeTracking instance by its ID or all instances if ID is None.
    
    Args:
        TimeTracking_id (int, optional): ID of the TimeTracking to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if timetracking_id is not None:
            record = TimeTracking.objects.get(pk=timetracking_id)
            serializer = TimeTrackingSerializer(record)
        else:
            records = TimeTracking.objects.all()
            serializer = TimeTrackingSerializer(records, many=True)
        return success(serializer.data)
    
    except TimeTracking.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TimeTracking does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_timetracking(timetracking_id):
    """
    Deletes a TimeTracking instance with the given ID.
    
    Args:
        timetracking_id (int): ID of the TimeTracking to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TimeTracking.objects.get(pk=timetracking_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TimeTracking.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stockadjustment(material_id, project_id, quantity_adjusted, reason, adjustment_date):
    """
    Creates a StockAdjustment instance with the provided data.
        Args:
        material_id, project_id, quantity_adjusted, reason, adjustment_date: Keyword arguments for StockAdjustment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if material_id is not None and material_id != '': 
             Material.objects.get(pk=material_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = StockAdjustment.objects.create(
            material_id=material_id,
            project_id=project_id,
            quantity_adjusted=quantity_adjusted,
            reason=reason,
            adjustment_date=adjustment_date,
        )
        return success(f'Successfully created {instance}')
    except Material.DoesNotExist:
        return error('Invalid Material ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stockadjustment(stockadjustment_id,material_id=None, project_id=None, quantity_adjusted=None, reason=None, adjustment_date=None):
    """
    Updates a StockAdjustment instance with the provided data.
    
    Args:
        stockadjustment_id (int): ID of the StockAdjustment to update.
        material_id=None, project_id=None, quantity_adjusted=None, reason=None, adjustment_date=None: Keyword arguments for StockAdjustment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if material_id is not None and material_id != '': 
             Material.objects.get(pk=material_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = StockAdjustment.objects.get(pk=stockadjustment_id)
        instance.material_id = material_id if material_id is not None else instance.material_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.quantity_adjusted = quantity_adjusted if quantity_adjusted is not None else instance.quantity_adjusted
        instance.reason = reason if reason is not None else instance.reason
        instance.adjustment_date = adjustment_date if adjustment_date is not None else instance.adjustment_date
        instance.save()
        return success('Successfully Updated')
    except Material.DoesNotExist:
        return error('Invalid Material ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  StockAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stockadjustment(stockadjustment_id=None):
    """
    Retrieves and serializes a StockAdjustment instance by its ID or all instances if ID is None.
    
    Args:
        StockAdjustment_id (int, optional): ID of the StockAdjustment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stockadjustment_id is not None:
            record = StockAdjustment.objects.get(pk=stockadjustment_id)
            serializer = StockAdjustmentSerializer(record)
        else:
            records = StockAdjustment.objects.all()
            serializer = StockAdjustmentSerializer(records, many=True)
        return success(serializer.data)
    
    except StockAdjustment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('StockAdjustment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stockadjustment(stockadjustment_id):
    """
    Deletes a StockAdjustment instance with the given ID.
    
    Args:
        stockadjustment_id (int): ID of the StockAdjustment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = StockAdjustment.objects.get(pk=stockadjustment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except StockAdjustment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stockreplenishmentrequest(material_id, project_id, quantity_requested, request_date):
    """
    Creates a StockReplenishmentRequest instance with the provided data.
        Args:
        material_id, project_id, quantity_requested, request_date: Keyword arguments for StockReplenishmentRequest fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if material_id is not None and material_id != '': 
             Material.objects.get(pk=material_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = StockReplenishmentRequest.objects.create(
            material_id=material_id,
            project_id=project_id,
            quantity_requested=quantity_requested,
            request_date=request_date,
        )
        return success(f'Successfully created {instance}')
    except Material.DoesNotExist:
        return error('Invalid Material ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stockreplenishmentrequest(stockreplenishmentrequest_id,material_id=None, project_id=None, quantity_requested=None, request_date=None):
    """
    Updates a StockReplenishmentRequest instance with the provided data.
    
    Args:
        stockreplenishmentrequest_id (int): ID of the StockReplenishmentRequest to update.
        material_id=None, project_id=None, quantity_requested=None, request_date=None: Keyword arguments for StockReplenishmentRequest fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if material_id is not None and material_id != '': 
             Material.objects.get(pk=material_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = StockReplenishmentRequest.objects.get(pk=stockreplenishmentrequest_id)
        instance.material_id = material_id if material_id is not None else instance.material_id
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.quantity_requested = quantity_requested if quantity_requested is not None else instance.quantity_requested
        instance.request_date = request_date if request_date is not None else instance.request_date
        instance.save()
        return success('Successfully Updated')
    except Material.DoesNotExist:
        return error('Invalid Material ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  StockReplenishmentRequest.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stockreplenishmentrequest(stockreplenishmentrequest_id=None):
    """
    Retrieves and serializes a StockReplenishmentRequest instance by its ID or all instances if ID is None.
    
    Args:
        StockReplenishmentRequest_id (int, optional): ID of the StockReplenishmentRequest to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stockreplenishmentrequest_id is not None:
            record = StockReplenishmentRequest.objects.get(pk=stockreplenishmentrequest_id)
            serializer = StockReplenishmentRequestSerializer(record)
        else:
            records = StockReplenishmentRequest.objects.all()
            serializer = StockReplenishmentRequestSerializer(records, many=True)
        return success(serializer.data)
    
    except StockReplenishmentRequest.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('StockReplenishmentRequest does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stockreplenishmentrequest(stockreplenishmentrequest_id):
    """
    Deletes a StockReplenishmentRequest instance with the given ID.
    
    Args:
        stockreplenishmentrequest_id (int): ID of the StockReplenishmentRequest to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = StockReplenishmentRequest.objects.get(pk=stockreplenishmentrequest_id)
        instance.delete()
        return success("Successfully deleted")
    
    except StockReplenishmentRequest.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_mitigationaction(mitigation_strategy_id, action_name, action_description, due_date, completed, completed_date):
    """
    Creates a MitigationAction instance with the provided data.
        Args:
        mitigation_strategy_id, action_name, action_description, due_date, completed, completed_date: Keyword arguments for MitigationAction fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if mitigation_strategy_id is not None and mitigation_strategy_id != '': 
             MitigationStrategy.objects.get(pk=mitigation_strategy_id)
        instance = MitigationAction.objects.create(
            mitigation_strategy_id=mitigation_strategy_id,
            action_name=action_name,
            action_description=action_description,
            due_date=due_date,
            completed=completed,
            completed_date=completed_date,
        )
        return success(f'Successfully created {instance}')
    except MitigationStrategy.DoesNotExist:
        return error('Invalid MitigationStrategy ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_mitigationaction(mitigationaction_id,mitigation_strategy_id=None, action_name=None, action_description=None, due_date=None, completed=None, completed_date=None):
    """
    Updates a MitigationAction instance with the provided data.
    
    Args:
        mitigationaction_id (int): ID of the MitigationAction to update.
        mitigation_strategy_id=None, action_name=None, action_description=None, due_date=None, completed=None, completed_date=None: Keyword arguments for MitigationAction fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if mitigation_strategy_id is not None and mitigation_strategy_id != '': 
             MitigationStrategy.objects.get(pk=mitigation_strategy_id)
        instance = MitigationAction.objects.get(pk=mitigationaction_id)
        instance.mitigation_strategy_id = mitigation_strategy_id if mitigation_strategy_id is not None else instance.mitigation_strategy_id
        instance.action_name = action_name if action_name is not None else instance.action_name
        instance.action_description = action_description if action_description is not None else instance.action_description
        instance.due_date = due_date if due_date is not None else instance.due_date
        instance.completed = completed if completed is not None else instance.completed
        instance.completed_date = completed_date if completed_date is not None else instance.completed_date
        instance.save()
        return success('Successfully Updated')
    except MitigationStrategy.DoesNotExist:
        return error('Invalid MitigationStrategy ID: Destination not found.')
    except  MitigationAction.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_mitigationaction(mitigationaction_id=None):
    """
    Retrieves and serializes a MitigationAction instance by its ID or all instances if ID is None.
    
    Args:
        MitigationAction_id (int, optional): ID of the MitigationAction to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if mitigationaction_id is not None:
            record = MitigationAction.objects.get(pk=mitigationaction_id)
            serializer = MitigationActionSerializer(record)
        else:
            records = MitigationAction.objects.all()
            serializer = MitigationActionSerializer(records, many=True)
        return success(serializer.data)
    
    except MitigationAction.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('MitigationAction does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_mitigationaction(mitigationaction_id):
    """
    Deletes a MitigationAction instance with the given ID.
    
    Args:
        mitigationaction_id (int): ID of the MitigationAction to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = MitigationAction.objects.get(pk=mitigationaction_id)
        instance.delete()
        return success("Successfully deleted")
    
    except MitigationAction.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_tenderscope(tender_id, scope_description, technical_specifications, delivery_timeline, quality_standards):
    """
    Creates a TenderScope instance with the provided data.
        Args:
        tender_id, scope_description, technical_specifications, delivery_timeline, quality_standards: Keyword arguments for TenderScope fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tender_id is not None and tender_id != '': 
             TenderDocument.objects.get(pk=tender_id)
        instance = TenderScope.objects.create(
            tender_id=tender_id,
            scope_description=scope_description,
            technical_specifications=technical_specifications,
            delivery_timeline=delivery_timeline,
            quality_standards=quality_standards,
        )
        return success(f'Successfully created {instance}')
    except TenderDocument.DoesNotExist:
        return error('Invalid TenderDocument ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_tenderscope(tenderscope_id,tender_id=None, scope_description=None, technical_specifications=None, delivery_timeline=None, quality_standards=None):
    """
    Updates a TenderScope instance with the provided data.
    
    Args:
        tenderscope_id (int): ID of the TenderScope to update.
        tender_id=None, scope_description=None, technical_specifications=None, delivery_timeline=None, quality_standards=None: Keyword arguments for TenderScope fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tender_id is not None and tender_id != '': 
             TenderDocument.objects.get(pk=tender_id)
        instance = TenderScope.objects.get(pk=tenderscope_id)
        instance.tender_id = tender_id if tender_id is not None else instance.tender_id
        instance.scope_description = scope_description if scope_description is not None else instance.scope_description
        instance.technical_specifications = technical_specifications if technical_specifications is not None else instance.technical_specifications
        instance.delivery_timeline = delivery_timeline if delivery_timeline is not None else instance.delivery_timeline
        instance.quality_standards = quality_standards if quality_standards is not None else instance.quality_standards
        instance.save()
        return success('Successfully Updated')
    except TenderDocument.DoesNotExist:
        return error('Invalid TenderDocument ID: Destination not found.')
    except  TenderScope.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_tenderscope(tenderscope_id=None):
    """
    Retrieves and serializes a TenderScope instance by its ID or all instances if ID is None.
    
    Args:
        TenderScope_id (int, optional): ID of the TenderScope to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tenderscope_id is not None:
            record = TenderScope.objects.get(pk=tenderscope_id)
            serializer = TenderScopeSerializer(record)
        else:
            records = TenderScope.objects.all()
            serializer = TenderScopeSerializer(records, many=True)
        return success(serializer.data)
    
    except TenderScope.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TenderScope does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_tenderscope(tenderscope_id):
    """
    Deletes a TenderScope instance with the given ID.
    
    Args:
        tenderscope_id (int): ID of the TenderScope to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderScope.objects.get(pk=tenderscope_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TenderScope.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_tendersubmission(tender_id, vendor_name, proposal_details, submitted_on, cost_estimate):
    """
    Creates a TenderSubmission instance with the provided data.
        Args:
        tender_id, vendor_name, proposal_details, submitted_on, cost_estimate: Keyword arguments for TenderSubmission fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tender_id is not None and tender_id != '': 
             TenderDocument.objects.get(pk=tender_id)
        instance = TenderSubmission.objects.create(
            tender_id=tender_id,
            vendor_name=vendor_name,
            proposal_details=proposal_details,
            submitted_on=submitted_on,
            cost_estimate=cost_estimate,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except TenderDocument.DoesNotExist:
        return error('Invalid TenderDocument ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_tendersubmission(tendersubmission_id,tender_id=None, vendor_name=None, proposal_details=None, submitted_on=None, cost_estimate=None):
    """
    Updates a TenderSubmission instance with the provided data.
    
    Args:
        tendersubmission_id (int): ID of the TenderSubmission to update.
        tender_id=None, vendor_name=None, proposal_details=None, submitted_on=None, cost_estimate=None: Keyword arguments for TenderSubmission fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tender_id is not None and tender_id != '': 
             TenderDocument.objects.get(pk=tender_id)
        instance = TenderSubmission.objects.get(pk=tendersubmission_id)
        instance.tender_id = tender_id if tender_id is not None else instance.tender_id
        instance.vendor_name = vendor_name if vendor_name is not None else instance.vendor_name
        instance.proposal_details = proposal_details if proposal_details is not None else instance.proposal_details
        instance.submitted_on = submitted_on if submitted_on is not None else instance.submitted_on
        instance.cost_estimate = cost_estimate if cost_estimate is not None else instance.cost_estimate
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except TenderDocument.DoesNotExist:
        return error('Invalid TenderDocument ID: Destination not found.')
    except  TenderSubmission.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_tendersubmission(tendersubmission_id=None):
    """
    Retrieves and serializes a TenderSubmission instance by its ID or all instances if ID is None.
    
    Args:
        TenderSubmission_id (int, optional): ID of the TenderSubmission to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tendersubmission_id is not None:
            record = TenderSubmission.objects.get(pk=tendersubmission_id)
            serializer = TenderSubmissionSerializer(record)
        else:
            records = TenderSubmission.objects.all()
            serializer = TenderSubmissionSerializer(records, many=True)
        return success(serializer.data)
    
    except TenderSubmission.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TenderSubmission does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_tendersubmission(tendersubmission_id):
    """
    Deletes a TenderSubmission instance with the given ID.
    
    Args:
        tendersubmission_id (int): ID of the TenderSubmission to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderSubmission.objects.get(pk=tendersubmission_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TenderSubmission.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_stakeholderevaluation(evaluation_id, stakeholder_id, feedback):
    """
    Creates a StakeholderEvaluation instance with the provided data.
        Args:
        evaluation_id, stakeholder_id, feedback: Keyword arguments for StakeholderEvaluation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if evaluation_id is not None and evaluation_id != '': 
             ProposalEvaluation.objects.get(pk=evaluation_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = StakeholderEvaluation.objects.create(
            evaluation_id=evaluation_id,
            stakeholder_id=stakeholder_id,
            feedback=feedback,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ProposalEvaluation.DoesNotExist:
        return error('Invalid ProposalEvaluation ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_stakeholderevaluation(stakeholderevaluation_id,evaluation_id=None, stakeholder_id=None, feedback=None):
    """
    Updates a StakeholderEvaluation instance with the provided data.
    
    Args:
        stakeholderevaluation_id (int): ID of the StakeholderEvaluation to update.
        evaluation_id=None, stakeholder_id=None, feedback=None: Keyword arguments for StakeholderEvaluation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if evaluation_id is not None and evaluation_id != '': 
             ProposalEvaluation.objects.get(pk=evaluation_id)
        if stakeholder_id is not None and stakeholder_id != '': 
             Stakeholder.objects.get(pk=stakeholder_id)
        instance = StakeholderEvaluation.objects.get(pk=stakeholderevaluation_id)
        instance.evaluation_id = evaluation_id if evaluation_id is not None else instance.evaluation_id
        instance.stakeholder_id = stakeholder_id if stakeholder_id is not None else instance.stakeholder_id
        instance.feedback = feedback if feedback is not None else instance.feedback
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except ProposalEvaluation.DoesNotExist:
        return error('Invalid ProposalEvaluation ID: Destination not found.')
    except Stakeholder.DoesNotExist:
        return error('Invalid Stakeholder ID: Destination not found.')
    except  StakeholderEvaluation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_stakeholderevaluation(stakeholderevaluation_id=None):
    """
    Retrieves and serializes a StakeholderEvaluation instance by its ID or all instances if ID is None.
    
    Args:
        StakeholderEvaluation_id (int, optional): ID of the StakeholderEvaluation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if stakeholderevaluation_id is not None:
            record = StakeholderEvaluation.objects.get(pk=stakeholderevaluation_id)
            serializer = StakeholderEvaluationSerializer(record)
        else:
            records = StakeholderEvaluation.objects.all()
            serializer = StakeholderEvaluationSerializer(records, many=True)
        return success(serializer.data)
    
    except StakeholderEvaluation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('StakeholderEvaluation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_stakeholderevaluation(stakeholderevaluation_id):
    """
    Deletes a StakeholderEvaluation instance with the given ID.
    
    Args:
        stakeholderevaluation_id (int): ID of the StakeholderEvaluation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = StakeholderEvaluation.objects.get(pk=stakeholderevaluation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except StakeholderEvaluation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_payment(invoice_id, payment_date, amount_paid, payment_method, payment_reference, project_id, milestone, payment_due, status):
    """
    Creates a Payment instance with the provided data.
        Args:
        invoice_id, payment_date, amount_paid, payment_method, payment_reference, project_id, milestone, payment_due, status: Keyword arguments for Payment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if invoice_id is not None and invoice_id != '': 
             Invoice.objects.get(pk=invoice_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Payment.objects.create(
            invoice_id=invoice_id,
            payment_date=payment_date,
            amount_paid=amount_paid,
            payment_method=payment_method,
            payment_reference=payment_reference,
            project_id=project_id,
            milestone=milestone,
            payment_due=payment_due,
            status=status,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Invoice.DoesNotExist:
        return error('Invalid Invoice ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_payment(payment_id,invoice_id=None, payment_date=None, amount_paid=None, payment_method=None, payment_reference=None, project_id=None, milestone=None, payment_due=None, status=None):
    """
    Updates a Payment instance with the provided data.
    
    Args:
        payment_id (int): ID of the Payment to update.
        invoice_id=None, payment_date=None, amount_paid=None, payment_method=None, payment_reference=None, project_id=None, milestone=None, payment_due=None, status=None: Keyword arguments for Payment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if invoice_id is not None and invoice_id != '': 
             Invoice.objects.get(pk=invoice_id)
        if project_id is not None and project_id != '': 
             Project.objects.get(pk=project_id)
        instance = Payment.objects.get(pk=payment_id)
        instance.invoice_id = invoice_id if invoice_id is not None else instance.invoice_id
        instance.payment_date = payment_date if payment_date is not None else instance.payment_date
        instance.amount_paid = amount_paid if amount_paid is not None else instance.amount_paid
        instance.payment_method = payment_method if payment_method is not None else instance.payment_method
        instance.payment_reference = payment_reference if payment_reference is not None else instance.payment_reference
        instance.project_id = project_id if project_id is not None else instance.project_id
        instance.milestone = milestone if milestone is not None else instance.milestone
        instance.payment_due = payment_due if payment_due is not None else instance.payment_due
        instance.status = status if status is not None else instance.status
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Invoice.DoesNotExist:
        return error('Invalid Invoice ID: Destination not found.')
    except Project.DoesNotExist:
        return error('Invalid Project ID: Destination not found.')
    except  Payment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_payment(payment_id=None):
    """
    Retrieves and serializes a Payment instance by its ID or all instances if ID is None.
    
    Args:
        Payment_id (int, optional): ID of the Payment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if payment_id is not None:
            record = Payment.objects.get(pk=payment_id)
            serializer = PaymentSerializer(record)
        else:
            records = Payment.objects.all()
            serializer = PaymentSerializer(records, many=True)
        return success(serializer.data)
    
    except Payment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Payment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_payment(payment_id):
    """
    Deletes a Payment instance with the given ID.
    
    Args:
        payment_id (int): ID of the Payment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Payment.objects.get(pk=payment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Payment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_criticalpathmonitoring(critical_path_id, actual_start_date, actual_end_date, delay_days, comments):
    """
    Creates a CriticalPathMonitoring instance with the provided data.
        Args:
        critical_path_id, actual_start_date, actual_end_date, delay_days, comments: Keyword arguments for CriticalPathMonitoring fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if critical_path_id is not None and critical_path_id != '': 
             CriticalPath.objects.get(pk=critical_path_id)
        instance = CriticalPathMonitoring.objects.create(
            critical_path_id=critical_path_id,
            actual_start_date=actual_start_date,
            actual_end_date=actual_end_date,
            delay_days=delay_days,
            comments=comments,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except CriticalPath.DoesNotExist:
        return error('Invalid CriticalPath ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_criticalpathmonitoring(criticalpathmonitoring_id,critical_path_id=None, actual_start_date=None, actual_end_date=None, delay_days=None, comments=None):
    """
    Updates a CriticalPathMonitoring instance with the provided data.
    
    Args:
        criticalpathmonitoring_id (int): ID of the CriticalPathMonitoring to update.
        critical_path_id=None, actual_start_date=None, actual_end_date=None, delay_days=None, comments=None: Keyword arguments for CriticalPathMonitoring fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if critical_path_id is not None and critical_path_id != '': 
             CriticalPath.objects.get(pk=critical_path_id)
        instance = CriticalPathMonitoring.objects.get(pk=criticalpathmonitoring_id)
        instance.critical_path_id = critical_path_id if critical_path_id is not None else instance.critical_path_id
        instance.actual_start_date = actual_start_date if actual_start_date is not None else instance.actual_start_date
        instance.actual_end_date = actual_end_date if actual_end_date is not None else instance.actual_end_date
        instance.delay_days = delay_days if delay_days is not None else instance.delay_days
        instance.comments = comments if comments is not None else instance.comments
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except CriticalPath.DoesNotExist:
        return error('Invalid CriticalPath ID: Destination not found.')
    except  CriticalPathMonitoring.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_criticalpathmonitoring(criticalpathmonitoring_id=None):
    """
    Retrieves and serializes a CriticalPathMonitoring instance by its ID or all instances if ID is None.
    
    Args:
        CriticalPathMonitoring_id (int, optional): ID of the CriticalPathMonitoring to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if criticalpathmonitoring_id is not None:
            record = CriticalPathMonitoring.objects.get(pk=criticalpathmonitoring_id)
            serializer = CriticalPathMonitoringSerializer(record)
        else:
            records = CriticalPathMonitoring.objects.all()
            serializer = CriticalPathMonitoringSerializer(records, many=True)
        return success(serializer.data)
    
    except CriticalPathMonitoring.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('CriticalPathMonitoring does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_criticalpathmonitoring(criticalpathmonitoring_id):
    """
    Deletes a CriticalPathMonitoring instance with the given ID.
    
    Args:
        criticalpathmonitoring_id (int): ID of the CriticalPathMonitoring to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = CriticalPathMonitoring.objects.get(pk=criticalpathmonitoring_id)
        instance.delete()
        return success("Successfully deleted")
    
    except CriticalPathMonitoring.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_adjustment(delay_id, adjusted_task_id, new_start_date, new_end_date, adjusted_by_id, adjustment_reason):
    """
    Creates a Adjustment instance with the provided data.
        Args:
        delay_id, adjusted_task_id, new_start_date, new_end_date, adjusted_by_id, adjustment_reason: Keyword arguments for Adjustment fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if delay_id is not None and delay_id != '': 
             Delay.objects.get(pk=delay_id)
        if adjusted_task_id is not None and adjusted_task_id != '': 
             Task.objects.get(pk=adjusted_task_id)
        if adjusted_by_id is not None and adjusted_by_id != '': 
             User.objects.get(pk=adjusted_by_id)
        instance = Adjustment.objects.create(
            delay_id=delay_id,
            adjusted_task_id=adjusted_task_id,
            new_start_date=new_start_date,
            new_end_date=new_end_date,
            adjusted_by_id=adjusted_by_id,
            adjustment_reason=adjustment_reason,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except Delay.DoesNotExist:
        return error('Invalid Delay ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_adjustment(adjustment_id,delay_id=None, adjusted_task_id=None, new_start_date=None, new_end_date=None, adjusted_by_id=None, adjustment_reason=None):
    """
    Updates a Adjustment instance with the provided data.
    
    Args:
        adjustment_id (int): ID of the Adjustment to update.
        delay_id=None, adjusted_task_id=None, new_start_date=None, new_end_date=None, adjusted_by_id=None, adjustment_reason=None: Keyword arguments for Adjustment fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if delay_id is not None and delay_id != '': 
             Delay.objects.get(pk=delay_id)
        if adjusted_task_id is not None and adjusted_task_id != '': 
             Task.objects.get(pk=adjusted_task_id)
        if adjusted_by_id is not None and adjusted_by_id != '': 
             User.objects.get(pk=adjusted_by_id)
        instance = Adjustment.objects.get(pk=adjustment_id)
        instance.delay_id = delay_id if delay_id is not None else instance.delay_id
        instance.adjusted_task_id = adjusted_task_id if adjusted_task_id is not None else instance.adjusted_task_id
        instance.new_start_date = new_start_date if new_start_date is not None else instance.new_start_date
        instance.new_end_date = new_end_date if new_end_date is not None else instance.new_end_date
        instance.adjusted_by_id = adjusted_by_id if adjusted_by_id is not None else instance.adjusted_by_id
        instance.adjustment_reason = adjustment_reason if adjustment_reason is not None else instance.adjustment_reason
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except Delay.DoesNotExist:
        return error('Invalid Delay ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  Adjustment.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_adjustment(adjustment_id=None):
    """
    Retrieves and serializes a Adjustment instance by its ID or all instances if ID is None.
    
    Args:
        Adjustment_id (int, optional): ID of the Adjustment to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if adjustment_id is not None:
            record = Adjustment.objects.get(pk=adjustment_id)
            serializer = AdjustmentSerializer(record)
        else:
            records = Adjustment.objects.all()
            serializer = AdjustmentSerializer(records, many=True)
        return success(serializer.data)
    
    except Adjustment.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Adjustment does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_adjustment(adjustment_id):
    """
    Deletes a Adjustment instance with the given ID.
    
    Args:
        adjustment_id (int): ID of the Adjustment to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Adjustment.objects.get(pk=adjustment_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Adjustment.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourcereallocation(original_allocation_id, new_task_id, reallocated_quantity, reason, reallocated_by_id):
    """
    Creates a ResourceReallocation instance with the provided data.
        Args:
        original_allocation_id, new_task_id, reallocated_quantity, reason, reallocated_by_id: Keyword arguments for ResourceReallocation fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if original_allocation_id is not None and original_allocation_id != '': 
             ResourceAllocation.objects.get(pk=original_allocation_id)
        if new_task_id is not None and new_task_id != '': 
             Task.objects.get(pk=new_task_id)
        if reallocated_by_id is not None and reallocated_by_id != '': 
             User.objects.get(pk=reallocated_by_id)
        instance = ResourceReallocation.objects.create(
            original_allocation_id=original_allocation_id,
            new_task_id=new_task_id,
            reallocated_quantity=reallocated_quantity,
            reason=reason,
            reallocated_by_id=reallocated_by_id,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ResourceAllocation.DoesNotExist:
        return error('Invalid ResourceAllocation ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourcereallocation(resourcereallocation_id,original_allocation_id=None, new_task_id=None, reallocated_quantity=None, reason=None, reallocated_by_id=None):
    """
    Updates a ResourceReallocation instance with the provided data.
    
    Args:
        resourcereallocation_id (int): ID of the ResourceReallocation to update.
        original_allocation_id=None, new_task_id=None, reallocated_quantity=None, reason=None, reallocated_by_id=None: Keyword arguments for ResourceReallocation fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if original_allocation_id is not None and original_allocation_id != '': 
             ResourceAllocation.objects.get(pk=original_allocation_id)
        if new_task_id is not None and new_task_id != '': 
             Task.objects.get(pk=new_task_id)
        if reallocated_by_id is not None and reallocated_by_id != '': 
             User.objects.get(pk=reallocated_by_id)
        instance = ResourceReallocation.objects.get(pk=resourcereallocation_id)
        instance.original_allocation_id = original_allocation_id if original_allocation_id is not None else instance.original_allocation_id
        instance.new_task_id = new_task_id if new_task_id is not None else instance.new_task_id
        instance.reallocated_quantity = reallocated_quantity if reallocated_quantity is not None else instance.reallocated_quantity
        instance.reason = reason if reason is not None else instance.reason
        instance.reallocated_by_id = reallocated_by_id if reallocated_by_id is not None else instance.reallocated_by_id
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except ResourceAllocation.DoesNotExist:
        return error('Invalid ResourceAllocation ID: Destination not found.')
    except Task.DoesNotExist:
        return error('Invalid Task ID: Destination not found.')
    except User.DoesNotExist:
        return error('Invalid User ID: Destination not found.')
    except  ResourceReallocation.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourcereallocation(resourcereallocation_id=None):
    """
    Retrieves and serializes a ResourceReallocation instance by its ID or all instances if ID is None.
    
    Args:
        ResourceReallocation_id (int, optional): ID of the ResourceReallocation to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourcereallocation_id is not None:
            record = ResourceReallocation.objects.get(pk=resourcereallocation_id)
            serializer = ResourceReallocationSerializer(record)
        else:
            records = ResourceReallocation.objects.all()
            serializer = ResourceReallocationSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceReallocation.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceReallocation does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourcereallocation(resourcereallocation_id):
    """
    Deletes a ResourceReallocation instance with the given ID.
    
    Args:
        resourcereallocation_id (int): ID of the ResourceReallocation to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceReallocation.objects.get(pk=resourcereallocation_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceReallocation.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_resourceusage(task_resource_allocation_id, start_time, end_time, quantity_used):
    """
    Creates a ResourceUsage instance with the provided data.
        Args:
        task_resource_allocation_id, start_time, end_time, quantity_used: Keyword arguments for ResourceUsage fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_resource_allocation_id is not None and task_resource_allocation_id != '': 
             TaskResourceAllocation.objects.get(pk=task_resource_allocation_id)
        instance = ResourceUsage.objects.create(
            task_resource_allocation_id=task_resource_allocation_id,
            start_time=start_time,
            end_time=end_time,
            quantity_used=quantity_used,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except TaskResourceAllocation.DoesNotExist:
        return error('Invalid TaskResourceAllocation ID: Destination not found.')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_resourceusage(resourceusage_id,task_resource_allocation_id=None, start_time=None, end_time=None, quantity_used=None):
    """
    Updates a ResourceUsage instance with the provided data.
    
    Args:
        resourceusage_id (int): ID of the ResourceUsage to update.
        task_resource_allocation_id=None, start_time=None, end_time=None, quantity_used=None: Keyword arguments for ResourceUsage fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if task_resource_allocation_id is not None and task_resource_allocation_id != '': 
             TaskResourceAllocation.objects.get(pk=task_resource_allocation_id)
        instance = ResourceUsage.objects.get(pk=resourceusage_id)
        instance.task_resource_allocation_id = task_resource_allocation_id if task_resource_allocation_id is not None else instance.task_resource_allocation_id
        instance.start_time = start_time if start_time is not None else instance.start_time
        instance.end_time = end_time if end_time is not None else instance.end_time
        instance.quantity_used = quantity_used if quantity_used is not None else instance.quantity_used
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except TaskResourceAllocation.DoesNotExist:
        return error('Invalid TaskResourceAllocation ID: Destination not found.')
    except  ResourceUsage.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_resourceusage(resourceusage_id=None):
    """
    Retrieves and serializes a ResourceUsage instance by its ID or all instances if ID is None.
    
    Args:
        ResourceUsage_id (int, optional): ID of the ResourceUsage to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if resourceusage_id is not None:
            record = ResourceUsage.objects.get(pk=resourceusage_id)
            serializer = ResourceUsageSerializer(record)
        else:
            records = ResourceUsage.objects.all()
            serializer = ResourceUsageSerializer(records, many=True)
        return success(serializer.data)
    
    except ResourceUsage.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('ResourceUsage does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_resourceusage(resourceusage_id):
    """
    Deletes a ResourceUsage instance with the given ID.
    
    Args:
        resourceusage_id (int): ID of the ResourceUsage to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = ResourceUsage.objects.get(pk=resourceusage_id)
        instance.delete()
        return success("Successfully deleted")
    
    except ResourceUsage.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_client(name, address, contact_person, email, phone):
    """
    Creates a Client instance with the provided data.
        Args:
        name, address, contact_person, email, phone: Keyword arguments for Client fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Client.objects.create(
            name=name,
            address=address,
            contact_person=contact_person,
            email=email,
            phone=phone,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_client(client_id,name=None, address=None, contact_person=None, email=None, phone=None):
    """
    Updates a Client instance with the provided data.
    
    Args:
        client_id (int): ID of the Client to update.
        name=None, address=None, contact_person=None, email=None, phone=None: Keyword arguments for Client fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Client.objects.get(pk=client_id)
        instance.name = name if name is not None else instance.name
        instance.address = address if address is not None else instance.address
        instance.contact_person = contact_person if contact_person is not None else instance.contact_person
        instance.email = email if email is not None else instance.email
        instance.phone = phone if phone is not None else instance.phone
        instance.save()
        return success('Successfully Updated')
    except  Client.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_client(client_id=None):
    """
    Retrieves and serializes a Client instance by its ID or all instances if ID is None.
    
    Args:
        Client_id (int, optional): ID of the Client to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if client_id is not None:
            record = Client.objects.get(pk=client_id)
            serializer = ClientSerializer(record)
        else:
            records = Client.objects.all()
            serializer = ClientSerializer(records, many=True)
        return success(serializer.data)
    
    except Client.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('Client does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_client(client_id):
    """
    Deletes a Client instance with the given ID.
    
    Args:
        client_id (int): ID of the Client to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = Client.objects.get(pk=client_id)
        instance.delete()
        return success("Successfully deleted")
    
    except Client.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_bidqualification(rfp_rfq_title, response_due_date, alignment_with_strategy, capacity_evaluation, is_qualified):
    """
    Creates a BidQualification instance with the provided data.
        Args:
        rfp_rfq_title, response_due_date, alignment_with_strategy, capacity_evaluation, is_qualified: Keyword arguments for BidQualification fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidQualification.objects.create(
            rfp_rfq_title=rfp_rfq_title,
            response_due_date=response_due_date,
            alignment_with_strategy=alignment_with_strategy,
            capacity_evaluation=capacity_evaluation,
            is_qualified=is_qualified,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_bidqualification(bidqualification_id,rfp_rfq_title=None, response_due_date=None, alignment_with_strategy=None, capacity_evaluation=None, is_qualified=None):
    """
    Updates a BidQualification instance with the provided data.
    
    Args:
        bidqualification_id (int): ID of the BidQualification to update.
        rfp_rfq_title=None, response_due_date=None, alignment_with_strategy=None, capacity_evaluation=None, is_qualified=None: Keyword arguments for BidQualification fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidQualification.objects.get(pk=bidqualification_id)
        instance.rfp_rfq_title = rfp_rfq_title if rfp_rfq_title is not None else instance.rfp_rfq_title
        instance.response_due_date = response_due_date if response_due_date is not None else instance.response_due_date
        instance.alignment_with_strategy = alignment_with_strategy if alignment_with_strategy is not None else instance.alignment_with_strategy
        instance.capacity_evaluation = capacity_evaluation if capacity_evaluation is not None else instance.capacity_evaluation
        instance.is_qualified = is_qualified if is_qualified is not None else instance.is_qualified
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  BidQualification.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_bidqualification(bidqualification_id=None):
    """
    Retrieves and serializes a BidQualification instance by its ID or all instances if ID is None.
    
    Args:
        BidQualification_id (int, optional): ID of the BidQualification to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if bidqualification_id is not None:
            record = BidQualification.objects.get(pk=bidqualification_id)
            serializer = BidQualificationSerializer(record)
        else:
            records = BidQualification.objects.all()
            serializer = BidQualificationSerializer(records, many=True)
        return success(serializer.data)
    
    except BidQualification.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('BidQualification does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_bidqualification(bidqualification_id):
    """
    Deletes a BidQualification instance with the given ID.
    
    Args:
        bidqualification_id (int): ID of the BidQualification to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = BidQualification.objects.get(pk=bidqualification_id)
        instance.delete()
        return success("Successfully deleted")
    
    except BidQualification.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
def create_tenderproposalmanagement(rfp_rfq_title, issued_date, response_deadline, response_tracking, issued_by):
    """
    Creates a TenderProposalManagement instance with the provided data.
        Args:
        rfp_rfq_title, issued_date, response_deadline, response_tracking, issued_by: Keyword arguments for TenderProposalManagement fields.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderProposalManagement.objects.create(
            rfp_rfq_title=rfp_rfq_title,
            issued_date=issued_date,
            response_deadline=response_deadline,
            response_tracking=response_tracking,
            issued_by=issued_by,
            created_by = request.user,
            updated_by = request.user,
        )
        return success(f'Successfully created {instance}')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def update_tenderproposalmanagement(tenderproposalmanagement_id,rfp_rfq_title=None, issued_date=None, response_deadline=None, response_tracking=None, issued_by=None):
    """
    Updates a TenderProposalManagement instance with the provided data.
    
    Args:
        tenderproposalmanagement_id (int): ID of the TenderProposalManagement to update.
        rfp_rfq_title=None, issued_date=None, response_deadline=None, response_tracking=None, issued_by=None: Keyword arguments for TenderProposalManagement fields to update.

    Returns:
        dict: Success or error message.
    """
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderProposalManagement.objects.get(pk=tenderproposalmanagement_id)
        instance.rfp_rfq_title = rfp_rfq_title if rfp_rfq_title is not None else instance.rfp_rfq_title
        instance.issued_date = issued_date if issued_date is not None else instance.issued_date
        instance.response_deadline = response_deadline if response_deadline is not None else instance.response_deadline
        instance.response_tracking = response_tracking if response_tracking is not None else instance.response_tracking
        instance.issued_by = issued_by if issued_by is not None else instance.issued_by
        instance.updated_by = request.user,
        instance.save()
        return success('Successfully Updated')
    except  TenderProposalManagement.DoesNotExist:
        return error('Instance does not exist')
    except ValidationError as e:
        return error(f"Validation Error: {e}")
    except Exception as e:
        return error(f"An error occurred: {e}")

def view_tenderproposalmanagement(tenderproposalmanagement_id=None):
    """
    Retrieves and serializes a TenderProposalManagement instance by its ID or all instances if ID is None.
    
    Args:
        TenderProposalManagement_id (int, optional): ID of the TenderProposalManagement to retrieve.

    Returns:
        dict: A success response with the serialized data if found,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        if tenderproposalmanagement_id is not None:
            record = TenderProposalManagement.objects.get(pk=tenderproposalmanagement_id)
            serializer = TenderProposalManagementSerializer(record)
        else:
            records = TenderProposalManagement.objects.all()
            serializer = TenderProposalManagementSerializer(records, many=True)
        return success(serializer.data)
    
    except TenderProposalManagement.DoesNotExist:
        # Return an error response if the {model_name} does not exist
        return error('TenderProposalManagement does not exist')
    except Exception as e:
        # Return an error response with the exception message
        return error(f"An error occurred: {e}")

def delete_tenderproposalmanagement(tenderproposalmanagement_id):
    """
    Deletes a TenderProposalManagement instance with the given ID.
    
    Args:
        tenderproposalmanagement_id (int): ID of the TenderProposalManagement to delete.

    Returns:
        dict: A success response if deletion is successful,
              or an error response if an exception occurs.
    """
    
    try:
        request = get_current_request()
        if not request.user.is_authenticated:
            return error('Login required')
        
        instance = TenderProposalManagement.objects.get(pk=tenderproposalmanagement_id)
        instance.delete()
        return success("Successfully deleted")
    
    except TenderProposalManagement.DoesNotExist:
        return error('Instance does not exist')
    except Exception as e:
        return error(f"An error occurred: {e}")
