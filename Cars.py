def make_car(modelname, manufactor, **kvarg):
    kvarg['modelname'] = modelname
    kvarg['manufactor'] = manufactor
    return kvarg

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)