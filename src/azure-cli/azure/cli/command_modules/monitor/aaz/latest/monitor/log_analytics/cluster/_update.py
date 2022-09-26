# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor log-analytics cluster update",
)
class Update(AAZCommand):
    """Update a cluster instance.

    Update a cluster instance.

    :example: Update a cluster instance.
        az monitor log-analytics cluster update -g MyResourceGroup -n MyCluster --key-vault-uri https://myvault.vault.azure.net/ --key-name my-key --key-version fe0adcedd8014aed9c22e9aefb81a1ds --sku-capacity 1000
    """

    _aaz_info = {
        "version": "2021-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/clusters/{}", "2021-06-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="Name of the Log Analytics Cluster.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Identity"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--identity-type"],
            arg_group="Identity",
            help="Type of managed service identity.",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned = AAZDictArg(
            options=["--user-assigned"],
            arg_group="Identity",
            help="The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.",
            nullable=True,
        )

        user_assigned = cls._args_schema.user_assigned
        user_assigned.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        # define Arg Group "Key Properties"

        _args_schema = cls._args_schema
        _args_schema.key_name = AAZStrArg(
            options=["--key-name"],
            arg_group="Key Properties",
            help="The name of the key associated with the Log Analytics cluster.",
            nullable=True,
        )
        _args_schema.key_rsa_size = AAZIntArg(
            options=["--key-rsa-size"],
            arg_group="Key Properties",
            help="Selected key minimum required size.",
            nullable=True,
        )
        _args_schema.key_vault_uri = AAZStrArg(
            options=["--key-vault-uri"],
            arg_group="Key Properties",
            help="The Key Vault uri which holds they key associated with the Log Analytics cluster.",
            nullable=True,
        )
        _args_schema.key_version = AAZStrArg(
            options=["--key-version"],
            arg_group="Key Properties",
            help="The version of the key associated with the Log Analytics cluster.",
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.billing_type = AAZStrArg(
            options=["--billing-type"],
            arg_group="Properties",
            help="The cluster's billing type.",
            nullable=True,
            enum={"Cluster": "Cluster", "Workspaces": "Workspaces"},
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.sku_capacity = AAZIntArg(
            options=["--sku-capacity"],
            arg_group="Sku",
            help="The capacity of the SKU. It can be decreased only after 31 days.",
            nullable=True,
            enum={"1000": 1000, "2000": 2000, "500": 500, "5000": 5000},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ClustersGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ClustersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    # @register_callback
    def pre_instance_update(self, instance):
        pass

    # @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_cluster_read(cls._schema_on_200)

            return cls._schema_on_200

    class ClustersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_cluster_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType)
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("billingType", AAZStrType, ".billing_type")
                properties.set_prop("keyVaultProperties", AAZObjectType)

            key_vault_properties = _builder.get(".properties.keyVaultProperties")
            if key_vault_properties is not None:
                key_vault_properties.set_prop("keyName", AAZStrType, ".key_name")
                key_vault_properties.set_prop("keyRsaSize", AAZIntType, ".key_rsa_size")
                key_vault_properties.set_prop("keyVaultUri", AAZStrType, ".key_vault_uri")
                key_vault_properties.set_prop("keyVersion", AAZStrType, ".key_version")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("capacity", AAZIntType, ".sku_capacity")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_cluster_read = None


def _build_schema_cluster_read(_schema):
    global _schema_cluster_read
    if _schema_cluster_read is not None:
        _schema.id = _schema_cluster_read.id
        _schema.identity = _schema_cluster_read.identity
        _schema.location = _schema_cluster_read.location
        _schema.name = _schema_cluster_read.name
        _schema.properties = _schema_cluster_read.properties
        _schema.sku = _schema_cluster_read.sku
        _schema.tags = _schema_cluster_read.tags
        _schema.type = _schema_cluster_read.type
        return

    _schema_cluster_read = AAZObjectType()

    cluster_read = _schema_cluster_read
    cluster_read.id = AAZStrType(
        flags={"read_only": True},
    )
    cluster_read.identity = AAZObjectType()
    cluster_read.location = AAZStrType(
        flags={"required": True},
    )
    cluster_read.name = AAZStrType(
        flags={"read_only": True},
    )
    cluster_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    cluster_read.sku = AAZObjectType()
    cluster_read.tags = AAZDictType()
    cluster_read.type = AAZStrType(
        flags={"read_only": True},
    )

    identity = _schema_cluster_read.identity
    identity.principal_id = AAZStrType(
        serialized_name="principalId",
        flags={"read_only": True},
    )
    identity.tenant_id = AAZStrType(
        serialized_name="tenantId",
        flags={"read_only": True},
    )
    identity.type = AAZStrType(
        flags={"required": True},
    )
    identity.user_assigned_identities = AAZDictType(
        serialized_name="userAssignedIdentities",
    )

    user_assigned_identities = _schema_cluster_read.identity.user_assigned_identities
    user_assigned_identities.Element = AAZObjectType()

    _element = _schema_cluster_read.identity.user_assigned_identities.Element
    _element.client_id = AAZStrType(
        serialized_name="clientId",
        flags={"read_only": True},
    )
    _element.principal_id = AAZStrType(
        serialized_name="principalId",
        flags={"read_only": True},
    )

    properties = _schema_cluster_read.properties
    properties.associated_workspaces = AAZListType(
        serialized_name="associatedWorkspaces",
        flags={"read_only": True},
    )
    properties.billing_type = AAZStrType(
        serialized_name="billingType",
    )
    properties.capacity_reservation_properties = AAZObjectType(
        serialized_name="capacityReservationProperties",
    )
    properties.cluster_id = AAZStrType(
        serialized_name="clusterId",
        flags={"read_only": True},
    )
    properties.created_date = AAZStrType(
        serialized_name="createdDate",
        flags={"read_only": True},
    )
    properties.is_availability_zones_enabled = AAZBoolType(
        serialized_name="isAvailabilityZonesEnabled",
    )
    properties.key_vault_properties = AAZObjectType(
        serialized_name="keyVaultProperties",
    )
    properties.last_modified_date = AAZStrType(
        serialized_name="lastModifiedDate",
        flags={"read_only": True},
    )
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
        flags={"read_only": True},
    )

    associated_workspaces = _schema_cluster_read.properties.associated_workspaces
    associated_workspaces.Element = AAZObjectType(
        flags={"read_only": True},
    )

    _element = _schema_cluster_read.properties.associated_workspaces.Element
    _element.associate_date = AAZStrType(
        serialized_name="associateDate",
        flags={"read_only": True},
    )
    _element.resource_id = AAZStrType(
        serialized_name="resourceId",
        flags={"read_only": True},
    )
    _element.workspace_id = AAZStrType(
        serialized_name="workspaceId",
        flags={"read_only": True},
    )
    _element.workspace_name = AAZStrType(
        serialized_name="workspaceName",
        flags={"read_only": True},
    )

    capacity_reservation_properties = _schema_cluster_read.properties.capacity_reservation_properties
    capacity_reservation_properties.last_sku_update = AAZStrType(
        serialized_name="lastSkuUpdate",
        flags={"read_only": True},
    )
    capacity_reservation_properties.min_capacity = AAZIntType(
        serialized_name="minCapacity",
        flags={"read_only": True},
    )

    key_vault_properties = _schema_cluster_read.properties.key_vault_properties
    key_vault_properties.key_name = AAZStrType(
        serialized_name="keyName",
    )
    key_vault_properties.key_rsa_size = AAZIntType(
        serialized_name="keyRsaSize",
    )
    key_vault_properties.key_vault_uri = AAZStrType(
        serialized_name="keyVaultUri",
    )
    key_vault_properties.key_version = AAZStrType(
        serialized_name="keyVersion",
    )

    sku = _schema_cluster_read.sku
    sku.capacity = AAZIntType()
    sku.name = AAZStrType()

    tags = _schema_cluster_read.tags
    tags.Element = AAZStrType()

    _schema.id = _schema_cluster_read.id
    _schema.identity = _schema_cluster_read.identity
    _schema.location = _schema_cluster_read.location
    _schema.name = _schema_cluster_read.name
    _schema.properties = _schema_cluster_read.properties
    _schema.sku = _schema_cluster_read.sku
    _schema.tags = _schema_cluster_read.tags
    _schema.type = _schema_cluster_read.type


__all__ = ["Update"]
