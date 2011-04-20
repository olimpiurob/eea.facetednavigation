""" Faceted Navigation public interfaces
"""
from zope.component.interfaces import IObjectEvent

# Subtypes
from eea.facetednavigation.subtypes.interfaces import IPossibleFacetedNavigable
from eea.facetednavigation.subtypes.interfaces import IFacetedNavigable

# Criteria
from eea.facetednavigation.criteria.interfaces import ICriteria

# Layout
from eea.facetednavigation.layout.interfaces import IFacetedLayout

# Search
from eea.facetednavigation.search.interfaces import IFacetedCatalog

# Widgets
from eea.facetednavigation.widgets.interfaces import IWidget
from eea.facetednavigation.widgets.interfaces import IWidgetsInfo

# After query adapter
from eea.facetednavigation.widgets.interfaces import IWidgetFilterBrains

# Language
from eea.facetednavigation.indexes.language.interfaces import (
    ILanguageWidgetAdapter,
)

# Versioning
from eea.facetednavigation.versions.interfaces import IFacetedVersion

# Wrapper
from eea.facetednavigation.subtypes.interfaces import IFacetedWrapper

#
# Events
#
class IFacetedEvent(IObjectEvent):
    """ All faceted events should inherit from this class
    """

class IFacetedGlobalSettingsChangedEvent(IFacetedEvent):
    """ Faceted global settings updated
    """

class IFacetedWillBeEnabledEvent(IFacetedEvent):
    """ Faceted navigation is going to be enabled
    """

class IFacetedEnabledEvent(IFacetedEvent):
    """ Faceted navigation enabled
    """

class IFacetedWillBeDisabledEvent(IFacetedEvent):
    """ Faceted navigation is going to be disabled
    """

class IFacetedDisabledEvent(IFacetedEvent):
    """ Faceted navigation disabled
    """

# pylint, pyflakes
__all__ = [
    IPossibleFacetedNavigable.__name__,
    IFacetedNavigable.__name__,
    IWidgetsInfo.__name__,
    IWidgetFilterBrains.__name__,
    IFacetedCatalog.__name__,
    IFacetedLayout.__name__,
    IFacetedVersion.__name__,
    ILanguageWidgetAdapter.__name__,
    ICriteria.__name__,
    IFacetedWrapper.__name__,
    IWidget.__name__,
]
