# Patches for Dependencies

This directory contains patches for dependencies used by OpenHands.

## litellm-request-attribute.patch

### Description
This patch fixes an issue in the litellm library where an `Exception` object is raised without a `request` attribute, but later code tries to access this attribute.

### Root Cause
In `convert_dict_to_response.py`, an `Exception` object is created and only `status_code` and `message` attributes are set on it. In `exception_mapping_utils.py`, the code assumes that the exception object has a `request` attribute and tries to access it. When the code tries to access `original_exception.request`, it fails with the AttributeError.

### Fix
The patch adds the missing `request` attribute to the exception object in the `convert_dict_to_response.py` file, setting it to `None` since we don't have a real request object to attach.

### Alternative Fix
A workaround has been implemented in the OpenHands LLM class that catches the specific AttributeError and adds the missing `request` attribute to the exception object before re-raising it. This allows the exception handling to continue as expected.

### Testing
Unit tests have been created to verify that the fix works correctly.
