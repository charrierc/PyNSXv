__author__ = 'asteer'

import lib.session as session

default_transport_zone_name = 'LocalTransportZone'

# Create a new Session - debug is enabled so will be very noisy
s = session.Session('172.17.100.109', debug=True)

# Create a new logical switch
lswitch_xml_tree = s.logicalSwitch.create(default_transport_zone_name, 'new-lswitch10')

# And then delete it...
s.logicalSwitch.delete(lswitch_xml_tree.find('objectId').text)
