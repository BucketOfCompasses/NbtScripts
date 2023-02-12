from nbt import nbt
import json
import os

def add_list_tag(values, tag):
    if not (tag.id == nbt.TAG_LIST or tag.id == nbt.TAG_COMPOUND):
        values.append(tag.value)
    elif tag.id == nbt.TAG_LIST:
        value = []
        for t in tag.tags:
            add_list_tag(value, t)
        values.append(value)
    elif tag.id == nbt.TAG_COMPOUND:
        value = {}
        for t in tag.tags:
            add_tag(value, t)
        values.append(value)
    else:
        print(tag)

def add_tag(dictionary, tag):
    if not (tag.id == nbt.TAG_LIST or tag.id == nbt.TAG_COMPOUND):
        dictionary[tag.name] = tag.value
    elif tag.id == nbt.TAG_LIST:
        value = []
        for t in tag.tags:
            add_list_tag(value, t)
        dictionary[tag.name] = value
    elif tag.id == nbt.TAG_COMPOUND:
        value = {}
        for t in tag.tags:
            add_tag(value, t)
        dictionary[tag.name] = value
    else:
        print(tag)


if __name__ == "__main__":
    files = os.listdir("nbt")
    for file in files:
        data = {}
        nbtfile = nbt.NBTFile(f"nbt/{file}", "rb")
        for tag in nbtfile.tags:
            add_tag(data, tag)
        with open("json/" + file.replace(".dat", ".json"), "w+") as f:
            f.write(json.dumps(data, sort_keys = True, indent = 4))
        # with open("json/" + file.replace(".dat", ".pp"), "w+") as f:
        #     f.write(nbtfile.pretty_tree())
        print()
