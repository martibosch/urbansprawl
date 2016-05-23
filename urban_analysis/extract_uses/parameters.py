####################################################################################
""" Parameters
This file contains several parameters used for all the scripts
"""
####################################################################################
USE_verbose = True

# Population count per squared km
population_count_file = "/home/lgervasoni/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-2000/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals_2000.tif"


city_name = "grenoble"
line_shapefile = '/home/lgervasoni/Downloads/greno_shape/grenoble_france_osm_line.shp'
point_shapefile = '/home/lgervasoni/Downloads/greno_shape/grenoble_france_osm_point.shp'
polygon_shapefile = '/home/lgervasoni/Downloads/greno_shape/grenoble_france_osm_polygon.shp'
prj_shapefile = '/home/lgervasoni/Downloads/greno_shape/grenoble_france_osm_point.prj'
'''
city_name = "paris"
line_shapefile = '/home/lgervasoni/Downloads/paris_france.osm2pgsql-shapefiles/paris_france_osm_line.shp'
point_shapefile = '/home/lgervasoni/Downloads/paris_france.osm2pgsql-shapefiles/paris_france_osm_point.shp'
polygon_shapefile = '/home/lgervasoni/Downloads/paris_france.osm2pgsql-shapefiles/paris_france_osm_polygon.shp'
prj_shapefile = '/home/lgervasoni/Downloads/paris_france.osm2pgsql-shapefiles/paris_france_osm_point.prj'


city_name = "phoenix"
line_shapefile = '/home/lgervasoni/Downloads/phoenix_arizona.osm2pgsql-shapefiles/phoenix_arizona_osm_line.shp'
point_shapefile = '/home/lgervasoni/Downloads/phoenix_arizona.osm2pgsql-shapefiles/phoenix_arizona_osm_point.shp'
polygon_shapefile = '/home/lgervasoni/Downloads/phoenix_arizona.osm2pgsql-shapefiles/phoenix_arizona_osm_polygon.shp'
prj_shapefile = '/home/lgervasoni/Downloads/phoenix_arizona.osm2pgsql-shapefiles/phoenix_arizona_osm_line.prj'
'''
####################################################################################
############# Name of files
### Folders:
# Prefix for outputting results (if any)
fn_prefix = city_name+'/'
# If dividing in sub-regions for easier processing, temporary folder:
fn_subregions = 'quadrants/'
fn_final_clasif = "full_"

### Intermmediate:
# Classification
fn_residential = "residential"
fn_activities = "activities"
fn_uncertain = "uncertain"

# For infer_poly_uses
fn_inferred = "_inferred"

### Type of object:
fn_pts_from_poly = "_pts_from_poly"
fn_poly = "_poly"
fn_pts = "_pts"

fn_residential_final = fn_prefix+fn_final_clasif+fn_residential
fn_activities_final = fn_prefix+fn_final_clasif+fn_activities
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

'''
Inferring
'''
# building=yes and no other tag compute as Residential
USE_infer_polyBuildings = True
# If False: When performing assumption on buildings, ignore items which contain tag Non-Null, or { !='' }
USE_ignoreRowsWithTaggingInformation = True
# Those inferred polygons which remain uncertain: Classify as residential?
USE_Assume_Residential_under_uncertainty = True
# Remove duplicates which are in more than one category (e.g. a shop and an amenity using the same osm_id)
# Note: Sometimes a point represents more than one valid category: e.g. A big shop containing amenities inside
USE_dropDuplicates = False

# Merge files representing the different categories into one
USE_Merge_categories = True

##########
# Filter buildings smaller than X squared meters
USE_filterSmallResidentialBuildings = True
USE_filterSmallActivitiesBuildings = False
squaredMeterThreshold = 12
### Parallelization during polygon classification infer
USE_parallel = True
num_processes = 8
sizeChunk = 100
# Sub-sample a few polygons to infer
USE_TestInferFewPolys = False
##########################################

# When merging files, delete the different cut parts?
deleteParts = True
# When converting polygons to points, delete polygon file?
deletePolyToPts = True
# When merging to final classification, delete the files?
deleteMergedParts = True
# Since using quadrants, it is cut in 4 different files. Possibilities = [1,2,4,9,16,25,...]
numCuts = 9
####################################################################################