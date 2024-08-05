"""Shift weekly pre-processing tasks to business hours.
With some datetime print statements to help keep track of where processing is upto,
and to highlight where improvements could be made.
"""

# You can't import datetime from datetime since
# the namespace is altered in some of the scripts.

import datetime
print(f'begin vicmap_biz_datashare {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_biz_datashare
print(f'vicmap_biz_datashare is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_address
print(f'vicmap_address is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_property
print(f'vicmap_property is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_property_view
print(f'vicmap_property_view is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_parcel
print(f'vicmap_parcel is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_parcel_view
print(f'vicmap_parcel_view is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_annotation
print(f'vicmap_annotation is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_cad_area_bdy
print(f'vicmap_cad_area_bdy is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_easement
print(f'vicmap_easement is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import vicmap_others
print(f'vicmap_others is done {datetime.datetime.now().strftime("%H:%M:%S")}')
# unq_lbl_calc has to run before the exports
# but after address and property have been updated.
import unq_lbl_calc
print(f'unq_lbl_calc is done {datetime.datetime.now().strftime("%H:%M:%S")}')
## below are derived from above
import polygon_to_point
print(f'polygon_to_point is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import waste_4bins
print(f'waste_4bins is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import wfh_export
print(f'wfh_export is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import wfh_parcel_to_point
print(f'wfh_parcel_to_point is done {datetime.datetime.now().strftime("%H:%M:%S")}')
# manually run wfh_make_archive upon completion
# done seperately to release lock by restarting shell
print(r'manually run wfh_make_archive upon completion '
      r'done seperately to release lock by restarting shell')
print(r'Run the .\weekly_biz\aaa_geoserver.bat')
