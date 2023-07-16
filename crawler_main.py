from bs4 import BeautifulSoup


def extract_primary_data_1st_instance(html):
    # This function extracts the primary data from a first instance process

    soup_header_data = BeautifulSoup(html, 'html.parser')

    classe = soup_header_data.find("span", {"id": "classeProcesso"}).get_text().strip()
    assunto = soup_header_data.find("span", {"id": "assuntoProcesso"}).get_text().strip()
    juiz = soup_header_data.find("span", {"id": "juizProcesso"}).get_text().strip()
    distrubuicao = soup_header_data.find("div", {"id": "dataHoraDistribuicaoProcesso"}).get_text().strip()
    area = soup_header_data.find("div", {"id": "areaProcesso"}).get_text().strip()
    preco = soup_header_data.find("div", {"id": "valorAcaoProcesso"}).get_text().replace(" ", "")

    # Data extracted:
    extracted_elements = {
        "Classe": classe,
        "Area": area,
        "Assunto": assunto,
        "Data de distribuicao": distrubuicao,
        "Juiz": juiz,
        "Valor da acao": preco,
    }

    return extracted_elements


def extract_primary_data_2nd_instance(html):
    # This function extracts the primary data from a second instance process

    soup_header_data = BeautifulSoup(html, 'html.parser')

    classe = soup_header_data.find("div", {"id": "classeProcesso"}).get_text().strip()
    assunto = soup_header_data.find("div", {"id": "assuntoProcesso"}).get_text().strip()
    juiz = soup_header_data.find("div", {"id": "relatorProcesso"}).get_text().strip()
    area = soup_header_data.find("div", {"id": "areaProcesso"}).get_text().strip()
    preco = soup_header_data.find("div", {"id": "valorAcaoProcesso"}).get_text().replace(" ", "")

    # Data retrieved:
    extracted_elements = {
        "Classe": classe,
        "Area": area,
        "Assunto": assunto,
        "Relator": juiz,
        "Valor da acao": preco,
    }

    return extracted_elements


def extract_parties_involved(html):
    # This function extracts the parties involved in the process

    soup_parties_involved = BeautifulSoup(html, 'html.parser')
    types_of_parties_html = soup_parties_involved.find_all("span", {"class": "tipoDeParticipacao"})
    parties_html = soup_parties_involved.find_all("td", {"class": "nomeParteEAdvogado"})
    parties_elements = {}

    for (type_of_party, party) in zip(types_of_parties_html, parties_html):
        key = type_of_party.get_text().replace(':', '').strip()
        value_pre_treated = party.get_text().replace('\n', '').replace('\t', '').replace('\xa0', ' ')
        value = " ".join(value_pre_treated.split()).strip()

        util = {key: value}
        parties_elements.update(util)

    return parties_elements


def extract_legal_moviments_1st_instance(html):
    # This function extracts the legal moviments from a first instance process

    soup_movement_table_elements = BeautifulSoup(html, 'html.parser')
    movement_dates_html = soup_movement_table_elements.find_all("td", {"class": "dataMovimentacao"})
    movement_descriptions_html = soup_movement_table_elements.find_all("td", {"class": "descricaoMovimentacao"})
    moviment_elements = []

    # Iterating through the moviments and adding them to the moviment_elements list.
    for (movement_date, movement_description) in zip(movement_dates_html, movement_descriptions_html):
        value_pre_treated = movement_description.get_text().replace('\t', '').replace('\r', '\n')
        value = " ".join(value_pre_treated.split()).strip()
        key = movement_date.get_text().strip()

        util = {key: value}

        moviment_elements.append(util)

    return moviment_elements


def extract_legal_moviments_2nd_instance(html):
    # This function extracts the legal moviments from a first instance process

    soup_movement_table_elements = BeautifulSoup(html, 'html.parser')
    movement_dates_html = soup_movement_table_elements.find_all("td", {"class": "dataMovimentacaoProcesso"})
    movement_descriptions_html = soup_movement_table_elements.find_all("td", {"class": "descricaoMovimentacaoProcesso"})
    moviment_elements = []

    # Iterating through the moviments and adding them to the moviment_elements list.
    for (movement_date, movement_description) in zip(movement_dates_html, movement_descriptions_html):
        value_pre_treated = movement_description.get_text().replace('\t', '').replace('\r', '\n')
        value = " ".join(value_pre_treated.split()).strip()
        key = movement_date.get_text().strip()

        util = {key: value}

        moviment_elements.append(util)

    return moviment_elements

