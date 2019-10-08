import pytest
import yt

def test_count_particles(json_metadata, ds_info, dobj_type, dobj_args):
    ds = yt.load(ds_info['filename'])
    dobj = getattr(ds, dobj_type)(*tuple(dobj_args))
    json_metadata['yt_test_result'] = {_: dobj[_, "particle_ones"].shape
                                       for _ in ds_info['particle_types']}
    json_metadata['yt_test_name'] = "{}_{}".format(str(ds), dobj_type, dobj_args)
    return True
