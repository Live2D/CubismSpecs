import jsonschema
import os
import json
import re

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def schema_check(filetype,schemafilne,targetdir):
    print filetype + " checks"
    try:
        schema = json.load(open(schemafilne,"r"))
        jsonschema.Draft4Validator.check_schema(schema)
    except Exception, e :
        print e.message
    for file in find_all_files(targetdir):
        if re.search(filetype+"$",file) :
            try:
                jdata = json.load(open(file,"r"))
                jsonschema.validate(jdata,schema)
                print file + " OK"
            except Exception,e:
                print file + " Error"
                print e.message

def filename_check_2(targetdir):
    print "filetypecheck start" + targetdir
    for file in find_all_files(targetdir):
        if re.search(r"\.(txt|md)$",file) :
            print file
    print "filetypecheck end"

tagetdir = "./"
schema_check("model3.json","model3.json.schema",tagetdir)
schema_check("motion3.json","motion3.json.schema",tagetdir)
schema_check("physics3.json","physics3.json.schema",tagetdir)
schema_check("userdata3.json","userdata3.json.schema",tagetdir)
schema_check("exp3.json","exp3.json.schema",tagetdir)
schema_check("pose3.json","pose3.json.schema",tagetdir)
