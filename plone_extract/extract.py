""" Needs to be run from within the Plone environment. """

import simplejson

from Products.CMFCore.utils import getToolByName

import settings

def get_id(obj, obj_exp):
    """ Fetches the ID and prepends the traversal path.
        Puts into the obj_exp dict.
    """
    # TODO: Finish!
    obj_exp['id'] = obj.getId()
    
    return obj_exp

def get_dublin_core(obj, obj_exp):
    """ Fetches the Dublin core from the obj.
        Puts into the obj_exp dict.
    """
    for attr in settings.DUBLIN_CORE:
        if hasattr(obj, attr):
            obj_exp[attr]   = getattr(obj, attr, None)
    return obj_exp
    
def get_workflow_state(obj, obj_exp, workflow_tool):
    """ Fetches the workflow state from the obj.
        Puts into the obj_exp dict.
    """
    status = workflowTool.getStatusOf("plone_workflow", obj)
    obj_exp['workflow_state'] = status["review_state"]
    return obj_exp
    
def get_custom_fields(obj, obj_exp, plone_utils):
    """ Fetches custom fields that are not media or file types.
        Puts into the obj_exp dict.
    """
    # TODO: Finish!
    obj_exp['custom_fields'] = {}
    return obj_exp
    

    

def main(context):
    plone_utils     = getToolByName(context,"plone_utils")
    portal_catalog  = getToolByName(context, "portal_catalog")
    workflow_tool   = getToolByName(context, "portal_workflow")
    
    export = []
    for obj in portal_catalog(full_object=True):
        obj_exp = {}

        obj_exp = get_id(obj, obj_exp)

        obj_exp = get_dublin_core(obj, obj_exp)
        
        obj_exp = get_workflow_state(obj, obj_exp, workflow_tool)
        
        obj_exp = get_custom_fields(obj, obj_exp, plone_utils)
        
        obj_exp['content_type'] = obj.portal_type        
        
        export.append(obj_exp)
        
        
    jsonified_export = simplejson.loads(export)




if __name__ == "__main__":
    main()