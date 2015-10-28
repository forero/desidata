from astropy.table import Table
filename="mtl_Gonzalez13.DB.MillGas.field1.FITS"
t = Table.read(filename, format='fits')
print t
t.write(filename+".txt", format='ascii')
