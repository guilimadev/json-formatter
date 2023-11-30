import streamlit as st 
import json

f = st.file_uploader("Coloque o JSON")

if f:
  data = json.load(f)

  # Create the new JSON structure
  new_json = {
      "evtTabRubrica": {
          "ideEvento": {
              "tpAmb": "2",
              "procEmi": "1",
              "verProc": "1.6.0"
          },
          "ideEmpregador": {
              "tpInsc": "1",
              "nrInsc": "08498701"
          },
          "infoRubrica": {
              "inclusao": {
                  "ideRubrica": {
                      "codRubr": data["ideRubrica"]["codRubr"],
                      "ideTabRubr": data["ideRubrica"]["ideTabRubr"],
                      "iniValid": data["ideRubrica"]["iniValid"],
                      "fimValid": ""
                  },
                  "dadosRubrica": {
                      "dscRubr": data["dadosRubrica"]["dscRubr"],
                      "natRubr": data["dadosRubrica"]["natRubr"],
                      "tpRubr": data["dadosRubrica"]["tpRubr"],
                      "codIncCP": data["dadosRubrica"]["codIncCP"],
                      "codIncIRRF": data["dadosRubrica"]["codIncIRRF"],
                      "codIncFGTS": data["dadosRubrica"]["codIncFGTS"],
                      "codIncCPRP": data["dadosRubrica"]["codIncCPRP"],
                      "tetoRemun": data["dadosRubrica"]["tetoRemun"],
                      "observacao": data["dadosRubrica"]["tetoRemun"],
                      "ideProcessoCP": [
                        {
                          "tpProc": "",
                          "nrProc": "",
                          "extDecisao": "",
                          "codSusp": ""
                        }
                      ],
                      "ideProcessoIRRF": [
                        {
                          "nrProc": "",
                          "codSusp": ""
                        }
                      ],
                      "ideProcessoFGTS": [
                        {
                          "nrProc": ""
                        }
                      ]
                  }
              }
          }
      }
  }

  # Convert the new JSON to a string
  new_json_string = json.dumps(new_json, indent=2)

  # Print the result
  st.write(new_json_string)

  st.download_button(
      label="Download data as JSON",
      data=new_json_string,
      file_name='new_json_string.json',
    
  )