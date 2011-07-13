from zope.event import notify

from Products.CMFCore.utils import getToolByName

from plone.app.openid.events import OpenIDUserLoggedInEvent

def registration_received(principal, event):
    portal_membership = getToolByName(principal, 'portal_membership')
    member = portal_membership.getMemberById(principal.getId())

    # Fields defined in openid.extensions.sreg.data_fields
    new_properties = {
        'fullname': event.simple_registration.get('fullname'),
        'email': event.simple_registration.get('email'),
    }

    location = []
    for fname, title in {'postcode': 'Postal Code', 'country': 'Country',
                         'timezone': 'Time Zone'}.items():
        if fname in event.simple_registration and \
           event.simple_registration[fname]:
            location.append('%s: %s' %
                            (title, event.simple_registration[fname]))
    if location:
        new_properties['location'] = ', '.join(location)

    member.setMemberProperties(new_properties)
    notify(OpenIDUserLoggedInEvent(principal))
