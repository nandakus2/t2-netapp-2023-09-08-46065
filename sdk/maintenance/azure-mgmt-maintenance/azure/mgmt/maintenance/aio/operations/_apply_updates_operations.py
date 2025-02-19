# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._apply_updates_operations import (
    build_create_or_update_parent_request,
    build_create_or_update_request,
    build_get_parent_request,
    build_get_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ApplyUpdatesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.maintenance.aio.MaintenanceManagementClient`'s
        :attr:`apply_updates` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        apply_update_name: str,
        **kwargs: Any
    ) -> _models.ApplyUpdate:
        """Track Updates to resource with parent.

        Track maintenance updates to resource with parent.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param provider_name: Resource provider name. Required.
        :type provider_name: str
        :param resource_parent_type: Resource parent type. Required.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier. Required.
        :type resource_parent_name: str
        :param resource_type: Resource type. Required.
        :type resource_type: str
        :param resource_name: Resource identifier. Required.
        :type resource_name: str
        :param apply_update_name: applyUpdate Id. Required.
        :type apply_update_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplyUpdate or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ApplyUpdate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ApplyUpdate] = kwargs.pop("cls", None)

        request = build_get_parent_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            resource_parent_type=resource_parent_type,
            resource_parent_name=resource_parent_name,
            resource_type=resource_type,
            resource_name=resource_name,
            apply_update_name=apply_update_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_parent.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_parent.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/{applyUpdateName}"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        apply_update_name: str,
        **kwargs: Any
    ) -> _models.ApplyUpdate:
        """Track Updates to resource.

        Track maintenance updates to resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param provider_name: Resource provider name. Required.
        :type provider_name: str
        :param resource_type: Resource type. Required.
        :type resource_type: str
        :param resource_name: Resource identifier. Required.
        :type resource_name: str
        :param apply_update_name: applyUpdate Id. Required.
        :type apply_update_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplyUpdate or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ApplyUpdate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ApplyUpdate] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            resource_type=resource_type,
            resource_name=resource_name,
            apply_update_name=apply_update_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/{applyUpdateName}"
    }

    @distributed_trace_async
    async def create_or_update_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        **kwargs: Any
    ) -> _models.ApplyUpdate:
        """Apply Updates to resource with parent.

        Apply maintenance updates to resource with parent.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param provider_name: Resource provider name. Required.
        :type provider_name: str
        :param resource_parent_type: Resource parent type. Required.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier. Required.
        :type resource_parent_name: str
        :param resource_type: Resource type. Required.
        :type resource_type: str
        :param resource_name: Resource identifier. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplyUpdate or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ApplyUpdate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ApplyUpdate] = kwargs.pop("cls", None)

        request = build_create_or_update_parent_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            resource_parent_type=resource_parent_type,
            resource_parent_name=resource_parent_name,
            resource_type=resource_type,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.create_or_update_parent.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update_parent.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/default"
    }

    @distributed_trace_async
    async def create_or_update(
        self, resource_group_name: str, provider_name: str, resource_type: str, resource_name: str, **kwargs: Any
    ) -> _models.ApplyUpdate:
        """Apply Updates to resource.

        Apply maintenance updates to resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param provider_name: Resource provider name. Required.
        :type provider_name: str
        :param resource_type: Resource type. Required.
        :type resource_type: str
        :param resource_name: Resource identifier. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplyUpdate or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ApplyUpdate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ApplyUpdate] = kwargs.pop("cls", None)

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            resource_type=resource_type,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ApplyUpdate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/applyUpdates/default"
    }

    @distributed_trace
    def list(self, **kwargs: Any) -> AsyncIterable["_models.ApplyUpdate"]:
        """Get Configuration records within a subscription.

        Get Configuration records within a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ApplyUpdate or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.maintenance.models.ApplyUpdate]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListApplyUpdate] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ListApplyUpdate", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Maintenance/applyUpdates"}
