from restfly.endpoint import APIEndpoint

from .host import HostAPI
from .network import NetworkAPI
from .wildcard import WildcardAPI
from .group import GroupAPI
from .gsn_handover_group import GSNHandoverGroupAPI
from .address_range import AddressRangeAPI
from .multicast_address_range import MulticastAddressRangeAPI
from .group_with_exclusion import GroupWithExclusionAPI


class NetworkObjects(APIEndpoint):
    @property
    def host(self):
        """The interface object for the network objects type "Host" Management."""
        return HostAPI(self)

    @property
    def network(self):
        """The interface object for the network objects type "Network" Management."""
        return NetworkAPI(self)

    @property
    def wildcard(self):
        """The interface object for the network objects type "Wildcard" Management."""
        return WildcardAPI(self)

    @property
    def group(self):
        """The interface object for the network objects type "Group" Management."""
        return GroupAPI(self)

    @property
    def gsn_handover_group(self):
        """The interface object for the network objects type "GSN Handover Group" Management."""
        return GSNHandoverGroupAPI(self)

    @property
    def address_range(self):
        """The interface object for the network objects type "Address Range" Management."""
        return AddressRangeAPI(self)

    @property
    def multicast_address_range(self):
        """The interface object for the network objects type "Multicast Address Range" Management."""
        return MulticastAddressRangeAPI(self)

    @property
    def group_with_exclusion(self):
        """The interface object for the network objects type "Group With Exclusion" Management."""
        return GroupWithExclusionAPI(self)
