==============
Plone Extract
==============

.. contents:: 

Introduction
============

A common use case in Plone is content extraction. Either to another Plone site or to another framework. Existing Plone export methods are either incomplete or rely heavily on complex XML structures. This project will focus on keeping things simple and easy. Some quick notes:

#. Rather than traversing the content of the system, a simple portal_catalog query against all content will be performed.
#. Content types will be stored in one file, users in another, and so forth. Rendering multiple types of data in one file adds too much complexity.
#. Each content item is represented by a dictionary.
#. The export format is JSON.

Content Type Format
===================

Each content type will be represented by a standard python dict. Since Plone content types have many of the metadata fields defined by `Dublin core`_ as their standard fields, the extract will include those fields. It will add these as well:

:id:
    More than just a standard Zope id, this displays the location of the content in the Plone heirarchy. So instead of just ``my-content`` you would get ``root/major-content-section/sub-content-section/my-content``. Based off of this you can infer the location of the content within the architecture of the site.
    
:content_type:
    This field provides the type of the content type. In Plone terms this would be the ``portal_type``. 
    
:workflow_state:
    This field displays the current workflow state of the content type. In Plone terms this would be the ``review_state``
    
:custom_fields:
    This field provides a dictionary that lists the names of all custom fields and the content within.

.. _Dublin core: http://dublincore.org/