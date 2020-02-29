# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6219, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SubscriptionOperations(object):
    """SubscriptionOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~subscription_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _create_subscription_in_enrollment_account_initial(
        self,
        enrollment_account_name,  # type: str
        display_name=None,  # type: Optional[str]
        management_group_id=None,  # type: Optional[str]
        owners=None,  # type: Optional[List["AdPrincipal"]]
        offer_type=None,  # type: Optional[Union[str, "models.OfferType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        error_map = kwargs.pop('error_map', {})

        body = models.SubscriptionCreationParameters(display_name=display_name, management_group_id=management_group_id, owners=owners, offer_type=offer_type)
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self._create_subscription_in_enrollment_account_initial.metadata['url']
        path_format_arguments = {
            'enrollmentAccountName': self._serialize.url("enrollment_account_name", enrollment_account_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(body, 'SubscriptionCreationParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('str', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_subscription_in_enrollment_account_initial.metadata = {'url': '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription'}

    def begin_create_subscription_in_enrollment_account(
        self,
        enrollment_account_name,  # type: str
        display_name=None,  # type: Optional[str]
        management_group_id=None,  # type: Optional[str]
        owners=None,  # type: Optional[List["AdPrincipal"]]
        offer_type=None,  # type: Optional[Union[str, "models.OfferType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        """Creates an Azure subscription.

        :param enrollment_account_name: The name of the enrollment account to which the subscription
         will be billed.
        :type enrollment_account_name: str
        :param display_name: The display name of the subscription.
        :type display_name: str
        :param management_group_id: The Management Group Id.
        :type management_group_id: str
        :param owners: The list of principals that should be granted Owner access on the subscription.
         Principals should be of type User, Service Principal or Security Group.
        :type owners: list[~subscription_client.models.AdPrincipal]
        :param offer_type: The offer type of the subscription. For example, MS-AZR-0017P
         (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are available. Only valid
         when creating a subscription in a enrollment account scope.
        :type offer_type: str or ~subscription_client.models.OfferType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns SubscriptionCreationResult
        :rtype: ~azure.core.polling.LROPoller[~subscription_client.models.SubscriptionCreationResult]

        :raises ~subscription_client.models.ErrorResponseException:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        raw_result = self._create_subscription_in_enrollment_account_initial(
            enrollment_account_name=enrollment_account_name,
            display_name=display_name,
            management_group_id=management_group_id,
            owners=owners,
            offer_type=offer_type,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_subscription_in_enrollment_account.metadata = {'url': '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription'}

    def cancel(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CanceledSubscriptionId"
        """The operation to cancel a subscription.

        :param subscription_id: Subscription Id.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CanceledSubscriptionId or the result of cls(response)
        :rtype: ~subscription_client.models.CanceledSubscriptionId
        :raises: ~subscription_client.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.CanceledSubscriptionId"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.cancel.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('CanceledSubscriptionId', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel'}

    def rename(
        self,
        subscription_id,  # type: str
        subscription_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.RenamedSubscriptionId"
        """The operation to rename a subscription.

        :param subscription_id: Subscription Id.
        :type subscription_id: str
        :param subscription_name: New subscription name.
        :type subscription_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenamedSubscriptionId or the result of cls(response)
        :rtype: ~subscription_client.models.RenamedSubscriptionId
        :raises: ~subscription_client.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.RenamedSubscriptionId"]
        error_map = kwargs.pop('error_map', {})

        body = models.SubscriptionName(subscription_name=subscription_name)
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.rename.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(body, 'SubscriptionName')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('RenamedSubscriptionId', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    rename.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename'}

    def enable(
        self,
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.EnabledSubscriptionId"
        """The operation to enable a subscription.

        :param subscription_id: Subscription Id.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EnabledSubscriptionId or the result of cls(response)
        :rtype: ~subscription_client.models.EnabledSubscriptionId
        :raises: ~subscription_client.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.EnabledSubscriptionId"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.enable.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('EnabledSubscriptionId', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    enable.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable'}

    def _create_subscription_initial(
        self,
        billing_account_name,  # type: str
        billing_profile_name,  # type: str
        invoice_section_name,  # type: str
        display_name,  # type: str
        sku_id,  # type: str
        cost_center=None,  # type: Optional[str]
        owner=None,  # type: Optional["models.AdPrincipal"]
        management_group_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        error_map = kwargs.pop('error_map', {})

        body = models.ModernSubscriptionCreationParameters(display_name=display_name, sku_id=sku_id, cost_center=cost_center, owner=owner, management_group_id=management_group_id)
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self._create_subscription_initial.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(body, 'ModernSubscriptionCreationParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_subscription_initial.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription'}

    def begin_create_subscription(
        self,
        billing_account_name,  # type: str
        billing_profile_name,  # type: str
        invoice_section_name,  # type: str
        display_name,  # type: str
        sku_id,  # type: str
        cost_center=None,  # type: Optional[str]
        owner=None,  # type: Optional["models.AdPrincipal"]
        management_group_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        """The operation to create a new WebDirect or EA Azure subscription.

        :param billing_account_name: The name of the Microsoft Customer Agreement billing account for
         which you want to create the subscription.
        :type billing_account_name: str
        :param billing_profile_name: The name of the billing profile in the billing account for which
         you want to create the subscription.
        :type billing_profile_name: str
        :param invoice_section_name: The name of the invoice section in the billing account for which
         you want to create the subscription.
        :type invoice_section_name: str
        :param display_name: The friendly name of the subscription.
        :type display_name: str
        :param sku_id: The SKU ID of the Azure plan. Azure plan determines the pricing and service-
         level agreement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft
         Azure Plan for DevTest.
        :type sku_id: str
        :param cost_center: If set, the cost center will show up on the Azure usage and charges file.
        :type cost_center: str
        :param owner: Active Directory Principal who’ll get owner access on the new subscription.
        :type owner: ~subscription_client.models.AdPrincipal
        :param management_group_id: The identifier of the management group to which this subscription
         will be associated.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns SubscriptionCreationResult
        :rtype: ~azure.core.polling.LROPoller[~subscription_client.models.SubscriptionCreationResult]

        :raises ~subscription_client.models.ErrorResponseException:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        raw_result = self._create_subscription_initial(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            display_name=display_name,
            sku_id=sku_id,
            cost_center=cost_center,
            owner=owner,
            management_group_id=management_group_id,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_subscription.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription'}

    def _create_csp_subscription_initial(
        self,
        billing_account_name,  # type: str
        customer_name,  # type: str
        display_name,  # type: str
        sku_id,  # type: str
        reseller_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        error_map = kwargs.pop('error_map', {})

        body = models.ModernCspSubscriptionCreationParameters(display_name=display_name, sku_id=sku_id, reseller_id=reseller_id)
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self._create_csp_subscription_initial.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(body, 'ModernCspSubscriptionCreationParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_csp_subscription_initial.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription'}

    def begin_create_csp_subscription(
        self,
        billing_account_name,  # type: str
        customer_name,  # type: str
        display_name,  # type: str
        sku_id,  # type: str
        reseller_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        """The operation to create a new CSP subscription.

        :param billing_account_name: The name of the Microsoft Customer Agreement billing account for
         which you want to create the subscription.
        :type billing_account_name: str
        :param customer_name: The name of the customer.
        :type customer_name: str
        :param display_name: The friendly name of the subscription.
        :type display_name: str
        :param sku_id: The SKU ID of the Azure plan. Azure plan determines the pricing and service-
         level agreement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft
         Azure Plan for DevTest.
        :type sku_id: str
        :param reseller_id: Reseller ID, basically MPN Id.
        :type reseller_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns SubscriptionCreationResult
        :rtype: ~azure.core.polling.LROPoller[~subscription_client.models.SubscriptionCreationResult]

        :raises ~subscription_client.models.ErrorResponseException:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        raw_result = self._create_csp_subscription_initial(
            billing_account_name=billing_account_name,
            customer_name=customer_name,
            display_name=display_name,
            sku_id=sku_id,
            reseller_id=reseller_id,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_csp_subscription.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription'}
