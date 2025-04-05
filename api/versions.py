"""
Holds information about the default versions of the API

"""

# Links a version name (the thing that would be included in the request url) to a `urls.app_name`
# which will url_patterns for that version
VERSIONS_TO_APP_NAME = {
    "v1alpha1": "v1alpha",
}
AVAILABLE_VERSIONS = set(VERSIONS_TO_APP_NAME.keys())
