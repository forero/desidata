from astropy.table import Table

filename = 'mtl_000000.fits'
mtl = Table.read(filename, format='fits')
print(mtl.pformat)
