import json
with open('Timeseries_board_1.json', 'r') as f:
    panel_data = json.load(f)

# panel_uid = panel_data['uid']
# panel_template_tags = panel_data["templating"]['list'][0]
def create_dict():
    tag_template = {
                  "selected": True,
                  "text": "tag",
                  "value": "tag"
                }
    return tag_template
def prepare_panel(asset_name, tags)
  
  option_list = []
  for tag in tags:
      tag_template = create_dict()
      if tags.index(tag) == 0:
          tag_template["selected"] = True
      else:
          tag_template["selected"] = False
      tag_template["text"] = str(tag)
      tag_template["value"] = str(tag) 
      option_list.append(tag_template)
  panel_data["templating"]['list'][0]['options'] = option_list
  with open(f'{asset_name}.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

tags = ['tag1', 'tag2']
asset_name = 'asset1'
prepare_panel(asset_name, tags)