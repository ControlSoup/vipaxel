import polars as pl
import zentrope.template_parsing as tp
import zentrope.tar_database as tardb
import os

FILE_PATH = os.path.dirname(__file__) 
config =  tp.parse_yaml('examples/example.yaml')
file_path = lambda path: os.path.join(FILE_PATH, path)
tdb = file_path('example.tar.gz')

set4 = pl.DataFrame({'a [lbf]': [0.0, 100.0, 0.0], 'time [s]': [-10.0, 5.0, 10.0]})

# Create a db (I hate python try catches)
tardb.create_tar_gzip(tdb)

try:
    tardb.add_entries(tdb, file_path('set-2.csv'), file_path('set-3.csv'))

    # Create the figs
    figs = tp.parse_template(config, {'set-4': set4})

    for fig in figs:
        fig.show()

except Exception as e:
    print(e)

os.remove(tdb)