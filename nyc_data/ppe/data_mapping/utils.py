from datetime import datetime

from ppe.dataclasses import Item


class ErrorCollector:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def report_error(self, err: str):
        self.errors.append(err)

    def report_warning(self, warning: str):
        self.warnings.append(warning)

    def __repr__(self):
        return f'{len(self.errors)} errors and {len(self.warnings)} warnings'


def asset_name_to_item(asset_name: str, error_collector: ErrorCollector) -> Item:
    mapping = {
        "KN95 Masks": Item.kn95_mask,
        "Face Masks-Other": Item.mask_other,
        "Surgical Grade N95s Masks": Item.n95_mask_surgical,
        "Non-Surgical Grade N95s Masks": Item.n95_mask_non_surgical,
        "Isolation Gowns": Item.gown,
        "Gowns": Item.gown,
        "Materials for Gowns": Item.gown_material,
        "Coveralls": Item.coveralls,
        "Non Full Service Ventilators": Item.ventilators_non_full_service,
        "Face Coverings-Non Medical": Item.mask_other,
        "Goggles": Item.goggles,
        "Other PPE, Healthcare": Item.ppe_other,
        "Full Service Ventilators": Item.ventilators_full_service,
        "Face Shields": Item.faceshield,
        "Faceshield": Item.faceshield,
        "Face Shield": Item.faceshield,
        "Gloves": Item.gloves,
        "Surgical Masks": Item.surgical_mask,
        "N95": Item.n95_mask_surgical,
        "Facemasks": Item.mask_other,
        "Eyewear": Item.generic_eyeware,
        "Vents": Item.ventilators_full_service,
        "BiPAP Machines": Item.bipap_machines,
        "Body Bags": Item.body_bags
    }
    match = mapping.get(asset_name)
    if match is not None:
        return match
    error_collector.report_warning(f"Unknown type: {asset_name}")
    return Item.unknown


def parse_date(date: any, error_collector: ErrorCollector):
    formats = [
        ("%m/%d/%Y", lambda x: x),  # 04/10/2020
        ("%d-%b", lambda d: d.replace(year=2020)),
        ("%m/%d", lambda d: d.replace(year=2020)),
    ]
    if isinstance(date, str):
        for fmt, mapper in formats:
            try:
                return mapper(datetime.strptime(date, fmt))
            except ValueError:
                pass
        error_collector.report_error(f"Unknown date format: {date}")
        return None
    elif isinstance(date, datetime):
        return date
    else:
        return None

def parse_int_or_zero(inp: str, error_collector: ErrorCollector):
    return parse_int(inp, error_collector) or 0

def parse_int(inp: str, error_collector: ErrorCollector):
    if isinstance(inp, int):
        return inp
    if inp is None:
        return None
    try:
        return int(inp)
    except ValueError:
        # Maybe there's a unit or some other crap
        error_collector.report_error(f"Can't parse {inp}. Returning None for now [TODO]")
        return None