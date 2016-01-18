from nebriosmodels import NebriOSModel, NebriOSField, NebriOSReference

class TestModel(NebriOSModel):
    name = NebriOSField(required=True)
    story = NebriOSField()
    number = NebriOSField()
