from lxml import objectify


def parse_rois_xml(xml_path):
    """
    Parse INbreast 1.0 ROIs XML given the XML path.
    :param xml_path: XML file name
    :return: A dictionary object that contains all raw information of the INbreast1.0 XML ROIs description.
    """
    xml = objectify.parse(xml_path)
    root = xml.getroot()

    return __parse_rois_xml(root.getchildren()[0])


def __parse_rois_xml(root):
    """
    Parse INbreast 1.0 ROIs XML given the XML root.
    :param root: Root element of the XML.
    :return: A dictionary object that contains information of the INbreast 1.0 ROIs XML description.
    """
    if root.tag == 'dict':
        data = {}
        children = root.getchildren()
        for i in range(0, len(children) - 1, 2):
            key = __parse_rois_xml(children[i])
            value = __parse_rois_xml(children[i + 1])
            data[key] = value
        return data

    if root.tag == 'array':
        data = []
        for child in root.getchildren():
            data.append(__parse_rois_xml(child))

        return data

    if root.tag == 'key' or root.tag == 'string':
        return str(root.text)
    if root.tag == 'integer':
        return int(root.text)
    if root.tag == 'real':
        return float(root.text)

    raise Exception('Not supported INBreast1.0 XML ROIs description format')
