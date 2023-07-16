import json
import requests
from bs4 import BeautifulSoup
from crawler_main import *


def tj_handling(api_input):
    # In order to scale the search, I opted to set a list with the current courts avaialble:
    available_tj = ["02", "06"]

    # Setting the number of the process.
    num_processo = api_input.replace(".", "").replace("-", "").strip()

    # Extracting the respective tj regarding the process number.
    respective_tj = num_processo[14:16]

    if respective_tj not in available_tj:
        print(f'Currently we only accept processes from the following TJs: {available_tj}')

    # Setting the links for the respective Tj retrieved
    else:
        if respective_tj == '02':
            # TJAL

            current_urls = {
                "url_1st_instance": f'https://www2.tjal.jus.br/cpopg/show.do?processo.foro=1&processo.numero={num_processo}',
                "url_2nd_instance": f'https://www2.tjal.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&dePesquisaNuUnificado={num_processo}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO',
                "url_with_process_code": 'https://www2.tjal.jus.br/cposg5/show.do?processo.codigo='
            }
            return current_urls

        if respective_tj == '06':
            # TJCE

            current_urls = {
                "url_1st_instance": f'https://esaj.tjce.jus.br/cpopg/show.do?processo.foro=1&processo.numero={num_processo}',
                "url_2nd_instance": f'https://esaj.tjce.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&dePesquisaNuUnificado={num_processo}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO',
                "url_with_process_code": 'https://esaj.tjce.jus.br/cposg5/show.do?processo.codigo='
            }
            return current_urls


def buscar_processo(api_input):
    # Setting the current urls from the retrieved TJ
    tj_urls = tj_handling(api_input)

    try:
        response_1st_instance = requests.get(tj_urls['url_1st_instance'])
        html_1st_instance = response_1st_instance.content
        primary_data_1st_isntance = extract_primary_data_1st_instance(html_1st_instance)  # Returns the primary data, such as name, prioce, etc.
        parties_involved_1st_instance = extract_parties_involved(html_1st_instance)  # Returns the parties involved on the process.
        legal_moviments_data_1st_instance = extract_legal_moviments_1st_instance(html_1st_instance)  # Returns the moviments of the process.

        # This block of code checks if there is a 2nd level for the process
        try:
            response_2nd_instance = requests.get(tj_urls['url_2nd_instance'])
            html_2nd_instance = response_2nd_instance.content
            soup_2nd_instance = BeautifulSoup(html_2nd_instance, 'html.parser')

            if soup_2nd_instance.find("td", {"id": "mensagemRetorno"}):
                print("The process is limited to the 1st level.")

                final_result = {
                    "Primary_data_1st_instance": primary_data_1st_isntance,
                    "Parties_involved_1st_instance": parties_involved_1st_instance,
                    "legal_moviments_data_1st_instance": legal_moviments_data_1st_instance,
                }

                second_level = False
                return final_result
            else:
                second_level = True

        except:
            print("There was an error searching your query. Try again.")
            second_level = False

    except:
        print("The process has not been found. Try again with another number.")

    # This part accesses the data from the second level
    try:
        # If there is a 2nd instance, we make another request using the code, going to the process page itself.
        if second_level:
            process_code = soup_2nd_instance.find("input", {"type": "radio"}).get('value')
            url_2nd_instance_itself = f'{tj_urls["url_with_process_code"]}{process_code}'
            response_2nd_instance_itself = requests.get(url_2nd_instance_itself)
            html_2nd_instance = response_2nd_instance_itself.content

            primary_data_2nd_instance = extract_primary_data_2nd_instance(html_2nd_instance)
            parties_involved_2nd_instance = extract_parties_involved(html_2nd_instance)
            legal_moviments_data_2nd_instance = extract_legal_moviments_2nd_instance(html_2nd_instance)

            final_result = {
                "primary_data_1st_instance": primary_data_1st_isntance,
                "legal_moviments_data_1st_instance": legal_moviments_data_1st_instance,
                "parties_involved_1st_instance": parties_involved_1st_instance,
                "primary_data_2nd_instance": primary_data_2nd_instance,
                "parties_involved_2nd_instance": parties_involved_2nd_instance,
                "legal_moviments_data_2nd_instance": legal_moviments_data_2nd_instance
            }

            return final_result

    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro: ", e)
        return None


"""
Mock:

api_input1 = "0014073-15.2016.8.06.0182"  # Irajane Alves Fontenele
api_input2 = "0710802-55.2018.8.02.0001"  # José Carlos Cerqueira Souza Filho
api_input3 = "0099480-39.2008.8.02.0001"  # Lucimar Jane Lira
api_input4 = "0014073-15.2016.8.06.0182"  # Irajane Alves Fontenele
api_input5 = "0137352-91.2019.8.06.0001"  # Benedito Gerson Marques
api_input6 = "0200221-69.2022.8.06.0168"  # Maria Jose Sousa Rolim
"""
