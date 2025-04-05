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


def addresses_url():
    return reverse("v1alpha:addresses", kwargs={
        'version': 'v1alpha1'
    })
