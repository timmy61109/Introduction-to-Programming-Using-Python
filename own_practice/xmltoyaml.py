"""Use xmlplain translate to ymal."""

import xmlplain

# Read to plain object
with open(
        "/home/timmy/Git/my-tasks/金門縣金寧鄉仁愛新村89號 房租基金.fods",
        encoding="utf8") as inf:
    root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

# Output plain YAML
with open(
        "/home/timmy/Git/my-tasks/金門縣金寧鄉仁愛新村89號 房租基金.yml",
        "w", encoding="utf8") as outf:
    xmlplain.obj_to_yaml(root, outf)

# Read the YAML file
with open(
        "/home/timmy/Git/my-tasks/金門縣金寧鄉仁愛新村89號 房租基金.yml",
        encoding="utf8") as inf:
    root = xmlplain.obj_from_yaml(inf)

# Output back XML
with open(
        "/home/timmy/Git/my-tasks/金門縣金寧鄉仁愛新村89號 房租基金.fods",
        mode="w", encoding="utf8") as outf:
    xmlplain.xml_from_obj(root, outf, pretty=True)
