import streamlit as st 
import json
import requests

def gerar_primeira_estrutura(json):
    primeira_estrutura = f'''
    cpfcnpjtransmissor=08498701000104
    cpfcnpjempregador=08498701000104
    idgrupoeventos=3
    versaomanual=S.01.01.00
    ambiente=1

    INCLUIRS1200
    indRetif_4=1
    nrRecibo_5=
    indApuracao_6={data["indApuracao"]}
    perApur_7={data["perApur"]}
    indGuia_106=
    tpAmb_8=1
    procEmi_9=1
    verProc_10=1.0
    tpInsc_12=1
    nrInsc_13=08498701
    cpfTrab_15={data["ideTrabalhador"]["cpfTrab"]}
    indMV_18=
    nmTrab_25=
    dtNascto_26=
    tpInsc_107=
    nrInsc_108=
    matricAnt_93=
    dtAdm_97=
    observacao_95=

    INCLUIRREMUNOUTREMPR_150
    tpInsc_109=
    nrInsc_110=
    codCateg_22=
    vlrRemunOE_23=
    SALVARREMUNOUTREMPR_150

    INCLUIRPROCJUDTRAB_151
    tpTrib_31=
    nrProcJud_32=
    codSusp_33=
    SALVARPROCJUDTRAB_151

    INCLUIRINFOINTERM_152
    dia_111=
    SALVARINFOINTERM_152

    INCLUIRDMDEV_153
    ideDmDev_35={data["dmDev"][0]["ideDmDev"]}
    codCateg_112={data["dmDev"][0]["codCateg"]}
    indRRA_128=
    codCBO_103=
    natAtividade_104=
    qtdDiasTrab_105=
    tpProcRRA_129=
    nrProcRRA_130=
    descRRA_131=
    qtdMesesRRA_132=
    vlrDespCustas_133=
    vlrDespAdvogados_134=
    SALVARDMDEV_153

    INCLUIRIDEESTABLOT_154
    tpInsc_113={data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["tpInsc"]}
    nrInsc_114={data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["nrInsc"]}
    codLotacao_41={data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["codLotacao"]}
    qtdDiasAv_42=
    SALVARIDEESTABLOT_154

    INCLUIRREMUNPERAPUR_155
    matricula_44={data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["remunPerApur"][0]["matricula"]}
    indSimples_45=
    grauExp_64={data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["remunPerApur"][0]["infoAgNocivo"]["grauExp"]}
    SALVARREMUNPERAPUR_155

    '''

        # Adiciona blocos de "INCLUIRITENSREMUN_156" com base no número de remunerações
    for remun in data["dmDev"][0]["infoPerApur"]["ideEstabLot"][0]["remunPerApur"][0]["itensRemun"]:
      primeira_estrutura += f'''
    INCLUIRITENSREMUN_156
    codRubr_47={remun["codRubr"]}
    ideTabRubr_48={remun["ideTabRubr"]}
    qtdRubr_49={remun["qtdRubr"]}
    fatorRubr_50=
    vrRubr_52={remun["vrRubr"]}
    indApurIR_115={remun["indApurIR"]}
    SALVARITENSREMUN_156
    '''

        # Adiciona o restante da estrutura
    primeira_estrutura += '''
    INCLUIRIDEADC_157
    dtAcConv_67=
    tpAcConv_68=
    dsc_70=
    remunSuc_90=
    SALVARIDEADC_157

    INCLUIRIDEPERIODO_158
    perRef_72=
    SALVARIDEPERIODO_158

    INCLUIRIDEESTABLOT_159
    tpInsc_116=
    nrInsc_117=
    codLotacao_118=
    SALVARIDEESTABLOT_159

    INCLUIRREMUNPERANT_160
    matricula_119=
    indSimples_120=
    grauExp_121=
    SALVARREMUNPERANT_160

    INCLUIRITENSREMUN_161
    codRubr_122=
    ideTabRubr_123=
    qtdRubr_124=
    fatorRubr_125=
    vrRubr_126=
    indApurIR_127=
    SALVARITENSREMUN_161
    SALVARS1200
    '''
    headers = {
    'Content-Type': 'text/tx2',
    'cnpj_sh': '50955669000105',
    'token_sh': 'f68d493f383d6bf96858e876cc8aa783',  # Substitua pelo seu token
    'empregador': '08498701000104'
    }

   

json_input = st.file_uploader("Coloque o JSON")

if json_input:
  data = json.load(json_input)

  try:
    data = json.loads(json_input)
  except json.JSONDecodeError as e:
      print(f"Erro ao decodificar o JSON: {e}")
      exit(1)

  # Chamada da função
  primeira_estrutura = gerar_primeira_estrutura(data)

  # Saída da primeira estrutura
  print(primeira_estrutura)


