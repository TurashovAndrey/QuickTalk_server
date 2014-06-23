from storm.locals import *

class User(object):
    __storm_table__ = "leasing_user"
    id = Int(primary=True)
    user_id = UUID()
    username = Unicode()
    hashed_pw = Unicode()
    first_name = Unicode()
    last_name = Unicode()
    email = Unicode()
    created = Int()
    created_ip = Unicode()
    updated = Int()
    updated_ip = Unicode()
    birthday = Date()
    hometown = Unicode()
    telephone = Unicode()

class AdvertCategories(object):
    __storm_table__ = "leasing_advert_categories"
    id = Int(primary=True)
    category_name = Unicode()

class AdvertTypes(object):
    __storm_table__ = "leasing_advert_types"
    id = Int(primary=True)
    category_id = Int()
    type_name = Unicode()

class Advert(object):
    __storm_table__ = "leasing_advert"
    id = Int(primary=True)
    advert_id = UUID()
    title = Unicode()
    description = Unicode()
    type_id = Int()
    status_id = Int()
    created_by = UUID()
    updated_by = UUID()
    price = Float()

class AdvertLocations(object):
    __storm_table__ = "leasing_advert_locations"
    id = Int(primary=True)
    advert_id = UUID()
    location = Unicode()
    latitude = Decimal()
    longitude = Decimal()
    is_pickup_location = Bool()

class Statuses(object):
    __storm_table__ = "leasing_statuses"
    id = Int(primary=True)
    status = Unicode()

class AdvertGroups(object):
    __storm_table__ = "leasing_advert_groups"
    id = Int(primary=True)
    advert_id = UUID()
    group_id = Int()

class AdvertUserGroups(object):
    __storm_table__ = "leasing_advert_user_groups"
    id = Int(primary=True)
    advert_id = UUID()
    group_id = Int()
    user_id = UUID()

class AdvertItems(object):
    __storm_table__ = "leasing_advert_items"
    id = Int(primary=True)
    advert_id = UUID()
    item_id = UUID()

class Locations(object):
    __storm_table__ = "leasing_locations"
    id = Int(primary=True)
    hub_id = UUID()
    location = Unicode()
    latitude = Decimal()
    longitude = Decimal()

class Request(object):
    __storm_table__ = "leasing_request"
    id = Int(primary=True)
    advert_id = UUID()
    request_user_id = UUID()

class UserComment(object):
    __storm_table__ = "leasing_user_comment"
    id = Int(primary=True)
    user_id = UUID()
    from_user_id = UUID()
    description = Unicode()

class AdvertComment(object):
    __storm_table__ = "leasing_advert_comment"
    id = Int(primary=True)
    advert_id = UUID()
    from_user_id = UUID()
    description = Unicode()

class City(object):
    __storm_table__ = "leasing_city"
    id = Int(primary=True)
    city_name = Unicode()
    country_id = Int()