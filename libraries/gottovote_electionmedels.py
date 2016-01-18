# This will come in after the MVP

#
#
# class Aspirants(NebriOSModel):
#     countyid = NebriOSField(required=True)
#     candidate = NebriOSField(required=True)
#     # 2
#     # 8
#     total = NebriOSField(required=True)
#
#
# class presidential_candidates(NebriOSModel):
#     surname = NebriOSField(required=True)
#     other_name = NebriOSField(required=True)
#     code = NebriOSField(required=True)
#     party = NebriOSField(required=True)
#     running_mate = NebriOSField(required=True)
#     contest_id = NebriOSField(required=True)
#     winner = NebriOSField(required=True, default=0)
#
# class parties(NebriOSModel):
#     name = NebriOSField(required=True)
#     abr = NebriOSField(required=True)
#     picture = NebriOSField(required=True)
#     code = NebriOSField(required=True)
#
#
# class womenrep_candidates(NebriOSModel):
#     # this could be combined with presidentials
#     countyid = NebriOSField(required=True)
#     surname = NebriOSField(required=True)
#     other_name = NebriOSField(required=True)
#     code = NebriOSField(required=True)
#     party = NebriOSField(required=True)
#     running_mate = NebriOSField(required=True)
#     picture = NebriOSField(required=True)
#     contest_id = NebriOSField(required=True)
#     county = NebriOSField(required=True)
#     winner = NebriOSField(required=True, default=0)
#
# class senatorial_candidates(NebriOSModel):
#     pass