from rest_framework.reverse import reverse


# TODO - ideally these models would be created directly in the DB but it doesn't appear to be
# working with the boilerplate code and fixing it was taking too long


def create_address(client, street, city, postcode, council):
    address = {
        'street': street,
        'city': city,
        'postcode': postcode,
        'council': council,
    }

    url = addresses_url()

    response = client.post(url, address, format="json")

    return response.data


def create_rubbish_type(client, name):
    rubbish_type = {
        'name': name,
    }

    url = rubbish_types_url()

    response = client.post(url, rubbish_type, format="json")

    return response.data


def create_collection_schedule(client, address_id, rubbish_type, frequency, start_date):
    collection_schedule = {
        'rubbish_type': rubbish_type,
        'frequency': frequency,
        'start_date': start_date,
    }

    url = collection_schedules_url(address_id)

    response = client.post(url, collection_schedule, format="json")

    return response.data


def addresses_url():
    return reverse("v1alpha:addresses", kwargs={
        'version': 'v1alpha1'
    })


def rubbish_types_url():
    return reverse("v1alpha:rubbish_types", kwargs={
        'version': 'v1alpha1'
    })


def collection_schedules_url(address_id):
    return reverse("v1alpha:collection_schedules", kwargs={
        'version': 'v1alpha1',
        'address_id': address_id,
    })
