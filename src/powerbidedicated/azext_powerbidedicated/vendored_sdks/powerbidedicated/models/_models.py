# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CheckCapacityNameAvailabilityParameters(Model):
    """Details of capacity name request body.

    :param name: Name for checking availability.
    :type name: str
    :param type: The resource type of PowerBI dedicated. Default value:
     "Microsoft.PowerBIDedicated/capacities" .
    :type type: str
    """

    _validation = {
        'name': {'max_length': 63, 'min_length': 3, 'pattern': r'^[a-z][a-z0-9]*$'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckCapacityNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', "Microsoft.PowerBIDedicated/capacities")


class CheckCapacityNameAvailabilityResult(Model):
    """The checking result of capacity name availability.

    :param name_available: Indicator of availability of the capacity name.
    :type name_available: bool
    :param reason: The reason of unavailability.
    :type reason: str
    :param message: The detailed message of the request unavailability.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckCapacityNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Resource(Model):
    """Represents an instance of an PowerBI Dedicated resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: An identifier that represents the PowerBI Dedicated resource.
    :vartype id: str
    :ivar name: The name of the PowerBI Dedicated resource.
    :vartype name: str
    :ivar type: The type of the PowerBI Dedicated resource.
    :vartype type: str
    :param location: Required. Location of the PowerBI Dedicated resource.
    :type location: str
    :param sku: Required. The SKU of the PowerBI Dedicated resource.
    :type sku: ~azure.mgmt.powerbidedicated.models.ResourceSku
    :param tags: Key-value pairs of additional resource provisioning
     properties.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.sku = kwargs.get('sku', None)
        self.tags = kwargs.get('tags', None)


class DedicatedCapacity(Resource):
    """Represents an instance of a Dedicated Capacity resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: An identifier that represents the PowerBI Dedicated resource.
    :vartype id: str
    :ivar name: The name of the PowerBI Dedicated resource.
    :vartype name: str
    :ivar type: The type of the PowerBI Dedicated resource.
    :vartype type: str
    :param location: Required. Location of the PowerBI Dedicated resource.
    :type location: str
    :param sku: Required. The SKU of the PowerBI Dedicated resource.
    :type sku: ~azure.mgmt.powerbidedicated.models.ResourceSku
    :param tags: Key-value pairs of additional resource provisioning
     properties.
    :type tags: dict[str, str]
    :param administration: A collection of Dedicated capacity administrators
    :type administration:
     ~azure.mgmt.powerbidedicated.models.DedicatedCapacityAdministrators
    :ivar state: The current state of PowerBI Dedicated resource. The state is
     to indicate more states outside of resource provisioning. Possible values
     include: 'Deleting', 'Succeeded', 'Failed', 'Paused', 'Suspended',
     'Provisioning', 'Updating', 'Suspending', 'Pausing', 'Resuming',
     'Preparing', 'Scaling'
    :vartype state: str or ~azure.mgmt.powerbidedicated.models.State
    :ivar provisioning_state: The current deployment state of PowerBI
     Dedicated resource. The provisioningState is to indicate states for
     resource provisioning. Possible values include: 'Deleting', 'Succeeded',
     'Failed', 'Paused', 'Suspended', 'Provisioning', 'Updating', 'Suspending',
     'Pausing', 'Resuming', 'Preparing', 'Scaling'
    :vartype provisioning_state: str or
     ~azure.mgmt.powerbidedicated.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'administration': {'key': 'properties.administration', 'type': 'DedicatedCapacityAdministrators'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DedicatedCapacity, self).__init__(**kwargs)
        self.administration = kwargs.get('administration', None)
        self.state = None
        self.provisioning_state = None


class DedicatedCapacityAdministrators(Model):
    """An array of administrator user identities.

    :param members: An array of administrator user identities.
    :type members: list[str]
    """

    _attribute_map = {
        'members': {'key': 'members', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(DedicatedCapacityAdministrators, self).__init__(**kwargs)
        self.members = kwargs.get('members', None)


class DedicatedCapacityUpdateParameters(Model):
    """Provision request specification.

    :param sku: The SKU of the Dedicated capacity resource.
    :type sku: ~azure.mgmt.powerbidedicated.models.ResourceSku
    :param tags: Key-value pairs of additional provisioning properties.
    :type tags: dict[str, str]
    :param administration: A collection of Dedicated capacity administrators
    :type administration:
     ~azure.mgmt.powerbidedicated.models.DedicatedCapacityAdministrators
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'administration': {'key': 'properties.administration', 'type': 'DedicatedCapacityAdministrators'},
    }

    def __init__(self, **kwargs):
        super(DedicatedCapacityUpdateParameters, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.tags = kwargs.get('tags', None)
        self.administration = kwargs.get('administration', None)


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Operation(Model):
    """Capacities REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.powerbidedicated.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft.PowerBIDedicated.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: capacity,
     etc.
    :vartype resource: str
    :ivar operation: Operation type: create, update, delete, etc.
    :vartype operation: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None


class ResourceSku(Model):
    """Represents the SKU name and Azure pricing tier for PowerBI Dedicated
    resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the SKU level.
    :type name: str
    :param tier: The name of the Azure pricing tier to which the SKU applies.
     Possible values include: 'PBIE_Azure'
    :type tier: str or ~azure.mgmt.powerbidedicated.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)


class SkuDetailsForExistingResource(Model):
    """An object that represents SKU details for existing resources.

    :param sku: The SKU in SKU details for existing resources.
    :type sku: ~azure.mgmt.powerbidedicated.models.ResourceSku
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
    }

    def __init__(self, **kwargs):
        super(SkuDetailsForExistingResource, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)


class SkuEnumerationForExistingResourceResult(Model):
    """An object that represents enumerating SKUs for existing resources.

    :param value: The collection of available SKUs for existing resources
    :type value:
     list[~azure.mgmt.powerbidedicated.models.SkuDetailsForExistingResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SkuDetailsForExistingResource]'},
    }

    def __init__(self, **kwargs):
        super(SkuEnumerationForExistingResourceResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class SkuEnumerationForNewResourceResult(Model):
    """An object that represents enumerating SKUs for new resources.

    :param value: The collection of available SKUs for new resources
    :type value: list[~azure.mgmt.powerbidedicated.models.ResourceSku]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceSku]'},
    }

    def __init__(self, **kwargs):
        super(SkuEnumerationForNewResourceResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)