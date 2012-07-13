"""Python interface to GenoLogics LIMS via its REST API.

Example usage: Set the UDF 'Queued' of a project.

NOTE: You need to set the BASEURI, USERNAME AND PASSWORD.

Per Kraulis, Science for Life Laboratory, Stockholm, Sweden.
"""

import datetime

from genologics.lims import *

# Login parameters for connecting to a LIMS instance.
# NOTE: Modify according to your setup.
from genologics.site_cloud import BASEURI, USERNAME, PASSWORD

# Create the LIMS interface instance, and check the connection and version.
lims = Lims(BASEURI, USERNAME, PASSWORD)
lims.check_version()

# Get the project with the LIMS id KLL60, and print some info.
project = Project(lims, id='KLL60')
print project, project.name, project.open_date
print project.udf.items()

d = datetime.date(2012,1,2)
print d

project.udf['Queued'] = d
project.put()
