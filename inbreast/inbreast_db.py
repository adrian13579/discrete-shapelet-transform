from os import path
from .rois_xml import parse_rois_xml

import numpy as np

_DCM_IMG_FOLDER_NAME = "AllDICOMs"
_XML_ROIS_FOLDER_NAME = "AllXML"
_EXCEL_FILE_NAME = "INbreast"


def iter_over_masses(db_source):
    db = INbreastDB(db_source)

    for _, row in db.iterrows():
        if row["Bi-Rads"] != 1:
            fn = row["File Name"]

            rois = db.get_rois(fn)

            if "Mass" in rois:
                yield fn, db.get_dcm_img(fn), rois, row["Laterality"]


def iter_over_normal_cases(db_source):
    db = INbreastDB(db_source)

    for _, row in db.iterrows():
        if row["Bi-Rads"] == 1:
            fn = row["File Name"]

            yield fn, db.get_dcm_img(fn), row["Laterality"]


class INbreastDB:
    def __init__(self, source):
        assert path.exists(source) and path.isdir(
            source
        ), "Invalid database source directory"

        self.source = source
        self.__excel_file = path.join(source, _EXCEL_FILE_NAME + ".xls")
        self.__dcm_img_dir = path.join(source, _DCM_IMG_FOLDER_NAME)
        self.__xml_rois_dir = path.join(source, _XML_ROIS_FOLDER_NAME)

        assert path.exists(self.__excel_file) and path.isfile(
            self.__excel_file
        ), "Not such .xls database file"
        assert path.exists(self.__dcm_img_dir) and path.isdir(
            self.__dcm_img_dir
        ), "Not such .dcm images directory"
        assert path.exists(self.__xml_rois_dir) and path.isdir(
            self.__xml_rois_dir
        ), "Not such .xml rois directory"

        from os import listdir

        self.__dcm_file_list = listdir(self.__dcm_img_dir)
        self.__data = self.__read_excel("C:Q", 2)

        self.__col_names = [str(col_name) for col_name in self.__data]

    def __read_excel(self, cols, skip_footer):
        from pandas import read_excel

        pd = read_excel(self.__excel_file, usecols=cols, skipfooter=skip_footer)

        return pd

    def get_data(self):
        return self.__data.copy()

    def col_names(self):
        return self.__col_names

    def iterrows(self):
        for row in self.__data.iterrows():
            yield row

    def iteritems(self):
        for item in self.__data.iteritems():
            yield item

    def __iter__(self):
        for col_name in self.__data:
            yield col_name

    def get_dcm_img(self, dcm_file):
        dcm_path = [
            dcmfile
            for dcmfile in self.__dcm_file_list
            if dcmfile.startswith(str(dcm_file))
        ]

        assert len(dcm_path) == 1, str.format("DICOM file {0} is ambiguous", dcm_file)

        dcm_path = dcm_path[0]
        dcm_path = path.join(self.__dcm_img_dir, dcm_path)

        from pydicom import dcmread

        return dcmread(dcm_path)

    def get_rois(self, xml_file, roi_names=None):
        xml_path = path.join(self.__xml_rois_dir, str(xml_file) + ".xml")

        assert path.exists(xml_path) and path.isfile(xml_path), "Invalid XML file"

        xml_data = parse_rois_xml(xml_path)
        rois_data = {}

        for roi in xml_data["Images"][0]["ROIs"]:
            roi_name = roi["Name"]
            if roi_names is None or roi_name in roi_names:
                roi_points = []
                for value in roi["Point_px"]:
                    x, y = [int(v) for v in eval(value)]
                    if (x, y) not in roi_points:
                        roi_points.append((x, y))

                roi_points = np.array(roi_points)
                if roi_name not in rois_data:
                    rois_data[roi_name] = [roi_points]
                else:
                    rois_data[roi_name].append(roi_points)

        return rois_data

    # TODO: Generalize this implementation...
    def iter_over_mass_info(self):
        for _, row in self.iterrows():
            if row["Bi-Rads"] != 1:

                fn = row["File Name"]
                rois = self.get_rois(fn)

                if "Mass" in rois:
                    yield row
