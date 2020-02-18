
# Read house price data files from: https://valuation.property.nsw.gov.au/embed/propertySalesInformation 
# B;001;4229165;5;20190805 01:00;;;86;MAURICE RD;POKOLBIN;2320;1.038;H;20190613;20190725;850000;;R;RESIDENCE;;;;0;AP418234;
# Directory that contains the zip files

DOWNLOAD_DIR = "Downloads"
OUTFILE_NAME = "out.csv"

FIELD_NAMES = ["Record Type",
"District Code",
"Property Id.",
"Sale Counter",
"Download Date / Time",
"Property Name",
"Property Unit Number",
"Property House Number",
"Property Street Name",
"Property Locality",
"Property Post Code",
"Area",
"Area Type",
"Contract Date",
"Settlement Date",
"Purchase Price",
"Zoning",
"Nature of Property",
"Primary Purpose",
"Strata Lot Number",
"Component code",
"Sale Code",
"% Interest of Sale",
"Dealing Number"]

import os
import zipfile

def main():
    outfile = open(OUTFILE_NAME, "w")
    printFieldHeaders(outfile)
    files = os.listdir(DOWNLOAD_DIR)
    
    for azipfile in files:
        zip_file_path = os.path.join(DOWNLOAD_DIR, azipfile)
        print(f"opening {zip_file_path}")
        try:
            archive = zipfile.ZipFile(zip_file_path)
            data_file_list = archive.namelist()
            for data_file in data_file_list:
                if data_file.endswith(".DAT"):
                    for line in archive.open(data_file):
                        lineStr = line.decode('UTF-8')
                        if lineStr.startswith("B"):
                            fields = lineStr.strip().split(";")
                            for field in fields:
                                print("%s\t" %field, end='', file=outfile)
                            print(file=outfile)
        except:
            continue
            #print(f"Error opening {azipfile}")


def printFieldHeaders(outfile):
    for fieldName in FIELD_NAMES:
        print("%s\t" %fieldName, end='', file=outfile)
    print(file=outfile)


if __name__ == "__main__":
    main()