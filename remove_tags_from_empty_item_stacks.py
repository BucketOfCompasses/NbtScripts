from nbt import nbt
import os

def clean_empty_item_tags(tag):
    if tag.id == nbt.TAG_COMPOUND:
        if "Count" in tag and "id" in tag and "tag" in tag:
            if tag["id"].value == "minecraft:air":
                del tag["tag"]
                return
    
    if tag.id == nbt.TAG_COMPOUND or tag.id == nbt.TAG_LIST:
        for t in tag.tags:
            clean_empty_item_tags(t)


if __name__ == "__main__":
    files = os.listdir("dirty_players")
    for file in files:
        nbtfile = nbt.NBTFile(f"dirty_players/{file}", "rb")
        for tag in nbtfile.tags:
            clean_empty_item_tags(tag)
        nbtfile.write_file(f"clean_players/{file}")
