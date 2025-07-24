import xml.etree.ElementTree as ET

# Load your XML template
tree = ET.parse('./ptp_project_tmpl.kml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    
# Find an element and update its text
element_to_update = root.find('Site C - Site D')
if element_to_update is not None:
#    element_to_update.text = 'New Value'
    print(element_to_update.tag)
    
# Add a new element
#new_element = ET.SubElement(root, 'new_data')
#new_element.text = 'Some new information'

# Save the modified XML
#tree.write('updated_output.kml', encoding='utf-8', xml_declaration=True)