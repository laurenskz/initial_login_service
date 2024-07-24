from com.baboea.models import scraping_pb2 as _scraping_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainsList(_message.Message):
    __slots__ = ("domains", "nextPageToken")
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedCompositeFieldContainer[_scraping_pb2.ScrapeDomain]
    nextPageToken: str
    def __init__(self, domains: _Optional[_Iterable[_Union[_scraping_pb2.ScrapeDomain, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class GetPagesRequest(_message.Message):
    __slots__ = ("domainId",)
    DOMAINID_FIELD_NUMBER: _ClassVar[int]
    domainId: str
    def __init__(self, domainId: _Optional[str] = ...) -> None: ...

class UpdatePagesRequest(_message.Message):
    __slots__ = ("domainId", "urls")
    DOMAINID_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    domainId: str
    urls: _containers.RepeatedCompositeFieldContainer[_scraping_pb2.UrlScrapeNode]
    def __init__(self, domainId: _Optional[str] = ..., urls: _Optional[_Iterable[_Union[_scraping_pb2.UrlScrapeNode, _Mapping]]] = ...) -> None: ...

class GetPagesResponse(_message.Message):
    __slots__ = ("urls", "nextPageToken")
    URLS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGETOKEN_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedCompositeFieldContainer[_scraping_pb2.UrlScrapeNode]
    nextPageToken: str
    def __init__(self, urls: _Optional[_Iterable[_Union[_scraping_pb2.UrlScrapeNode, _Mapping]]] = ..., nextPageToken: _Optional[str] = ...) -> None: ...

class ScrapedObject(_message.Message):
    __slots__ = ("recipe",)
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    recipe: _recipes_pb2.RemoteRecipe
    def __init__(self, recipe: _Optional[_Union[_recipes_pb2.RemoteRecipe, _Mapping]] = ...) -> None: ...

class ScrapedPage(_message.Message):
    __slots__ = ("domain", "url", "nugget", "localeIso6391")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NUGGET_FIELD_NUMBER: _ClassVar[int]
    LOCALEISO6391_FIELD_NUMBER: _ClassVar[int]
    domain: str
    url: str
    nugget: ScrapedObject
    localeIso6391: str
    def __init__(self, domain: _Optional[str] = ..., url: _Optional[str] = ..., nugget: _Optional[_Union[ScrapedObject, _Mapping]] = ..., localeIso6391: _Optional[str] = ...) -> None: ...
