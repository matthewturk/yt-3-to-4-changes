import yaml
import re

# Modified version of:
# https://stackoverflow.com/questions/39553008/how-to-read-a-python-tuple-using-pyyaml

def yml_tuple_constructor(loader, node): 
    # this little parse is really just for what I needed, feel free to change it!
    def parse_tup_el(el):
        # try to convert into int or float else keep the string
        if el.isdigit():
            return int(el)
        try:
            return float(el)
        except ValueError:
            el = el.strip()
            if len(el) > 1 and el[0] == el[-1] and el[0] in ('"',"'"):
                el = el[1:-1]
            return el
    value = loader.construct_scalar(node)
    # remove the ( ) from the string
    tup_elements = value[1:-1].split(',')
    # remove the last element if the tuple was written as (x,b,)
    if tup_elements[-1] == '':
        tup_elements.pop(-1)
    tup = tuple(map(parse_tup_el, tup_elements))
    return tup

# !tuple is my own tag name, I think you could choose anything you want
# this is to spot the strings written as tuple in the yaml
class CustomLoader(yaml.SafeLoader):
    pass

CustomLoader.add_implicit_resolver(u'!tuple',
                                   re.compile(r'\(([^)]*)\)'),
                                   None)
CustomLoader.add_constructor(u'!tuple', yml_tuple_constructor)

def pytest_generate_tests(metafunc):
    config = yaml.load(open("dataset_descriptions.yml"), Loader = CustomLoader)
    print(config.keys())
    if "ds_info" in metafunc.fixturenames:
        cc = config['datasets']
        metafunc.parametrize("ds_info", cc, ids = [_['name'] for _ in cc])
    if "dobj_type" in metafunc.fixturenames:
        params = [(_['type'], _['arguments']) for _ in config['data_objects']]
        ids = [_['name'] for _ in config['data_objects']]
        metafunc.parametrize("dobj_type,dobj_args", params, ids = ids)
