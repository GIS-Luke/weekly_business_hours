'''
vicmap_biz_datashare is done 09:18:29
vicmap_address is done 09:23:57
vicmap_property is done 09:25:04
vicmap_property_view is done 09:25:42
vicmap_parcel is done 09:26:01
vicmap_parcel_view is done 09:26:49
vicmap_annotation is done 09:27:34
vicmap_cad_area_bdy is done 09:30:01
vicmap_easement is done 09:30:09
vicmap_others is done 09:32:43
unq_lbl_calc is done 09:58:43
polygon_to_point is done 09:59:41
wfh_export is done 10:02:28
shape position 0
wfh_parcel_to_point is done 10:03:08
waste_4bins is done 10:05:13
'''

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
import wfh_export
print(f'wfh_export is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import wfh_parcel_to_point
print(f'wfh_parcel_to_point is done {datetime.datetime.now().strftime("%H:%M:%S")}')
import waste_4bins
print(f'waste_4bins is done {datetime.datetime.now().strftime("%H:%M:%S")}')
# manually run wfh_make_archive upon completion
# done seperately to release lock by restarting shell
print(r'manually run wfh_make_archive upon completion '
      r'done seperately to release lock by restarting shell')
print(r'Run the .\weekly_biz\aaa_geoserver.bat')
