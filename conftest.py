import yaml

def pytest_generate_tests(metafunc):
    config = yaml.load(open("dataset_descriptions.yml"), Loader = yaml.SafeLoader)
    print(config.keys())
    if "ds" in metafunc.fixturenames:
        cc = config['datasets']
        metafunc.parametrize("ds", [_['filename'] for _ in cc],
                             ids = [_['name'] for _ in cc])
    if "dobj_type" in metafunc.fixturenames:
        params = [(_['type'], _['arguments']) for _ in config['data_objects']]
        ids = [_['name'] for _ in config['data_objects']]
        metafunc.parametrize("dobj_type,dobj_args", params, ids = ids)
