def attr_builder(target, *attributes):
    final_dict = {}
    for attribute in attributes:
        final_dict[attribute] = getattr(target, attribute, None)
    return final_dict