
def pass_through_undefined(str):
    if str != "undefined":
        str = '"' + str + '"'
    return str

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            # base 64
            'quote_defined_strings': pass_through_undefined
        }