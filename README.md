This simple Python testdatagen module generates pipe ('|') delimited test data with the following fields - 
firstname, lastname, email, streetAddress, ZipCode, City, State, StateAbrv, County, Latitude, Longitude

The intention of this module is to provide a simple way to quickly generate person test data. 
It can generate a million record test file in just under 20 seconds.

Usage :

    import testdatagen
    testdatagen.test_data(filename, recordcount)
    
    example : testdatagen.test_data('persons.csv', 300)
    
    This example will create  a file named 'persons.csv' in the  directory where this program is located.
    The file 'persons.csv' will have 300 lines.
    It is recommended that you provide a fuly qualified file name (i.e /path/filename


It needs the included csv files to generate the test data. These files are listed below -

	testdata_dn.csv
	testdata_fn.csv
	testdata_ln.csv
	testdata_st.csv
	us_postal_codes.csv