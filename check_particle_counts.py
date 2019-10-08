import pytest
import yt

data_objects = [
    ('small_sphere', ('sphere', ('c', (0.1, 'unitary')))),
    ('bigger_sphere', ('sphere', ('c', (0.25, 'unitary')))),
]

datasets = ['IsolatedGalaxy/galaxy0030/galaxy0030']

def test_count_particles(json_metadata, ds, dobj_type, dobj_args):
    ds = yt.load(ds)
    json_metadata['yt_test_result'] = {}
    json_metadata['yt_test_name'] = "{}_{}".format(str(ds), dobj_type, dobj_args)
    return True


#@pytest.mark.parametrize("ds", datasets)
#@pytest.mark.parametrize("dobj_name,dobj_def", data_objects)


