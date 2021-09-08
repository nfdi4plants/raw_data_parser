#!/usr/bin/env python
from mzml2isa.mzml import MzMLFile
import json
from pathlib import Path
import pandas as pd

def return_module_name():
    print("mzml_parser module loaded")


def mzml_metadata_parser (mzml_input = 'example.mzml',
                          template_url = "https://github.com/nfdi4plants/SWATE_templates/raw/main/templates/3ASY02_ProteomicsMassSpec/3ASY02_ProteomicsMassSpec.xlsx",
                          output = 'mzml_metadata'):

    swate_template = pd.read_excel(template_url,'3ASY02_ProteomicsMassSpec')
    mzml_metadata = MzMLFile('',mzml_input)

    sheet = swate_template
    header =sheet.iloc[0,4:].tolist()[::3]
    ont = []
    for row in header:
            print(row) 
            try: 
                ontology = row.split("#t")[1]
                print(ontology[:-1])
                ont.append(ontology[:-1])
            except IndexError :
                print("no_ontoloy")
                ont.append("")

    mzml_name_list= [["Experiment type",
    "Quantification method",
    "technical replicate",
    "Variable modification",
    "Fixed modification",
    "sample volume",
    "injection volume",
    "count unit",
    "Instrument",
    "duration"],
                    ["Experiment type",
    "Quantification method",
    "technical replicate",
    "Variable modification",
    "Fixed modification",
    "sample volume",
    "injection volume",
    "count unit",
    "name",
    "duration"],

                    ont]

    # pso = "NFDI4PSO:0000000"
    full_list = []
    for i,parameters in enumerate(mzml_name_list[0]):
        full_list.append(dict( swate_name = parameters, 
                              nfdi4pso = mzml_name_list[2][i], 
                              mzml_key1 = mzml_name_list[0][i], 
                              mzml_key2 = mzml_name_list[1][i]  ))

    def search_mzml_name(mzml_metadata , dict_name, dict_value, ):
        '''
        a function to search the mzml metadata by dictionary names and value, it also handels exceptions
        '''
        try:
            mzml_metadata.metadata[dict_name][dict_value]
            return [mzml_metadata.metadata[dict_name]['accession'], mzml_metadata.metadata[dict_name][dict_value]]
        except KeyError:
            return [ 'no relavent ontology', 'please fill this cell manually' ]

    output_dict = {}
    for i,dict_row in enumerate(full_list):         
        ont, value = search_mzml_name(mzml_metadata, dict_row['mzml_key1'], dict_row['mzml_key2'] )
        dict_row.update(dict( mzml_output = value, mzml_ont = ont ))
        output_dict['{}'.format(dict_row['mzml_key1'])] = dict_row 
        
    with open('{}.json'.format(output), 'w') as f:
        json.dump(output_dict, f)
